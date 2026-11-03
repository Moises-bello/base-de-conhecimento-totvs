---
article_id: 360027969371
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 295a2c03c2a4c360646e2f2f549568e2e433fae787853c880314a83c1451cdec
fetched_at: '2026-06-28T22:38:58.642290+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST- MATA650 - "Não existe quantidade suficiente em estoque para atender
  esta requisição."
type: support-article
updated_at: '2021-04-28T15:45:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027969371-MP-SIGAEST-MATA650-N%C3%A3o-existe-quantidade-suficiente-em-estoque-para-atender-esta-requisi%C3%A7%C3%A3o
---

**Dúvida**Ao confirmar a inclusão de Ordem de Produção (OP) o sistema apresenta mensagem:

"Não existe quantidade suficiente em estoque para atender esta requisição. Itens Sem Sld / Bloqs. / Empenhos Pendentes. Produto Armazém Saldo Ocorrência". O que fazer para resolver este problema?

**Ambiente**Microsiga Protheus – Estoque – A partir da versão 11.80  
  
**Solução**

Ao ser apresentada esta mensagem , deve-se efetuar as seguintes validações:

- Atentar ao saldo dos componentes, verificando se o processo de requisição não é realizado de forma manual, utilizando a rotina de movimentação múltipla ou informando numero de OP no documento de entrada (D1\_OP);

- Valide o parâmetro MV\_REQAUT. Quando parametrizado como "A", sempre requisitará o que está empenhando, não validando requisições manuais. Para que no apontamento considere a requisição manual, este parâmetro deve estar igual a "D".

- Valide se os registros na tabela SDC (Composição do Empenho) estão coerentes, referentes aos itens apresentados.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
