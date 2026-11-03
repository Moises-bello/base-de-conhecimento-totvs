---
article_id: 360062870393
category: TAF - REINF
content_hash: 291608dbb2cefbb6829dc4f749b6e151044ed913cc82ddd506de70f063c99221
fetched_at: '2026-06-28T22:41:33.499856+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - TAF - REINF -  Como fazer o encerramento/Alteração
  no R-1000 '
type: support-article
updated_at: '2023-04-04T12:19:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062870393-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-fazer-o-encerramento-Altera%C3%A7%C3%A3o-no-R-1000
---

**Duvida:**

* Como fazer o encerramento do R-1000?
* Como fazer alteração no R-1000?

**Ambiente:**

* Microsiga Protheus – Livros Fiscais – A partir da versão 12

**Solução:**

* O R-1000 é um evento que deve ser enviado apenas uma vez, por esse motivo a Receita Federal (e-cac) não permite que você envie o R-1000 mais de uma vez sem encerrar o período, dessa forma é necessário fazer a seguinte alteração.

**Encerramento de Período:**

* Acesse o Complemento Cadastral.
* Atualizações
* Configs. Taf
* Complemento Cadastral

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101252154/mceclip0.png)

* Selecione a Matriz da alteração
* Alterar

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101252794/mceclip2.png)

* Aba e-Social/Reinf
* Aba Reinf
* DT ini Oper = Deve conter o inicio do Reinf igual ao site do e-cac.(ex: 05/2018)
* DT. Fim Per = Data do mês de encerramento do período.(ex: 01/2021)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103415393/mceclip1.png)

* Atualizações
* Eventos Reinf
* Painel REINF.

* Apure e transmita o R-1000.

![R-1000.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13606838295191)

Transmitir

![R-1000_transmitido.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13606828641175)

Importante: Retornando consistente/ Autorizado o evento foi encerrado no E-cac.

**Após o envio do encerramento você pode fazer a alteração do R-1000**

**Alteração complemento Cadastral:**

* Acesse o complemento Cadastral
* Selecione a Matriz e selecione alterar
* Efetue a Alteração desejada
* Aba e-Social/Reinf
* Aba Reinf
* Campo DT ini Oper, preencha com a data superior do fechamento.(ex 02/2021)
* campo DT Fim Per, Deixar em branco.

![Complemento_cadastral.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13065059974167)

* Vá no Painel REINF.
* Apure e transmita os eventos.
