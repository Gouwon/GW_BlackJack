package blackjack;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class GameRule implements Deck {
	
	public static ArrayList<Card> deck = Card.setCardList(); 
	
	// 점수를 확인하고 평가하는 함수 
	public static void compare(Player player1, Player player2) {
		boolean _isBusted = (player1.point > 21 || player2.point > 21) ? true : false;
		boolean _isBlackJack = (player1.point == 21 || player2.point == 21) ? true : false;
		
		if(_isBusted) {
			if(player1.point > player2.point && player1.point > 21 && player2.point < 21) System.out.println(player2 + "께서 승리하셨습니다!\n");
			else if(player1.point < player2.point && player2.point > 21 && player1.point < 21) System.out.println(player1 +"께서 승리하셨습니다.\n");
			else {
				System.out.println("무승부입니다.");
			}
			System.out.println(player1 + " 의 점수 : " + player1.point + "\t" + player2 + " 의 점수 : " + player2.point);
			player1.isHit = player2.isHit = false;
		}
		
		if(_isBlackJack) {
			if(player1.point == 21) System.out.println(player1 + "이 블랙잭을 만들었습니다!");
			else System.out.println(player2 + "이 블랙잭을 만들었습니다!");
			
		}
	}
	
	public static String userInput(String msg) {
		System.out.print(msg);
		Scanner scanner = new Scanner(System.in);
		String usermsg = scanner.nextLine();

		return usermsg;
	}
	
	public static void getDeck() {
		Collections.shuffle(deck);
	};

	public static void dispenseCard(Player player) {
		Card card = deck.get(0);
		deck.remove(0);

		if(player.isHit) player.setHand(card);
	}
	
	public static void game(String gamerName) {
		
//		GameRule.getDeck();
//		GameRule.deck;
		getDeck();
		Player gamer = new Gamer(gamerName);
		Player dealer = new Dealer("Dealer");
		
		while(gamer.hand.size() < 2) {
			dispenseCard(gamer);
			dispenseCard(dealer);
		}
		
		gamer.check();
		dealer.check();
		
		compare(gamer, dealer);
		
		while(gamer.isHit) {
			System.out.println("-------");
			gamer.isStay();
			dispenseCard(gamer);
			gamer.check();
		}
		
		while(dealer.isHit) {
			dealer.isStay();
			dealer.check();
			dispenseCard(dealer);
		}
		
		compare(gamer, dealer);
	}
	
	public static void main(String[] args ) {
	
		System.out.println(":::::::::::::::::::");
		game("r");
		
	}

}
