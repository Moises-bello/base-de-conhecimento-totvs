---
article_id: 1500001351901
category: LEGAIS - BLOCO H/MATR460
content_hash: 860574d14a66ec1414c596d3e1400ab8368bc140d04fded78d804ec86079c6d8
fetched_at: '2026-06-28T22:42:15.183657+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Parâmetros (SX6) relacionados
  ao relatório MATR460 - Registro de Inventário Modelo 7
type: support-article
updated_at: '2023-09-05T20:32:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Par%C3%A2metros-SX6-relacionados-ao-relat%C3%B3rio-MATR460-Registro-de-Invent%C3%A1rio-Modelo-7
---

**Dúvida**

Quais os parâmetros têm relação com o relatório MATR460 (P7)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O relatório MATR460 - Inventário Modelo 7 (P7) é um relatório de suma importância que traz informações valiosas tais como: Saldos em estoque e Custos destes saldos para os mais variados produtos.

Porém, este relatório possui parâmetros que podem influenciar diretamente na impressão das informações, abaixo listaremos eles:

**MV\_CONTERC:** Permite o controle do custo médio do saldo em poder de Terceiros (EM terceiros). É utilizado apenas quando MV\_CUSFIL = F;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100253974/mceclip3.png)

**MV\_ALMTERC:** Este parâmetro trabalha junto ao MV\_CONTERC. Ele serve para definir o armazém padrão do terceiro (EM terceiros). Também é usado apenas quando MV\_CUSFIL = F;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100253934/mceclip1.png)

**MV\_M460PRC:** Considera todo o saldo do armazém delegado no parâmetro MV\_LOCPROC como saldo em processo.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100254054/mceclip4.png)

**MV\_MT460EP:** O parâmetro tem como objetivo indicar se a composição dos valores para o Saldo em Processo, apresentado no relatório MATR460 (Registro de Inventário Modelo 7), será realizada considerando o conceito de proporção do custo (MV\_PRODPR0).

**MV\_R460PRC:** Indica se o Relatório MATR460 irá utilizar o Calculo do Saldo em Processo Antigo (2) ou Novo (1);

**MV\_SDTESN3:** Indica se deve considerar TES que **não** **atualiza** **estoque** na impressão do P7 sendo:

* 0 (zero): desconsidera saldo que contém TES que não atualiza estoque (comportamento padrão).
* 1 (um): considera saldo com TES que não atualiza estoque e, inclusive, subtrai da composição do saldo em estoque os itens que estão em poder de terceiros.
* 2 (dois): considera saldo com TES que não atualiza estoque, porém, não realiza a subtração do saldo em poder de terceiros para composição do saldo em estoque.

**MV\_R460TPC:** Este parâmetro tem o intuito de configurar o tratamento do Custo de produtos em terceiros sendo M = Custo médio ou R = Custo Remessa)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100254714/mceclip5.png)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Bloco H/MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)*
