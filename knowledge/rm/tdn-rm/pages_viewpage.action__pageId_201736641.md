---
content_hash: c707242dbd844ebabcb7e1cbb8520feaf70a632f557ed02b16dd8ebeabcb374d
fetched_at: '2026-06-29T00:06:07.593208+00:00'
page_id: '201736641'
product: rm
source: tdn-rm
title: TTEEVF_DT_Dias_Trabalhados_Interseção_Ferias_Afastamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201736641
version: 1
---

# DIAS TRABALHADOS COM INTERSEÇÃO DE FÉRIAS E AFASTAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Dias Trabalhados* |
| **Situação/Requisito:** | *Dias trabalhados não estão sendo calculados corretamente quando existem dias de interseção de férias e afastamentos.* *O mesmo dia está sendo abatido duas vezes, uma para cada motivo.*  *Por exemplo, no caso de funcionária que trabalhou alguns dias no mês, entrou de férias e durante seu período de férias iniciou sua licença maternidade.* |
| **Solução/Implementação:** | *Ajustar no cálculo dos dias trabalhados para abater somente uma vez os dias que estiverem como interseção de férias e afastamentos.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTEEVF* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
