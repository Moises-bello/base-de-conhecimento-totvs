---
article_id: 21682807800471
category: Faturamento - Cadastros
content_hash: fd881c4af294f02df00c76446ba6e83a7e942ca80501019dd56f657513bf8ec8
fetched_at: '2026-06-28T22:38:35.446981+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Criação da condição de pagamento
  Tipo 9
type: support-article
updated_at: '2024-04-05T11:42:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21682807800471-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-9
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21682833207319) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como criar uma condição de pagamento do tipo 9?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Recomendado para condições da mais extrema complexidade;

Determina-se manualmente no pedido de vendas (Rotina MATA410 - Tabela SC5), a data das parcelas e os valores das parcelas.

Caso nenhum dos Tipos de Condição disponíveis atenda plenamente a particularidade de sua necessidade, pode-se utilizar a Condição de Pagamento Tipo 9, que é usada quando não há um tipo que automatize a especificidade da regra do cliente.

O cadastro é feito na rotina Condições de Pagamento - [Rotina MATA360 - Tabela SE4], mas a configuração dos valores das parcelas e data de vencimento das parcelas é informada na rotina Pedidos de Vendas - [Rotina MATA410 - Tabela SC5] ou Orçamentos de Vendas - [Rotina MATA415 - Tabela SCJ].

Há dois tipos de uso sobre a Condição de Pagamento Tipo 9, o modo por percentual e o modo por valor fixo.

Valor Fixo (E4\_COND = 0): O valor das parcelas é determinado inteiramente.

Valor Percentual (E4\_COND = %): O valor das parcelas é determinado em porcentagens em relação ao total das parcelas.

**Exemplo de Cadastro 1 - Condição de Pagamento Tipo 9 - Valor Fixo**

E4\_CODIGO = 001

E4\_TIPO = 9

→ E4\_COND = 0 (Valor fixo)

E4\_DESCRI = “TIPO 9 VALOR FIXO”

**Exemplo de Uso da condição “001” que é Tipo 9 e tem o valor fixo:**

Pedido de venda 1:

“Pedido de Vendas” - C5\_NUM: 000001  
“Condição de Pagamento” - C5\_COND: 001

“Parcela 1” - C5\_PARC1 = 100  
“Parcela 2” - C5\_PARC2 = 300  
“Parcela 3” - C5\_PARC3 = 300  
“Parcela 4” - C5\_PARC4 = 300

“Vencimento 1” - C5\_DATA1 = 25/03/2022  
“Vencimento 2” - C5\_DATA1 = 20/04/2022  
“Vencimento 3” - C5\_DATA1 = 05/05/2022  
“Vencimento 4” - C5\_DATA1 = 10/06/2022

Valor Total do Pedido de Venda R$ 1.000,00 (Total de todos os itens [C6\_VALOR])

Resultado do Pedido de venda 1:

* Parcela 1: 100,00 e vencimento 25/03/2022
* Parcela 2: 300,00 e vencimento 20/04/2022
* Parcela 3: 300,00 e vencimento 05/05/2022
* Parcela 4: 300,00 e vencimento 10/06/2022

**Exemplo de Cadastro 2 - Condição de Pagamento Tipo 9 - Valor Percentual**

E4\_CODIGO = 002

E4\_TIPO = 9

→ E4\_COND = % (Valor em percentual)

E4\_DESCRI = “TIPO 9 PERCENTUAL”

**Exemplo de Uso da condição “002” que é Tipo 9 e tem valor em percentual:**

Pedido de venda 2:

“Pedido de Vendas” - C5\_NUM: 000002  
“Condição de Pagamento” - C5\_COND: 002

“Parcela 1” - C5\_PARC1 = 10  
“Parcela 2” - C5\_PARC2 = 30  
“Parcela 3” - C5\_PARC3 = 30  
“Parcela 4” - C5\_PARC4 = 30

“Vencimento 1” - C5\_DATA1 = 25/03/2022  
“Vencimento 2” - C5\_DATA1 = 20/04/2022  
“Vencimento 3” - C5\_DATA1 = 05/05/2022  
“Vencimento 4” - C5\_DATA1 = 10/06/2022

Valor Total do Pedido de venda R$ 1.000,00 (Total de todos os itens [C6\_VALOR])

Resultado do Pedido de venda 2:

* Parcela 1: 10% sobre o total do pedido (R$100,00) e vencimento 25/03/2022
* Parcela 2: 30% sobre o total do pedido (R$ 300,00) e vencimento 20/04/2022
* Parcela 3: 30% sobre o total do pedido (R$ 300,00) e vencimento 05/05/2022
* Parcela 4: 30% sobre o total do pedido (R$ 300,00) e vencimento 10/06/2022

**Saiba mais:**

[**Todas as Condições de Pagamento (MATA360)**](https://tdn.totvs.com/x/PdpSDg)

**[Quando a mensagem TMKTIP905 é apresentada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003523132-MP-FAT-Quando-a-mensagem-TMKTIP905-%C3%A9-apresentada)**

**[Funcionamento do parâmetro MV\_TIPO9SP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13227131753751-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Funcionamento-do-par%C3%A2metro-MV-TIPO9SP)**
