function image = crop_image(image)

    image_size = size(image);
    height = image_size(1);
    width = image_size(2);

    % Sum of rows and columns
    horizontal_sum = sum(image, 1);
    gorizontal_sum = sum(image, 2);

    % Index
    horizontal_index = find(horizontal_sum < height * 255 - 10);
    gorizontal_index = find(gorizontal_sum < width * 255 - 10);

    image = image(gorizontal_index(1):gorizontal_index(end), ...
        horizontal_index(1):horizontal_index(end));

end

