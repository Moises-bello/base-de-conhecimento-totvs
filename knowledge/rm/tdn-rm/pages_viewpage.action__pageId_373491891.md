---
content_hash: 9bdcd9c66f102c03673cc0697cde4d4d613d2783084088926c9b63a33c4d6b88
fetched_at: '2026-06-29T00:09:01.543392+00:00'
page_id: '373491891'
product: rm
source: tdn-rm
title: 1233902 FOPCALCULO01-930 - Afastamento Licença Maternidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=373491891
version: 1
---

# Histórico de Afastamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Funcionários | Histórico de Afastamentos |
| **Situação/Requisito:** | O sistema está permitindo que lance 2 afastamentos de Licença Maternidade dentro do mesmo mês e ainda paga salário acima de 31 dias.  O sistema deveria bloquear e não permitir que o registro de 02 histórico pelo mesmo tipo, com interseção entre eles fosse salvo. |
| **Solução/Implementação:** | No Totvs Folha de Pagamento foi identificado que o sistema está permitindo cadastrar um segundo histórico de afastamento por licença maternidade com datas que possuem interseção. Foi ajustado para que o sistema não permita a criação de um novo afastamento por licença maternidade com datas que contenham interseção e exibir uma mensagem com esta informação, evitando assim que o lançamento do salário maternidade seja duplicado. |
| **Tickets relacionados:** | 1233902 |
