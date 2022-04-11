import java.io.*;
import java.util.Scanner;

public class VotingMachine extends ElectionMachine
{
    private final String ballotFile;
    public VotingMachine(String county, String state, String republican, String democrat, String ballotFile)
    {
        this.county = county;
        this.state = state;
        this.republican = republican;
        this.democrat = democrat;
        this.ballotFile = ballotFile;
    }

    public String getBallotFile() { return ballotFile; }

    public void printBallotToFile(String name, int id, int age, String vote)
    {
        PrintWriter outfile = null;
        try
        {
            FileWriter fileWriter = new FileWriter(ballotFile, true);
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
            outfile = new PrintWriter(bufferedWriter);
        }
        catch (IOException e)
        {
            System.out.println("File not found.");
            e.printStackTrace();
            System.exit(0);
        }
        outfile.append(name + " " + age + " " + id + " " + vote + '\n');
        outfile.close();
    }

    public void startMachine()
    {
        while(true)
        {
            System.out.println("Welcome to  " + county + " county precinct.");
            Scanner input = new Scanner(System.in);
            String name, vote = null;
            int age, id;
            System.out.println("Please enter your name: ");
            name = input.nextLine();
            if(name.equals("OFF")){ break; }
            System.out.println("Please enter your voter ID number: ");
            id = input.nextInt();
            System.out.println("Please enter your age: ");
            age = input.nextInt();
            if(age < 18)
            {
                System.out.println("You are not eligible to vote.");
                continue;
            }
            boolean validVote = false;
            int choice;
            System.out.println("Please choose your candidate");
            System.out.println("1) GOP: " + republican);
            System.out.println("2) DEM: " + democrat);
            while(!validVote)
            {
                choice = input.nextInt();
                if (choice == 1) { vote = republican;  validVote = true; }
                else if (choice == 2) { vote = democrat; validVote = true; }
                else { System.out.println("INVALID VOTE. Enter 1 or 2"); }
            }
            printBallotToFile(name, id, age, vote);
        }
    }
}
