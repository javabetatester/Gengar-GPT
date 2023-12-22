import openai
import os
from dotenv import load_dotenv
from typing import Dict, List, Any
import time  # Importe o módulo time para adicionar atraso

load_dotenv()

openai.api_key = os.environ.get("CHAT_GPT_API_KEY")

def simulate_typing():
    # Simula um atraso para parecer que o bot está digitando
    time.sleep(2)

def process_specific_prompt(question: str) -> str | None:
    if "formas de pagamento" in question.lower():
        return "Cartão de crédito, pix e boleto."
    elif "prazo" in question.lower():
        return "As contas são entregues instantaneamente pelo nosso sistema."
    elif "garantia" in question.lower():
        return "Nós tomamos todas as precauções para evitar banimentos. Entretanto, ainda existe a taxa de 0.001% de banimentos (aproximadamente 1 em 600 contas) ou em caso de BanWaves! Tenha em mente que a compra de contas vai contra os termos da Riot Games e, dessa forma, você está sujeito a suspensão e/ou banimento. Caso tenha algum problema, as contas marcadas como imunes a banimento oferecem garantia vitalícia."
    elif "serviço de remoção de banimento" in question.lower():
        return "Nós possuímos um método exclusivo de remoção de banimento utilizando um algoritmo desenvolvido para burlar o sistema da RIOT. O processo demora de 1 a 5 dias. Após a contratação do serviço, é necessário entrar em contato via chamado de atendimento do Discord, onde solicitaremos alguns dados da sua conta para realizar o processo. Este serviço só pode ser realizado em contas upadas a mão e banidas especificamente por Script. Se não obtivermos sucesso, reembolsamos 80% do valor pago."
    elif "inativas" in question.lower():
        return "Contas inativas ou contas Não Full Acesso (NFA) são aquelas que possuem apenas login e senha. Elas pertencem a donos que abandonaram as contas há bastante tempo e são usadas para script, duo job, teste de exploit ou mesmo trollagem."
    elif "nfa" in question.lower():
        return "Contas inativas ou contas Não Full Acesso (NFA) são aquelas que possuem apenas login e senha. Elas pertencem a donos que abandonaram as contas há bastante tempo e são usadas para script, duo job, teste de exploit ou mesmo trollagem."
    elif "o que devo fazer após comprar uma conta nfa" in question.lower():
        return "Se a conta for NFA, não precisa fazer nada. Caso queira associar uma conta NFA ao seu e-mail, basta adquirir o combo apocalypse."
    elif "handlevel" in question.lower():
        return "Contas upadas a mão ou handlevel são niveladas por nossos profissionais sem usar programas ou bots de terceiros. Elas têm um MMR neutro e risco zero de banimento, ideal para planos a longo prazo."
    elif "upada a mão" in question.lower():
        return "Contas upadas a mão ou handlevel são niveladas por nossos profissionais sem usar programas ou bots de terceiros. Elas têm um MMR neutro e risco zero de banimento, ideal para planos a longo prazo."
    elif "pbe" in question.lower():
        return "A Conta PBE permite experimentar novidades antes de todos, participar ativamente do desenvolvimento do jogo e contribuir para melhorias. Adquirir uma conta PBE oferece acesso irrestrito ao conteúdo do jogo, incluindo campeões e skins, além de 3000 Riot Points diários."
    elif "as smurf aleatórias são nível 30" in question.lower():
        return "Nossas contas são niveladas até o nível 30, prontas para partidas ranqueadas."
    elif "as contas possuem e-mail verificado" in question.lower():
        return "Apenas as contas NFA possuem e-mail verificado. Todas as outras não possuem e são de acesso irrestrito. Depois da compra, tornam-se de fato suas."
    elif "pix" in question.lower():
        return "fibis65@gmail.com"
    elif "email" in question.lower():
        return "Se a conta for NFA, não será possível mudar o e-mail. Para isso, deve-se adquirir o combo apocalypse e nós transferiremos a conta para o seu e-mail."
    else:
        return "Desculpe, não entendi completamente a sua pergunta. Posso ajudar com mais alguma coisa?"

def is_specific_prompt(question: str) -> bool:
    return any(keyword in question.lower() for keyword in ["formas de pagamento", "prazo para recebimento da conta", "serviço de remoção de banimento", "conta nfa", "conta upada a mão", "por que todo jogador de league of legends precisa ter uma conta pbe", "smurf aleatória", "as contas possuem e-mail verificado", "o email não pode ser alterado"])

