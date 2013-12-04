function [name] = get_name(name)
    pos = strfind(name, '.');
    name = name(1 : pos(end) - 1);
end

