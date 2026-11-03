---
article_id: 360025941832
category: Financeiro - Conciliador Backoffice
content_hash: 21839f502e149bb18dbb692d4b5ff6c174daa3cdd8af1c3ffc581cae157b23f1
fetched_at: '2026-06-28T22:37:47.273218+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: MP - SIGAFIN - CTBA940 -  E5_TIPODOC = JR não apresenta na Conciliação
type: support-article
updated_at: '2025-07-10T13:08:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025941832-MP-SIGAFIN-CTBA940-E5-TIPODOC-JR-n%C3%A3o-apresenta-na-Concilia%C3%A7%C3%A3o
---

**Dúvida**Ao efetuar **baixa parcial** no **Contas a Receber,** onde possui multa e juros, o sistema não apresenta na conciliação.  
Sendo que na tabela **SE5** tem 3 movimentos nos campos **E5\_TIPODOC=** **VL**, **E5\_TIPODOC=** **MT** e **E5\_TIPODOC=****JR** apenas o campo **E5\_TIPODOC=** **VL** apresenta.

**Ambiente**  
Microsiga Protheus – Financeiro – A partir da versão 11.80  
  
  
**Solução**

De fato, os juros não são considerados na conciliação bancária, uma vez que o campo **E5\_TIPODOC = 'JR'** não atualiza o saldo bancário.

Em casos de **baixa parcial**, os juros somente serão refletidos na **baixa total** do título.

**Exemplo:**  
Título no valor de R$ 1.000,00 com R$ 10,00 de juros.  
Na primeira baixa, no valor de R$ 500,00, o sistema registra esse valor no campo **E5\_VALOR** com **E5\_TIPODOC = 'VL'**.  
Somente na baixa do valor restante (R$ 500,00), o sistema irá considerar os juros, registrando R$ 510,00 no campo **E5\_VALOR**.  
Dessa forma, os juros serão refletidos apenas na última baixa, momento em que aparecerão na conciliação bancária.
