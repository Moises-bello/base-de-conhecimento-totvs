---
article_id: 4408518888343
category: Financeiro - Consultas / Relatórios
content_hash: e0d0f07fe5a71a4bab8654b5040cf7a0caa8e4d1922ca208c3a8627236a811f9
fetched_at: '2026-06-28T22:37:58.439483+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Funcionamento
  do cálculo de dias de atraso do relatório FINR130
type: support-article
updated_at: '2023-01-25T21:08:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408518888343-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Funcionamento-do-c%C3%A1lculo-de-dias-de-atraso-do-relat%C3%B3rio-FINR130
---

**Dúvida**Como funciona o cálculo de dias de atraso no relatório **FINR130**?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Financeiro – Todas as versões. 

**Solução**O relatório de contas a receber **(FINR130)** possui duas formas de realizar o cálculo para dias de atraso, são elas: Por data de vencimento e por vencimento Real.

A rotina sempre irá considerar o vencimento **(E1\_VENCTO)** para cálculo de dias de atraso, porém o único modo de considerar o vencimento real **(E1\_VENCREA)** é em casos onde o vencimento real seja maior ou igual a data base usada na emissão do  relatório. Esse modo é mais utilizado em casos onde o vencimento cai em finais de semana ou feriado atribuindo o vencimento real para o próximo dia útil.

**Exemplos:**Abaixo temos um título com emissão em 25/08/2021 e relatório considerando a **data base** em 31/08/2021 (terça) e 30/08/2021 (segunda)

**1º Exemplo:**

- Com vencimento em 28/08/2021 (sábado) e vencimento real em 30/08/2021 (segunda);

- **Data base** emissão 31/08/2021 (terça) considera 3 dias de atraso, devido o vencimento ter caído em um sábado considera o **vencimento**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4422778786711/mceclip3.png)

**2º Exemplo:**

- Com vencimento em 28/08/2021 (sábado) e vencimento real em 30/08/2021 (segunda);

- **Data base** emissão 30/08/2021 (segunda) considera 0 dias de atraso, devido o **vencimento real** ser igual a **data base** da emissão do relatório considera o **vencimento real.**

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4422773787415/mceclip5.png)**

**Saiba mais**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=547226162>
