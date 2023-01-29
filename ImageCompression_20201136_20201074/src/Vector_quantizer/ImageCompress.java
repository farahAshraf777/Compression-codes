package Vector_quantizer;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Vector;

import javax.imageio.ImageIO;

public class ImageCompress {
//	ReadWriteImage w;
	int VectorHeight;
	int VectorWidth;
	int NewVectorHeight;
	int NewVectorWidth;
	Vector<Vector<Integer>> block = new Vector<>();
	Vector<Vector<Integer>> CodeBook = new Vector<>();
//	public int getNewVectorHeight() {
//		return NewVectorHeight;
//	}
//
//	public void setNewVectorHeight(int newVectorHeight) {
//		NewVectorHeight = newVectorHeight;
//	}
//
//	public int getNewVectorWidth() {
//		return NewVectorWidth;
//	}
//
//	public void setNewVectorWidth(int newVectorWidth) {
//		NewVectorWidth = newVectorWidth;
//	}

	public Vector<Vector<Integer>> getBlock() {
		return block;
	}

	public void setBlock(Vector<Integer> temp) {
		block.add(temp);
	}

	public int getVectorHeight() {
		return VectorHeight;
	}

	public void setVectorHeight(int vectorHeight) {
		VectorHeight = vectorHeight;
	}

	public int getVectorWidth() {
		return VectorWidth;
	}

	public void setVectorWidth(int vectorWidth) {
		VectorWidth = vectorWidth;
	}

	public Vector<Vector<Integer>> getCodeBook() {
		return CodeBook;
	}

	public void setCodeBook(Vector<Vector<Integer>> codeBook) {
		CodeBook = codeBook;
	}
	public int[][] squareImage(int [][] image)  {
		NewVectorHeight=image.length;
		NewVectorWidth=image[0].length;
		
		if(image.length % VectorHeight != 0) {
			NewVectorHeight=((image.length/VectorHeight)+1)*VectorHeight;
		}
		if((image[0].length) % VectorWidth != 0) {
			NewVectorWidth=(((image[0].length)/VectorWidth)+1)*VectorWidth;
		}
		
		int row =0 ;
		int col =0 ;
		int[][] squareImage= new int [NewVectorHeight][NewVectorWidth];
		for(int i =0 ; i<NewVectorHeight;i++) {
			row=i;
			for(int j =0 ; j<NewVectorWidth;j++) {
				col=j;
				if((i+1)>image.length||(j+1)>image[0].length) {
					squareImage[i][j]=0;
				}
				else {
					squareImage[i][j]=image[row][col];
				}
			}
			
		}
		return squareImage;	
	}
	public Vector<Vector<Integer>> getVectors(int [][] squareImage){
//		Vector<Vector<Integer>> block = new Vector<>();
//		int counter=0;
		for (int row = 0; row < NewVectorHeight; row += getVectorHeight()) {
            for (int column = 0; column < NewVectorWidth; column += getVectorWidth()) {
            	Vector temp = new Vector();
                for (int k = row; k <row+ getVectorHeight(); k++) {
                    for (int l = column; l <column+ getVectorWidth(); l++) {
                        temp.add(squareImage[k][l]);                        
                    }
                    setBlock(temp);
//                    counter += 1;
                    
                }
                
            }
            
        }
		System.out.println(getBlock());
		return getBlock();
	}
	public Vector<Integer> K_mean(Vector<Vector <Integer>> blockvec){
		Vector<Integer> mean = new Vector<>();
		int average=0;
		for(int s=0; s<(getVectorHeight()*getVectorWidth()); s++) {
			for(int i=0; i<blockvec.size(); i++) {
				average += blockvec.get(i).get(s); 
			}
			mean.add(average/(blockvec.size()));
			average = 0;
		}
		return mean;
	}
	public int NearestPosition(Vector<Integer> mainVector, Vector<Integer> SplitVector){
		int nearest=0;
		for(int i=0; i<SplitVector.size(); i++) {
			nearest += Math.abs(SplitVector.get(i)- mainVector.get(i));
		}
		
		return nearest;
	}
	// position of block according to code book
	public Vector<Integer> getPosition(){
		Vector<Integer> position = new Vector<>();
		int minimum = 10000, m=0, p=0;
		for(int j=0; j<block.size(); j++) {
			for(int i=0; i<CodeBook.size(); i++) {
				m = (NearestPosition(block.get(j), CodeBook.get(i)));
				if(m < minimum) {
					minimum = m;
					p = i;
				}
			}
			position.add(p);
		}
		return position;
	}
	

	public void PutInRight(int CodeBookLength, Vector<Vector<Integer>> V){
		if(CodeBookLength == 1) {
			if(V.size()>0) {
				CodeBook.add(K_mean(V));
			}
			
			return;
		}
		Vector<Integer> kmean = K_mean(V);
		
		Vector<Vector<Integer>> LeftVectors = new Vector<Vector<Integer>>();
		Vector<Vector<Integer>> RightVectors = new Vector<Vector<Integer>>();
		Vector<Integer> left = new Vector<>();
		Vector<Integer> right = new Vector<>();
		for(int i=0; i<kmean.size(); i++) {
			left.add(kmean.get(i)-1);
			right.add(kmean.get(i)+1);
		}
		for(int i=0; i<V.size(); i++) {
			int r = NearestPosition(V.get(i), right);
			int l = NearestPosition(V.get(i), left);
			if(r > l) {
				LeftVectors.add(V.get(i));
			}else {
				RightVectors.add(V.get(i));
				
			}
		}
		
		PutInRight((CodeBookLength / 2), RightVectors);
		PutInRight((CodeBookLength / 2), LeftVectors);
		
	}
	public void Compress(Vector<Integer> position) throws IOException {
		FileWriter myWriter = new FileWriter("new.txt");
		for(int i=0; i<position.size(); i++) {
			
		      myWriter.write(Integer.toBinaryString(position.get(i)));
		      
		}
		myWriter.close();
	}
	
	
}
