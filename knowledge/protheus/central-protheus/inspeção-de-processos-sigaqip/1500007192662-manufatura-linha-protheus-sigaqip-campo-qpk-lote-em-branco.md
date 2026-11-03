---
article_id: 1500007192662
category: Inspeção de Processos (SIGAQIP)
content_hash: b989fee212ff52becc8f7d922b51d21cf57c60c9ddd1d05934290bb316296acf
fetched_at: '2026-06-28T22:42:25.707545+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Campo QPK_LOTE em branco
type: support-article
updated_at: '2024-05-17T13:36:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007192662-Manufatura-Linha-Protheus-SIGAQIP-Campo-QPK-LOTE-em-branco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:30 min**  
**Dúvida**Por quê o campo **QPK\_LOTE - Lote** encontra-se em branco após a criação de uma **OP - Ordem de Produção** pela rotina **MATA650 - Ordens de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Todas as versões  
  
**Solução**Quando o parâmetro **MV\_QINSPEC - Indica onde será realizada a Inspeção do Material quando houver integração QIP x PCP** está **igual a 1** o registro de inspeção é gerado no momento da abertura da **OP - Ordem de Produção**. Como neste momento não temos o número do lote a ser produzido, o campo **QPK\_LOTE** ficará em branco.   
Ao configurar o parâmetro **MV\_QINSPEC**com o valor **2**, deve ser realizado o apontamento da **OP** por meio das rotinas **MATA680** **- Produção PCP Mod 1** ou **MATA681 - Produção PCP Mod 2.** Desta forma o campo **QPK\_LOTE** terá origem com as informações dos campos **H6\_LOTECTL - Lote** + **H6\_NUMLOTE - Sub-Lote**.
