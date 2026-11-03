---
article_id: 360028428152
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 79ee621ffceaaae2ff5018bf20491e84617c0a25d22bb5c2b43575b670ec3ffe
fetched_at: '2026-06-28T22:39:57.575921+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - NaturezaOperacao
  São Leopoldo-RS
type: support-article
updated_at: '2025-06-25T21:18:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028428152-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-NaturezaOperacao-S%C3%A3o-Leopoldo-RS
---

**Dúvida**Como alterar o conteúdo da tag NaturezaOperacao para São Leopoldo-RS?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Conforme [Manual Webservice de São Leopoldo](http://www.saoleopoldo.rs.gov.br/?template=abreAnexos&arquivo=8455&nomeArquivo=Manual%20Web%20Service%20v.%201.1&categoriaDownload=1) a tag NaturezaOperacao é composta pelos seguintes códigos:

51- Imposto devido em São Leopoldo, com obrigação de retenção na fonte  
52 - Imposto devido em São Leopoldo, sem obrigação de retenção na fonte  
58 - Não tributável  
59 - Imposto recolhido pelo regime único de arrecadação Simples Nacional  
61 - Imposto devido em São Leopoldo, com obrigação de retenção na fonte  
62 - Imposto devido em São Leopoldo, sem obrigação de retenção na fonte  
63 - Imposto devido fora de São Leopoldo, com obrigação de retenção na fonte  
64 - Imposto devido fora de São Leopoldo, sem obrigação de retenção na fonte  
68 - Não tributável  
69 - Imposto recolhido pelo regime único de arrecadação Simples Nacional  
78 - Não tributável

Tratamos as naturezas conforme abaixo:

51: Campos F4\_ISSST=1 e A1\_RECISS ou C5\_RECISS=1;  
52: Campos F4\_ISSST=1 e A1\_RECISS ou C5\_RECISS=2;  
58: Campo F4\_ISSST=3, 4 ou 7;  
59: Parâmetro MV\_OPTSIMP=1;   
63: Campo F4\_ISSST=2;  
78: Tomador estrangeiro;
