-- script that lists all bands with glam rock as their main style, ranked by their longevity
-- columns: band_name and lifespan
SELECT band_name, IFNULL(split,2023) - formed as lifespan from metal_bands WHERE style LIKE "%Glam rick%" ORDER BY lifespan DESC
