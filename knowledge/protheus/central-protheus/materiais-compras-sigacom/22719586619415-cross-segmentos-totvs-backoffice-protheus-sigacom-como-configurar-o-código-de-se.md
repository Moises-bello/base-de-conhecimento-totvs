---
article_id: 22719586619415
category: Materiais - Compras (SIGACOM)
content_hash: 27da8b2d65658b3bae067d7a5f8703871d2c19cb505bc79934f6c079475a7e1f
fetched_at: '2026-06-28T22:41:14.511265+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar o código
  de serviço para NFS-e no Importador Xml x Totvs Transmite?
type: support-article
updated_at: '2024-04-11T10:57:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22719586619415-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-o-c%C3%B3digo-de-servi%C3%A7o-para-NFS-e-no-Importador-Xml-x-Totvs-Transmite
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22719595622167) Tempo aproximado para leitura: **00:05:00min** **Dúvida**Como configurar o código de serviço para NFS-e no Importador Xml x Totvs Transmite?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Solução**

Sistema apresenta código de erro no monitor do Importador Xml ao integrar Nota Fiscal de Serviço (**NFS**) do Totvs Transmite.

**COM018** *- Este XML possui um código de serviço que não está cadastrado em um produto na empresa/filial corrente.*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22719595622935)

Para consultar o ***Codigo de Servico*** no Totvs Transmite, acessar o Portal do Transmite selecionar o documento e clicar em "Detalhar".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22719586590359)

No cadastro do produto amarrado ao fornecedor, informar o código do serviço conforme exemplo abaixo:

***Observação: Caso não tenha o código do serviço cadastrado, acesse a SX5, filtre a tabela 60 e realize o cadastro.***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22719586592663)

Após executar o processo realize o reprocessamento do documento para que seja apresentado no Monitor do Importador Xml:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22719586594711)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22719595630359)

No Documento ficará conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22719586598167)

***Saiba Mais :***

[Códigos de erro](https://tdn.totvs.com/pages/releaseview.action?pageId=271663193)

[Ponto de Entrada para manipular o código de serviço na geração da NF de Serviço](https://tdn.totvs.com/pages/releaseview.action?pageId=284475863)

[CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
