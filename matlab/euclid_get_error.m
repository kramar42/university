function error = euclid_get_error (unknown_cache, avg_cache)
    % Cell of result
    error = cell([1 numel(avg_cache.values)]);
    % Creating cells in Cell
    for i = 1 : numel(avg_cache.values)
        error{i} = cell([1 numel(avg_cache.values)]);
    end
    
    % For every class
    for i = 1 : numel(avg_cache.values)
        % Find that class
        tmpclass = find_class(unknown_cache,['image' num2str(i)]);
        % Get it's values and keys
        values = tmpclass.values;
        keys = tmpclass.keys;
        
        % For every picture
        for j = 1 : numel(values)
            % Count distance
            class = euclid_distance(values{j}, avg_cache);
            % And write in Cells
            error{i}{class}{numel(error{i}{class})+1} = keys{j};
        end
     end
end
