CREATE TABLE employes (id INT PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(255), prenom VARCHAR(255), salaire DECIMAL, id_service INT);
INSERT employes(id, nom, prenom, salaire, id_service) VALUES (NULL, "Jean", "Bidule", "1500", "1"), (NULL, "Gertrude", "Labas", "2700", "1"), (NULL, "Nique", "Zebi", "4000", "2"), (NULL, "Sucka", "Blyat", "5000", "2"), (NULL, "Edy", "Narouille", "6000", "2");
SELECT *FROM employes WHERE salaire > "3000";