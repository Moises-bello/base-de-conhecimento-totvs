---
article_id: 360024138112
category: Materiais - Compras (SIGACOM)
content_hash: c6b0f3dfcfe016b120ccd06e810c04b53a8f9ea29557ad76654fe07922f2fac0
fetched_at: '2026-06-28T22:41:10.161488+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Permitir Autorização
  de Entrega para um fornecedor diferente do Contrato de Parceria
type: support-article
updated_at: '2025-03-17T19:57:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024138112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Permitir-Autoriza%C3%A7%C3%A3o-de-Entrega-para-um-fornecedor-diferente-do-Contrato-de-Parceria
---

**Dúvida**

Permitir Autorização de Entrega para um Fornecedor diferente do Contrato de Parceria.

**Ambiente**

Protheus - Compras - A partir da versão 11.08

**Solução**

Na rotina MATA122 - Autorização de Entrega, para que possa selecionar todos os Contratos de parceria, independente do Fornecedor, o parâmetro MV\_CTRSELF precisa estar com o conteúdo igual a .T..

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419467266071/mceclip2.png)

Serão apresentados os Contratos de todos os fornecedores, conforme exemplo abaixo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419475135383/mceclip3.png)

Caso o parâmetro MV\_CTRSELF esteja com o conteúdo igual a .F., será apresentado somente os Contratos do Fornecedor do Contrato de Parceria.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419467145239/mceclip1.png)

Acessar o Configurador (SIGACFG) Base de Dados / Dicionário / Base de Dados opção Parâmetros

Pesquisa por: **MV\_CTRSELF**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055229734/mceclip0.png)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
