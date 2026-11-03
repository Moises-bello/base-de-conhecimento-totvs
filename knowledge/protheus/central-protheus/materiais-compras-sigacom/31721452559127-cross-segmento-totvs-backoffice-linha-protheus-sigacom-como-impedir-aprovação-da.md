---
article_id: 31721452559127
category: Materiais - Compras (SIGACOM)
content_hash: e9986a2c220aae27fe6073e9bac857de31eea0f25b523a4fe85d4a9ff9801b44
fetched_at: '2026-06-28T22:41:11.601353+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Como Impedir
  aprovação da Solicitação de compras no Botão Aprovação por Grupo de usuário ?
type: support-article
updated_at: '2025-04-28T18:35:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31721452559127-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Como-Impedir-aprova%C3%A7%C3%A3o-da-Solicita%C3%A7%C3%A3o-de-compras-no-Bot%C3%A3o-Aprova%C3%A7%C3%A3o-por-Grupo-de-usu%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31721452526487) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como Impedir aprovação da Solicitação de compras no Botão Aprovação por Grupo de usuário ?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus compras - Todas as versões  
  
**Solução**

**1.**No configurador do sistema acesse **Usuários>Senhas>Privilégios**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31721452527255)

Cadastre um privilégio , **permitindo** acesso a Rotina **MATA110** e configure como **negado** o acesso para o  item 7 - 'Aprovação' conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31721471112471)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31721471114775)

**2.**Vincule o privilégio no Grupo de usuários no Configurador do sistema conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31721471115927)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31721471116311)

**3**.Vincule o grupo ao cadastro dos usuários, que não terão acesso ao botão de aprovação das solicitações de compras.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31722674760343)

**4.**Quando o usuário configurado conforme acima, acessar o sistema e tentar clicar no botão 'Aprovação' em 'Outras Ações' na rotina de solicitação de compras, será exibido o seguinte help:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31722674764823)

***Saiba Mais:***

* [Ponto de entrada MT110APV - Aprovação da Solicitação de Compras](https://tdn.totvs.com/pages/releaseview.action?pageId=6085823)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
