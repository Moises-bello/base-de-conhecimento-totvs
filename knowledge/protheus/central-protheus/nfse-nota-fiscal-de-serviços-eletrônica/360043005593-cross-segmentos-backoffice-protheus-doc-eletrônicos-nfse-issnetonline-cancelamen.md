---
article_id: 360043005593
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 531a9cb163ede6182680c395104549a3f25649710a43fa324eab31cebf5e1221
fetched_at: '2026-06-28T22:39:57.516892+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - IssNetOnline:
  Cancelamento E160 - Arquivo enviado fora da estrutura.'
type: support-article
updated_at: '2025-06-02T12:02:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005593-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-IssNetOnline-Cancelamento-E160-Arquivo-enviado-fora-da-estrutura
---

**Dúvida**Ao transmitir um cancelamento para prefeituras IssNetOnline ocorre:  
E160-ARQUIVO ENVIADO FORA DA ESTRUTURA DO ARQUIVO XML DE ENTRADA. ENVIE UM ARQUIVO DENTRO DO SCHEMA DO ARQUIVO XML DE ENTRADA.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**O código do cancelamento é obrigatório para esse município.  
Habilite o parâmetro **MV\_CODCANC=.T.**  
Dessa forma, ao transmitir o cancelamento, será apresentado uma tela com as opções de cancelamento para seleção.
