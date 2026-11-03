---
article_id: 38392455452183
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 01aaabb01be9d9548f606fa136f24cde2adf4ad4e43e9ae14eeec685f4b4e0a4
fetched_at: '2026-06-28T22:41:48.413078+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - Divergência entre os
  relatórios ATFSV003, ATFSV005 e ATFSV009
type: support-article
updated_at: '2026-02-18T19:36:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38392455452183-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Diverg%C3%AAncia-entre-os-relat%C3%B3rios-ATFSV003-ATFSV005-e-ATFSV009
---

**Dúvida**  
Diferença entre os relatórios Posição Valorizada dos Bens (ATFSV003), Posição Valorizada por Conta na Data (ATFSV005) e Resumo por Conta (ATFSV009).  
  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Ativo Fixo – a partir da release 12.1.2310  
  
  
**Solução**

1. **Posição Valorizada dos Bens (ATFSV003):** Este relatório apresenta os bens agrupados por contas, exibindo a posição valorizada em até cinco moedas. Também contempla os bens totalmente depreciados, para os quais não há mais incidência de depreciação, utilizando uma visão analítica detalhada de cada item. Além disso, demonstra o campo Valor Depr. Mês Moeda 1 (N3\_VRDMES1).  
     
   Atenção as perguntas, "Quanto às baixas" e "Imprime Total de Baixas" no relatório, elas iram alterar os movimentos e consequentemente os valores.  
     
   [ATFSV003 - Posição Valorizada dos Bens](https://tdn.totvs.com/pages/releaseview.action?pageId=772014331)
2. **Posição Valorizada por Conta na Data (ATFSV005):** Permite a impressão da posição valorizada dos bens em uma data específica, com base nas movimentações e não com base no saldo contábil do bem. O objetivo do relatório é demonstrar os valores dos bens na data informada pelo usuário, conforme as movimentações e seus impactos nos saldos das contas que compõe o bem. Além disso, demonstra o valor da ampliação para os bens que tiveram.  
     
   [ATFSV005 - Posição Valorizada por Conta na Data](https://tdn.totvs.com/pages/releaseview.action?pageId=770959747)
3. **Resumo por Conta (ATFSV009):** Focado em uma visão sintética, agrupa os valores diretamente pelas contas contábeis cadastradas no bem.  
     
   [ATFSV009 - Resumo por Conta](https://tdn.totvs.com/display/public/PROT/Smart+View+-+Resumo+por+Conta)

**Por que os valores podem não bater?**

1. **Depreciação e Saldos**: O relatório ATFSV005 tem como foco as movimentações do ativo. Podem ocorrer divergências de valores caso existam depreciações específicas (como a Acelerada) influenciando o campo N3\_VRDMES1, ou ainda, se houver depreciações não processadas.
2. **Data de Referência**: Se o ATFSV003 for gerado hoje e o ATFSV005 com data retroativa, os valores não baterão, pois o primeiro reflete o estado atual da tabela SN3 e o segundo reflete o cálculo histórico.  
     
   Para que os valores "batam", todos devem ser extraídos com a mesma data de referência. E se mesmo assim apresentar diferença no ATFSV005 deve executar o cálculo mensal ou descálculo mensal. Assim, a depreciação acumulada será alterada.

Todos os relatórios são gerados com base nas tabelas de cadastro (SN1) e saldos e valores (SN3).  
  
  
**Saiba mais:**  
[Smart View - Ativo Fixo](https://%20https://tdn.totvs.com/display/public/PROT/Smart+View+-+Ativo+Fixo)
