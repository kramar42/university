function [ ] = transform_images(img_cache, file_path, times)
    % Here holds values & keys
    values = img_cache.values;
    
    % For every image
    for i = 1 : numel(values)
        img_name = ['image' int2str(i)];
        img_name = fullfile(file_path, img_name);
        makedir(img_name)
        % Do times
        for j = 1 : times
            % Transform image
            image = transform_image(values{i});
            % Binarize
            %level = graythresh(image);
            %image = im2bw(image, level);
            % And write it
            imwrite(image, fullfile(img_name, [int2str(j) '.jpg']))
        end
    end
end

