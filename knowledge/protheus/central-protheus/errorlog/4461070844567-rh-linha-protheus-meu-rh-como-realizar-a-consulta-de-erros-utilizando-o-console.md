---
article_id: 4461070844567
category: ERRORLOG
content_hash: 0886de456272dec8cf38a81ce1695facae795d9f8a8f282cd98814b2c447321a
fetched_at: '2026-06-28T22:44:39.480381+00:00'
product: protheus
section_id: 10299583475863
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como realizar a consulta de erros utilizando
  o console do navegador (F12)
type: support-article
updated_at: '2026-06-18T18:11:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4461070844567-RH-Linha-Protheus-MEU-RH-Como-realizar-a-consulta-de-erros-utilizando-o-console-do-navegador-F12
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24768691181591) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como realizar a consulta de erro utilizando o console do navegador (F12) ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**  
Caso esteja sofrendo com algum problema e o *console.log* não foi o suficiente para constatar a origem daquele problema, faça a consulta do erro pelo navegador. Neste artigo utilizaremos o navegador *Google Chrome*, a lógica seguirá a mesma para os demais navegadores mas a exibição pode variar.  
  
Acesse o MEU RH na rotina com erro, pressione a tecla F12, selecione a aba *Network*, ative as opções *Preserve* *log* e *Disable cache*, verifique se a função *Record*/Gravar (botão vermelho) está ativo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4460854147223)

Pressione F5 (Atualizar página), para que as informações sejam recarregadas, todos os elementos daquela página serão carregados no console e nele podemos ver as requisições da *API* com Protheus:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4460866073879)

Clicando em um desses elementos e selecionando a opção *Headers*, podemos ver a requisição da URL o status dela e o tipo de requisição:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4460884301847)  
  
Quando ocorre algum erro o elemento com problema fica destacado em vermelho, facilitando a identificação de onde está a origem do erro:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4460931158551)

Clicando em Preview podemos ver se existe alguma mensagem de erro:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4460955528087)

Neste exemplo eu recusei propositalmente a localização e ele apresentou a mensagem de erro na verificação do *timezone* para marcação.  
Se eu tivesse permitido acesso a minha localização ele teria concluído com sucesso essa requisição:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4461004954903)

O objetivo deste artigo é ajudar o cliente na identificação do erro para agilizar a solução.  
  
**Saiba Mais:  
[CLIQUE AQUI para acessar a documentação de referência do MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
