import pandas as pd
import numpy as np
import os


def read_data(data_path, split_type="train", shuffle=False, sub_split=False):
    """
    Read data in from CSV files and format properly for neural networks.
    :param data_path: Absolute file path to data.
    :param split_type: If splitting the same dataset, which split to designate this one as.
    :param shuffle: Whether data should be kept in sequential order or shuffled.
    :param sub_split: Should the data be split in half and returned as a two-tuple.
    :return: Data formatted for neural network training.
    """
    # Fixed params
    n_class = 6
    n_channels = 1
    n_steps = 2496

    train_days = [1, 2, 3]
    test_days = [1, 2, 3]

    if split_type == 'train':
        split = train_days
    else:
        split = test_days

    # Assign numeric label to categories:
    #
    # cyl = 1
    # hook = 2
    # lat = 3
    # palm = 4
    # spher = 5
    # tip = 6
    #
    labels = np.concatenate(
        (
            [[class_id for _ in range(100 * len(split))] for class_id in range(1, n_class + 1)]
        )
    )

    files = [
        'cyl_ch2.csv',
        'hook_ch2.csv',
        'lat_ch2.csv',
        'palm_ch2.csv',
        'spher_ch2.csv',
        'tip_ch2.csv'
    ]

    # Merge files of different grip types into one long file, per channel
    channels = []
    for num_channel in range(n_channels):

        all_of_channel = []
        for file in files[num_channel::n_channels]:

            gesture_by_day = []
            for day in split:
                full_day_path = os.path.join(data_path, 'male_day_%d' % day)
                full_file_path = os.path.join(full_day_path, file)

                # Drop last 4 data points to more easily subdivide into layers
                gesture_by_day.append(pd.read_csv(full_file_path,  header=None).drop(labels=[2496, 2497, 2498, 2499], axis=1))

            all_of_channel.append(pd.concat(gesture_by_day))

        channels.append(
            (pd.concat(all_of_channel), 'channel_%d' % num_channel)
        )

    # Initiate array
    list_of_channels = []
    X = np.zeros((len(labels), n_steps, n_channels))

    i_ch = 0
    for channel_data, channel_name in channels:
        X[:, :, i_ch] = np.array(channel_data)
        list_of_channels.append(channel_name)
        i_ch += 1

    if shuffle:
        shuff_labels = np.zeros((len(labels), 1, n_channels))
        shuff_labels[:, 0, 0] = labels

        new_data = np.concatenate([shuff_labels, X], axis=1)

        np.reshape(new_data, (n_steps + 1, len(labels), n_channels))
        np.random.shuffle(new_data)
        np.reshape(new_data, (len(labels), n_steps + 1, n_channels))

        final_data = new_data[:, 1:, :]
        final_labels = np.array(new_data[:, 0, 0]).astype(int)

        # Return (train, test)
        if sub_split:
            return (
                final_data[int(len(final_labels) / 2):, :, :],
                final_labels[int(len(final_labels) / 2):],
                list_of_channels,
                final_data[:int(len(final_labels) / 2), :, :],
                final_labels[:int(len(final_labels) / 2)],
                list_of_channels
            )
        else:
            return final_data, final_labels, list_of_channels

    else:
        return X, labels, list_of_channels


def standardize(train, test):
    """
    Standardize data.
    :param train: Train data split.
    :param test: Test data split.
    :return: Normalized data set.
    """

    # Standardize train and test
    X_train = (train - np.mean(train, axis=0)[None, :, :]) / np.std(train, axis=0)[None, :, :]
    X_test = (test - np.mean(test, axis=0)[None, :, :]) / np.std(test, axis=0)[None, :, :]

    return X_train, X_test


def one_hot(labels, n_class=6):
    """
    One-hot encoding.
    :param labels: Labels to encode.
    :param n_class: Number of classes.
    :return: One-hot encoded labels.
    """
    expansion = np.eye(n_class)
    y = expansion[:, labels-1].T

    assert y.shape[1] == n_class, "Wrong number of labels!"

    return y


def get_batches(X, y, batch_size=100):
    """
    Return a generator for batches.
    :param X: Data set.
    :param y: Labels.
    :param batch_size: Batch size.
    :return: Portion of data in batch-size increments.
    """
    n_batches = len(X) // batch_size
    X, y = X[:n_batches * batch_size], y[:n_batches * batch_size]

    # Loop over batches and yield
    for b in range(0, len(X), batch_size):
        yield X[b:b + batch_size], y[b:b + batch_size]
