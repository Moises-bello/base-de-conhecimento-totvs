---
article_id: 360020917572
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 620e4386a0fac08f5ca2f6c4141e1868f4da4d67e7cf746ea6245a7c8cce939f
fetched_at: '2026-06-28T22:39:36.962813+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Valor de ICMS na
  Base de Cálculo do PIS COFINS
type: support-article
updated_at: '2024-03-11T12:40:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020917572-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Valor-de-ICMS-na-Base-de-C%C3%A1lculo-do-PIS-COFINS
---

**Dúvida**Quais os procedimentos para retirar e incluir o valor de ICMS na base de cálculo de PIS e Cofins apuração?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - A partir da versão 11.80  
  
**Solução**Para deduzir o ICMS na base do Pis/Cofins

**Parâmetros:**

MV\_DEDBPIS= I

MV\_DEDBCOF= I

O sistema irá deduzir o ICMS na base do Pis/Cofins.

Exemplo: R$1.000,00 produtos + R$50,00 ICMS

**Base de Cálculo**= R$950,00

É possível também, configurar os parâmetros da seguinte forma:

MV\_DEDBPIS= S

MV\_DEDBCOF= S

**Detalhe importante:** O conteúdo = S são para os casos que é necessário deduzir tanto o IPI como o ICMS próprio. 

# Para não deduzir o ICMS na base do Pis/Cofins

Configure os parâmetros conforme abaixo:

MV\_DEDBPIS= N

 MV\_DEDBCOF= N

**ATENÇÃO: PARA NÃO EXECUTAR DEDUÇÃO NA ENTRADA "FORNECEDOR"**

Utilize o campo criado no cadastro de fornecedor: <http://tdn.totvs.com/pages/viewpage.action?pageId=274312092>

Disponibilização de opção de configuração no fornecedor para que seja configurado se o ICMS deve ou não ser deduzido da base de PIS/COFINS.

Esta configuração deverá ser feita no novo campo Ded.PIS/COF (A2\_DEDBSPC)

As opções são: 

1 - Legado: Deduz conforme parâmetros MV\_DEDBPIS e MV\_DEDBCOF. Esta é a configuração padrão e não altera os tratamentos já existentes.

2 - ICMS e IPI: Deduz ICMS e IPI.

3 - ICMS: Deduz apenas o ICMS.

4 - IPI: Deduz apenas o IPI.

**5 - Nenhum: Não deduz nem o ICMS e nem o IPI.**

6 - Soma IPI

# [**MP - FIS - Dedução Apenas do ICMS Tributado da Base de Cálculo do PIS e COFINS**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053374314-MP-FIS-Dedu%C3%A7%C3%A3o-Apenas-do-ICMS-Tributado-da-Base-de-C%C3%A1lculo-do-PIS-e-COFINS?source=search)

**Observação:**

o STF apresentou a sua decisão favorável ao Recursos Extraordinário - RE 574706  que requeria a desvinculação do ICMS da base de cálculo do PIS e da COFINS. Esta decisão é de repercussão geral, isto é, a princípio se aplica aos processos que tramitam pelo judiciário.

<http://www.stf.jus.br/portal/cms/verNoticiaDetalhe.asp?idConteudo=338378>

**Importante:**

Após realizar a configuração o tratamento será somente para próximas notas lançadas, esta configuração não altera lançamentos já realizados antes da parametrização.

Abaixo documentação completa: 

<https://tdn.totvs.com/pages/releaseview.action?pageId=717693406>
