function output = stats (error_matrix)
    success = 0;
    fail = 0;
    for i = 1 : numel(error_matrix)
        for j = 1 : numel(error_matrix{i})
            if i == j
                success = success + numel(error_matrix{i}{j});
            else
                fail = fail + numel(error_matrix{i}{j});
            end
        end
    end
    percent = double(success)/(success+fail);
    output = [ percent success fail ];
end
