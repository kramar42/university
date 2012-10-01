function cache = norm_cache(cache, size)
    keys = cache.keys;
    for i = 1 : numel(valueset)
        img = cache(keys{i});
        
        img = imresize(img, size);
        img = imadjust(img);
        img = im2double(img);
        img = img(:);
        
        cache(keys{i}) = img;
    end
end

