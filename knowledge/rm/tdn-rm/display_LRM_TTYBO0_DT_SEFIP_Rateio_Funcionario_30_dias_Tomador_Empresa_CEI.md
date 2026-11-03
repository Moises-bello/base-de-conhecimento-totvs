---
content_hash: 55180b700b2460a2cef6c09b628c437f9e3fa570c113f2f82bafa76f5f54b5c2
fetched_at: '2026-06-29T00:06:25.104711+00:00'
page_id: '224131673'
product: rm
source: tdn-rm
title: TTYBO0_DT_SEFIP_Rateio_Funcionario_30_dias_Tomador_Empresa_CEI
type: documentation
url: https://tdn.totvs.com/display/LRM/TTYBO0_DT_SEFIP_Rateio_Funcionario_30_dias_Tomador_Empresa_CEI
version: 120
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Relatório SEFIP* |
| **Situação/Requisito:** | Ao utilizar rateio de 30 dias no funcionário para o tomador empresa, porém utilizando CEI, o funcionário estava sendo considerado como administrativo na geração da SEFIP. Porém, pelo fato de estar utilizando um CEI, ele não é um funcionário administrativo. |
| **Solução/Implementação:** | *Acrescentar na consulta da flag de Funcionários Administrativos a verificação da utilização ou não do CEI.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTYBO0, TUELYF, TUITHC |
| **Requisito (ISSUE):** |  |

divs
