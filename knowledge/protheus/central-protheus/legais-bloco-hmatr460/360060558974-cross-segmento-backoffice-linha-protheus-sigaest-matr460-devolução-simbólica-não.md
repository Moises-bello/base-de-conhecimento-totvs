---
article_id: 360060558974
category: LEGAIS - BLOCO H/MATR460
content_hash: 938ce74a00515ee0661ccdaea48786348302665e927bd7ed27105179125b001e
fetched_at: '2026-06-28T22:42:15.118917+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Devolução
  simbólica não deu baixa no Saldo de Poder de Terceiros do P7
type: support-article
updated_at: '2021-06-14T14:30:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060558974-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Devolu%C3%A7%C3%A3o-simb%C3%B3lica-n%C3%A3o-deu-baixa-no-Saldo-de-Poder-de-Terceiros-do-P7
---

**Dúvida**Fiz a devolução simbólica porém o saldo do poder de terceiros não deu baixa, pois quando consulto o Inventário Mod. 7 (P7) ele ainda consta lá. Como ajustar este problema?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Este problema pode ser solucionado através do parâmetro **MV\_SDTESN3**. Este parâmetro, no relatório de **Registro de Inventário Modelo 7 (MATR460)** considera, em sua impressão, o saldo de poder de terceiros no Tipo de Entrada/Saída (TES) que **não**atualiza estoque. Desta forma, ele é utilizado quando a pergunta do relatório **Saldo em poder de 3º?** estiver configurada com a opção **SIM** e pode assumir os seguintes critérios:

* 0 (zero): desconsidera saldo com registro da tabela **SB6 (Saldo em/de poder de terceiros)** que contém TES que não atualiza estoque (comportamento padrão).
* 1 (um): considera saldo com TES que não atualiza estoque e, inclusive, subtrai da composição do saldo em estoque os itens que estão em poder de terceiros.
* 2 (dois): considera saldo com TES que não atualiza estoque, porém, não realiza a subtração do saldo em poder de terceiros para composição do saldo em estoque.

Desta forma basta parametrizar da forma que melhor atenderá e satisfará na impressão.

**Saiba mais:**

*[MP - SIGAEST - Dicas de Análise dos Saldos no Relatório MATR460 (P7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061829673-MP-SIGAEST-Dicas-de-An%C3%A1lise-dos-Saldos-no-Relat%C3%B3rio-MATR460-P7-)*

*[Clique aqui e veja mais artigos sobre Bloco H/MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)*
