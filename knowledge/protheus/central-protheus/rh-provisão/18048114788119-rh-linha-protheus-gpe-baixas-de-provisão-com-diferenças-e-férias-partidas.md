---
article_id: 18048114788119
category: RH - Provisão
content_hash: b57cc2b067afc19e9158b9f669518b49cbebbd04d3ed91430ae412a9f635bf19
fetched_at: '2026-06-28T22:43:55.646696+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Baixas de Provisão com Diferenças e Férias Partidas
type: support-article
updated_at: '2025-06-17T19:59:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18048114788119-RH-Linha-Protheus-GPE-Baixas-de-Provis%C3%A3o-com-Diferen%C3%A7as-e-F%C3%A9rias-Partidas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18048100348439) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como Conferir as Baixas de Provisão quando há Diferença de Férias na Folha e as Férias são Partidas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Quando houver Alteração Salarial ou Alteração de Médias e/ou Adicionais após o cálculo das Férias, na Folha de Pagamento serão calculadas verbas de Diferença de Férias.   
Estas diferenças serão consideradas para Baixa de Férias na Provisão.  
   
Para realizar a conferência dos valores de baixas de férias, realize os seguintes passos:

**Exemplo 1:**  
1. Acesse: Configurador > Cadastros > Parâmetros > Localize o parâmetro MV\_TPBXFER:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18044914488727)  
Quando o Parâmetro MV\_TPBXFER está preenchido com 1, as férias partidas serão baixadas integralmente no mês de início das férias.  
  
2. Emita o Relatório da Folha de Pagamento. Acesse: Relatórios > Períodicos > Folha de Pagamento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18045258594967)  
Veja que foram calculadas verbas de Diferença de Férias Mês e Diferença de Férias Mês Seguinte.  
  
3. Emita o Relatório de Provisão de Férias. Acesse: Relatórios > Provisões > Provisões de Férias (GPER070):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18045368254743)  
Os valores baixados são a soma das verbas de Férias Mês, Férias Mês Seguinte e Diferenças.  
  
**Valor:** Férias Mês + Férias Mês Seguinte + Diferença de Férias + Diferença de Férias Mês Seguinte.  
Verba 027 - Férias - 2.367,81  
Verba 028 - Férias Mês Seg. - 1.810,68  
Verba 043 - Dif. Férias - 94,71  
Verba 044 - Dif. Férias Mês Seg. - 72,43  
Soma: **2.345,63**  
  
**Adicionais:** ATS Férias Mês + ATS Férias Mês Seguinte + Dif. ATS Férias + Dif. ATS Férias Mês Seguinte.  
Verba 110 - ATS Férias - 118,39  
Verba 111 - ATS Férias Mês Seg. - 90,53  
Verba 169 - Dif. ATS Férias - 4,74  
Verba 170 - Dif. ATS Férias Mês Seg. - 3,63  
Soma: **217,29**  
  
**1/3 de Férias:** 1/3 Férias Mês + 1/3 Férias Mês Seguinte + Diferença 1/3 Férias + Diferença 1/3Férias Mês Seguinte.  
Verba 032 - 1/3 de Férias - 828,73  
Verba 033 - 1/3 de Férias Mês Seg. - 633,74  
Verba 045 - Dif. 1/3 de Férias - 33,15  
Verba 046 - Dif. 1/3 de Férias Mês Seg. - 25,35  
Soma: **1.520,97**  
  
  
**Exemplo 2:**  
1. Acesse: Configurador > Cadastros > Parâmetros > Localize o parâmetro MV\_TPBXFER:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18046599318551)  
Quando o Parâmetro MV\_TPBXFER está preenchido com 2, as férias partidas serão baixadas nos dos meses de gozo de férias..  
  
2. Emita o Relatório da Folha de Pagamento. Acesse: Relatórios > Períodicos > Folha de Pagamento do Mês 08/2023:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18045258594967)  
Veja que foram calculadas verbas de Diferença de Férias Mês e Diferença de Férias Mês Seguinte, mas como o parâmetro MV\_TPBXFER está consifurado com 2, apenas as verbas de Férias do Mês serão consideradas para as Baixas.  
  
3. Emita o Relatório de Provisão de Férias. Acesse: Relatórios > Provisões > Provisões de Férias do mês 08/2023 (GPER070):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18046768263959)  
  
**Valor:** Férias Mês + Diferença de Férias.  
Verba 027 - Férias - 2.367,81  
Verba 043 - Dif. Férias - 94,71  
Soma: **2.462,52**  
  
**Adicionais:** ATS Férias Mês + Dif. ATS Férias.  
Verba 110 - ATS Férias - 118,39  
Verba 169 - Dif. ATS Férias - 4,74  
Soma: **123,13**  
  
**1/3 de Férias:** 1/3 Férias Mês + Diferença 1/3 Férias.  
Verba 032 - 1/3 de Férias - 828,73  
Verba 045 - Dif. 1/3 de Férias - 33,15  
Soma: **861,88**

4. Emita o Relatório da Folha de Pagamento. Acesse: Relatórios > Períodicos > Folha de Pagamento do Mês 09/2023:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18047591357719)

5. Emita o Relatório de Provisão de Férias. Acesse: Relatórios > Provisões > Provisões de Férias do mês 09/2023 (GPER070):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18046926346775)

**Valor:** Férias Mês + Diferença de Férias.  
Verba 027 - Férias - 1.810,68  
Verba 043 - Dif. Férias - 72,43  
Soma: **1.883,11**  
  
**Adicionais:** ATS Férias Mês + Dif. ATS Férias.  
Verba 110 - ATS Férias - 90,53  
Verba 169 - Dif. ATS Férias - 3,63  
Soma: **94,16**  
  
**1/3 de Férias:** 1/3 Férias Mês + Diferença 1/3 Férias.  
Verba 032 - 1/3 de Férias - 633,74  
Verba 045 - Dif. 1/3 de Férias - 25,35  
Soma: **659,09**

**Observação:** Os Encargos de INSS e FGTS são calculados à partir do Total das Férias.

**Saiba Mais:**[Parâmetro MV\_TPBXFER](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024752653-RH-Linha-Protheus-GPE-Ferias-partidas-na-provis%C3%A3o-par%C3%A2metro-MV-TPBXFER)  
[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
