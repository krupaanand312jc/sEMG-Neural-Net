cyl_emav = zeros(100,1);
cyl_dasdv = zeros(100,1);
cyl_fzc = zeros(100,1);
cyl_vare = zeros(100,1);

hook_emav = zeros(100,1);
hook_dasdv = zeros(100,1);
hook_fzc = zeros(100,1);
hook_vare = zeros(100,1);

lat_emav = zeros(100,1);
lat_dasdv = zeros(100,1);
lat_fzc = zeros(100,1);
lat_vare = zeros(100,1);

palm_emav = zeros(100,1);
palm_dasdv = zeros(100,1);
palm_fzc = zeros(100,1);
palm_vare = zeros(100,1);

spher_emav = zeros(100,1);
spher_dasdv = zeros(100,1);
spher_fzc = zeros(100,1);
spher_vare = zeros(100,1);

tip_emav = zeros(100,1);
tip_dasdv = zeros(100,1);
tip_fzc = zeros(100,1);
tip_vare = zeros(100,1);


for i = 1:100
    cyl_emav(i,:) = jfemg('emav', cyl_ch2(i,:));
    cyl_dasdv(i,:) = jfemg('dasdv', cyl_ch2(i,:));
    cyl_fzc(i,:) = jfemg('fzc', cyl_ch2(i,:));
    cyl_vare(i,:) = jfemg('vare', cyl_ch2(i,:));
    
    hook_emav(i,:) = jfemg('emav', hook_ch2(i,:));
    hook_dasdv(i,:) = jfemg('dasdv', hook_ch2(i,:));
    hook_fzc(i,:) = jfemg('fzc', hook_ch2(i,:));
    hook_vare(i,:) = jfemg('vare', hook_ch2(i,:));
    
    lat_emav(i,:) = jfemg('emav', lat_ch2(i,:));
    lat_dasdv(i,:) = jfemg('dasdv', lat_ch2(i,:));
    lat_fzc(i,:) = jfemg('fzc', lat_ch2(i,:));
    lat_vare(i,:) = jfemg('vare', lat_ch2(i,:));
    
    palm_emav(i,:) = jfemg('emav', palm_ch2(i,:));
    palm_dasdv(i,:) = jfemg('dasdv', palm_ch2(i,:));
    palm_fzc(i,:) = jfemg('fzc', palm_ch2(i,:));
    palm_vare(i,:) = jfemg('vare', palm_ch2(i,:));
    
    spher_emav(i,:) = jfemg('emav', spher_ch2(i,:));
    spher_dasdv(i,:) = jfemg('dasdv', spher_ch2(i,:));
    spher_fzc(i,:) = jfemg('fzc', spher_ch2(i,:));
    spher_vare(i,:) = jfemg('vare', spher_ch2(i,:));
    
    tip_emav(i,:) = jfemg('emav', tip_ch2(i,:));
    tip_dasdv(i,:) = jfemg('dasdv', tip_ch2(i,:));
    tip_fzc(i,:) = jfemg('fzc', tip_ch2(i,:));
    tip_vare(i,:) = jfemg('vare', tip_ch2(i,:));
end
feature_vector = [cyl_emav cyl_dasdv cyl_fzc cyl_vare; hook_emav hook_dasdv hook_fzc hook_vare; lat_emav lat_dasdv lat_fzc lat_vare; palm_emav palm_dasdv palm_fzc palm_vare; spher_emav spher_dasdv spher_fzc spher_vare; tip_emav tip_dasdv tip_fzc tip_vare];