---
article_id: 35361255827863
category: Materiais - Compras (SIGACOM)
content_hash: 415c6f8f78802ec7981d5e348e40d042ffdcb979db118502e4c8619735627e61
fetched_at: '2026-06-28T22:41:17.339570+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Documento de Entrada
  - HELP A103VLATF
type: support-article
updated_at: '2025-10-10T20:09:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35361255827863-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Documento-de-Entrada-HELP-A103VLATF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35361226938647) Tempo aproximado para leitura: **00:03:SS min**  
  
**Dúvida**

Ao incluir, excluir um documento de entrada ou estornar a classificação de uma nota de entrada, o sistema exibe o help A103VLATF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35361255810967)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Todas as versões  
  
**Solução**  
O erro ocorre em virtude do fonte do MATA103 estar atualizado e o fonte do FISXATF não estar.

Para solução, basta aplicar o novo pacote de expedição contínua do backoffice conforme link abaixo e de acordo com o release em uso do sistema, em seu ambiente.

[**Expedição contínua do backoffice**](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)

**Ou**

Pode-se resolver o help, mediante verificação dos cenários abaixo :

Então, temos dois cenários, mas antes é necessário verificar, o inspetor de objetos com as datas dos fontes, em seu ambiente.

**1-) Clientes que só aplicaram o pacote de expedição contínua do backoffice liberado em agosto de 2025, para correção do erro, devem aplicar o pacote abaixo, conforme a release em uso do Protheus em seu ambiente :**

12.1.2210:<https://r.totvs.io/p/1213692>

12.1.2310:<https://r.totvs.io/p/1213693>

12.1.2410:<https://r.totvs.io/p/1213691>

12.1.2510:<https://r.totvs.io/p/1213694>

***Importante :*** ***Clientes utilizando as releases 2210 e 2310, só devem aplicar o pacote correspondente, caso possuam a garantia extendida adquirida.***

**2-) Clientes que, aplicaram o pacote de expedição contínua do backoffice liberado em agosto de 2025 e, por algum motivo ou erro, aplicaram pacote que atualizou a MATA103 :**

Necessitam aplicar o pacote do item 1 e aceitar os fontes mais atuais.

Caso isso não seja possível, aplique, por favor o pacote do item 1 e reaplique o pacote que atualizou a MATA103.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001545042)
