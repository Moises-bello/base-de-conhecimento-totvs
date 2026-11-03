---
article_id: 4427849753367
category: NFe - Nota Fiscal Eletrônica
content_hash: 1d70bcc01e1f2c9e972d920849d9f557e64f36788b77481b6fdf86fcb4bdcbc3
fetched_at: '2026-06-28T22:40:05.356837+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 844 Rejeição: Código
  de Item da Lista de Serviços inexistente'
type: support-article
updated_at: '2025-07-18T18:17:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4427849753367-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-844-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-Item-da-Lista-de-Servi%C3%A7os-inexistente
---

**Dúvida**Como solucionar a rejeição 844 Rejeição: Código de Item da Lista de Serviços inexistente ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

Campos para cálculo do **ISSQN na NF-e conjugada,** onde há a prestação de serviços sujeitos ao ISSQN e fornecimento de peças sujeitas ao ICMS. Verificar se o Item da Lista de Serviços (campo: cListServ) consta na Tabela de Códigos de Item da Lista de Serviços.

1. Se realizada uma nota conjugada de produto e serviço o código utilizado na *TAG clistServ,* está incorreto.

2. Verificar a Tabela de Códigos de Item da ***Lista de Serviços*** publicada na aba ““Documentos”, opção “Diversos” do Portal Nacional da NF-e ***(www.nfe.fazenda.gov.br), ou no link abaixo:***

*[Tabela de Códigos de item da Lista de Serviços](Tabela%20de%20C%C3%B3digos%20de%20item%20da%20Lista%20de%20Servi%C3%A7os)*

3. Após alterar o código de item de serviço no cadastro de produto no campo ***Cod. serv. ISS*** **B1\_CODISS ou  BZ\_CODISS** (Indicador de Produtos), conforme a tabela , ***exclua a nota e gere novamente.***

* ***Validação da Sefaz:***

![844_rejeicao.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4427791930903)
