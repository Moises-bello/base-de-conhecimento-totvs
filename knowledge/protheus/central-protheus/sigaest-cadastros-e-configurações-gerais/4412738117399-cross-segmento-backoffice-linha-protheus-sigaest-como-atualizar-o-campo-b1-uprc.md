---
article_id: 4412738117399
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: e2b607d6554fc9f44a169c252ee1de4d6f6e9d178e3630bf1684976ed0f713e7
fetched_at: '2026-06-28T22:39:08.088285+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como atualizar o campo
  B1_UPRC com o ultimo preço de Compra?
type: support-article
updated_at: '2021-11-10T14:10:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412738117399-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-atualizar-o-campo-B1-UPRC-com-o-ultimo-pre%C3%A7o-de-Compra
---

**Dúvida**Como configurar o sistema para que ao realizar entradas no sistema o campo B1\_UPRC seja atualizado?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Para que o campo B1\_UPRC seja preenchido com as informações da ultima compra, é necessário a seguinte configuração:

1. Configurar uma TES (MATA080) com o campo F4\_UPRC = "Sim":

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412737376791/mceclip0.png)  
2. Após isso realizar o Documento de Entrada (MATA103). Vale lembrar que o campo B1\_UPRC só será atualizado se o tipo for "Normal" ou "Complemento":

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412706681879/mceclip1.png)  
3. Veja que após isso o campo B1\_UPRC já se encontra atualizado:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412737702039/mceclip2.png)

**Importante:** Na rotina de Documento de Entrada (MATA103), clicando em F12, existem dois perguntes relacionados a atualização do campo B1\_UPRC:

1. "Ultimo preco c/Desc" - Opção utilizada para considerar o valor de desconto na atualização dos campos B1\_UPRC (Último preço de compra), no momento da gravação do Documento de Entrada:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412738272791/mceclip4.png)

2. "Atualiza ultimo preço por" - Caso o usuário tenha a necessidade de considerar a data de recebimento, será gravado o conteúdo do campo D1\_DTDIGIT (Data de Digitação), caso necessite considerar a data de emissão, será gravado o conteúdo do campo D1\_Emissão (Data de Emissão):

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412738378903/mceclip5.png)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
