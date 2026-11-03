---
article_id: 360045564053
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 51f5a2c9baf8c7b176488b8ba211e28560c91f3a942470221430983a9621d6dd
fetched_at: '2026-06-28T22:39:57.648526+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Qual a finalidade
  dos Rdmakes
type: support-article
updated_at: '2025-05-21T18:53:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045564053-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Qual-a-finalidade-dos-Rdmakes
---

**Dúvida**Qual a finalidade de cada rdmake para NFSE?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões   
  
**Solução**NFSEXML001.PRW - Atende modelo **DSFNET.**NFSEXML002.PRW - Atende modelo **ABRASF.**NFSEXML003.PRW - Atende modelo **Egoverne/Osasco-SP.**NFSEXML102.PRW - Atende modalidade upload de arquivo **TXT/XML.**NFSEXMLUNI.PRW - Atende exclusivamente **Totvs Colaboração.**NFSEXMLENV.PRW - Atende os modelos  **DSFNET, ABRASF, e Egoverne,** substituindo os rdmakes NFSEXML001, NFSEXML002 e NFSEXML003.  
  
Na versão 12, em qualquer release, os rdmakes NFSEXML001, NFSEXML002 e NFSEXML003, **foram descontinuados**, sendo substituídos pelo rdmake NFSEXMLENV.  
  
Portanto, basta que compile o rdmake NFSEXMLENV e mantenha o parâmetro MV\_NFSEMOD = .T.

Link para download dos últimos rdmake disponíveis: [clique aqui.](https://suporte.totvs.com/portal/p/10098/download?e=1152109)
