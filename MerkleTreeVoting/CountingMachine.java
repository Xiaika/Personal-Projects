import java.io.FileNotFoundException;
import java.io.FileReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.stream.*;

public class CountingMachine extends ElectionMachine
{
    private ArrayList<Ballot> criminals;
    private final ArrayList<Ballot> ballots;
    private ArrayList<BallotToTree> trees;
    int count = 0;

    public CountingMachine(VotingMachine vm)
    {
        this.county = vm.county;
        this.state = vm.state;
        this.republican = vm.republican;
        this.democrat = vm.democrat;
        this.ballots = new ArrayList<>();
        this.criminals = new ArrayList<>();
        this.trees = new ArrayList<>();
        readBallotsFromFile(vm.getBallotFile());
        buildTree();
        fraudCheck();
    }

    private void buildTree()
    {
        for(Ballot b: ballots) { trees.add(new BallotToTree(b)); }
    }

    private void fraudCheck()
    {
        //Search the tree array for duplicates
        for(int j = 0; j < trees.size(); j++)
        {
            for(int k = 0; k < trees.size(); k++)
            {
                //if a fraudulent ballot is found invalidate it
                if (j != k && trees.get(j).getRootHash().equals(trees.get(k).getRootHash())) {
                    trees.get(j).getBallot().invalidate();
                }
            }
        }
        trees = removeFraud(trees);
    }

    private ArrayList<BallotToTree> removeFraud(ArrayList<BallotToTree> trees)
    {
        ArrayList<BallotToTree> filtered = new ArrayList<>();
        for(BallotToTree t : trees)
        {
            if(t.getBallot().valid)
            {
                filtered.add(t);
            }
            else if(!t.getBallot().valid)
            {
                if(criminals.contains(t.getBallot()))
                continue;
                else
                    criminals.add(t.getBallot());
            }
            else
                System.out.println("Error");
        }
        return filtered;
    }

    public void tabulateBallots()
    {
        int gopVotes = 0;
        int demVotes = 0;
        int other = 0;
        String vote;
        for(BallotToTree t : trees)
        {
            vote = t.getBallot().getVote();
            if(vote.equals(republican)) { gopVotes++; }
            else if(vote.equals(democrat)) { demVotes++; }
            else { other++; }
        }

        System.out.println(republican + " votes: " + gopVotes);
        System.out.println(democrat + " votes:  " + demVotes);
        if(other > 0) { System.out.println("Other votes: " + other); }
        if(gopVotes > demVotes)
            System.out.println(republican + " wins!");
        else System.out.println(democrat + " wins!");
    }

    public void printBallots()
    {
        for(Ballot b : this.ballots)
        { System.out.println(b.toString()); }
    }

    public void printTrees()
    {
        for(BallotToTree t : trees)
        {
            System.out.println("Hash " + t.getRootHash());
        }
    }

    public void printCriminals()
    {
        System.out.println();
        System.out.println("________________CRIMINAL LIST________________");
        for(Ballot b : criminals)
        {
            System.out.println("Name: " + b.getName() + ", ID: " + b.getId());
        }
        System.out.println("---------------------------------------------");
    }

    public void readBallotsFromFile(String filename)
    {
        //Open input file
        Scanner infile = null;

        try { infile = new Scanner(new FileReader(filename)); }
        catch (FileNotFoundException e)
        {
            System.out.println("File not found.");
            e.printStackTrace();
            System.exit(0);
        }
        //Create Variables for ballot data
        String name, vote;
        int age, id;
        while(infile.hasNextLine())
        {
            String line = infile.nextLine();
            StringTokenizer tokenizer = new StringTokenizer(line);
            name = tokenizer.nextToken();
            age = Integer.parseInt(tokenizer.nextToken());
            id = Integer.parseInt(tokenizer.nextToken());
            vote = tokenizer.nextToken();
            Ballot temp = new Ballot(name, age, id, vote);
            ballots.add(temp);
            count++;
        }
        infile.close();
    }
}
