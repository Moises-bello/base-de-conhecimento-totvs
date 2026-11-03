---
content_hash: 8c8dd833b730fc1afa07035575ee7c3efd2379dbd1a1271ea9227f6a7ca237de
fetched_at: '2026-06-29T00:08:31.790257+00:00'
page_id: '273310558'
product: rm
source: tdn-rm
title: 385217 MRH-8692 DT Folha Analitica Dados do Cabecalho
type: documentation
url: https://tdn.totvs.com/display/LRM/385217+MRH-8692+DT+Folha+Analitica+Dados+do+Cabecalho
version: 108
---

# Folha Analítica

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Folha de Pagamento. |
| **Função:** | Emissão dos Cabeçalhos da Folha Analítica. |
| **Situação/Requisito:** | Ao gerar a Folha Analítica no .Net, onde na quebra de seção foi utilizada uma quebra com um código especifico de seção exemplo “02” o é relatório gerado somente para a filial 02, na página de “Total Geral” (Última página do relatório) está sendo levado os dados da Matriz, porém o CNPJ que está saindo é o da Filial. Deveria ser levado os dados da Filial, tanto o endereço quanto o CNPJ assim como ocorre no DELPHI. |
| **Solução/Implementação:** | A Folha Analítica .Net quando na quebra de seção for utilizada um código especifico de seção nos cabeçalhos será usado os dados de seção especificada. Os dados da matriz (Coligada) só será usado quando a quebra for informada com máscaras. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 385217. |
| **Requisito:** |  |

divs
