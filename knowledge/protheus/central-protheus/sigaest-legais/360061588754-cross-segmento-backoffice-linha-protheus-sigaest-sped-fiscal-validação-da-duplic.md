---
article_id: 360061588754
category: SIGAEST - LEGAIS
content_hash: 51753f6dda36fca8e3bcfe012094607207f48467c77c680c863e532ef7e7caa4
fetched_at: '2026-06-28T22:38:51.866210+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SPED Fiscal - Validação
  da Duplicidade no Registro K200
type: support-article
updated_at: '2021-10-07T02:30:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061588754-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SPED-Fiscal-Valida%C3%A7%C3%A3o-da-Duplicidade-no-Registro-K200
---

**Ocorrência**Ao gerar o Bloco K do SPED Fiscal é apresentado, no validador, o erro relacionado à Duplicidade no registro K200 com os dizeres:

"*Duplicidade de ocorrência da chave DT\_EST, COD\_ITEM, IND\_EST, COD\_PART.*"

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**

Este problema normalmente acontece em linha de saldo de Poder de Terceiros. Normalmente é causado por dois motivos:

1° - Quando há alguma inconsistência no Cliente/Fornecedor envolvido neste saldo (**estando deletado, com código duplicado entre tabela de Clientes(SA1) e Fornecedores(SA2) ou bloqueado em seu cadastro**);

2° - Quando há inconsistências em seu registro na tabela SB6:  **B6\_TPCF vazio, B6\_CLIFOR vazio** ou **B6\_IDENT vazio**.

**Solução**Temos um caso onde o produto PA5000 apresentou Duplicidade no SPED, onde estão Em Terceiros para o mesmo cliente (000001) com saldos 1 e 10. Neste caso, sendo do mesmo cliente, deveriam estar na mesma linha com saldo **11**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102035654/mceclip0.png)

**1° Passo - Validarmos como está esse registro no Relatório "Relação do Bloco K". Aqui podemos identificar que o Saldo de 1, diz pertencer ao Fornecedor  de código 01.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003169162/mceclip1.png)

**Observação importante**: O Relatório MATR241 imprime os dados conforme estão nas tabelas (SB2, SB6). Já a o SPEDFISCAL, valida também tabelas relacionadas, por exemplo: existência dos clientes na tabela SA1, existência dos fornecedores na tabela SA2, etc.

Portanto, aqui identificamos que na verdade o saldo de 1, na SB6, diz que pertence ao Fornecedor 01. Vamos conferir isso no próximo passo.

**2° Passo - Validar o registro na tabela SB6 e existência do Fornecedor na tabela SA2.**

**Campo B6\_CLIFOR: ✔**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102035754/mceclip2.png)

**Campos B6\_IDENT e B6\_TPCF: ✔**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003206561/mceclip0.png)

**Tabela SA2:** ⛔

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102035774/mceclip4.png)

Neste exemplo prático, o problema foi o registro excluído do fornecedor 01 na tabela SA2. Então o SPED no momento de montar aquela linha do produto PA5000 para ele, acabou não encontrando e assim acabou replicando os mesmos dados do registro da linha acima, gerando a duplicidade.

Portanto, estas são as validações padrões a serem feitas em caso de Duplicidade no Registro K200 do Bloco K no SPED.

**Saiba mais:**

*[MP - SIGAEST - No Registro K200 do Bloco K os produtos que tem saldo de terceiro, em terceiro e próprio não está gerando "em estoque próprio"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002838202-MP-SIGAEST-No-Registro-K200-do-Bloco-K-os-produtos-que-tem-saldo-de-terceiro-em-terceiro-e-pr%C3%B3prio-n%C3%A3o-est%C3%A1-gerando-em-estoque-pr%C3%B3prio-)*

*[Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
