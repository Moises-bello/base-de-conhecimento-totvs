---
content_hash: d63ccc9243a75bfd4df801bc45fceb1c962b8e00f6259599978c219dafa6d3a5
fetched_at: '2026-06-29T00:08:30.482586+00:00'
page_id: '272695961'
product: rm
source: tdn-rm
title: 512712 MEDU-2826 DT Avaliação Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272695961
version: 115
---

# Avaliação patrimonial

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Patrimonial |
| **Função:** | Avaliação Patrimonial |
| **Situação/Requisito:** | Ao realizar o processo de avaliação patrimonial preenchendo todas as informações, avançar e executar o processo, o sistema apresenta a mensagem abaixo.  Erro ao gravar a(s) Ocorrência(s) - Não foi localizada uma cotação para o símbolo "R$" na data 10/08/2011! |
| **Solução/Implementação:** | Para recuperar a cotação é necessário informar a moeda e a moeda de referência. Essas informações estavam sendo passadas incorretamente em cenários que envolviam moedas estrangeiras, por isso foi necessário modificar os dados passados como parâmetro. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
