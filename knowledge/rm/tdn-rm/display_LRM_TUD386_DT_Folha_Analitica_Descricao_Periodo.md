---
content_hash: a7119a9da7c3be4ecb272b9ef758c2886ec5e736d5cee22a4ca22a613995df29
fetched_at: '2026-06-29T00:06:27.902860+00:00'
page_id: '233737250'
product: rm
source: tdn-rm
title: TUD386_DT_Folha_Analitica_Descricao_Periodo
type: documentation
url: https://tdn.totvs.com/display/LRM/TUD386_DT_Folha_Analitica_Descricao_Periodo
version: 118
---

# Folha Analitica

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Emissão da Folha Analítica* |
| **Situação/Requisito:** | A Folha Analítica Delphi quando o parâmetro "Descrição do Período" está marcado, sempre busca a descrição do período Atual ao ser informado competência anteriores |
| **Solução/Implementação:** | A Folha Analítica Delphi quando o parâmetro "Descrição do Período" está marcado, e informado competência anteriores sendo solicitado o período atual ou informado um único período. Nestas condições será buscado a descrição do Período do campo Descrição gravado no envelope de pagamento do primeiro funcionário encontrado. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TUD386* |
| **Requisito (ISSUE):** |  |

divs
