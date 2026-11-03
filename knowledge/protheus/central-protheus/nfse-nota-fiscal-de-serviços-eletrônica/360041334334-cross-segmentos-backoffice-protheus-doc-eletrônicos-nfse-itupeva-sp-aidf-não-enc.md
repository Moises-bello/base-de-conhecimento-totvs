---
article_id: 360041334334
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 0ccb7de63b5b0ff2064d433b3dbc06d487bd32a754116a9ea4523be381206f3b
fetched_at: '2026-06-28T22:39:57.525193+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Itupeva-SP:
  AIDF não encontrado'
type: support-article
updated_at: '2025-07-02T14:14:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041334334-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Itupeva-SP-AIDF-n%C3%A3o-encontrado
---

**Dúvida**Como corrigir o erro AIDF não encontrado para NFSe de Itupeva?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Acesse o portal de Itupeva e faça download da lista de pré-notas em:  
- Consulta/Manutenção de Blocos p/ Pré-NFS-e p/ Utilização de WebService.  
- Acesse rotina **FISA022**, no menu 'Outras Acoes' há uma opção para importar a tabela AIDF, faça a importação na rotina.  
- Emita os RPSs seguindo o sequencial determinado pela prefeitura no AIDF.  
  
**Observação:**Para importar o arquivo na rotina **FISA022**, renomeie o arquivo de .TXT para .AIDF, todos os dados serão gravados na tabela C0P do Protheus.
