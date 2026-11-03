---
article_id: 35313151498391
category: Escrita Fiscal - Error.log
content_hash: cdbee4c4dc07b9b37677039b764f803ce5753eaafac6a89d79f88f3d86338ed8
fetched_at: '2026-06-28T22:39:32.768218+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Inconsistência no
  CFOP ao utilizar a função Retornar no Documento de Entrada
type: support-article
updated_at: '2025-09-30T22:02:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35313151498391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Inconsist%C3%AAncia-no-CFOP-ao-utilizar-a-fun%C3%A7%C3%A3o-Retornar-no-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35313125382679) Tempo aproximado para leitura: **00:10 min**  
  
**Ocorrência**  
Ao utilizar a função **Retornar** no Documento de Entrada, o sistema está trazendo o **CFOP (Código Fiscal de Operações e Prestações)** incorreto.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - A partir da 12.1.2310  
  
**Causa**  
Após a atualização do acumulado, está apresentado inconsistência na função Retornar no Documento de Entrada, trazendo CFOP incorreto  
  
**Solução**  
Para corrigir o problema, é necessário aplicar o pacote de correção disponibilizado pela TOTVS:

| Versão | Link para Patch |
| --- | --- |
| 12.1.2210 | <https://r.totvs.io/p/1214653> |
| 12.1.2310 | <https://r.totvs.io/p/1214650> |
| 12.1.2410 | <https://r.totvs.io/p/1214651> |
| 12.1.2510 | <https://r.totvs.io/p/1214652> |
