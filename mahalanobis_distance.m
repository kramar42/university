function answ = mahalanobis_distance(img, avg_cache, cov_cache)
    keyset = avg_cache.keys;
    avg_valueset = avg_cache.values;
    cov_valueset = cov_cache.values;
    dist = zeros(numel(avg_valueset), 1);
    for i = 1 : numel(avg_valueset)
        tmp = avg_valueset{i};
        Cx = cov_valueset{i};
        Yc = img(:) - tmp(:);
        dist(i) = Yc' * Cx * Yc;
    end
    disp(min(abs(dist)))
    answ = str2num(keyset{abs(dist) == min(abs(dist))});
end