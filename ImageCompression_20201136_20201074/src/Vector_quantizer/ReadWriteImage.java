package Vector_quantizer;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class ReadWriteImage {
	public int[][] readImage(String filePath) {
        File file = new File(filePath);
        BufferedImage image;
        int width, height;
        try {
            image = ImageIO.read(file);
            width = image.getWidth();
            height = image.getHeight();
            int[][] pixels = new int[height][width];
            int rgb;
            for (int x = 0; x < width; x++) {
                for (int y = 0; y < height; y++) {
                    rgb = image.getRGB(x, y);
                    pixels[y][x] = (rgb>>16) & 0xff; // to get red color as our gray scale
//                    pixels[y][x] = rgb & 0xff; // to get blue
                }
            }
            return pixels;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
	
	 public void writeImage(int[][] pixels) {
	        int height = pixels.length;
	        int width = pixels[0].length;
	        BufferedImage image2 = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
	        for (int x = 0; x < width; x++) {
	            for (int y = 0; y < height; y++) {
	                image2.setRGB(x, y, (pixels[y][x]));
	            }
	        }
	       for(int i=0; i<height; i++) {
	    	   for(int j=0; j<width; j++) {
		    	   System.out.print(pixels[i][j] + " ");
		       }
	    	   System.out.println();
	       }
	    }
}

