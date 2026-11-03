---
article_id: 360026401391
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: fff9b2192fffd435c5ef6abbe243f429911f59cfdb567ef718932cbab15f68c5
fetched_at: '2026-06-28T22:39:57.418430+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Envio Sincrono
  e Assincrono
type: support-article
updated_at: '2025-07-08T19:46:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026401391-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Envio-Sincrono-e-Assincrono
---

**Dúvida**Método de envio Síncrono e Assíncrono  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para alterar o método de envio do XML, utilize o parâmetro **MV\_ENVSINC**.  
Acesse o SIGACFG do Protheus para configuração.  
  
MV\_ENVSINC = N (Assincrono)  
                           S (Sincrono)  
  
Após ajuste do parâmetro, acesse a rotina FISA022 e reconfigure o wizard.config, dessa forma o parâmetro que também existe na SPED000 será atualizado.   
  
**Importante:** A prefeitura determina o método de envio, portanto verifique o método usado por sua prefeitura.
