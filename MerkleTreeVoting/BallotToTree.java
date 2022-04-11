import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
public class BallotToTree
{
    private final MerkleTree tree;
    private final Ballot ballot;

    /* convert an integer into bytes*/
    public byte[] intToBytes(int i)
    {
        byte[] bytes = new byte[4];

        bytes[0] = (byte) (i >> 24);
        bytes[1] = (byte) (i >> 16);
        bytes[2] = (byte) (i >> 8);
        bytes[3] = (byte) (i);
        return bytes;
    }

    public BallotToTree(Ballot ballot)
    {
        this.ballot = ballot;
        //Choose SHA-256 digest for hash. Required to catch error
        MessageDigest sha = null;
        try{ sha = MessageDigest.getInstance("SHA"); }
        catch (NoSuchAlgorithmException e)
        {
            System.out.println("Specified algorithm does not exist.");
            e.printStackTrace();
            System.exit(0);
        }

        //Build tree using SHA-256 hashing

        //Convert strings and integers in ballot to bytes
        final byte[] leaf1 = ballot.getName().getBytes();
        final byte[] leaf2 = intToBytes(ballot.getAge());
        final byte[] leaf3 = intToBytes(ballot.getId());
        final byte[] leaf4 = ballot.getVote().getBytes();

        //Create nodes from the byte arrays
        Node node1 = new Node(leaf1);
        Node node2 = new Node(leaf2);
        Node node3 = new Node(leaf3);
        Node node4 = new Node(leaf4);

        //Finally create the tree from the leaves using the specified SHA-256 hash algorithm
        MerkleTree tree = new MerkleTree(sha);
        tree.insert(node1, node2);
        tree.insert(node3, node4);

        this.tree = tree;
    }

    public MerkleTree getTree() { return this.tree; }
    public Ballot getBallot() { return this.ballot; }
    public String getRootHash() { return tree.toString(tree.getHashValue()); }
}
