package blackjack;

public class Main {

	public static void main(String[] args) {
		
		boolean isStart = true;
		boolean isContinue = true;

		while (isStart) {

			String msg = GameRule.userInput("Welcome to BlackJack Game!!\nStart ::>> 1, Quit ::>> 2\n >>>>>> ");

			if (msg.equals("2")) {
				break;
			} 
			else if (msg.equals("1")) {
				String gamerName = GameRule.userInput("플레이할 캐릭터명을 입력해주세요!! >>>> ");
				while (isContinue) {

					GameRule.game(gamerName);

					while (isContinue) {
						String continueMsg = GameRule.userInput("게임을 계속하시겠습니까? \nContinue ::>> 1, Quit ::>> 2 \n >>>>>>> ");

						if (continueMsg.equals("2")) {
							isContinue = false;
							isStart = false;
							System.out.println("플레이해주셔서 감사합니다!");
							break;
						} 
						else if (continueMsg.equals("1")) {
							System.out.println("\n\n\n새로운 게임을 시작합니다.");
							break;
						}
					else {
							System.out.println("잘못된 입력입니다. 다시 입력해주세요.");
							continue;
						}
					}
					
				}
			} 
		else {
				System.out.println("잘못된 입력입니다. 다시 입력해주세요.");
				continue;
			}
		}
		System.exit(0);
	}
}
