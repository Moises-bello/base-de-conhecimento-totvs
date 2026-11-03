---
article_id: 26355570227607
category: Financeiro
content_hash: 39b00a7b3c99639163f5c0d31158acd774255581fcc43967982c2f57d9e9217c
fetched_at: '2026-06-28T22:38:03.090294+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Fluxo de
  caixa não puxa as informações do Banco filtrado
type: support-article
updated_at: '2024-09-13T17:40:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26355570227607-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Fluxo-de-caixa-n%C3%A3o-puxa-as-informa%C3%A7%C3%B5es-do-Banco-filtrado
---

**Tempo aproximado para leitura: 00:08:00 min**

**Ocorrência**

No novo painel gestor, na aba Conciliado, ao aplicar o filtro para um banco específico, o sistema não está exibindo exclusivamente os títulos referentes aos borderôs desse banco.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Causa**

Por padrão, o sistema não restringirá a exibição apenas aos títulos com portador específico. O objetivo do fluxo de caixa é filtrar os títulos futuros em aberto, independentemente de estarem ou não em borderô.

**Solução**

Como pode observar abaixa temos o relatório FINR190, o mesmo está filtrando as informações referentes aos títulos em borderô para os banco do Brasil e itau.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26355570204951)

Em movimentações financeiras, os devidos saldos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26355570208151)

Na aba consolidado ao filtrar o banco itau, por exemplo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26355541599767)

A informação sobre o banco será exibida apenas no campo **Em Bancos**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26355570214551)

As colunas "Entradas" e "Saídas" têm como objetivo exibir os títulos em aberto.

Para os títulos em atraso, serão apresentados nos campos "A Receber" e A Pagar", os valores dos títulos com acumulados de juros, se aplicáveis, pois se referem aos valores a serem recebidos ou pagos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26355570217751)

**Calculo da Variação**

A coluna Variação do fluxo de caixa, apresenta quanto da sua renda está comprometida.

Exemplo:

Entradas R$ 5.555,00

Saídas R$ 80.000,00

Saldo do Período R$74.445,00

Temos:

(Saídas / Entradas) \* 100 = Variação

(80.000,00 / 5.555,00) \*100 = 1440,00%

**Saldo Acumulado**

**Exemplo:**

Em banco: R$ 1000.000,00

Entradas R$ 5.555,00

Em atraso a pagar: R$ 25.555,00

Saídas: R$ 80.000,00

**Temos**

(Em banco+Entradas): R$ 1.005.555,00

(Em atraso a pagar-Saídas): R$ 105.555,00

Saldo Acumulado: R$ 900.000,00

**Saiba mais**  
[Movimentações Financeiras - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=622668231#detalhes_fluxo_caixa-consolidado)
