---
article_id: 360038769994
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 072b1818461e3fe9c1775ef01d21b82db117a7a132ce225886f0910206d35152
fetched_at: '2026-06-28T22:39:58.498195+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - São Paulo
  CodigoCEI e MatriculaObra.
type: support-article
updated_at: '2025-06-20T12:05:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038769994-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-S%C3%A3o-Paulo-CodigoCEI-e-MatriculaObra
---

**Dúvida**Como enviar as tags abaixo no XML da nota de Serviços de São Paulo-SP?<CodigoCEI> - Código do CEI – Cadastro específico do INSS  
<MatriculaObra> - Número da matrícula de obra.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.

**Solução**Para transmitir essas tags na NFS-e, devem ser criados dois novos campos na tabela SC5 e estes campos devem ser informados no parâmetro MV\_XMLOBRA, nas posições 12 e 14.

Para maiores detalhes sobre o parâmetro MV\_XMLOBRA, consulte o [Documento Técnico](http://tdn.totvs.com/pages/viewpage.action?pageId=187533341).  
  
Exemplo de preenchimento do parâmetro MV\_XMLOBRA:  
{,,,,,,,,,,,'C5\_CEI',,'C5\_MOBRA'}

[Manual de integração webservice SP.](http://notadomilhao.prefeitura.sp.gov.br/cidadao/informacoes-gerais/manuais-arquivos/nfe_web_service.pdf/@@download/file/NFe_Web_Service%20.pdf)
