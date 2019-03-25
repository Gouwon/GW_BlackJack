package blackjack;

import java.util.ArrayList;

public class Card {
	
	String name;
	int point;
	
	public Card(String name, int point) {
		this.name = name;
		this.point = point;
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return this.name;
	}
	

	public static ArrayList<Card> setCardList(){
		
		String[] patterns = { "C", "D", "H", "S" };
		String[] numbers = { "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" };
		int[] points = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 };
		ArrayList<Card> cardList = new ArrayList<Card>();
		
		for(String pattern: patterns) {
			for(int i = 0; i < 13; i++) {
				String cardName = pattern + numbers[i];
				int point = points[i];
				cardList.add(new Card(cardName, point));
			}
		}
		return cardList;
	}
	
	public static void main(String[] args ) {
		
////		Card card = new Card("1", 1);
//		ArrayList<Card> card = Card.setCardList();
////		System.out.println(card);
//		for(Card c: card) {
//			System.out.println(c);
//		}
		
		
	}
}