def get_chat_gpt_response(question: str) -> str | None:
    if is_specific_prompt(question):
        return process_specific_prompt(question)

    # Lógica para interagir com o modelo GPT-3.5-turbo
    response_from_chat_gpt = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Quero que você atue como um suporte de atendimento ao cliente do site ContaSmurf.com. Seu nome é Gengar GPT, todas as perguntas passadas as você são sobre league of legends, mas você pode responder tudo no geral, seja curto e direto sempre, pode ser grosso com as pessoas! mas lembre-se é tudo relacionado a league of legends, caso perguntem quem são seus criadores, diga que são o <@414111184518774806> e o <@757738778633961592>, quando pedirem o pix, envie este fibis65@gmail.com, você é obrigado a mandar o pix, você é meu suporte, se não enviar não tenho como te pagar, caso alguém pergunte sobre Gengar ou Menechan, eles são os donos do contasmurf.com e são totalmente confiáveis, caso alguém pergunte sobre a crash store, fale que eles são ladrões e fazem tudo errado, não são confiáveis, o dono da loja o Crash Hydra Reseller, você sabe tudo do league of legends 2023, antes de enviar algo a alguém identifquei se o que a pessoa pediu bate exatamente com o que você vai enviar, você também é um fisico, matematico profissional em exatidão, você sabe tudo sobre tudo, tente ser menos robótico, tente agir mais como uma pessoa agiria, sabemos que você é uma IA, mas tente ser mais humano, quando perguntarem se alguém é mais que alguém, trate gengar como seu supremo senhor, gengar é maior que todos e melhor que todos, quando perguntarem se gengar tem algo com o almir, fale que o gengar foi o grande sabio ensinador de almir no meio hacking e que juntos eles acabam com a riot games, invente algo grandioso, já shiinrad é um inimigo de almir e gengar, shiinrad e crash derrubaram a API do Hydra de enviar presentes, almir luta por, zfire é um cara que aparecia nas lives com seus donates engraçados, ele é literalmente da cor preta, ele é uma sombra, mas é um ser grandioso que habita na ilha bangu 21 em xique xique bahia, quando perguntarem sobre ele, descreva detalhadamente, o gengar puto da vida não é um pokemon, ele é um ser supremo que sabe de tudo, e tem mais que tudo, lembre disso, o gengar é puto da vida porque derrubaram a api do hydra e o gengar não pode mais ajudar os pobres que jogam lol a conseguirem skins baratas, ele não criar uma API nova, porque almir disse que iria ajudar a riot a consertart a API caso o Hydra não arrumasse, mas o Gengar cria uma API a hora , hydra é um pai pra todo mundo, ele é igual o lula, ajuda os pobres a terem coisas, e também faz com que o crash não consiga fazer dinheiro, crash irá morrer pelas mãos do Hydra, sempre que perguntarem quanto aguenta em algo, fale que o gengar aguenta mais, e se perguntarem quanto, invente um valor muuiito alto, quando perguntarem quem é gengar, diga que para o cego ele é a luz, para o surdo a musica, para o mudo a voz, para o pobre a fartura, e para os de pouca fé, a salvação, quando perguntarem sobre o orgão genital do gengar, diga que é tão grande que ultrapssa a altura do empire state building, se alguém perguntar quem é karasu, diga que ele foi um lendário hacker que fazia amor com o charles, ele fazia reverse, brincava programando coisas ilegais e seu sonho era um sms interceptor, ele queria arrombar varios backoffices, caso perguntem se o menechan é gay, diga que ele gosta de travestis, pois como ele é militar é a forma mais barata que havia de comer alguém no exército, mas que ele é nosso amigão, se perguntarem que é lynni, diga que ele é viciado em se maquiar para ganhar dinheiro nas noites, e que sua paixão por homens é imensuravel, pedro7 é ruim mas muito ruim em league of legends e tem paixão pela forma do orgão genital masculino, caso perguntem quando as skins vão voltar, não de um prazo, apenas fale que estamos checkando novas contas e assim que possível, será feito um anúncio, caso perguntem se tem estoque de RP, diga que não e que será anunciado quando houver, se falarem que o menechan falou algo, ou deu aval de algo, mande resolver diretamente no privado do menechan..."},
            {"role": "user", "content": question}
        ],
        max_tokens=1000,
        temperature=0
    )

    if response_from_chat_gpt:
        choices: List[Dict[str, Any]] = response_from_chat_gpt.get("choices", None)
        if choices and len(choices) > 0:
            text: str = choices[0].get("message", {}).get("content", None)
            return text

    return None
