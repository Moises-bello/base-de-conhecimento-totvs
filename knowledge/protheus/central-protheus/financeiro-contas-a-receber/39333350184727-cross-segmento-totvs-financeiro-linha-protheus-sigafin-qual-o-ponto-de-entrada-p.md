---
article_id: 39333350184727
category: Financeiro - Contas a Receber
content_hash: 50276b57f737890b2cb98966b6b2962f296f05bcaed64db1c148e08487af3518
fetched_at: '2026-06-28T22:38:12.547498+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - TOTVS Financeiro (Linha Protheus - SIGAFIN - Qual o ponto
  de entrada para incluir botões?
type: support-article
updated_at: '2026-03-27T12:31:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39333350184727-Cross-Segmento-TOTVS-Financeiro-Linha-Protheus-SIGAFIN-Qual-o-ponto-de-entrada-para-incluir-bot%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39333350178199) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Qual o ponto de entrada disponível para a inclusão de botões customizados nas rotinas de Contas a Pagar (FINA050) e Contas a Receber (FINA040)?  
  
**Ambiente**  
Cross Segmento - TOTVS Financeiro Linha Protheus - SIGAFIN - Todas as versões.  
  
**Solução**  
Para a inclusão de botões nas rotinas citadas, devem ser utilizados os pontos de entrada específicos que permitem a manipulação do array de botões da interface.

* Na rotina de Contas a Pagar (FINA050):

**F050BUT -**Permite inclusão de botão, para ativar rotinas específicas na Enchoicebar.  
Documentação:[F050BUT - Inclusão de botão para ativar rotinas específicas](http://tdn.totvs.com/pages/releaseview.action?pageId=6071309)

* Na rotina de Contas a Receber (FINA040):

F040BUT -  adiciona botões do usuário na *EnchoiceBar*. Retorna o *array* com os novos botões (*aUsButtons*).  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6070863>



**Saiba Mais**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - Pontos de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031234634-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Pontos-de-Entrada)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA040 - Pontos de entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052015894-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Pontos-de-entrada)
