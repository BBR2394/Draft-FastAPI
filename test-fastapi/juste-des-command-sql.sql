SELECT * FROM disease_type;

SELECT * FROM disease

INSERT INTO disease (name_disease, description) VALUES ('Maladie 1', 'ceci est une description de la maladie 1');

SELECT med.name,  ARRAY_AGG(ARRAY["type"])  FROM medicine AS med LEFT JOIN medecine_type AS medtpe ON medtpe.id = ANY(list_type) GROUP BY med.name;

