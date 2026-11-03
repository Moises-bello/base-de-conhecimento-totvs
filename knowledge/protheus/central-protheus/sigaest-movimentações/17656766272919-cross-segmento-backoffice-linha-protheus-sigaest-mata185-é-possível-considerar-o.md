---
article_id: 17656766272919
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 70a57427a04a71445ad58665207a56c0cb0739fa8e1cad8be4c9d1f095e401bb
fetched_at: '2026-06-28T22:38:56.861689+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA185 - É possível
  considerar o saldo da requisição quando disponível em outro Armazém diferente da
  SA?
type: support-article
updated_at: '2023-09-20T12:21:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17656766272919-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA185-%C3%89-poss%C3%ADvel-considerar-o-saldo-da-requisi%C3%A7%C3%A3o-quando-dispon%C3%ADvel-em-outro-Armaz%C3%A9m-diferente-da-SA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17656812660247) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

O saldo de determinado produto consta em um outro Armazém, é possível considerar o saldo da requisição quando disponível em outro Armazém diferente da SA? Como proceder?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17667305629335)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

No padrão não é possível alterar a baixa da pré-requisição quando não possui saldo no Armazém solicitado na rotina Solicitação ao Armazém (MATA105). Nesse cenário, pode efetuar o processo de duas formas:

   
***- 1-***Transferir o Saldo que consta em outro Armazém para o Armazém da Baixa pela rotinas de TRANSFERÊNCIAS MÚLTIPLAS (MATA261), [clique aqui](https://www.youtube.com/watch?v=-C05diWV9D4) e conheça a rotina.

   
***- 2 -*** Customizar a Baixa da Pré-requisição com os Pontos de Entrada dos links abaixo.

***M185BAIX - Customiza baixa de pré-requisição***  
***<http://www.tdn.totvs.com/pages/releaseview.action?pageId=6087549>***  
  
***M185MOD1 - Validação da baixa da pré-requisição mod1***  
***<http://www.tdn.totvs.com/pages/releaseview.action?pageId=6087555>***  
  
***M185MOD2 - Baixa de Pré-requisição Mod2***  
***<http://tdn.totvs.com/pages/releaseview.action?pageId=6087556>***

***Saiba Mais:***

*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
