function image = rotate(image, angle)
    % Choose random angle
    phy  = (angle - 0.5) * 30;
    
    % Create affine transformation
    tform = maketform('affine', [cos(phy) sin(phy) 0; ...
                                -sin(phy) cos(phy) 0; ...
                                0 0 1]);
    
    % Apply it
    image = imtransform(image, tform, 'FillValues', 255);
end