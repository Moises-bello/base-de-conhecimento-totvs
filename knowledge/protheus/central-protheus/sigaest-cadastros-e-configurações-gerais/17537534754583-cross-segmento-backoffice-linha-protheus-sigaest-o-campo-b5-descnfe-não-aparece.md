---
article_id: 17537534754583
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: b6f45f03628ae0f5bd5c1cfb1b0ed6c839ac3c3f3555228d29a57c052767a2de
fetched_at: '2026-06-28T22:39:09.671547+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O campo B5_DESCNFE
  não aparece no Browser
type: support-article
updated_at: '2023-09-14T21:38:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17537534754583-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-O-campo-B5-DESCNFE-n%C3%A3o-aparece-no-Browser
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17537526128663) Tempo aproximado para leitura: **00:02:00 min****Dúvida**

O campo **B5\_DESCNFE** campo não aparece no Browser, na rotina complemento de produto.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para o campo **B5\_DESCNFE**aparecer no Browser é necessário realizar algumas configurações:

* Abrir o configurador no caminho Base de Dados, Dicionário, Base de Dados.
* Buscar pela tabela **SB5** e localizar o campo **B5\_DESCNFE**.
* Posicionado no campo clica na aba outros deixar a opção "Usado" e "Browser" marcados, conforme o Print:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17537198598551)

* Marcando essas opções clica em salvar via configurador conforme o Print:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17537276866455)

* Depois de salvo acessa o sistema via **SIGAMDI** no módulo **Estoque/Custos** na rotina complemento de produto(**MATA180**).
* Altera o produto em questão clica na aba "**Outros**" e o campo apresentará no **Browser** conforme o Print .

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17537831276567)

***Saiba Mais:***

*[Clique aqui e veja mais artigos sobre CADASTROS E CONFIGURAÇÕES GERAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
