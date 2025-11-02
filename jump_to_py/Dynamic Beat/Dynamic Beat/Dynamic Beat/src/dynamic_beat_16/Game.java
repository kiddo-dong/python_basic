package dynamic_beat_16;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.RenderingHints;
import java.util.ArrayList;

import javax.swing.ImageIcon;

public class Game extends Thread {

	private Image noteRouteLineImage = new ImageIcon(Main.class.getResource("../images/noteRouteLine.png"))
			.getImage();
	private Image judgementLineImage = new ImageIcon(Main.class.getResource("../images/judgementLine.png"))
			.getImage();
	private Image gameInfoImage = new ImageIcon(Main.class.getResource("../images/gameInfo.png"))
			.getImage();
	private Image noteRouteSImage = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
	private Image noteRouteDImage = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
	private Image noteRouteFImage = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
	private Image noteRouteSpace1Image = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
	private Image noteRouteSpace2Image = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
	private Image noteRouteJImage = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
	private Image noteRouteKImage = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
	private Image noteRouteLImage = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
	private Image blueFlareImage;
	private Image judgeImage;
	private Image keyPadSImage = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();
	private Image keyPadDImage = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();
	private Image keyPadFImage = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();
	private Image keyPadSpace1Image = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();
	private Image keyPadSpace2Image = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();
	private Image keyPadJImage = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();
	private Image keyPadKImage = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();
	private Image keyPadLImage = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();

	private String titleName;
	private String difficulty;
	private String musicTitle;
	private Music gameMusic;
	
	ArrayList<Note> noteList = new ArrayList<Note>();
	
	public Game(String titleName, String difficulty, String musicTitle) {
		this.titleName = titleName;
		this.difficulty = difficulty;
		this.musicTitle = musicTitle;
		gameMusic = new Music(this.musicTitle, false);
	}
	
	public void screenDraw(Graphics2D g) {
		g.drawImage(noteRouteSImage, 228, 30, null);
		g.drawImage(noteRouteDImage, 332, 30, null);
		g.drawImage(noteRouteFImage, 436, 30, null);
		g.drawImage(noteRouteSpace1Image, 540, 30, null);
		g.drawImage(noteRouteSpace2Image, 640, 30, null);
		g.drawImage(noteRouteJImage, 744, 30, null);
		g.drawImage(noteRouteKImage, 848, 30, null);
		g.drawImage(noteRouteLImage, 952, 30, null);
		g.drawImage(noteRouteLineImage, 224, 30, null);
		g.drawImage(noteRouteLineImage, 328, 30, null);
		g.drawImage(noteRouteLineImage, 432, 30, null);
		g.drawImage(noteRouteLineImage, 536, 30, null);
		g.drawImage(noteRouteLineImage, 740, 30, null);
		g.drawImage(noteRouteLineImage, 844, 30, null);
		g.drawImage(noteRouteLineImage, 948, 30, null);
		g.drawImage(noteRouteLineImage, 1052, 30, null);
		g.drawImage(gameInfoImage, 0, 660, null);
		g.drawImage(judgementLineImage, 0, 580, null);
		for(int i = 0; i < noteList.size(); i++)
		{
			Note note = noteList.get(i);
			if(note.getY() > 620) {
				judgeImage = new ImageIcon(Main.class.getResource("../images/judgeMiss.png")).getImage();
			}
			if(!note.isProceeded()) {
				noteList.remove(i);
				i--;
			}
			else {
				note.screenDraw(g);
			}
		}
		g.setColor(Color.white);
		g.setRenderingHint( RenderingHints.KEY_TEXT_ANTIALIASING, 
				RenderingHints.VALUE_TEXT_ANTIALIAS_ON);
		g.setColor(Color.WHITE);
		g.setFont(new Font("Arial", Font.BOLD, 30));
		g.drawString(titleName, 20, 702);
		g.drawString(difficulty, 1190, 702);
		g.setFont(new Font("Arial", Font.PLAIN, 26));
		g.setColor(Color.DARK_GRAY);
		g.drawString("S", 270, 609);
		g.drawString("D", 374, 609);
		g.drawString("F", 478, 609);
		g.drawString("Space Bar", 580, 609);
		g.drawString("J", 784, 609);
		g.drawString("K", 889, 609);
		g.drawString("L", 993, 609);
		g.setColor(Color.LIGHT_GRAY);
		g.setFont(new Font("Elephant", Font.BOLD, 30));
		g.drawString("000000", 565, 702);
		g.drawImage(blueFlareImage, 300, 430, null);
		g.drawImage(judgeImage, 460, 420, null);
		g.drawImage(keyPadSImage, 228, 580, null);
		g.drawImage(keyPadDImage, 332, 580, null);
		g.drawImage(keyPadFImage, 436, 580, null);
		g.drawImage(keyPadSpace1Image, 540, 580, null);
		g.drawImage(keyPadSpace2Image, 640, 580, null);
		g.drawImage(keyPadJImage, 744, 580, null);
		g.drawImage(keyPadKImage, 848, 580, null);
		g.drawImage(keyPadLImage, 952, 580, null);
	}
	
