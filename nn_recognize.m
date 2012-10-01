function class = nn_recognize(nn,img)
    result = nn(img(:));
    class = find(result == max(result));
end