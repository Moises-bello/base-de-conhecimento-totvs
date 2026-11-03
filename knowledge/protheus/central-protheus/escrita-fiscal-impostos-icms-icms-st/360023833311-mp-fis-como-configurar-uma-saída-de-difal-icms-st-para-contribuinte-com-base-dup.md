---
article_id: 360023833311
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 3e4b52bc1cb786ae75107ed0a81b80130a4898ba5d4d04d7dedcd9d0fe20b8c9
fetched_at: '2026-06-28T22:39:20.570739+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: MP - FIS - Como Configurar uma Saída de Difal ICMS ST para Contribuinte com
  Base Dupla ?
type: support-article
updated_at: '2024-10-08T21:21:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023833311-MP-FIS-Como-Configurar-uma-Sa%C3%ADda-de-Difal-ICMS-ST-para-Contribuinte-com-Base-Dupla
---

**Dúvida**Como configurar uma saída de Difal de icms st  para Contribuinte com Base Dupla  
  
**Ambiente**Protheus - Faturamento - A partir da versão 11.80  
  
**Solução**

Para esse calculo o tipo de pedido de vendas = Consumidor Final

**Solução**

O Diferencial de Alíquota na Saída para Cliente Contribuinte será o Diferencial ST*:*

Informe no **Cadastro do Produto Campo:** Solid Saida ( B1\_PICMRET) ou da **Exceção Fiscal** Campo: Margem de Lucro (F7\_MARGEM)  o percentual de ICMS-ST (MVA) estabelecido por norma legal, caso não exista, informe um percentual fictício (por exemplo 0,01) somente para possibilitar o cálculo pelo diferencial:

**TES**

* **Calcula ICMS**(F4\_ICM) = SIM
* **L. FISC. ICMS** (F4\_LFICM) = TRIBUTADO
* **Calc Dif ICM**. (F4\_COMPL) = NÃO
* **MATL CONSUMO** (F4\_CONSUMO) = SIM
* **AGREGA SOLID.** (F4\_INCSOL) = SIM
* **MKP.ICM.COMP** (F4\_MKPCMP) = NÃO
* **MARG. SOLID.** (F4\_MKPSOL) = NUNCA (Indica que o sistema deve ignorar o MVA preenchido no produto ou exceção fiscal)

**CLIENTE** (SA1) deve ser um dos tipos preenchido no parâmetro **MV\_TPSOLCF**, o **CLIENTE** deve ser de um Estado diferente do emitente (**MV\_ESTADO**) e ter a Inscrição Estadual preenchida.

**IPI na Base (F4\_INCIDE):**Este campo permite informar se valor de IPI incide na base de ICMS. Para o exemplo a seguir o IPI entrou na base de cálculo do ICMS, desta forma pode ser definido como "Consumidor Final" ou como "Sim/Não

**BASE DUPLA**

Para tratar Base Dupla deverá configurar o parâmetro **MV\_UFBDST**informe os estados que devem ter base dupla para o ST e o cadastro do cliente/pedido de venda o tipo de cliente deve ser **CONSUMIDOR FINAL.**
