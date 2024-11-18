public class HardDrive {
    public byte[] read(long lba, int size) {
        System.out.println("HardDrive reading data.");
        return new byte[size];
    }
}