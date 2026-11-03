---
article_id: 360020204771
category: Faturamento - Cenários de Venda
content_hash: 3082697f20c48965e50f7ce2be6596e2678db9e3f4c606787be4663fd9591e33
fetched_at: '2026-06-28T22:38:34.051374+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Tabela de preço por estado
  [DA1_ESTADO] ou tipo de operação [DA1_TPOPER]
type: support-article
updated_at: '2025-11-13T13:17:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020204771-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Tabela-de-pre%C3%A7o-por-estado-DA1-ESTADO-ou-tipo-de-opera%C3%A7%C3%A3o-DA1-TPOPER
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36308728628503)** Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**Como utilizar o campo estado e tipo operação na tabela de preço?

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

É possível validar o preço por localização de duas maneiras, pelo campo **"**Estado (DA1\_ESTADO)" ou "Tipo Operação (DA1\_TPOPER)".

Para que um seja validado o outro tem de estar vazio, ou é por estado específico (DA1\_ESTADO) ou por estados da região (DA1\_TPOPER).

Caso a escolha seja de formular o preço pelo campo "Tipo de Operação (DA1\_TPOPER)", o sistema leva em conta o parâmetro da sua localização (MV\_ESTADO) para formular o preço no pedido/orçamento de venda.

Exemplos:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12233317790231)

* 1. Se MV\_ESTADO = SP e o A1\_EST do cliente colocado no pedido de venda for SP, o preço será R$10 (DA1\_TPOPER = Estadual)
* 2. Se MV\_ESTADO = SP e o A1\_EST do cliente colocado no pedido de venda for qualquer estado se não SP, o preço será R$20 (DA1\_TPOPER = Interestadual)
* 3. Se MV\_ESTADO = SP e o A1\_EST do cliente colocado no pedido de venda for qualquer estado da região norte/nordeste, o preço será R$30 (DA1\_TPOPER = Norte/Nordeste)

Os tópicos 2 e 3 podem existir juntos, nesse caso, será acatado a linha que se enquadra com o pedido de vendas, sendo "Norte/Nordeste", caso o Estado (A1\_EST) do cliente colocado no pedido/orçamento não seja igual ao MV\_ESTADO, ficando com o valor R$30 e não R$20.

**Fluxo nativo do Tipo de Operação (DA1\_TPOPER):**

1 - Estadual: Indica que a Tabela de Preço vale apenas para clientes dentro do Estado definido no parâmetro MV\_ESTADO.

2 - Interestadual: Indica que a Tabela de Preço vale para todos os Estados, exceto o Estado definido no parâmetro MV\_ESTADO.

3 - Norte e Nordeste: Indica que a Tabela de Preços vale apenas para as regiões Norte e Nordeste.

4 - Todos: Indica que a Tabela de Preço vale para todos os Estados da tabela 12 - Unidade Federativa.

**Observação 1:**

Para os campos Estado e Tp. Operação, existe uma regra de prioridade. Ao informar o Estado o sistema desconsidera o campo Tp. Operação, independente do seu conteúdo.

Portanto, para que as informações contidas no campo Tp.Operação tenham valor, deixe o campo Estado em branco.

Existe a opção **"**DA1\_TPOPER = Todos/Em branco**"** em que o **"**Estado do cliente (A1\_EST)**"** do cliente é desconsiderado.

**Observação 2:**

O campo Tipo de Operação (DA1\_TPOPER) na Tabela de Preços (OMSA010) opera com mesma diretriz utilizada nos Livros Fiscais. Neste campo validamos a operação utilizando o parâmetro MV\_NORTE

**Saiba Mais:**

* **[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Reajuste de Valores na Tabela de Preço, Preço Base e Pedidos em Aberto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019193491-MP-FAT-Reajuste-de-Valores-na-Tabela-de-Pre%C3%A7o-Pre%C3%A7o-Base-e-Pedidos-em-Aberto)**
* **[Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT - Como bloquear a tabela de preço para novos pedidos de venda e manter o valor nos pedidos em aberto já gravados?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049369453-MP-FAT-Bloquear-Tabela-de-Pre%C3%A7o)**
* [**FAT0269\_Precificação no módulo Faturamento**](https://tdn.totvs.com/x/GkNyFw)
* [**FAT0175\_Campo\_Tipo\_de\_operação\_da\_Tabela\_de\_Preço (DA1\_TPOPER)**](https://tdn.totvs.com/x/T7IpE)
