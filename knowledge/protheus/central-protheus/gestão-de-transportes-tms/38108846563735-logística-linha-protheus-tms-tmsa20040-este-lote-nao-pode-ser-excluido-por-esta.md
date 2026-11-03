---
article_id: 38108846563735
category: Gestão de Transportes (TMS)
content_hash: fee4a60cb4efed2e5b34b1696b8bf9108768bebb7021682d02e8c073e4593a91
fetched_at: '2026-06-28T22:45:33.405897+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - TMSA20040 - Este lote nao pode ser excluido
  por esta rotina. Favor verifique a sua origem
type: support-article
updated_at: '2026-02-03T21:44:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38108846563735-Log%C3%ADstica-Linha-Protheus-TMS-TMSA20040-Este-lote-nao-pode-ser-excluido-por-esta-rotina-Favor-verifique-a-sua-origem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38108862797847) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao selecionar o documento para  realizar o estornar do cálculo do frete, ocorre o help **TMSA20040 - Este lote não pode ser excluído por esta rotina. Favor verifique a sua origem.**  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**  
Essa validação ocorre somente ao estornar um documento em que o **Docto.Transp - DT6\_DOCTMS** seja de um documento que não é gerado via cálculo do frete pelas rotinas **TMSA050 - Entrada de Documentos**, **TMSA170 - Lote de Entrada de Notas Fiscais** ou **TMSA200 - Cálculo do Frete.**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Necessário avaliar o **DT6\_DOCTMS** do documento para identificar a origem de geração desse documento.   
Por exemplo, se a mensagem ocorrer ao tentar estornar o cálculo de um **CT-e Complementar - DT6\_DOCTMS = 8**, como esse tipo de documento é gerado pela rotina **TMSA500 - Manutenção de Documentos**, ele deve ser cancelado pela mesma rotina.
