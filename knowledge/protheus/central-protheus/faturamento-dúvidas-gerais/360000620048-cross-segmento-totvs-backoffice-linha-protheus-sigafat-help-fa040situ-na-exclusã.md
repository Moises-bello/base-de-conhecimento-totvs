---
article_id: 360000620048
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 6ad992fae37b327656c00e2d6ca99e438b13ed8795c5f114cacbe9a2ca50c376
fetched_at: '2026-06-28T22:38:32.797168+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help FA040SITU
  na Exclusão do Documento de Saída
type: support-article
updated_at: '2025-04-10T14:22:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000620048-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-FA040SITU-na-Exclus%C3%A3o-do-Documento-de-Sa%C3%ADda
---

**Ocorrência**No módulo **Faturamento**, ao tentar excluir o Documento de Saída na **Rotina MATA521** é exibida a mensagem **FA040SITU "Verifica se o titulo esta em carteira, pois os que não estiverem, não serão deletados."**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 11.80.  
  
**Causa**Esta mensagem ocorre quando o sistema verifica o campo **E1\_SITUACA** e verifica que o título **não está** em **Carteira**, ou seja, campo "**E1\_SITUACA**" **diferente** de "**0**".  
  
**Solução**Verifique se os títulos gerados para essa Nota estão estornados para que o sistema permita sua exclusão.

Acesse a rotina "**Transferências (FINA060)**" e **transfira** os títulos gerados para essa nota para **Carteira** "**0**".
