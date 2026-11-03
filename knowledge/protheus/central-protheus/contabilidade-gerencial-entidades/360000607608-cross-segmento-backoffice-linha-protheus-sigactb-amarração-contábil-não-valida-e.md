---
article_id: 360000607608
category: Contabilidade Gerencial - Entidades
content_hash: 21823ef9afc98f9cf350a72a8ff145ba6264be7a4fdbaa78ac3f70c274c95978
fetched_at: '2026-06-28T22:40:49.675993+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: Cross Segmento  Backoffice Linha Protheus - SIGACTB - Amarração Contábil não
  Valida Entidades
type: support-article
updated_at: '2023-08-24T14:26:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000607608-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Amarra%C3%A7%C3%A3o-Cont%C3%A1bil-n%C3%A3o-Valida-Entidades
---

**Ocorrência**Ao incluir utilizar uma entidade contábil não está sendo validada mesmo com o parâmetro **MV\_CTBAMAR = 2.**

**Ambiente**Protheus - Contábil - A partir da versão 11.80  
   
 **Causa**Esta situação ocorre normalmente quando há no cadastro de Amarração das Entidades **(CTBA250 - Tabela CTA)** algum registro com todas as entidades em branco, conforme o exemplo abaixo:

![](http://tdn.totvs.com/download/attachments/271653093/image2017-2-13%209%3A55%3A22.png?version=1&modificationDate=1486987163000&api=v2)

**Solução**Para solucionar essa ocorrência, realize os seguinte passo:  
1. Acesse o módulo contábil;  
2. Acesse a rotina Amarração de Entidades **(CTBA250);**3. Exclua o cadastro de amarração que estiver com as entidades em branco.
