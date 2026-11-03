---
article_id: 360016495272
category: Materiais - Compras (SIGACOM)
content_hash: 302567b71806dd53c6b70f70f7521b30049b58e59187962113bc602e9d795325
fetched_at: '2026-06-28T22:41:10.450814+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Substituição de Aprovadores
  no Grupo de Aprovação
type: support-article
updated_at: '2025-12-04T16:48:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016495272-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Substitui%C3%A7%C3%A3o-de-Aprovadores-no-Grupo-de-Aprova%C3%A7%C3%A3o
---

**Dúvida**  
Como realizar a substituição de aprovadores em um grupo de aprovação?  
  
**Ambiente**  
Microsiga Protheus – Compras – A partir da versão 12.1.17  
  
**Solução**

Para solucionar essa dúvida:

-  Veja o video How-to do link abaixo:

[How To | MP - SIGACOM Opção Substituição de Aprovadores na MATA114](https://youtu.be/YYhmAB5uxrM?si=ahGcfdnKmVD8EYu8)

- E seguem os passos a serem realizados:  
  
1. Acesse o módulo de Compras (SIGACOM);  
2. Acesse a rotina Grupo de Aprovaç. (MATA114) em Atualizações - Administração de Compras;  
3. Acesse Outras Ações - Subst. de Aprovadores;  
4. Preencha os campos de Dados Atuais / Filtro com as informações do aprovador que quer substituir;    5. Preencher os campos de Novos Dados / Atualização com o novo aprovador;  
5. Acesse Outras Ações - Buscar Aprovadores;  
6. Realize o c*heckbox* do aprovador que será substituído e selecione Confirmar.  
  
![Subs.Aprovadores.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17643378733975)

Após realizar o procedimento acima, as alçadas que estiverem pendentes na tabela Documentos com Alçada (SCR) não será alterada para o aprovador substituído, somente para os novos registros.

Caso haja muitos pedidos pendentes do antigo aprovador pode-se realizar as liberações antes da substituição ou a transferência para o superior aprovar.

Uma segunda opção para pedidos que ainda não foram aprovados para que apareçam para o novo aprovador substituto: pode-se efetuar uma alteração no pedido e salvar (**sem alterar nenhuma informação**). Pois com esse procedimento o sistema vai gerar novamente a alçada e incluirá o novo aprovador. **Esse procedimento reinicia a aprovação/alçada do pedido**.

**Obs:**

Caso se possua Tipo de Compras vinculado ao Aprovador que será substituído:

Conceitualmente o tipo de compras é vinculado ao Aprovador. Uma vez que esse aprovador é substituído, em outras palavras pelo conceito do sistema, ele é excluído do grupo de aprovação para que outro aprovador assuma o seu lugar, e assim existe a necessidade de realizar um novo vínculo com o Tipo de Compras que se deseje.

Atualmente não há no padrão do sistema uma forma para se modificar este comportamentento, mesmo que por customização.

***Saiba Mais :***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
* [How To | MP - SIGACOM Opção Substituição de Aprovadores na MATA114](https://youtu.be/YYhmAB5uxrM?si=ahGcfdnKmVD8EYu8)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help A220VLDAPRG Ao substituir um Aprovador na rotina Grupo de Aprovação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19635502786199-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-A220VLDAPRG-Ao-substituir-um-Aprovador-na-rotina-Grupo-de-Aprova%C3%A7%C3%A3o?source=search)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help: Emptyform Problema: O Formulário Atualização De Aprovadores(CONDETAIL) Não Foi Preenchido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046490133-MP-SIGACOM-HELP-AO-TENTAR-REALIZAR-A-SUBSTITUI%C3%87%C3%83O-DE-APROVADORES-NA-ROTINA-MATA114-HELP-EMPTYFORM-PROBLEMA-O-FORMUL%C3%81RIO-ATUALIZA%C3%87%C3%83O-DE-APROVADORES-CONDETAIL-N%C3%83O-FOI-PREENCHIDO-?source=search)
* [Alçadas - Visão Geral](http://tdn.totvs.com/pages/viewpage.action?pageId=274324462)
