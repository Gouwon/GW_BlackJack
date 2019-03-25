package blackjack;

import java.util.ArrayList;

public interface Deck {
	
	public static ArrayList<Card> deck = Card.setCardList();
	
	//	덱을 셔플하는 함수
	public static void getDeck(){};
	// 카드를 분배하는 함수
	public static void dispenseCard(boolean isHit, Player player) {}; 
}