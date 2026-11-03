---
article_id: 4420378223639
category: TAF - REINF
content_hash: af7fc95416fc6e443cec87b10b80d1017f902e42595d19f77bc6cb8793a378a6
fetched_at: '2026-06-28T22:41:33.455057+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Extrator fiscal
  - carga de cadastros -  REINF '
type: support-article
updated_at: '2023-03-30T13:05:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420378223639-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Extrator-fiscal-carga-de-cadastros-REINF
---

**Dúvida**

Alguns dos meus itens cadastrados não estão integrando ao TAF, o que fazer?

**Produto**

TAF - SIGATAF - A partir da 12.1.33

**Solução**

Esse erro ocorre pois o extrator fiscal sempre vai validar a data da criação dos cadastros, com isso é sempre necessário efetuar a Carga inicial antes de começar a utilizar o TAF.

Como Executar a carga inicial? Siga os passos abaixo para executar o procedimento.

1) Abra o extrator fiscal e configure conforme os prints abaixo.

Data inicial de 01/01/1970 até a data de hoje.

Filtra Apenas Cadastros.

Filtra apenas Reinf como "sim"

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420373342359/mceclip0.png)

Nota fiscal de ?, deixar em branco.

nota fiscal até?. deixar como ZZZZZ

serie de?, deixar em branco

seria até?, deixar como ZZZZZ

Espécie do documento?(separado por virgula) deixar sempre em branco

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420373434135/mceclip1.png)

Após Gere o extrator fiscal para concluir a carga inicial.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420378197271/mceclip2.png)
