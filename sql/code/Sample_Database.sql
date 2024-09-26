/* Capturar os dados brutos para o calculo das vendas e associar cada venda ao seu respectivo artista e gênero musical */
WITH sales_data AS (
    SELECT
        ar.Name AS artist,
        ge.Name AS genre,
        il.UnitPrice * il.Quantity AS sales
    FROM
        InvoiceLine il
    JOIN
        Track tr ON il.TrackId = tr.TrackId
    JOIN
        Genre ge ON tr.GenreId = ge.GenreId
    JOIN
        Album al ON tr.AlbumId = al.AlbumId
    JOIN
        Artist ar ON al.ArtistId = ar.ArtistId
),
/* Calcular o total de vendas para cada gênero */
genre_totals AS (
    SELECT
        genre,
        SUM(sales) AS total_sales
    FROM
        sales_data
    GROUP BY
        genre
),
/* Calcular o total de vendas combinando artirta e gênero */
artist_genre_sales AS (
    SELECT
        artist,
        genre,
        SUM(sales) AS sales
    FROM
        sales_data
    GROUP BY
        artist,
        genre
)
/* combina as subqueries artist_genre_sales e genre_totals para calcular a porcentagem de vendas de cada artista dentro de um gênero específico e também a soma acumulada dessas porcentagens */
SELECT
    ags.artist,
    ags.genre,
    ags.sales,
    ROUND((ags.sales / gt.total_sales) * 100, 2) AS sales_by_percentage_by_genre,
    ROUND(SUM((ags.sales / gt.total_sales) * 100) OVER (PARTITION BY ags.genre ORDER BY ags.sales DESC), 2) AS cumulative_sum_by_genre
FROM
    artist_genre_sales ags
JOIN
    genre_totals gt ON ags.genre = gt.genre
ORDER BY
    ags.genre ASC,
    sales_by_percentage_by_genre DESC
LIMIT 10;
