---
article_id: 4588706806295
category: Materiais - Compras (SIGACOM)
content_hash: 52ce9400a57da9baa34cd6c5a91640168cd4a2bc7a8b1933b7d375b09935cb34
fetched_at: '2026-06-28T22:41:19.986686+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Inclusão de saldo para
  movimentação -  Manutenção de Lançamento PCOA050
type: support-article
updated_at: '2022-03-04T20:33:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4588706806295-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Inclus%C3%A3o-de-saldo-para-movimenta%C3%A7%C3%A3o-Manuten%C3%A7%C3%A3o-de-Lan%C3%A7amento-PCOA050
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:02:00 min****Dúvida**Como incluir saldo no PCO para que os registros não sejam bloqueados na contingencia?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Planejamento e Controle Orçamentário - Todas as versões  
  
**Solução**Para gerar saldo no PCO para que o seu registro não seja bloqueado por sua contingencia, acesse a rotina PCOA050 ( Manutenção de Lançamentos ) :

1- Incluir:

A rotina de apresenta uma linha de registro, onde os cadastros devem ser preenchidos com as informações que vão compor o movimento de valor.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4588557042199/mceclip0.png)

O campo de valor do lançamento é o campo onde você vai definir o range de valor que poderá utilizar nos lançamentos.

O PCO valida as informações do lançamento de acordo com o C.O+CC. Então para que o saldo cadastrado seja reconhecido no movimento que esta utilizando, precisa utilizar o C.O e o CC utilizado no cadastro.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