	public void pressS() {
		judge("S");
		noteRouteSImage = new ImageIcon(Main.class.getResource("../images/noteRoutePressed.png")).getImage();
		keyPadSImage = new ImageIcon(Main.class.getResource("../images/keyPadPressed.png")).getImage();
		new Music("drumSmall1.mp3", false).start();
	}
	
	public void releaseS() {
		noteRouteSImage = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
		keyPadSImage = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();
	}
	
	public void pressD() {
		judge("D");
		noteRouteDImage = new ImageIcon(Main.class.getResource("../images/noteRoutePressed.png")).getImage();
		keyPadDImage = new ImageIcon(Main.class.getResource("../images/keyPadPressed.png")).getImage();
		new Music("drumSmall1.mp3", false).start();
	}
	
	public void releaseD() {
		noteRouteDImage = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
		keyPadDImage = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();
	}

	public void pressF() {
		judge("F");
		noteRouteFImage = new ImageIcon(Main.class.getResource("../images/noteRoutePressed.png")).getImage();
		keyPadFImage = new ImageIcon(Main.class.getResource("../images/keyPadPressed.png")).getImage();
		new Music("drumSmall1.mp3", false).start();
	}
	
	public void releaseF() {
		noteRouteFImage = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
		keyPadFImage = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();
	}

	public void pressSpace() {
		judge("Space");
		noteRouteSpace1Image = new ImageIcon(Main.class.getResource("../images/noteRoutePressed.png")).getImage();
		keyPadSpace1Image = new ImageIcon(Main.class.getResource("../images/keyPadPressed.png")).getImage();
		noteRouteSpace2Image = new ImageIcon(Main.class.getResource("../images/noteRoutePressed.png")).getImage();
		keyPadSpace2Image = new ImageIcon(Main.class.getResource("../images/keyPadPressed.png")).getImage();
		new Music("drumBig1.mp3", false).start();
	}
	
	public void releaseSpace() {
		noteRouteSpace1Image = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
		keyPadSpace1Image = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();
		noteRouteSpace2Image = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
		keyPadSpace2Image = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();
	}
	
	public void pressJ() {
		judge("J");
		noteRouteJImage = new ImageIcon(Main.class.getResource("../images/noteRoutePressed.png")).getImage();
		keyPadJImage = new ImageIcon(Main.class.getResource("../images/keyPadPressed.png")).getImage();
		new Music("drumSmall1.mp3", false).start();
	}
	
	public void releaseJ() {
		noteRouteJImage = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
		keyPadJImage = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();
	}
	
	public void pressK() {
		judge("K");
		noteRouteKImage = new ImageIcon(Main.class.getResource("../images/noteRoutePressed.png")).getImage();
		keyPadKImage = new ImageIcon(Main.class.getResource("../images/keyPadPressed.png")).getImage();
		new Music("drumSmall1.mp3", false).start();
	}
	
	public void releaseK() {
		noteRouteKImage = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
		keyPadKImage = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();
	}
	
	public void pressL() {
		judge("L");
		noteRouteLImage = new ImageIcon(Main.class.getResource("../images/noteRoutePressed.png")).getImage();
		keyPadLImage = new ImageIcon(Main.class.getResource("../images/keyPadPressed.png")).getImage();
		new Music("drumSmall1.mp3", false).start();
	}
	
	public void releaseL() {
		noteRouteLImage = new ImageIcon(Main.class.getResource("../images/noteRoute.png")).getImage();
		keyPadLImage = new ImageIcon(Main.class.getResource("../images/keyPadBasic.png")).getImage();
	}
	
	@Override
	public void run() {
		dropNotes(this.titleName);
	}
	
	public void close() {
		gameMusic.close();
		this.interrupt();
	}
	
