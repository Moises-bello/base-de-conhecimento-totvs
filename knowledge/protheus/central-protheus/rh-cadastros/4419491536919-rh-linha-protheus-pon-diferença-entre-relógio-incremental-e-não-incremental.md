---
article_id: 4419491536919
category: RH - Cadastros
content_hash: ddabf8a0fb78b1a541b9cef08731bfb80638716bd7b297f315d178398d54dc94
fetched_at: '2026-06-28T22:44:52.971381+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Diferença entre Relógio Incremental e Não Incremental
type: support-article
updated_at: '2025-11-12T18:48:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419491536919-RH-Linha-Protheus-PON-Diferen%C3%A7a-entre-Rel%C3%B3gio-Incremental-e-N%C3%A3o-Incremental
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34024558179991) Tempo aproximado para leitura: 01:00:00 min  
  
Dúvida**Qual é a diferença entre Relógio Incremental e Não Incremental?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução  
Incremental:** Efetua a leitura a partir do último registro lido. Exemplo Incremental:A leitura de marcações é efetuada às 09:00 e o último registro lido é do sequencial (NSR) 100. Para apontamento/classificação, será considerado do registro **101 em diante.**   
\*\*Observação: Para **relógios REP** a informação **Incremental= SIM é obrigatória** sendo exigida pela Portaria 1510 e 671 do Ministério do Trabalho.  
  
**Não Incremental:** Sempre lê todos os registros do arquivo texto, não validando qual seria o último registro lido. Exemplo Não Incremental:  
A leitura de marcações é efetuada às 09:00, após isso é efetuada novamente as às 18:00, neste caso, a leitura não vai considerar o último registro lido para apontamento. Portanto, serão geradas informações de **[Rejeição Automática](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015530551) na SP8 e no Espelho de Ponto**, para estas marcações que já foram lidas anteriormente.  
  
  
**Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
