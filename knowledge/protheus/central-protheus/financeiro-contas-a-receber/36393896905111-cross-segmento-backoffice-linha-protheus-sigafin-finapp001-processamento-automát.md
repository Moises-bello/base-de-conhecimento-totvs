---
article_id: 36393896905111
category: Financeiro - Contas a Receber
content_hash: 2cd2370a122c0444713d0f4c9949628f2ec6bd24b2bcb31dbfcc24d100efd401
fetched_at: '2026-06-28T22:38:12.523267+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINAPP001 - Processamento
  automático Limite de Crédito
type: support-article
updated_at: '2026-05-19T15:23:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36393896905111-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINAPP001-Processamento-autom%C3%A1tico-Limite-de-Cr%C3%A9dito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36393918049047) Tempo aproximado para leitura: **10:00 min**

**Dúvida:**  
Ao realizar a inserção de um título no financeiro, o valor dos títulos não é descontado do total de crédito do cliente. Gostaria de saber como podemos automatizar esse cálculo.

**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - 12.1.33 e superiores  
  
**Solução:**

Para compor o card de **“Limite de Crédito”**, o sistema utiliza as informações cadastradas no cliente.

O cálculo é feito com base nos seguintes campos da MATA030 (SA1):

* **"Lim. Credito"** **(A1\_LC)** – Aba *Vendas*

  *![](https://centraldeatendimento.totvs.com/hc/article_attachments/36393918050199)*
* "**Sal Moed For"**  **(A1\_SALDUPM)** – Aba *Adm/Fin*  
  *![](https://centraldeatendimento.totvs.com/hc/article_attachments/36393896893335)*
* "Sld Ped. Lib" **(A1\_SALPEDL)** – Aba *Vendas*  
  *![](https://centraldeatendimento.totvs.com/hc/article_attachments/36393918052631)*

**Fórmula utilizada pelo sistema:**  
**(****A1\_LC****) – (****A1\_SALDUPM** **+** **A1\_SALPEDL****) =** **Limite Atual de Crédito**

Exemplo prático:

* **A1\_SALDUPM = R$** **1690,00**
* **A1\_SALPEDL = R$** **00,00**
* **A1\_LC = R$** **2100,00**

**(****2100,00****) – (****1690,00** **+****00,00****) =** **410,00 R$**

Ou seja, o valor exibido no card corresponde ao limite disponível após considerar (deduzir) o saldo em aberto dos titulos e os pedidos já liberados.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36393918053015)

Quanto ao processamento dessas informações:

* Por padrão, o sistema utiliza o parâmetro **MV\_ATUSA1 = .F.** Deixando o calculo automático desativado. Com isso, os valores do cliente só são atualizados quando é executado o processo de reprocessamento na rotina **FINA410**.
* Caso a empresa deseje que, ao final do lançamento dos títulos, a somatória dos campos **A1\_SALDUPM** e **A1\_SALPEDL** seja atualizada automaticamente no cadastro do cliente, é necessário ajustar o parâmetro para **MV\_ATUSA1 = .T.**
