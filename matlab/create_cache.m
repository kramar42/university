function [] = create_cache(pic_path, count, size)
    % Read into tmp cache
    img_cache = read_images(pic_path, size);
    disp('Read originals images.')
    % Now img_cache holds prepared images
    img_cache = prepare_images(img_cache, 'prepared', size);
    disp('Made prepared images.')
    
    % Make 2 samples
    transform_images(img_cache, 'transformed', count);
    disp('Transformed sample created.')
    transform_images(img_cache, 'unknown', count)
    disp('Unknown sample created.')
    
    % Read transformed pictures
    img_cache = read_images('transformed');
    disp('Read from transformed images.')
    % Normalize them
    img_cache = norm_cache(img_cache, size);
    disp('Normilized them.')
    
    % Read unknow pictures
    unknown_cache = read_images('unknown');
    disp('Read from unknown images.')
    unknown_cache = norm_cache(unknown_cache, size);
    disp('Normilized them.')
    
    % Calculate class average
    class_avg = class_average(img_cache);
    disp('Calculated class average')
    
    % Save img_cache & unknown_cache
    save('caches.mat', 'img_cache', 'unknown_cache', 'class_avg')
    disp('Saved caches.')
end

