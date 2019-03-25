package blackjack;

import java.util.ArrayList;

public class Dealer extends Player {
	ArrayList<Card> bluff = new ArrayList<Card>();
	Boolean _doShow = false;
	public Dealer(String name) {
		this.name = name;

	}
	
	@Override
	public void showHand() {
		
		if(!this._doShow) {			
			this.bluff = (ArrayList<Card>) this.hand.clone();
			
			Card card1 = this.bluff.get(0);
			Card card2 = this.bluff.get(1);
			
			if(card1.point > card2.point) bluff.remove(0);
			else if(card1.point < card2.point) bluff.remove(1);
			else bluff.remove(1);
		}
		else {
			Card card3 = this.hand.get(this.hand.size() - 1);
			this.bluff.add(card3);
		}
		this._doShow = true;
	}
	
	@Override
	protected void check() {
		super.check();
		showHand();
		
		System.out.println(this + " 의 패 : " + this.bluff);
	}

	@Override
	public void isStay() {
//		System.out.println(this + "의 패 : " + this.hand);
		check();
		hasAce();
		
		if(this.isHit) {
			if(this.point < 17 ) {
				this.isHit = true;
			}
		}
	}
}
