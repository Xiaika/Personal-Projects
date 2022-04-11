import java.security.MessageDigest;
import java.util.Base64;

public class MerkleTree
{
    private byte[] hashValue;
    private MerkleTree leftTree= null;
    private MerkleTree rightTree = null;
    private Node leftLeaf = null;
    private Node rightLeaf = null;
    private final MessageDigest sha;


    /*Initialize empty tree*/
    public MerkleTree(MessageDigest sha){ this.sha = sha; }

    public MerkleTree(MessageDigest sha, Node leftLeaf, Node rightLeaf)
    {
        this.sha = sha;
        insert(leftLeaf, rightLeaf);
    }

    /*insert new leaves*/
    public void insert(Node leftLeaf, Node rightLeaf)
    {
        this.leftLeaf = leftLeaf;
        this.rightLeaf = rightLeaf;

        //Generate hash of new leaves
        sha.update(hash(leftLeaf));
        this.hashValue = sha.digest(hash(rightLeaf));
    }

    /*hash function to build a hash from the data in the leaf node*/
    private byte[] hash(Node leaf)
    {
        //Need to use java Message digest to hash each byte in the list
        final byte[] value = leaf.bytes;
        this.hashValue = sha.digest(value);
        return this.hashValue;
    }


    public String toString(byte[] bytes)
    {
        return Base64.getEncoder().encodeToString(bytes);
    }

    public byte[] getHashValue() { return hashValue; }
    public MerkleTree getLeftTree() { return leftTree; }
    public MerkleTree getRightTree() { return rightTree; }
    public Node getLeftLeaf() { return leftLeaf; }
    public Node getRightLeaf() { return rightLeaf; }

}
