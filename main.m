
    clear all
    % Size of pictures
    %size = [20 24];
    % Count of images
    %count = 200;
    % Create cache
    %create_cache(count, size)
    
    load('caches.mat')    
    disp('Caches loaded.')
    
    keys = img_cache.keys;
    images = zeros(numel(img_cache(keys{1}), numel(keys)));
    
    %euclid_error = euclid_get_error(unknown_cache, class_avg);
    %euclid_stats = stats(euclid_error);
    %disp('Counted euclid error.')
    
    %cov_cache = covariate_create(img_cache, numel(class_avg.values));
    %mahal_error = mahal_get_error(unknown_cache, class_avg, cov_cache);
    %mahal_stats = stats(mahal_error);
    %disp('Count mahalanobis error.')
    
    %nn = nn_learn(img_cache, numel(class_avg.values));
    %nn_error = nn_get_error(img_cache, nn, numel(class_avg.values));
    %disp('Calculated nn error.')
    %nn_stats = stats(nn_error);
    %disp('Count NN error.')
    