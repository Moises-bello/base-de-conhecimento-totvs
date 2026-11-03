---
content_hash: 40147da87d596158d25fdc7b12b35d1a7363e4cdc1c2bab54458018a6d5aaa91
fetched_at: '2026-06-29T00:08:34.816523+00:00'
page_id: '274845397'
product: rm
source: tdn-rm
title: 608708 FINANCEIRO01-324 DT CONTABILIZA BAIXA ZERADA
type: documentation
url: https://tdn.totvs.com/display/LRM/608708+FINANCEIRO01-324+DT+CONTABILIZA+BAIXA+ZERADA
version: 106
---

# Parâmetros de Contabilização de Baixa com Valor Zero

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Contabilização de Baixa |
| **Situação/Requisito:** | No cadastro do tipo de documento as opções “Usar Parâmetros Gerais” e “Não Contabilizar Baixa Zerada” estão desmarcadas. Porém mesmo assim o sistema está respeitando o parâmetro “Não contabilizar Baixa com Valor Zero” (Parâmetros do Integração Contábil, etapa Contab. Baixa), de modo que ao realizar uma baixa com valor zerado o sistema não está gerando contabilização. |
| **Solução/Implementação:** | Ajuste ao validar o parâmetro do Tipo de Documento e Não Contabilizar Baixa com Valor Zero. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000098 |
|  |  |

divs
