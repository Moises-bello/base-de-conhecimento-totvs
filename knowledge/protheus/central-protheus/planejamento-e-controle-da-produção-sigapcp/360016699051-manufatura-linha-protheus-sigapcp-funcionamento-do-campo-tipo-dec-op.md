---
article_id: 360016699051
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 38f58a200ef0f93731484709c8ddbc05a2cbf002697f582c957392378f2fd5e0
fetched_at: '2026-06-28T22:42:43.325011+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Funcionamento do campo Tipo Dec. OP
type: support-article
updated_at: '2022-09-19T17:27:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016699051-Manufatura-Linha-Protheus-SIGAPCP-Funcionamento-do-campo-Tipo-Dec-OP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como é o funcionamento do campo **Tipo Dec. OP - B1\_TIPODEC**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O campo **B1\_TIPODEC** no **MATA010 - Cadastro de Produto**, define o tratamento dos decimais para a explosão de estrutura da **Ordem de Produção**.

* **N - Tratamento Normal**, ou seja, não haverá nenhuma alteração de casas decimais ou de arredondamento;
* **A - Arredonda**, ou seja, irá arredondar para a quantidade mais próxima que o mesmo estiver;
* **I - Incrementa**, ou seja, incrementa decimais para casos que não tem as decimais;
* **T - Trunca as casas**, ou seja, omite as casas decimais.

Exemplos de como será o comportamento utilizando cada uma das opções:

* **N** - Se empenhar a quantidade 1,25 a mesma não irá se alterar e irá seguir com a quantidade original 1,25;
* **A** - Se empenhar a quantidade 1,25 ele irá arredondar para a casa decimal mais próxima ficando 1; Se empenhar a quantidade 1,55 ele irá arredondar para a casa decimal mais próxima ficando 2;
* **I** - Se empenhar a quantidade 1,25 ele irá incrementar mais 1, ficando assim o empenho de 2;
* **T** - Se empenhar a quantidade 1,25 ele irá cortar as casas decimais ficando 1. Se empenhar a quantidade 1,55 ele irá cortar as casas decimais ficando 1.
