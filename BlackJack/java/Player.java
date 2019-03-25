package blackjack;

import java.util.ArrayList;
import java.util.Iterator;

public abstract class Player {
	String name;
	ArrayList<Card> hand = new ArrayList<Card>();
	int point = 0;
	boolean isHit = true;

	public static final String[] aces = { "CA", "DA", "HA", "SA" };

	public Player() {

	}

	public Player(String name) {
		this.name = name;
	}
	
	
	// 초기 패가 A, A이면 _tPoint가 0이 되고, 카드의 합은 22 / 2가 아닌 12가 되어야 한다. 3장은 13, 4장은 14.
	public void hasAce() {
		boolean _hasAce = false;
		if(!_hasAce) {
			for(Card card : this.hand) {
				for(String ace : aces) {
					_hasAce = (card.name == ace) ? true : false;
				}
			}
		}
		
		sum();
		int _howAces = howAces();
		int _tPoint = this.point - _howAces;
		
		if(_hasAce && _tPoint <= 10) {
			this.point += 10;
		}
	}

	public int howAces() {
		int result = 0;
		for (Card card : this.hand) {
			switch (card.name) {
			case "CA":
				result++;
				continue;
			case "DA":
				result++;
				continue;
			case "HA":
				result++;
				continue;
			case "SA":
				result++;
				continue;
			default:
				continue;
			}
		}

		return result;
	}

	protected void sum() {
		Iterator<Card> itr = this.hand.iterator();
		this.point = 0;
		
		while (itr.hasNext()) {
			Card card = itr.next();
			this.point += card.point;
		}
	}

	public abstract void isStay();

	public ArrayList<Card> getHand() {
		return this.hand;
	}

	public void setHand(Card card) {
		this.hand.add(card);
	}

	@Override
	public String toString() {
		return this.name + "님";
	}

	protected void check() {
		sum();
		if(this.point > 21) {
			System.out.println(this + " Busted!!");
			this.isHit = false;
		}
		else if(this.point == 21) {
			System.out.println(this + " BlackJack!!");
			this.isHit = false;
		}
	};
	
	public abstract void showHand();	

		
}
