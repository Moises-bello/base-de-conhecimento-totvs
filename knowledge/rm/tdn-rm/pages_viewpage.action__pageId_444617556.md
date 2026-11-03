---
content_hash: 9d37fbeef138ffca9eb58d1f331c14a7528ced93878d48972253821c0a58e9e6
fetched_at: '2026-06-29T00:09:54.416207+00:00'
page_id: '444617556'
product: rm
source: tdn-rm
title: FISCAL01-7351 DT Rotina CAT42 - Devoluções de Entrada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=444617556
version: 3
---

# Rotina Estadual CAT-42 SP

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Obrigações Acessórias - Rotinas Legais Estaduais |
| **Situação/Requisito:** | Nas notas de devoluções os valores de ICMS suportado devem ser iguais ao valores gerados na nota original e consequentemente serão gerados no campo ICMS\_TOT dos registros 1100 e 1200.  Na nota de Devolução de Entrada os campos referentes ao valor de confronto e enquadramento legal (COD\_LEGAL e VL\_CONFR) devem ser gerados em branco e consequentemente serão gerados em branco nos registros 1100 e 1200. |
| **Solução/Implementação:** | Ajustado o layout da Rotina CAT42 para que nos registro 1100 e 1200 os campos do Valor de Confronto e Código do Enquadramento Legal sejam gerados com 0 (zero) e vazio respectivamente quando se tratar de notas de devolução. Para que o ajuste tenha efeito a natureza associada ao lançamento de devolução deve ter o parâmetro TIPO DE DEVOLUÇÃO (Pasta Outros Dados) setado para Devolução. |
