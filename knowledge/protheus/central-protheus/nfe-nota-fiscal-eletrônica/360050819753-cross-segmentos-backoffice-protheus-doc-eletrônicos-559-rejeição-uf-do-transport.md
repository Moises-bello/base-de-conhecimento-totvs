---
article_id: 360050819753
category: NFe - Nota Fiscal Eletrônica
content_hash: 7a140e828575341f6a1aef9a73c3335538334f28671201fd8f0de55d3c69c127
fetched_at: '2026-06-28T22:40:01.493872+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 559 Rejeição :
  UF do Transportador não informada'
type: support-article
updated_at: '2021-07-05T17:29:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050819753--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-559-Rejei%C3%A7%C3%A3o-UF-do-Transportador-n%C3%A3o-informada
---

**Dúvida**Como corrigir a rejeição abaixo?  
559 Rejeição : UF do Transportador não informada.

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**  
Esta rejeição, costuma ocorrer por ter informado a tag **IE** do transportador sem a **UF** no grupo **<transp>**, e segundo o Manual de Orientação do Contribuinte v6.00 da Sefaz a **UF** se torna obrigatória ao informar a **IE** do transportador, vide trecho abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076080674/mceclip2.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077204753/mceclip1.png)

Para ajuste, verifique se o cadastro da transportadora em uso na tabela **SA4 - A4\_EST** está corretamente preenchido, pois os dados para montar a tag **<transporta>**, no padrão, são buscados de lá.

Caso esteja corretamente preenchido, pode ser que alguma customização no *rdmake* NFESEFAZ (fonte responsável pela geração do xml da nfe) esteja influenciando na montagem desta tag.
