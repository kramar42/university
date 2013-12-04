function path = euclid_distance(img, avg_cache)
    % Keys & values
    keys = avg_cache.keys;
    values = avg_cache.values;
    
    dist = zeros(numel(values), 1);
    % Calculate diff
    for i = 1 : numel(values)
        dist(i) = norm(img(:) - values{i}(:),2);
    end
    % And return minimum diff
    path = str2num(keys{dist == min(dist)});
end
