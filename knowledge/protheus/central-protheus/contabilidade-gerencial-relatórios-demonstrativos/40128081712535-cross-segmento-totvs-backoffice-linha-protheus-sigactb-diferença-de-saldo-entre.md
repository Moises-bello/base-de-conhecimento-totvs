---
article_id: 40128081712535
category: Contabilidade Gerencial - Relatórios Demonstrativos
content_hash: e18fdd6892429c1adf6b4bafd5d7c7b4b178274f78575e83c00b85b5ffef6eec
fetched_at: '2026-06-28T22:40:38.904525+00:00'
product: protheus
section_id: 1500001548882
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - Diferença de
  saldo entre DRE (CTBR510) e Balancete (CTBR040)
type: support-article
updated_at: '2026-05-04T10:54:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40128081712535-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-Diferen%C3%A7a-de-saldo-entre-DRE-CTBR510-e-Balancete-CTBR040
---

Ao emitir o relatório Demonstrativo de Resultado (DRE) no TOTVS Backoffice (Protheus) pode haver divergência em relação ao balancete devido a inconsistências na visão gerencial ou na estrutura do modelo de demonstração. A solução envolve emitir relatórios com a visão padrão, ajustar a visão customizada da empresa conforme modelo disponibilizado ou, se necessário, reprocessar saldos para corrigir os valores.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40128081681815) Tempo aproximado para leitura: **1 min**  
  
**Ocorrência**  
Ao emitir o relatório de Demonstrativo de Resultado (DRE), é apresentada uma diferença de valor em relação ao balancete.   
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - a partir da versão 12  
  
  
**Causa**  
A divergência em relatórios que usam a visão gerencial costuma acontecer por conta de algumas inconsistências na configuração da visão que o usuário está utilizando ou na estrutura do modelo de demonstração. Para entender melhor o que está causando isso, é importante verificar se o problema está relacionado especificamente à visão customizada da empresa.  
  
  
**Solução**

1. Realize a emissão dos relatórios DRE (CTBR510) e Balancete (CTBR040), utilizando a visão padrão disponibilizada pela TOTVS para descartar inconsistências na visão gerencial da empresa.  
   * [Arquivos modelos - visões gerenciais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008505768-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-arquivos-modelos-plano-referencial-vis%C3%B5es-gerenciais?source=search)
   * Verifique a documentação que traz como realizar a importação visão gerencial:  
       
     [CTBA161 -](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007545672-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-importar-Vis%C3%A3o-Gerencial?source=search) [Como importar Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007545672-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-importar-Vis%C3%A3o-Gerencial?source=search)
2. Caso o erro não ocorra com a visão padrão, será necessário realizar o ajuste da visão da empresa, baseando-se no arquivo modelo disponibilizado.
3. Se o erro persistir mesmo utilizando a visão padrão, verifique a necessidade de reprocessamento de saldos, informando a data inicial como o último dia do mês com saldo correto e a data final como o último mês do período com movimentação.  
     
   [CTBA960 -](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36347421005975-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA960-Processo-de-atualiza%C3%A7%C3%A3o-de-saldos) [Processo de atualização de saldos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36347421005975-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA960-Processo-de-atualiza%C3%A7%C3%A3o-de-saldos)
