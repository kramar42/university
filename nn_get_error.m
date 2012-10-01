function error = nn_get_error(unknown_cache, nn, class_num)   
    
    error = cell([1 class_num]);
    for i=1:class_num
        error{i} = cell([1 class_num]);
    end
     for i=1:class_num
        tmpclass = find_class(unknown_cache,['image' num2str(i)]);
        valueset = tmpclass.values;
        keyset = tmpclass.keys;
        for j=1:numel(valueset)
            class = nn_recognize(nn,valueset{j});
            error{i}{class}{numel(error{i}{class}) + 1} = keyset{j};
        end
     end
end