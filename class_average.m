function class_avg = class_average(img_cache)
    % Counter of current class
    i = 1;
    class_avg = containers.Map();
    % While class isn't empty
    while 1
        % Try to find class
        found_class = find_class(img_cache, ['image' int2str(i)]);
        if (isempty(found_class.keys))
            break
        end
        % Tmp values
        tmpval = found_class.values;
        tmp_avg = 0;
        % Sum every value
        for j = 1 : numel(tmpval)
            tmp_avg = tmp_avg + tmpval{j};
        end
        
        % Write average of class
        class_avg(int2str(i)) = tmp_avg / numel(tmpval);
        % Next class
        i = i + 1;
    end
end