	public void dropNotes(String titleName) {
		Beat[] beats = null;
		if (titleName.equals("Joakim Karud - Mighty Love") && difficulty.equals("Easy")) {
			int startTime = 4460 - Main.REACH_TIME * 1000;
			int gap = 125;
			beats = new Beat[] {
					new Beat(startTime, "S"),
					new Beat(startTime + gap * 2, "D"),
					new Beat(startTime + gap * 4, "S"),
					new Beat(startTime + gap * 6, "D"),
					new Beat(startTime + gap * 8, "S"),
					new Beat(startTime + gap * 10, "D"),
					new Beat(startTime + gap * 12, "S"),
					new Beat(startTime + gap * 14, "D"),
					new Beat(startTime + gap * 18, "J"),
					new Beat(startTime + gap * 20, "K"),
					new Beat(startTime + gap * 22, "J"),
					new Beat(startTime + gap * 24, "K"),
					new Beat(startTime + gap * 26, "J"),
					new Beat(startTime + gap * 28, "K"),
					new Beat(startTime + gap * 30, "J"),
					new Beat(startTime + gap * 32, "K"),
					new Beat(startTime + gap * 36, "S"),
					new Beat(startTime + gap * 38, "D"),
					new Beat(startTime + gap * 40, "S"),
					new Beat(startTime + gap * 42, "D"),
					new Beat(startTime + gap * 44, "S"),
					new Beat(startTime + gap * 46, "D"),
					new Beat(startTime + gap * 48, "J"),
					new Beat(startTime + gap * 49, "K"),
					new Beat(startTime + gap * 50, "L"),
					new Beat(startTime + gap * 52, "F"),
					new Beat(startTime + gap * 52, "Space"),
					new Beat(startTime + gap * 52, "J"),
					new Beat(startTime + gap * 54, "D"),
					new Beat(startTime + gap * 56, "S"),
					new Beat(startTime + gap * 58, "D"),
					new Beat(startTime + gap * 59, "S"),
					new Beat(startTime + gap * 61, "D"),
					new Beat(startTime + gap * 63, "S"),
					new Beat(startTime + gap * 65, "D"),
					new Beat(startTime + gap * 67, "J"),
					new Beat(startTime + gap * 69, "K"),
					new Beat(startTime + gap * 72, "J"),
					new Beat(startTime + gap * 74, "K"),
					new Beat(startTime + gap * 76, "J"),
					new Beat(startTime + gap * 78, "K"),
					new Beat(startTime + gap * 81, "J"),
					new Beat(startTime + gap * 83, "K"),
					new Beat(startTime + gap * 85, "S"),
					new Beat(startTime + gap * 87, "D"),
					new Beat(startTime + gap * 89, "S"),
					new Beat(startTime + gap * 91, "D"),
					new Beat(startTime + gap * 93, "S"),
					new Beat(startTime + gap * 95, "D"),
					new Beat(startTime + gap * 97, "J"),
					new Beat(startTime + gap * 99, "K"),
					new Beat(startTime + gap * 102, "L"),
					new Beat(startTime + gap * 104, "F"),
					new Beat(startTime + gap * 104, "Space"),
					new Beat(startTime + gap * 104, "J"),
					new Beat(startTime + gap * 106, "J"),
					new Beat(startTime + gap * 108, "K"),
					new Beat(startTime + gap * 110, "S"),
					new Beat(startTime + gap * 112, "J"),
					new Beat(startTime + gap * 114, "S"),
					new Beat(startTime + gap * 116, "Space"),
					new Beat(startTime + gap * 118, "S"),
					new Beat(startTime + gap * 120, "J"),
					new Beat(startTime + gap * 122, "K"),
					new Beat(startTime + gap * 124, "S"),
					new Beat(startTime + gap * 126, "D"),
					new Beat(startTime + gap * 128, "S"),
					new Beat(startTime + gap * 128, "k"),
					new Beat(startTime + gap * 130, "Space"),
					new Beat(startTime + gap * 132, "S"),
					new Beat(startTime + gap * 134, "D"),
					new Beat(startTime + gap * 136, "F"),
					new Beat(startTime + gap * 138, "Space"),
					new Beat(startTime + gap * 140, "J"),
					new Beat(startTime + gap * 142, "K"),
					new Beat(startTime + gap * 144, "L"),
					new Beat(startTime + gap * 146, "S"),
					new Beat(startTime + gap * 148, "D"),
					new Beat(startTime + gap * 150, "S"),
					new Beat(startTime + gap * 152, "S"),
					new Beat(startTime + gap * 154, "D"),
					new Beat(startTime + gap * 156, "D"),
					new Beat(startTime + gap * 158, "F"),
					new Beat(startTime + gap * 160, "F"),
					new Beat(startTime + gap * 162, "Space"),
					new Beat(startTime + gap * 164, "Space"),
					new Beat(startTime + gap * 166, "J"),
					new Beat(startTime + gap * 168, "J"),
					new Beat(startTime + gap * 170, "k"),
					new Beat(startTime + gap * 172, "k"),
					new Beat(startTime + gap * 174, "L"),
					new Beat(startTime + gap * 176, "L"),
					new Beat(startTime + gap * 178, "D"),
					new Beat(startTime + gap * 180, "S"),
					new Beat(startTime + gap * 182, "D"),
					new Beat(startTime + gap * 184, "S"),
					new Beat(startTime + gap * 186, "D"),
					new Beat(startTime + gap * 190, "S"),
					new Beat(startTime + gap * 194, "D"),
					new Beat(startTime + gap * 196, "J"),
					new Beat(startTime + gap * 198, "K"),
					new Beat(startTime + gap * 200, "J"),
					new Beat(startTime + gap * 202, "K"),
					new Beat(startTime + gap * 204, "J"),
					new Beat(startTime + gap * 206, "K"),
					new Beat(startTime + gap * 208, "J"),
					new Beat(startTime + gap * 210, "K"),
					new Beat(startTime + gap * 212, "S"),
					new Beat(startTime + gap * 214, "D"),
					new Beat(startTime + gap * 216, "S"),
					new Beat(startTime + gap * 218, "D"),
					new Beat(startTime + gap * 220, "S"),
					new Beat(startTime + gap * 222, "D"),
					new Beat(startTime + gap * 224, "J"),
					new Beat(startTime + gap * 226, "K"),
					new Beat(startTime + gap * 228, "L"),
					new Beat(startTime + gap * 230, "F"),
					new Beat(startTime + gap * 232, "Space"),
					new Beat(startTime + gap * 234, "J"),
					new Beat(startTime + gap * 236, "D"),
					new Beat(startTime + gap * 238, "S"),
					new Beat(startTime + gap * 240, "D"),
					new Beat(startTime + gap * 242, "D"),
					new Beat(startTime + gap * 244, "S"),
					new Beat(startTime + gap * 246, "D"),
					new Beat(startTime + gap * 248, "J"),
					new Beat(startTime + gap * 250, "K"),
					new Beat(startTime + gap * 252, "J"),
					new Beat(startTime + gap * 254, "K"),
					new Beat(startTime + gap * 256, "J"),
					new Beat(startTime + gap * 258, "K"),
					new Beat(startTime + gap * 260, "J"),
					new Beat(startTime + gap * 262, "K"),
					new Beat(startTime + gap * 264, "S"),
					new Beat(startTime + gap * 266, "D"),
					new Beat(startTime + gap * 268, "S"),
					new Beat(startTime + gap * 270, "D"),
					new Beat(startTime + gap * 272, "S"),
					new Beat(startTime + gap * 274, "D"),
					new Beat(startTime + gap * 276, "J"),
					new Beat(startTime + gap * 278, "K"),
					new Beat(startTime + gap * 280, "L"),
					new Beat(startTime + gap * 282, "F"),
					new Beat(startTime + gap * 284, "Space"),
					new Beat(startTime + gap * 286, "J"),
					new Beat(startTime + gap * 288, "J"),
					new Beat(startTime + gap * 290, "K"),
					new Beat(startTime + gap * 292, "S"),
					new Beat(startTime + gap * 294, "J"),
					new Beat(startTime + gap * 296, "k"),
					new Beat(startTime + gap * 298, "L"),
					new Beat(startTime + gap * 300, "L"),
					new Beat(startTime + gap * 302, "D"),
					new Beat(startTime + gap * 304, "S"),
					new Beat(startTime + gap * 306, "D"),
					new Beat(startTime + gap * 308, "S"),
					new Beat(startTime + gap * 310, "D"),
					new Beat(startTime + gap * 312, "S"),
					new Beat(startTime + gap * 314, "D"),
					new Beat(startTime + gap * 316, "J"),
					new Beat(startTime + gap * 318, "D"),
					new Beat(startTime + gap * 320, "S"),
					new Beat(startTime + gap * 324, "Space"),
					new Beat(startTime + gap * 326, "J"),
					new Beat(startTime + gap * 328, "K"),
					new Beat(startTime + gap * 330, "L"),
					new Beat(startTime + gap * 332, "K"),
					new Beat(startTime + gap * 334, "S"),
					new Beat(startTime + gap * 336, "K"),
					new Beat(startTime + gap * 338, "J"),
					new Beat(startTime + gap * 340, "K"),
					new Beat(startTime + gap * 342, "S"),
					new Beat(startTime + gap * 346, "D"),
					new Beat(startTime + gap * 348, "S"),
					new Beat(startTime + gap * 350, "D"),
					new Beat(startTime + gap * 352, "S"),
					new Beat(startTime + gap * 354, "D"),
					new Beat(startTime + gap * 358, "J"),
					new Beat(startTime + gap * 360, "K"),
					new Beat(startTime + gap * 362, "L"),
					new Beat(startTime + gap * 364, "F"),
					new Beat(startTime + gap * 366, "S"),
					new Beat(startTime + gap * 369, "D"),
					new Beat(startTime + gap * 372, "J"),
					new Beat(startTime + gap * 375, "D"),
					new Beat(startTime + gap * 378, "S"),
					new Beat(startTime + gap * 381, "Space"),
					new Beat(startTime + gap * 384, "J"),
					new Beat(startTime + gap * 387, "K"),
					new Beat(startTime + gap * 390, "L"),
					new Beat(startTime + gap * 393, "K"),
					new Beat(startTime + gap * 396, "S"),
					new Beat(startTime + gap * 399, "K"),
					new Beat(startTime + gap * 402, "J"),
					new Beat(startTime + gap * 405, "F"),
					new Beat(startTime + gap * 408, "L"),
					new Beat(startTime + gap * 401, "K"),
					new Beat(startTime + gap * 404, "S"),
					new Beat(startTime + gap * 407, "J"),
					new Beat(startTime + gap * 410, "F"),
					new Beat(startTime + gap * 410, "Space"),
					new Beat(startTime + gap * 410, "J"),
			};
		}
		else if(titleName.equals("Joakim karud - Mighty Love") && difficulty.equals("Hard")) {
			int startTime = 4460 - Main.REACH_TIME * 1000;
			int gap = 125;
			beats = new Beat[] {
					new Beat(startTime + gap * 1, "S"),
					new Beat(startTime + gap * 2, "D"),
					new Beat(startTime + gap * 3, "S"),
					new Beat(startTime + gap * 4, "D"),
					new Beat(startTime + gap * 5, "S"),
					new Beat(startTime + gap * 6, "D"),
					new Beat(startTime + gap * 7, "S"),
					new Beat(startTime + gap * 8, "D"),
					new Beat(startTime + gap * 9, "S"),
					new Beat(startTime + gap * 10, "D"),
					new Beat(startTime + gap * 12, "S"),
					new Beat(startTime + gap * 14, "D"),
					new Beat(startTime + gap * 18, "J"),
					new Beat(startTime + gap * 19, "K"),
					new Beat(startTime + gap * 20, "J"),
					new Beat(startTime + gap * 21, "K"),
					new Beat(startTime + gap * 22, "J"),
					new Beat(startTime + gap * 23, "K"),
					new Beat(startTime + gap * 24, "J"),
					new Beat(startTime + gap * 25, "D"),
					new Beat(startTime + gap * 26, "J"),
					new Beat(startTime + gap * 28, "K"),
					new Beat(startTime + gap * 30, "J"),
					new Beat(startTime + gap * 32, "K"),
					new Beat(startTime + gap * 36, "S"),
					new Beat(startTime + gap * 38, "D"),
					new Beat(startTime + gap * 40, "S"),
					new Beat(startTime + gap * 42, "D"),
					new Beat(startTime + gap * 44, "S"),
					new Beat(startTime + gap * 46, "D"),
					new Beat(startTime + gap * 48, "J"),
					new Beat(startTime + gap * 49, "K"),
					new Beat(startTime + gap * 50, "L"),
					new Beat(startTime + gap * 52, "F"),
					new Beat(startTime + gap * 52, "Space"),
					new Beat(startTime + gap * 52, "J"),
					new Beat(startTime + gap * 54, "D"),
					new Beat(startTime + gap * 56, "S"),
					new Beat(startTime + gap * 58, "D"),
					new Beat(startTime + gap * 59, "S"),
					new Beat(startTime + gap * 61, "D"),
					new Beat(startTime + gap * 63, "S"),
					new Beat(startTime + gap * 65, "D"),
					new Beat(startTime + gap * 67, "J"),
					new Beat(startTime + gap * 56, "D"),
					new Beat(startTime + gap * 58, "S"),
					new Beat(startTime + gap * 59, "F"),
					new Beat(startTime + gap * 61, "J"),
					new Beat(startTime + gap * 63, "L"),
					new Beat(startTime + gap * 65, "K"),
					new Beat(startTime + gap * 67, "J"),
					new Beat(startTime + gap * 69, "K"),
					new Beat(startTime + gap * 72, "J"),
					new Beat(startTime + gap * 74, "K"),
					new Beat(startTime + gap * 76, "J"),
					new Beat(startTime + gap * 78, "K"),
					new Beat(startTime + gap * 81, "J"),
					new Beat(startTime + gap * 83, "K"),
					new Beat(startTime + gap * 85, "S"),
					new Beat(startTime + gap * 87, "D"),
					new Beat(startTime + gap * 89, "F"),
					new Beat(startTime + gap * 91, "D"),
					new Beat(startTime + gap * 93, "S"),
					new Beat(startTime + gap * 95, "D"),
					new Beat(startTime + gap * 87, "L"),
					new Beat(startTime + gap * 89, "K"),
					new Beat(startTime + gap * 91, "J"),
					new Beat(startTime + gap * 93, "S"),
					new Beat(startTime + gap * 95, "Space"),
					new Beat(startTime + gap * 97, "J"),
					new Beat(startTime + gap * 99, "K"),
					new Beat(startTime + gap * 102, "L"),
					new Beat(startTime + gap * 104, "F"),
					new Beat(startTime + gap * 104, "Space"),
					new Beat(startTime + gap * 104, "J"),
					new Beat(startTime + gap * 106, "J"),
					new Beat(startTime + gap * 108, "K"),
					new Beat(startTime + gap * 110, "S"),
					new Beat(startTime + gap * 112, "J"),
					new Beat(startTime + gap * 114, "S"),
					new Beat(startTime + gap * 104, "F"),
					new Beat(startTime + gap * 106, "S"),
					new Beat(startTime + gap * 108, "D"),
					new Beat(startTime + gap * 110, "S"),
					new Beat(startTime + gap * 112, "D"),
					new Beat(startTime + gap * 114, "K"),
					new Beat(startTime + gap * 116, "Space"),
					new Beat(startTime + gap * 118, "S"),
					new Beat(startTime + gap * 120, "J"),
					new Beat(startTime + gap * 122, "K"),
					new Beat(startTime + gap * 124, "S"),
					new Beat(startTime + gap * 126, "D"),
					new Beat(startTime + gap * 128, "S"),
					new Beat(startTime + gap * 128, "k"),
					new Beat(startTime + gap * 130, "Space"),
					new Beat(startTime + gap * 132, "S"),
					new Beat(startTime + gap * 134, "D"),
					new Beat(startTime + gap * 136, "F"),
					new Beat(startTime + gap * 138, "Space"),
					new Beat(startTime + gap * 140, "J"),
					new Beat(startTime + gap * 142, "K"),
					new Beat(startTime + gap * 144, "L"),
					new Beat(startTime + gap * 146, "S"),
					new Beat(startTime + gap * 148, "D"),
					new Beat(startTime + gap * 134, "D"),
					new Beat(startTime + gap * 136, "J"),
					new Beat(startTime + gap * 138, "Space"),
					new Beat(startTime + gap * 140, "K"),
					new Beat(startTime + gap * 142, "S"),
					new Beat(startTime + gap * 144, "F"),
					new Beat(startTime + gap * 146, "S"),
					new Beat(startTime + gap * 148, "D"),
					new Beat(startTime + gap * 150, "S"),
					new Beat(startTime + gap * 152, "S"),
					new Beat(startTime + gap * 154, "D"),
					new Beat(startTime + gap * 156, "D"),
					new Beat(startTime + gap * 158, "F"),
					new Beat(startTime + gap * 160, "F"),
					new Beat(startTime + gap * 162, "Space"),
					new Beat(startTime + gap * 164, "Space"),
					new Beat(startTime + gap * 166, "J"),
					new Beat(startTime + gap * 168, "J"),
					new Beat(startTime + gap * 170, "k"),
					new Beat(startTime + gap * 172, "k"),
					new Beat(startTime + gap * 174, "L"),
					new Beat(startTime + gap * 176, "L"),
					new Beat(startTime + gap * 178, "D"),
					new Beat(startTime + gap * 180, "S"),
					new Beat(startTime + gap * 182, "D"),
					new Beat(startTime + gap * 184, "S"),
					new Beat(startTime + gap * 186, "D"),
					new Beat(startTime + gap * 190, "S"),
					new Beat(startTime + gap * 194, "D"),
					new Beat(startTime + gap * 196, "J"),
					new Beat(startTime + gap * 198, "K"),
					new Beat(startTime + gap * 200, "J"),
					new Beat(startTime + gap * 202, "K"),
					new Beat(startTime + gap * 204, "J"),
					new Beat(startTime + gap * 206, "K"),
					new Beat(startTime + gap * 208, "J"),
					new Beat(startTime + gap * 196, "D"),
					new Beat(startTime + gap * 198, "S"),
					new Beat(startTime + gap * 200, "F"),
					new Beat(startTime + gap * 202, "SPACE"),
					new Beat(startTime + gap * 204, "S"),
					new Beat(startTime + gap * 206, "K"),
					new Beat(startTime + gap * 208, "J"),
					new Beat(startTime + gap * 210, "K"),
					new Beat(startTime + gap * 212, "S"),
					new Beat(startTime + gap * 214, "D"),
					new Beat(startTime + gap * 216, "S"),
					new Beat(startTime + gap * 218, "D"),
					new Beat(startTime + gap * 220, "S"),
					new Beat(startTime + gap * 222, "D"),
					new Beat(startTime + gap * 224, "J"),
					new Beat(startTime + gap * 226, "K"),
					new Beat(startTime + gap * 228, "L"),
					new Beat(startTime + gap * 230, "F"),
					new Beat(startTime + gap * 232, "Space"),
					new Beat(startTime + gap * 234, "J"),
					new Beat(startTime + gap * 236, "D"),
					new Beat(startTime + gap * 238, "S"),
					new Beat(startTime + gap * 240, "D"),
					new Beat(startTime + gap * 242, "D"),
					new Beat(startTime + gap * 244, "S"),
					new Beat(startTime + gap * 246, "D"),
					new Beat(startTime + gap * 248, "J"),
					new Beat(startTime + gap * 250, "K"),
					new Beat(startTime + gap * 252, "J"),
					new Beat(startTime + gap * 254, "K"),
					new Beat(startTime + gap * 256, "J"),
					new Beat(startTime + gap * 258, "K"),
					new Beat(startTime + gap * 260, "J"),
					new Beat(startTime + gap * 262, "K"),
					new Beat(startTime + gap * 264, "S"),
					new Beat(startTime + gap * 266, "D"),
					new Beat(startTime + gap * 268, "S"),
					new Beat(startTime + gap * 270, "D"),
					new Beat(startTime + gap * 272, "S"),
					new Beat(startTime + gap * 274, "D"),
					new Beat(startTime + gap * 276, "J"),
					new Beat(startTime + gap * 278, "K"),
					new Beat(startTime + gap * 280, "L"),
					new Beat(startTime + gap * 282, "F"),
					new Beat(startTime + gap * 284, "Space"),
					new Beat(startTime + gap * 286, "J"),
					new Beat(startTime + gap * 288, "J"),
					new Beat(startTime + gap * 290, "K"),
					new Beat(startTime + gap * 292, "S"),
					new Beat(startTime + gap * 294, "J"),
					new Beat(startTime + gap * 296, "k"),
					new Beat(startTime + gap * 298, "L"),
					new Beat(startTime + gap * 300, "L"),
					new Beat(startTime + gap * 302, "D"),
					new Beat(startTime + gap * 304, "S"),
					new Beat(startTime + gap * 306, "D"),
					new Beat(startTime + gap * 308, "S"),
					new Beat(startTime + gap * 310, "D"),
					new Beat(startTime + gap * 312, "S"),
					new Beat(startTime + gap * 314, "D"),
					new Beat(startTime + gap * 316, "J"),
					new Beat(startTime + gap * 296, "D"),
					new Beat(startTime + gap * 298, "S"),
					new Beat(startTime + gap * 300, "L"),
					new Beat(startTime + gap * 302, "K"),
					new Beat(startTime + gap * 304, "J"),
					new Beat(startTime + gap * 306, "Space"),
					new Beat(startTime + gap * 308, "D"),
					new Beat(startTime + gap * 310, "F"),
					new Beat(startTime + gap * 312, "S"),
					new Beat(startTime + gap * 314, "K"),
					new Beat(startTime + gap * 316, "L"),
					new Beat(startTime + gap * 318, "D"),
					new Beat(startTime + gap * 320, "S"),
					new Beat(startTime + gap * 324, "Space"),
					new Beat(startTime + gap * 326, "J"),
					new Beat(startTime + gap * 328, "K"),
					new Beat(startTime + gap * 330, "L"),
					new Beat(startTime + gap * 332, "K"),
					new Beat(startTime + gap * 334, "S"),
					new Beat(startTime + gap * 336, "K"),
					new Beat(startTime + gap * 338, "J"),
					new Beat(startTime + gap * 340, "K"),
					new Beat(startTime + gap * 342, "S"),
					new Beat(startTime + gap * 346, "D"),
					new Beat(startTime + gap * 348, "S"),
					new Beat(startTime + gap * 350, "D"),
					new Beat(startTime + gap * 352, "S"),
					new Beat(startTime + gap * 354, "D"),
					new Beat(startTime + gap * 358, "J"),
					new Beat(startTime + gap * 360, "K"),
					new Beat(startTime + gap * 362, "L"),
					new Beat(startTime + gap * 364, "F"),
					new Beat(startTime + gap * 366, "S"),
					new Beat(startTime + gap * 369, "D"),
					new Beat(startTime + gap * 372, "J"),
					new Beat(startTime + gap * 375, "D"),
					new Beat(startTime + gap * 378, "S"),
					new Beat(startTime + gap * 381, "Space"),
					new Beat(startTime + gap * 384, "J"),
					new Beat(startTime + gap * 387, "K"),
					new Beat(startTime + gap * 390, "L"),
					new Beat(startTime + gap * 393, "K"),
					new Beat(startTime + gap * 396, "S"),
					new Beat(startTime + gap * 399, "K"),
					new Beat(startTime + gap * 402, "J"),
					new Beat(startTime + gap * 405, "F"),
					new Beat(startTime + gap * 408, "L"),
					new Beat(startTime + gap * 401, "K"),
					new Beat(startTime + gap * 404, "S"),
					new Beat(startTime + gap * 407, "J"),
					new Beat(startTime + gap * 399, "S"),
					new Beat(startTime + gap * 402, "D"),
					new Beat(startTime + gap * 405, "J"),
					new Beat(startTime + gap * 408, "S"),
					new Beat(startTime + gap * 401, "D"),
					new Beat(startTime + gap * 404, "L"),
					new Beat(startTime + gap * 407, "F"),
					new Beat(startTime + gap * 410, "F"),
					new Beat(startTime + gap * 410, "Space"),
					new Beat(startTime + gap * 410, "J"),
					new Beat(startTime + gap * 411, "Space"),
					new Beat(startTime + gap * 412, "Space"),
					new Beat(startTime + gap * 413, "Space"),	
			};
		}
		else if(titleName.equals("Joakim Karud - Wild Flower") && difficulty.equals("Easy")) {
			int startTime = 1000;
			beats = new Beat[] {
					new Beat(startTime, "Space"),
			};
		}
		else if(titleName.equals("Joakim Karud - Wild Flower") && difficulty.equals("Hard")) {
			int startTime = 1000;
			beats = new Beat[] {
					new Beat(startTime, "Space"),
			};
		}
		else if(titleName.equals("Bendsound - Energy") && difficulty.equals("Easy")) {
			int startTime = 1000;
			beats = new Beat[] {
					new Beat(startTime, "Space"),
			};
		}
		else if(titleName.equals("Bendsound - Energy") && difficulty.equals("Hard")) {
			int startTime = 1000;
			beats = new Beat[] {
					new Beat(startTime, "Space"),
			};
		}
		
		int i = 0;
		gameMusic.start();
		while(i < beats.length && !isInterrupted()) {
			boolean dropped = false;
			if(beats[i].getTime() <= gameMusic.getTime()) {
				Note note = new Note(beats[i].getNoteName());
				note.start();
				noteList.add(note);
				i++;
				dropped = true;
			}
			if(!dropped) {
				try {
					Thread.sleep(5);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		}
	}
	public void judge(String input) {
		for(int i=0; i < noteList.size(); i ++) {
			Note note = noteList.get(i);
			if(input.equals(note.getNoteType())) {
				judgeEvent(note.judge());
				break;
			}
		}
	}

	public void judgeEvent(String judge) {
		if(!judge.equals("None")) {
			blueFlareImage = new ImageIcon(Main.class.getResource("../images/blueFlare.png")).getImage();
		}
		if(judge.equals("Miss")) {
			judgeImage = new ImageIcon(Main.class.getResource("../images/judgeMiss.png")).getImage();
		}
		else if(judge.equals("Late")) {
			judgeImage = new ImageIcon(Main.class.getResource("../images/judgeLate.png")).getImage();
		}
		else if(judge.equals("Good")) {
			judgeImage = new ImageIcon(Main.class.getResource("../images/judgeGood.png")).getImage();
		}
		else if(judge.equals("Great")) {
			judgeImage = new ImageIcon(Main.class.getResource("../images/judgeGreat.png")).getImage();
		}
		else if(judge.equals("Perfect")) {
			judgeImage = new ImageIcon(Main.class.getResource("../images/judgePerfect.png")).getImage();
		}
		else if(judge.equals("Early")) {
			judgeImage = new ImageIcon(Main.class.getResource("../images/judgeEarly.png")).getImage();
		}
	}
}
