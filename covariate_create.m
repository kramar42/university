function cache_new = covariate_create(cache, n)
   tmp_cache = containers.Map;
   for i = 1 : n
       tmp = find_class(cache,['image' int2str(i)]);
       value_set = tmp.values;
       matrix = [];
       for j = 1 : numel(tmp.values)
           temp = value_set{j};
           matrix(j, :) = temp(:)';
       end
       tmp_cache(int2str(i)) = inv(cov(matrix));
   end
   cache_new = tmp_cache;
end