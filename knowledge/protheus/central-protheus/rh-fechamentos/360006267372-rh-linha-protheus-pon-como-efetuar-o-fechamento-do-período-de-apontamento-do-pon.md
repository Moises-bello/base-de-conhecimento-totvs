---
article_id: 360006267372
category: RH - Fechamentos
content_hash: c4517a7a4645a050c3eac4279e1f19ce5532f659b619659be89380e4049e2a0d
fetched_at: '2026-06-28T22:44:48.862868+00:00'
product: protheus
section_id: 32419231682455
source: central-protheus
title: RH - Linha Protheus - PON - Como efetuar o fechamento do Período de Apontamento
  do Ponto Eletrônico por filial
type: support-article
updated_at: '2025-06-02T19:05:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006267372-RH-Linha-Protheus-PON-Como-efetuar-o-fechamento-do-Per%C3%ADodo-de-Apontamento-do-Ponto-Eletr%C3%B4nico-por-filial
---

**Dúvida**Como efetuar o fechamento do Período de Apontamento do Ponto Eletrônico por filial?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Em algumas empresas, as filiais possuem o **Período de Apontamento diferente** ou existe a necessidade de **fechar o Período de Apontamento de apenas uma filial** naquele momento. Para estes casos é necessário que a tabela de histórico de períodos de apontamento [(SPO) seja exclusiva](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045460153), assim como deve existir parâmetros **MV\_PAPONTA** e **MV\_PONMES** para cada uma das filiais.  
  
No momento do fechamento, será possível selecionar as filiais que precisa fechar e quais ficarão com fechamento pendente. Em **Miscelânea> Fechamentos> Mensal> Outras Ações> Parâmetros** é possível incluir a filial que deseja efetuar o fechamento: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/32102503158935)**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32102503160343)  
\*\*É importante frisar que a **data base do sistema** no momento do fechamento, deve estar com o **último dia do período de apontamento** a ser fechado, por exemplo, se o período é de 21/11/2024 à 20/12/2024,  a data base do Sistema deve ser 20/12/2024.  
  
**Saiba Mais:  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)**[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)  
[Como utilizar os parâmetros de Leitura e a Tabela SPO, responsável pelo no fechamento Mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045460153)
