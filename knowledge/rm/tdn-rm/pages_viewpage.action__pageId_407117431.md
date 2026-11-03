---
content_hash: 4b62c5027166ca160791465d14e4ab285ba215ff8249d81555574acc2a09fe2d
fetched_at: '2026-06-29T00:09:11.544657+00:00'
page_id: '407117431'
product: rm
source: tdn-rm
title: 3666645 FOPCALCULO01-4656 Cadastro de Férias com Afastamento por Licença Maternidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=407117431
version: 1
---

# Férias

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Férias |
| **Situação/Requisito:** | Sistema não está considerando a interrupção de contagem de dias para férias em dobro no caso de Licença Maternidade. Portanto está considerando férias em dobro indevidamente.  O parâmetro 'Não interrompe contagem do período para pagto de férias em dobro no afast. por Licença Maternidade(E)' encontra-se desmarcado, ou seja, o sistema deveria prorrogar 120 a mais na data Limite de gozo da funcionária (ou seja, interromper a contagem de dias). E o sistema está considerando a data Limite de gozo sem prorrogar esses dias. |
| **Solução/Implementação:** | Ajuste na soma de dias para limite de gozo para pagamento de férias em dobro.  Ajuste no cálculo de dias a mais para pagamento de férias em dobro para considerar data fim de período concessivo e não data fim período aquisitivo. |
| **Tickets relacionados:** | 3666645 |
