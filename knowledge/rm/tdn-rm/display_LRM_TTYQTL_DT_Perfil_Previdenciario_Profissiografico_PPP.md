---
content_hash: 4234faeb0e20be38e9fd2c43642af48696c0aff1f74d0e53cbb68cee7d57ae6f
fetched_at: '2026-06-29T00:06:22.439780+00:00'
page_id: '223917762'
product: rm
source: tdn-rm
title: TTYQTL_DT_Perfil_Previdenciario_Profissiografico_PPP
type: documentation
url: https://tdn.totvs.com/display/LRM/TTYQTL_DT_Perfil_Previdenciario_Profissiografico_PPP
version: 121
---

# PPP - PERFIL PROFISSIOGRÁFICO PREVIDENCIÁRIO.

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Segurança e Saúde Ocupacional* |
| **Função:** | *Relatório do Perfil Previdenciário Profissiográfico* |
| **Situação/Requisito:** | *Ao gerar o relatório do PPP para funcionários com data de demissão futura, os campos 13 e 14 trazem a data de demissão preenchida.* |
| **Solução/Implementação:** | *Ajuste na geração do relatório do PPP. Quando um funcionário tiver data de demissão posterior à data da geração do relatório os campos 13 e 14 assim como o 15 não poderão trazer como data final a data de demissão, pois segundo IN77, artigo 265 item III - fornecer à empresa meios de prova produzidos em tempo real, de modo a organizar e a individualizar as informações contidas em seus diversos setores ao longo dos anos, possibilitando que a empresa evite ações judiciais indevidas relativas a seus trabalhadores;* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTYQTL, TTZFUY |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43; 12.1.9* |

divs
