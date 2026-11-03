---
content_hash: 7eeae6233e3a269d6c2e4cb2a6ee65326b9af6a7533f44eacc3c3b640dcf9f8f
fetched_at: '2026-06-29T00:09:09.085268+00:00'
page_id: '392496046'
product: rm
source: tdn-rm
title: Geração dos Encargos - Criação do parâmetro 'Considerar duas casas decimais
  p/ fórmulas'.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=392496046
version: 2
---

# Campo "Considerar duas casas decimais p/ fórmulas".

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Geração de encargos |
| **Situação/Requisito:** | Permitir a geração dos encargos calculados por fórmula considerando duas casas decimais ou quatro casas decimais de acordo com parametrização do cliente. |
| **Solução/Implementação:** | Foi adicionada uma nova flag no processo de geração de encargos 'Considerar duas casas decimais p/ fórmulas'', com esta flag marcada os encargos calculados por fórmula serão gerados considerando apenas duas casas decimais, caso o parâmetro esteja desmarcado será gerado considerando quatro casas decimais. Na visualização dos históricos de encargos serão exibidos quatro casas decimais, caso os encargos tenham sido gerados com o parâmetro marcado as duas últimas casas decimais irão aparecer zeradas. |
| **Tickets relacionados:** | FOPROTINAS01-4749 |
