---
article_id: 4527773766679
category: Originação de Grãos (OG)
content_hash: 8f3bcae46b6058c5839749b001579c67cb193b3e7a1bcad0057aa9a70fd0a7a6
fetched_at: '2026-06-28T22:45:40.982857+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - MATA010M - Criação de novo fonte para comportar
  as funções
type: support-article
updated_at: '2025-06-24T14:42:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4527773766679-Agro-Linha-Protheus-AGR-MATA010M-Cria%C3%A7%C3%A3o-de-novo-fonte-para-comportar-as-fun%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20414800791575) Tempo aproximado para leitura: **00:00:25 min** **Dúvida**Como adiciono as funcionalidades na aba de produtos do agronegócio no cadastro de produto?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Foi criado o fonte **MATA010AGRO** com as funcionalidades para **incluir** produtos do agronegócio no cadastro de produto. Para habilitar a aba será necessário adicionar o termo **AGRO** no parâmetro **MV\_CADPROD - Parâmetro para informar quais cadastros complementares devem ser apresentados no cadastro de produto** e estar com o parâmetro **MV\_SIGAAGR - Ativa o Originação** ativo. Para integração com o Sistema **PIMS**, será necessário que o **adapter do MATA010 - Cadastro de Produtos** esteja na versão **4.007**.
