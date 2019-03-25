package blackjack;

public class Gamer extends Player {

	@Override
	public void showHand() {
		
	}

	public Gamer(String name) {
		this.name = name;
		
	}

	
	
	@Override
	protected void check() {
		super.check();
		
		System.out.println(this + " 의 패 : " + this.hand);
		System.out.println(this + " 의 점수 : " + this.point);
	}

	@Override
	public void isStay() {
		hasAce();
		
		if (this.isHit) {
			if (this.point < 21) {
				String msg = GameRule.userInput("Hit ::>> 1, Stay ::>> 2\n 입력하세요 : ");
				if (msg.equals("1")) {
					this.isHit = true;
				} else if (msg.equals("2")) {
					this.isHit = false;
				} else {
					System.out.println("잘못된 입력입니다. 다시 입력해주세요.");
					isStay();
				}
			}
		}
	}

	@Override
	public void hasAce() {
		boolean _hasAce = false;
		if(!_hasAce) {
			for(Card card : this.hand) {
				for(String ace : aces) {
					_hasAce = (card.name.equals(ace)) ? true : false;
					if(!_hasAce) continue;
					else break;
				}
				if(_hasAce) break;
			}
		}
		
		int _howAces = howAces();
		sum();
		
		if(_hasAce) {
			System.out.println("페에 Ace가 " + _howAces + "장 있습니다.");
			System.out.println(this.hand);
			String msg = GameRule.userInput("11점으로 계산할 카드 장 수를 입력해주세요.\n  입력하세요 : ");
			sum();
			this.point += (Integer.parseInt(msg) * 10);
			System.out.println(msg + "장이 11점으로 계산됩니다. 현재 점수 ::>> " + this.point);
		}
	}
}
