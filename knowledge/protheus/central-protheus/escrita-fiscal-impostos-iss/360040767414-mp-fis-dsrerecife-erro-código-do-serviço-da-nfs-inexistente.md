---
article_id: 360040767414
category: Escrita Fiscal - Impostos - ISS
content_hash: 5c2c6e2b903bdf11bff869fcbd562af6510a18fdabae4fd433925c3988f357f5
fetched_at: '2026-06-28T22:39:35.297531+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: MP - FIS - DSRE/RECIFE - Erro - Código do Serviço da NFS Inexistente
type: support-article
updated_at: '2021-04-28T20:26:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040767414-MP-FIS-DSRE-RECIFE-Erro-C%C3%B3digo-do-Servi%C3%A7o-da-NFS-Inexistente
---

**Dúvida**Erro - Código do Serviço da NFS Inexistente  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
O erro ocorre pois esta nota não teve calculo de ISS e não deveria ter gerado no arquivo. Será necessário  verificar o tipo de documento, se é realmente uma nota de serviço.

Para caracterizar uma nota de serviço, verifique como foram configuradas as informações abaixo:

CFOP no cadastro de TES e CODIGO DE SERVIÇO no cadastro de Produto.
