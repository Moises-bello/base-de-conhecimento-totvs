---
article_id: 13295404006935
category: SIGAACD - Automação e Coleta de Dados
content_hash: f21794abd0b69ca00cafffae4e73059ba4164c397accdaf2c0e1d7592076af79
fetched_at: '2026-06-28T22:39:11.315976+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV166 - Como efetuar
  apontamento de divergência durante a separação de produtos?
type: support-article
updated_at: '2025-02-24T14:54:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13295404006935-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV166-Como-efetuar-apontamento-de-diverg%C3%AAncia-durante-a-separa%C3%A7%C3%A3o-de-produtos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23470742610967) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como apontar Divergência na Separação e qual a relação dela com os parâmetros MV\_DIVERPV e MV\_DIVERCT?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**

O parâmetro **MV\_DIVERCT** tem a finalidade na utilização do atalho **CTRL + P** e informar o código da divergência pulando o item para dar andamento na finalização da ordem de separação e a ordem ficar finalizada na rotina **ACDA100**.

O Parâmetro **MV\_DIVERPV** tem a finalidade de excluir um item da separação retornando o status do pedido de vendas novamente liberado e gerar uma outra ordem de separação.

Os parâmetros **MV\_DIVERCT** e **MV\_DIVERPV** não pode ter o mesmo código de divergência para não haver travamento na rotina de separação.

 - **Veja abaixo um exemplo simulado utilizando as configurações descritas acima:**

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre ACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*

*[Separação - ACDV166 - Automação de Coleta de Dados - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=545240659)*

*[Divergência permanece na ordem de separação finalizada](https://tdn.totvs.com/pages/releaseview.action?pageId=545239668)*
