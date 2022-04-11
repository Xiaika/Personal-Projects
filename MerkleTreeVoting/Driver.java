public class Driver
{
    public static void main(String[] Args)
    {
        //Create voting machine
        VotingMachine vmachine = new VotingMachine("Williamson", "Texas", "Trump", "Biden", "./MerkleTree/src/Ballots.txt");
        vmachine.startMachine();
        //Create counting machine
        CountingMachine cmachine = new CountingMachine(vmachine);

        //Output
        cmachine.printBallots();
        System.out.println();
        cmachine.printTrees();
        System.out.println();
        cmachine.printCriminals();
        cmachine.tabulateBallots();
    }
}
