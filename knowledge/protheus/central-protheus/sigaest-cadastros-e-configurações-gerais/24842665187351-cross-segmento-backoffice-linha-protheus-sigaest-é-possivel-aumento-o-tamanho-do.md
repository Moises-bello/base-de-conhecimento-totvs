---
article_id: 24842665187351
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 4b370a34aa3090c3a65d9b61601683f0aa693a5a467ef9d128f5d6a8b66d5507
fetched_at: '2026-06-28T22:39:08.199337+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - É possivel aumento
  o tamanho dos campos de produto da tabela T0?
type: support-article
updated_at: '2025-03-12T12:25:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24842665187351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-possivel-aumento-o-tamanho-dos-campos-de-produto-da-tabela-T0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24842665177111) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**É possivel aumentar o tamanho de campo do produto na tabela T0?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.33  
  
**Solução**

Não é possível realizar a alteração do grupo T0, pois a SX5 não permite alteração do tamanho do campo.

Foi criado um grupo de campos para os registros voltados para a tabela **SBM (grupo de produtos)**.

Para solucionar essa limitação, foi desenvolvida a rotina **FISA308**:

[FISA308 - Grupos de Produto - Complemento de Rastreabilidade - Fiscal - P12](https://tdn.totvs.com/display/public/PROT/FISA308+-+Grupos+de+Produto+-+Complemento+de+Rastreabilidade+-+Fiscal+-+P12)

**A rotina FISA308 substitui a tabela T0 na SX5.**  
A implementação da rotina FISA308 oferece uma alternativa para vincular grupos de campos da tabela SBM, superando a limitação de tamanho de campo da tabela T0 na SX5.

**Saiba mais:**

*[Clique aqui para mais informações sobre a MATA010](https://tdn.totvs.com/display/public/PROT/Produtos+-+MATA010#ProdutosMATA010-PastaCadastrais)*

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de numeração automática (B1\_COD) via LicenceServer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406595504279-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-numera%C3%A7%C3%A3o-autom%C3%A1tica-B1-COD-via-LicenceServer)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de envio Messenger para ID de eventos do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003963562-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-envio-Messenger-para-ID-de-eventos-do-Estoque)*
