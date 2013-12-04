function cache = read_images (img_path)

    cache = containers.Map();

    % List of all files
    images = dir(img_path);
    
    for i = 1 : numel(images)
        if (images(i).isdir && ~strcmp(images(i).name, '.') ...
                && ~strcmp(images(i).name, '..'))
            cache = [cache; read_images(fullfile(img_path, images(i).name))];
        end
    end
    
    images = dir(fullfile(img_path, '*.jpg'));
    new_cache = containers.Map();

    % Read images to cache
    for i = 1 : numel(images),
        name = fullfile(img_path, images(i).name);
        new_cache(name) = imread(name);
    end
    norm_cache(new_cache, size)
    
    cache = [cache; new_cache];
end

