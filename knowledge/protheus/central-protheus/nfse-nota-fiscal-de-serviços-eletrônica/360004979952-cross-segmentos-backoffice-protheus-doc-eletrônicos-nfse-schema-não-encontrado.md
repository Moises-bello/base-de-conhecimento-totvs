---
article_id: 360004979952
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: e4f95c0ee89391d515cbb88d758eca285d9821ee3b1f86ec390b1a9836549a87
fetched_at: '2026-06-28T22:39:56.209621+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Schema não
  encontrado
type: support-article
updated_at: '2025-07-18T14:40:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004979952-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Schema-n%C3%A3o-encontrado
---

**Dúvida**Ao transmitir uma NFSE ocorre a falha de schema:

"SCHEMA não encontrado, verificar - \schemas\nfse\_v2.00\_3518800.xsd"  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
  
**Solução**

O erro de schema não encontrado ocorre quando é informado a versão incorreta no Wizard.cfg da rotina **FISA022**, no exemplo de erro acima usamos o município de Guarulhos-SP, mas esse erro pode ocorrer para qualquer município.

A nomenclatura do schema possui a versão (V2.00) seguida do código do município (3518800).

Para Guarulhos-SP o schema correto é nfse\_v3.00\_3518800.xsd, observe que a versão é 3.00 e não 2.00.

Identifique a versão do município no link abaixo ou pesquise o código do município na pasta schemas do TSS e localize a versão no nome do arquivo.

[Clique aqui: Versão dos Municípios Homologados](http://tdn.totvs.com/pages/releaseview.action?pageId=4814340)

Refaça o Wizard.cfg da rotina FISA022 informando a versão correta e em seguida retransmita e monitore a nota.
