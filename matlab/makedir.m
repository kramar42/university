% Creates directory without warings.
function [] = makedir (name)
    if ~isdir(name)
        mkdir(name)
    end
end
