function [image] = transform_image(image)
    n = round(rand()) + 1;
    for i = 1 : n
        switch (round(rand() * 3))
            case 0
                image = rotate(image, rand());
            case 1
                image = imnoise(image,'salt & pepper',rand(1)*(0.2)+0.1);
            case 2
                h = fspecial('disk',rand(1)*(2)+1);
                image = imfilter(image, h);
            case 3
                h = fspecial('motion',rand()+1,rand());
                image = imfilter(image, h);
        end
    end
    %image = im2double(image);
    %level = graythresh(image);
    %image = im2bw(image, level);
end

