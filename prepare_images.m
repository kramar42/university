function cache = prepare_images(img_cache, file_path, size)
    makedir(file_path)
    % Here holds values & keys
    values = img_cache.values;
    keys = img_cache.keys;
    % New cache for croped images
    cache = containers.Map();
    
    for i = 1 : numel(values)
        image = values{i};
        % To gray
        try
            image = rgb2gray(image);
        catch ME
        end
    
        % Adjust brightness
        image = imadjust(image);        
        %Crop image
        image = crop_image(image);
        % Resizing image
        image = imresize(image, size);
        
        % Saving image
        imwrite(image, fullfile(file_path, ['image' int2str(i) '.jpg']))
        cache(keys{i}) = image;
    end
end
