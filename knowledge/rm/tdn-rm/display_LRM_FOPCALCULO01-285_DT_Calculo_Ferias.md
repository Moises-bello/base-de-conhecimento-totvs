---
content_hash: 2f6dd81f4d52d3fbc49d2cb89d7f5521f8c0d127d990370833fba9d2f901b324
fetched_at: '2026-06-29T00:08:34.260775+00:00'
page_id: '274655869'
product: rm
source: tdn-rm
title: FOPCALCULO01-285_DT_Calculo_Ferias
type: documentation
url: https://tdn.totvs.com/display/LRM/FOPCALCULO01-285_DT_Calculo_Ferias
version: 97
---

# Cálculo Férias

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projeto |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Cálculo Férias |
| **Situação/Requisito:** | Ao lançar férias partidas com INSS outro emprego, o sistema não está considerado o INSS de Férias outro emprego do próximo mês.  São informados os valores dos eventos de base, porém no Log de cálculo o sistema não considera a base informada no Código de Cálculo 187, ocorrendo até mesmo a alteração da alíquota de INSS que deveria ser 11% e passou a calcular 8%. |
| **Solução/Implementação:** | Ajuste no lançamento de férias partidas com INSS outro emprego para somar as bases (atual e outro emprego).  Ajuste na dedução de valor de base para não considerar alíquota quando houver valor fixo cadastrado ou formula que retorne valor (CC187). |
| **Tickets relacionados:** |  |

divs
