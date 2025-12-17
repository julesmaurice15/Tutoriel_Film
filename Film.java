
public class Film
{
    private int duree;
    private String dateSortie;
    private Categorie categorie;

    public Film()
    {
        // initialisation des variables d'instance
        duree = 0;
        dateSortie = "2001/01/01";
    }

    public int getDuree()
    {
        return this.duree;
    }
    
    public void setDuree(int duree)
    {
        this.duree = duree;
    }
    
    public String getDateSortie()
    {
        return this.dateSortie;
    }
    
    public void setDateSortie(String dateSortie)
    {
        this.dateSortie = dateSortie;
    }
    
    public void setCategorie(Categorie categorie)
    {
        this.categorie = categorie;
    }
    
    public Categorie getCategorie()
    {
        return this.categorie;
    }
    
    public String description()
    {
        return "Je suis un film de catégorie " + this.categorie.getNom() + " et de durée " + this.duree + " sorti en " + this.dateSortie;
    }
    
}
