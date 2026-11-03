---
article_id: 9623144280855
category: Financeiro - Aplicação / Emprestimos
content_hash: d62a05362280a6739bbe3870a7cc306d1ca149f9f1c5f441913f170ea7e3f2d6
fetched_at: '2026-06-28T22:37:59.394501+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: ' Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA171 - Cálculo
  de juros incorretos'
type: support-article
updated_at: '2022-10-18T18:50:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9623144280855--Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA171-C%C3%A1lculo-de-juros-incorretos
---

**Dúvida**Ao incluir um contrato na rotina aplicações/empréstimos utiliza a tabela SAC a uma taxa a.m. ou a.a., o sistema cálculo os juros incorretamente  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA171 - A partir da versão 12.1.33  
  
**Solução**Independente da modalidade do juros do seu contrato, valide o conteúdo dos parâmetros:

**MV\_EMPCAL1**

**MV\_EMPCAL2**

**MV\_EMPCAL3**

**MV\_EMPCAL4**

Considere ajusta-los se necessário para a modalidade de sua inclusão.

O parâmetro **MV\_EMPCAL2** por exemplo indica que os empréstimos configurados serão em **moeda nacional** e os juros serão calculados no regime de **juros simples**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9623063726487)

**Saiba Mais**<https://tdn.totvs.com/pages/viewpage.action?pageId=392500138>
