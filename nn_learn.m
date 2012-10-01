function net = nn_learn(learn_cache,class_num)
    values = learn_cache.values;
    keys = learn_cache.keys;
    Y = zeros(class_num,numel(values));
    X = zeros(numel(values{1}),numel(values));
    
    for j = 1 : numel(values)
        name = '/image';
        tmpkey = keys{j};
        index = strfind(tmpkey,name);
        tmpnum = tmpkey(index+numel(name));
        if tmpkey(index + numel(name) + 1) ~= '/'
            tmpnum = strcat(tmpnum,tmpkey(index+numel(name)+1));
        end
        class = str2num(tmpnum);
            
         Y(class, j) = 1;
         X(:, j) = values{j}(:);
    end
    
    net = newff(minmax(X), [30 class_num], {'logsig' 'logsig'}, 'trainscg');

    net.performFcn = 'sse';
    net.trainParam.goal = 0.001;
    net.trainParam.min_grad = 1E-10;
    net.trainParam.epochs = 5000;
    net = init(net);
    net = train(net, X, Y);
    end
