---
article_id: 1500010778242
category: Materiais - Compras (SIGACOM)
content_hash: 54762c992f80969017ccff2abee4ac977f22bf87c8540317a36c93fc15fbdb8b
fetched_at: '2026-06-28T22:41:14.272601+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Cadastro de Comprador
  apresentando HELP Valor atribuído difere do tamanho do campo (Usuário)
type: support-article
updated_at: '2022-05-16T22:58:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010778242-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Cadastro-de-Comprador-apresentando-HELP-Valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-Usu%C3%A1rio
---

**Ocorrência**Ao fazer o cadastro de um novo comprador na rotina Grupo de Compras (COMA086) é apresentado o HELP: Valor atribuído difere do tamanho do campo (usuário) e não permite concluir o processo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017430302/mceclip0.png)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões.  
  
**Causa**Esse HELP é apresentando quando algum campo tenta receber uma informação de outro campo ou tabela, porém este campo anterior de onde vem a informação possui um tamanho diferente (normalmente maior) do que este campo que esta tentando receber a informação.

Neste exemplo, o campo ***AJ\_US2NAME*** não esta comportando a informação que esta´vindo do campo ***Y1\_NOME***.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

Ajustar no configurador o campo ***AJ\_US2NAME*** para o mesmo tamanho conforme o campo ***Y1\_NOME***.

O padrão é 40:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017695801/mceclip1.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017429042/mceclip3.png)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
