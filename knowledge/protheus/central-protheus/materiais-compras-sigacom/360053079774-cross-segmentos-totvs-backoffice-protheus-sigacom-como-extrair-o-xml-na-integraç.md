---
article_id: 360053079774
category: Materiais - Compras (SIGACOM)
content_hash: f4a16dc6eeb0d01b627946351b5bedb6bbf7673142f59bfdb9e7aa351df23a14
fetched_at: '2026-06-28T22:41:15.854239+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como extrair o XML
  na Integração EAI (Protheus) ?
type: support-article
updated_at: '2022-05-16T21:22:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053079774-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-extrair-o-XML-na-Integra%C3%A7%C3%A3o-EAI-Protheus
---

**Ocorrência**

Como extrair o XML na Integração EAI (Protheus) ?

**Ambiente**

Portheus – Compras – A partir da versão 11.80  
  
**Solução**

**Passo a passo:**

O EAI Protheus permite a troca de mensagens no formato XML com outros softwares, como por exemplo RM, Logix. Ao realizar a integração entre Software X Protheus existe a troca de mensagem em XML, desta forma podemos extrair XML de origem e o retorno.

Para extrair o XML entre no ambiente SIGACFG, acesse o Menu: Ambiente - Schedule - opção EAI:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087830634/mceclip1.png)

Na integração do Software com o Protheus, são criados os arquivos de transações:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087830654/mceclip2.png)

Selecione o arquivo que integrou e para extrair clique na lupa ![](https://tdn.totvs.com/download/thumbnails/356816635/image2018-4-25_17-28-23.png?version=1&modificationDate=1524688424000&api=v2) , ira apresentar as opções ![](https://tdn.totvs.com/download/thumbnails/356816635/image2018-4-25_17-29-20.png?version=1&modificationDate=1524688424000&api=v2) escolha qual XML deseja extrair.

**Visualizar mensagem Origem:** XML que o Software envia para o Protheus.

**Visualizar mensagem de Resposta:** XML que o Protheus envia para o Software.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087830734/mceclip3.png)

Através da tag **<Product>** consegue visualizar o Software que esta recebendo ou enviando.

**Exemplo:**

**XML de envio (original):** <Product version="12.1.18.0" **name="RM"**/>

**XML de resposta**:<Product version="12" **name="PROTHEUS"**/>

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
