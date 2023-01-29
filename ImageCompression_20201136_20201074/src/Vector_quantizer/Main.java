package Vector_quantizer;

import java.io.IOException;
import java.util.Arrays;
import java.util.Vector;

public class Main {

	public static void main(String[] args) throws IOException {
		String path = "Capture2.PNG";
		ReadWriteImage g= new ReadWriteImage();
		
		ImageCompress i = new ImageCompress();
		i.setVectorHeight(2);
		i.setVectorWidth(2);
		
		int[][] square= i.squareImage(g.readImage(path));

		Vector<Vector<Integer>> l = i.getVectors(square);
		i.PutInRight(4, l);
		Vector<Integer> m = i.getPosition();
		i.Compress(m);
		

}

	}
	


