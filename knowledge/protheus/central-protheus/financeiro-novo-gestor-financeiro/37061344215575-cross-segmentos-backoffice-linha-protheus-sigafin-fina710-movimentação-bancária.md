---
article_id: 37061344215575
category: Financeiro - Novo Gestor Financeiro
content_hash: 316cfe022715979b48ed5bfbaf7a7cf2571096aa0fbdf6167004bdba27237371
fetched_at: '2026-06-28T22:37:41.580386+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Movimentação
  bancária não calcula titulos baixados
type: support-article
updated_at: '2025-12-16T15:01:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37061344215575-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Movimenta%C3%A7%C3%A3o-banc%C3%A1ria-n%C3%A3o-calcula-titulos-baixados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37061344205207)** Tempo aproximado para leitura: **00:08:00 min**

**Dúvida**  
Na rotina Novo Gestor Financeiro, nas Movimentações Financeiras de Entrada, quando o título é baixado, o valor é descontado do campo Entradas, soma apenas títulos não baixados.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - todas as versões  
  
**Solução**  
O valor exibido no campo **Entradas** da rotina Novo Gestor Financeiro (Movimentações Financeiras) diminui (Debita) quando um título a receber é baixado, ou seja, o card de entradas soma apenas títulos **não baixados**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37061359450391)  
   
O Novo Gestor Financeiro (NGF) atua como uma ferramenta de **Fluxo de Caixa Provisório/Projetado**. O campo **Entradas** nesta tela tem a finalidade de demonstrar o valor de títulos a receber que **ainda impactarão o caixa**, ou seja, os valores esperados.

Por padrão, a tela de Movimentações Financeiras considera:

* **Entradas:** Títulos a Receber (Contas a Receber - **SE1** ou Pedidos de Venda - **SC6**) que ainda estão em aberto (ou seja, **não baixados**).
* **Saídas:** Títulos a Pagar (Contas a Pagar - **SE2** ou Pedidos de Compra - **SC7**) que ainda estão em aberto (ou seja, **não baixados**).

Quando um título a receber é **baixado (liquidado)**, ele deixa de ser uma **expectativa de entrada** futura no fluxo de caixa projetado e passa a ser considerado como um **saldo efetivo** (já realizado) na data da baixa, saindo da visão de projeção.  
   
Este não é um erro ou falha, mas sim o **comportamento padrão** da rotina para a projeção de fluxo de caixa. O valor do título baixado passa a compor a informação do saldo final, mas não mais o total das "Entradas" projetadas.  
   
A tela de Movimentações Financeiras é um **Fluxo de Caixa Gerencial**. O campo **Entradas** reflete a **projeção de recebimentos** (Contas a Receber em aberto) para os dias seguintes.  
   
**Impacto da Baixa:**

* Ao **baixar** um título a receber, ele é liquidado na tabela **SE1** (Contas a Receber).
* Como o título não está mais em aberto, ele é **removido** da soma do campo **Entradas** (que é o valor projetado/a receber).
* O valor **efetivamente recebido** (o da baixa) é refletido no **Saldo em Caixa/Bancos** na data da movimentação, se o processamento do Job do NGF estiver em dia.

Se o objetivo for visualizar o total de títulos **baixados** (os valores que **entraram** no caixa/banco), você deve observar o registro do dia correspondente na tabela de **Movimentações Financeiras**, focando nos seguintes campos:

* **Saldo em Caixa/Bancos (Acima da grade):** Reflete o saldo total atualizado das contas bancárias e caixa.
* **Entrada Acumulada (Na grade Diária):** Demonstra o total acumulado das entradas (recebimentos e outras movimentações) até a data da linha.

  A tabela que armazena os dados exibidos no Novo Gestor Financeiro é a **F75** (Saldos de Títulos) e **F76** (Saldos de Pedidos), sendo que a lógica de seleção de títulos a receber (Entradas) é para títulos **em aberto**.
