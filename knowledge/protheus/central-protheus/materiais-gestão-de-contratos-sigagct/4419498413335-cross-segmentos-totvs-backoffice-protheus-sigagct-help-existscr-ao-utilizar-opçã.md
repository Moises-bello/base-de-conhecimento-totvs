---
article_id: 4419498413335
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 25cddc8f9842f79d662a5a6f1ae39724010393f01ca1ddd1f46f0f861c398b61
fetched_at: '2026-06-28T22:37:22.948067+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help EXISTSCR ao utilizar
  opção "Aprovar Revisão " na rotina de Manutenção de Contratos
type: support-article
updated_at: '2022-01-18T19:07:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419498413335-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-EXISTSCR-ao-utilizar-op%C3%A7%C3%A3o-Aprovar-Revis%C3%A3o-na-rotina-de-Manuten%C3%A7%C3%A3o-de-Contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Ao utilizar opção "Aprovar Revisão " na rotina de Manutenção de Contratos, ocorre o Help " EXISTSCR ":

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419498080535/mceclip1.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419490578327/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

A mensagem de Help EXISTSCR ao tentar tentar utilizar a opção de "Aprovar Revisão" em "Outras Ações" na rotina de "Manutenção de Contratos, ocorre quando está se tentando aprovar uma revisão pela opção de aprovação da rotina de Manutenção, de um contrato que se encontra com o Status para ser aprovada a Revisão por "Alçadas" pela rotina de "Aprovações" (MATA094)

Veja se o contrato em questão se encontra com a legenda Roxa ( Revisão - Aprovação por Alçadas) :

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419498163607/mceclip2.png)

Neste caso a Aprovação do Documento deve ser realizada pela rotina de Aprovações, no caminho "SIGAGCT->Atualizações->Aprovações->Documentos (MATA094)":

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419490798359/mceclip4.png)

***Obs.:***

Na Visualização do contrato pode ser verificada a Alçada de aprovação, observando quais são os usuários Aprovadores que devem utilizar a rotina de Aprovação de Documentos por Alçada (MATA094) para aprovarem o documento:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419506565271/mceclip3.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419513037975/mceclip6.png)

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
