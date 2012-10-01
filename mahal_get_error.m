function error = mahal_get_error(unknown_cache, avg_cache, cov_cache)
    error = cell([1 numel(avg_cache.values)]);
    for i = 1 : numel(avg_cache.values)
        error{i} = cell([1 numel(avg_cache.values)]);
    end
    for i = 1 : numel(avg_cache.values)
        tmpclass = find_class(unknown_cache,['image' num2str(i)]);
        valueset = tmpclass.values;
        keyset = tmpclass.keys;
        for j = 1 : numel(valueset)
            class = mahalanobis_distance(valueset{j}, avg_cache, cov_cache);
            error{i}{class}{numel(error{i}{class})+1} = keyset{j};
        end
     end
end
