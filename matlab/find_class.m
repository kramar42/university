function found_class = find_class(img_cache, class)
    % Save keys
    keys = img_cache.keys;
    % New container
    found_class = containers.Map();
    % For every key
    for i = 1 : numel(keys)
        % If found class
        if ~isempty(strfind(keys{i}, ['/' class '/']))
            % Save it in contaiter
            found_class(keys{i}) = img_cache(keys{i});
        end
    end
end

