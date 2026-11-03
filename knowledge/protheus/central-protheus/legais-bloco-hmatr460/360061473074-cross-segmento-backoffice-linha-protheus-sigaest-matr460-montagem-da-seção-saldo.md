---
article_id: 360061473074
category: LEGAIS - BLOCO H/MATR460
content_hash: 2e3209000a39fbb087773a30e138440be258bc9fdbc7ac0ecfe68a55b8b80bb3
fetched_at: '2026-06-28T22:42:15.141500+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Montagem
  da seção "Saldo em Processo"
type: support-article
updated_at: '2021-11-03T18:29:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061473074-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Montagem-da-se%C3%A7%C3%A3o-Saldo-em-Processo
---

**Dúvida**Como é montada a seção "Em Processo" no relatório MATR460 (Inventário Modelo 7)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17

**Solução**O Saldo em Processo nada mais é do que um saldo de um produto que está sendo processado para seu consumo gerar um Produto Acabado. Vamos exemplificar um cenário onde teremos uma Estrutura do PA62 -> MP 62 de 1:1.

**1°** **-** Com ambos os produtos criados, daremos saldo inicial de quantidade 50 no MP62 - MATA220;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101880254/mceclip0.png)

**2°** **-** Criar estrutura de 1:1 entre o PA62 e MP62 - MATA200;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104047773/mceclip1.png)

**3° -** Criaremos uma OP para o PA62 de quantidade 30;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003004182/mceclip2.png)

**4°** **-** Após isso, incluiremos uma Requisição Manual do saldo a ser consumido indicando a OP para gerar o consumo.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101883974/mceclip3.png)

**5° -** Com isso, ao emitir o relatório MATR460, veja que, dos 50 itens, 20 estão em "Estoque Próprio" e 30 "Em Processo"

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003007462/mceclip7.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104052553/mceclip6.png)

**Observações**:

- No exemplo acima, não foi utilizado o conceito do parâmetro MV\_LOCPROC;

- Caso utilize o conceito do parâmetro MV\_LOCPROC, os produtos com Apropriação Indireta (B1\_APROPRI = I) já aparecerão na seção "Em Processo".

**Saiba mais:**

[*MP - SIGAEST - MATR460 - Saldo do Armazém de Processo não está saindo no relatório P7*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062097594)

*[MP - SIGAEST - Parâmetros (SX6) relacionados ao relatório MATR460 - Registro de Inventário Modelo 7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901)*

*[MP - SIGAEST - Perguntas do relatório MATR460 (Inventário Modelo 7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001540542-MP-SIGAEST-Perguntas-do-relat%C3%B3rio-MATR460-Invent%C3%A1rio-Modelo-7-)*

*[MP - SIGAEST - Dicas de Análise dos Saldos no Relatório MATR460 (P7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061829673-MP-SIGAEST-Dicas-de-An%C3%A1lise-dos-Saldos-no-Relat%C3%B3rio-MATR460-P7-)*

*[Clique aqui e veja mais artigos sobre o relatório MATR460 (P7)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)*
