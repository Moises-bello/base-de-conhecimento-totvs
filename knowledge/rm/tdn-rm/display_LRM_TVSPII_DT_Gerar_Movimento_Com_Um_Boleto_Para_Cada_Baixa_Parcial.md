---
content_hash: 3be5d032b8f0a9b17fd2d956f523c275a827e279d638f32cca8d62071c8a42b6
fetched_at: '2026-06-29T00:08:18.587257+00:00'
page_id: '265782376'
product: rm
source: tdn-rm
title: TVSPII_DT_Gerar_Movimento_Com_Um_Boleto_Para_Cada_Baixa_Parcial
type: documentation
url: https://tdn.totvs.com/display/LRM/TVSPII_DT_Gerar_Movimento_Com_Um_Boleto_Para_Cada_Baixa_Parcial
version: 112
---

# Geração de Movimento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de Movimento |
| **Situação/Requisito:** | Identificamos um cenário que ao regerar o movimento para um boleto estava apresentando a mensagem de não conformidade “Referência de objeto não definida para uma instância de um objeto.”  Esta situação estava ocorrendo somente quando o financeiro estava parametrizado para gerar um boleto para cada baixa parcial realizada no lançamento. |
| **Solução/Implementação:** | Melhoria na geração do movimento quando parametrizado para gerar movimento por boleto para que não seja apresentada a não conformidade “Referência de objeto não definida para uma instância de um objeto.”, esta situação ocorre em alguns cenários em que o lançamento financeiro é gerado agrupando as informações por aluno. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TVSPII |
| **Requisito (ISSUE):** | N/A |

divs
