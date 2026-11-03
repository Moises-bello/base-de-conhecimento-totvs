---
content_hash: ad4397f7893cee8fac16c037093c70157b5b8fb098e0f27fafc6c3d905b2d4ca
fetched_at: '2026-06-29T00:09:09.744241+00:00'
page_id: '393366456'
product: rm
source: tdn-rm
title: 3478418 FINANCEIRO01-8587 DT Cálculo do valor líquido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393366456
version: 1
---

# Cálculo do valor líquido

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Cálculo do valor líquido. |
| **Situação/Requisito:** | Foi observado que ao cadastrar um valor de integração do educacional com a ação 'Descontar' e assinala a flag "Até o vencimento", o sistema não tem o mesmo comportamento dos valores opcionais no cálculo do valor líquido parcial. Logo, o valor do código de barras nos boletos fica incorreto quando no convênio está parametrizado para utilizar "Líquido parcial". |
| **Solução/Implementação:** | Ajustado cálculo do liquido parcial para valores de integração com ação acrescentar, onde, está configurado dias de atraso maior que zero e valores de integração que desconta, onde, está configurados para aplicar o desconto até o vencimento. A partir de agora, esses valores não serão considerados no cálculo do valor líquido parcial. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | FINTRF000161 |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
