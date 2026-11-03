---
article_id: 1500003500281
category: SIGAEST - RELATORIOS
content_hash: 479365fef13fe0e9d505e32fe2566ad80f107f33803ff6347d2fb9933975b929
fetched_at: '2026-06-28T22:39:06.262797+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: MP - SIGAEST - MATR425 - Posição de Estoque para Produtos com Saldos em Lotes
  Vencidos
type: support-article
updated_at: '2021-04-28T15:09:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003500281-MP-SIGAEST-MATR425-Posi%C3%A7%C3%A3o-de-Estoque-para-Produtos-com-Saldos-em-Lotes-Vencidos
---

**Dúvida**Como obter o relatório de Lotes para visualizar os saldos e produtos que estão vencidos?

**Ambiente**Microsiga Protheus – Estoque/Custos – A partir da versão 12.1.17  
  
**Solução**Para emitir os saldos e produtos cujo que já chegaram à data de vencimento, com base no dia atual que for emitir, basta emitir o Relatório MATR425 com as seguintes perguntas-chave:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102555234/mceclip0.png)

Então, a pergunta "Até a Data de Validade?" se torna peça-chave para o sistema filtrar no relatório apenas produtos cuja validade vá até o dia delegado nesta pergunta.

Em um exemplo prático, temos o MP1001, que teve seu lote 1000 vencido em 24/02/2021. Emitindo o relatório no dia 01/03/2021 (por exemplo), saberemos que tudo antes deste dia está vencido. Então parametrizemos a Data de Validade até 28/03/2021. Veja abaixo o resultado:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003675062/mceclip1.png)

Desta forma conseguirás ter um controle por meio de relatórios dos produtos cujo lote venceu, apenas filtrando o lote (caso queira) ou a data de validade ("até).

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Relatórios no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012224673-SIGAEST-RELATORIOS)
