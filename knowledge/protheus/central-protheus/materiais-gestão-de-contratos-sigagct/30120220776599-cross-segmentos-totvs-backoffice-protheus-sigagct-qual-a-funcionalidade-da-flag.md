---
article_id: 30120220776599
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: fd9ee82e1896645f6174ac1d5eee8ee927b9b83047b9e496774fd7ae2ed9bc00
fetched_at: '2026-06-28T22:37:24.091550+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Qual a funcionalidade
  da Flag "Ignora Item Bloq." (CXN_IGITEM) da Planilha na Rotina de Medição ?
type: support-article
updated_at: '2025-02-20T17:29:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30120220776599-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Qual-a-funcionalidade-da-Flag-Ignora-Item-Bloq-CXN-IGITEM-da-Planilha-na-Rotina-de-Medi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30120220761111) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Qual a funcionalidade da Flag "Ignora Item Bloq." (***CXN\_IGITEM***) da Planilha na Rotina de Medição ?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões]

**Solução**

A Flag "Ignora Item Bloq." do campo ***CXN\_IGITEM*** tem a funcionalidade de não trazer os itens que possam ter alguma divergência ou impeditivo para se realizar o carregamento das informações do item do contrato para o item da medição, como por exemplo a existencia de produtos bloqueados ou também entidades contabeis bloqueadas em seus respectivos cadastros.

Abaixo link de artigo disponível com mais informações sobre esta flag:

[GCT0136 - Medição com produtos bloqueados/inconsistentes (CNTA121)](https://tdn.totvs.com/x/JP_8Hg)

***Obs1:***

No caso se possuir produtos ou entidades contabeis bloqueadas nos itens da planilha no cadastro do contrato, para que este itens possam ser carregados na rotina de Medição a possibilidade existente é se realizar uma Revisão do Tipo "Aberta" no Contrato para se retirar as entidades bloqueadas dos itens, ou substituir por Entidades que não estejam bloqueadas,

ou desbloquear as entidades bloqueadas, visto que no padrão do sistema a rotina de medição, conforme sua arquitetura, não carrega os itens que possuem informações (como produtos ou também entidades contábeis) que estejam bloqueadas em seus cadastros.

***Saiba Mais:***

[GCT0136 - Medição com produtos bloqueados/inconsistentes (CNTA121)](https://tdn.totvs.com/x/JP_8Hg)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
