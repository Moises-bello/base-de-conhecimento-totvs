---
content_hash: 04b0790509821897e1470bf09b344bcc511e1d036c694f0b3f349f0f38adcc8a
fetched_at: '2026-06-29T00:10:58.271672+00:00'
page_id: '604999251'
product: rm
source: tdn-rm
title: Pesquisa de Satisfação/Aceitação/FeedBack de Funcionalidades em Desenvolvimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=604999251
version: 3
---

Este documento tem por objetivo, demonstrar como incluir a pesquisa de Satisfação para os novos desenvolvimentos de funcionalidades aprovadas pelos POs, quanto a satisfação, entendimento, dificuldades e colher feedbacks de nossos usuários espontaneamente.

* Todos os dados coletados nesta pesquisa se encontra em uma planilha publica: <https://docs.google.com/spreadsheets/d/1u_xqv4y1FfzNIufzPAQGYcHKUw1L1I3-3kMUzgsJvD0/edit?usp=sharing>
* Para efetuar a chamada da Action (ImbAceitacaoPesquisaAction) que acionara a pesquisa, basta incluir na Action que deseja efetuar a avaliação a chamada da mesma na lista de Process, como no exemplo a seguir:  
     **Ex.:** ProcessActions.Add("ImbAceitacaoPesquisaAction", ImbImagensUtils.GetTransparentImage(ImbImagens.like\_unlike), Shortcut.None, Caption);  
  **Importante**: a variável "Caption" passada na chamada é a representação do descritivo que aparece na action a ser avaliada.  

  **Imagem padrão para utilização no link da pesquisa de feedBack:**  
   - Nome da Imagem "like\_unlike"
* Para uma melhor visualização no toolbar superior da visão da funcionalidade (no menu rápido da tela), vc deverá incluir a mesma em, ProcessActions.ShowOnCustomToolbar como no exemplo abaixo:  
      **Ex.:** ProcessActions.ShowOnCustomToolbar( "ImbAceitacaoPesquisaAction");  
    
  Imagem da action sendo incluída no InitializeAction() da Action que se deseja avaliar:

**Após implementar a chamada da action, como descrito acima, o resultado é esse:**
