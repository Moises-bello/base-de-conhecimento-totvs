---
article_id: 1500002648682
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 9c2cd7acbcb446f264689a1d0fc463876d1766a22f748cc2c012dd1e8f3e266e
fetched_at: '2026-06-28T22:39:58.489864+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - SALVADOR:
  P120 - Apenas serviços tributados, no município, podem sofrer retenção de ISS.'
type: support-article
updated_at: '2025-06-20T12:08:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002648682-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-SALVADOR-P120-Apenas-servi%C3%A7os-tributados-no-munic%C3%ADpio-podem-sofrer-reten%C3%A7%C3%A3o-de-ISS
---

**Dúvida**Ao transmitir um RPS para a prefeitura de Salvador-BA ocorre a rejeição: ***"P120 - Apenas serviços tributados, no município, podem sofrer retenção de ISS."***Essa rejeição normalmente está acompanhada da rejeição E36 - Campo ISS Retido inválido.

![P120.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002408942/P120.PNG)  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Essa é uma rejeição gerada pela prefeitura de salvador com base nas tags e conteúdos abaixo:  
  
<NaturezaOperacao> 2 - Tributado Fora de Salvador  
<IssRetido> 1 - Retido pelo tomador  
<ItemListaServico> CODISS será validado com base na Lei Complementar nº 116/2003  
<CodigoMunicipio> Município de prestação do serviço fora de Salvador.  
  
Parecer da prefeitura de Salvador com base no [Manual NFS-e](https://nfse.sefaz.salvador.ba.gov.br/OnLine/Documentos/MANUAL%20NFS-e.pdf):  
  
![Iss_Retido_fora.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002410802/Iss_Retido_fora.PNG)  
  
Nesse caso, é necessário validar o código de serviço na Lei Complementar nº 116/2003 e se o código realmente não permitir a retenção fora de Salvador, é necessário alterar os campos A1\_RECISS/C5\_RECISS para 2 e F4\_ISSST para 1-Dentro do município, dessa forma o serviço será tributado dentro de Salvador e o ISS será pago pelo próprio prestador do serviço.  
  
**É importante** frisar que essa é uma regra municipal, toda e qualquer argumentação com relação a esse tema deve ser feita junto ao fisco da prefeitura de Salvador.
