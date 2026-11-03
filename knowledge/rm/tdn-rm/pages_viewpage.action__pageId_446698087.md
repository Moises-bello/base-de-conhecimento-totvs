---
content_hash: cc5c3ff0bc7384535a0a0e56813e4269095a40a1ccbaaa40e8efb6b15e6481f9
fetched_at: '2026-06-29T00:09:55.064982+00:00'
page_id: '446698087'
product: rm
source: tdn-rm
title: FISCAL01-7350 DT Rotina CAT42 - Devoluções de Saída
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=446698087
version: 3
---

# Rotina Estadual CAT-42 SP

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Obrigações Acessórias - Rotinas Legais Estaduais |
| **Situação/Requisito:** | Nas notas de devoluções os valores de ICMS suportado devem ser iguais ao valores gerados na nota original e consequentemente serão gerados no campo ICMS\_TOT dos registros 1100 e 1200. No caso da nota de Devolução de Saída o campo referente ao enquadramento legal deve ser gerado normalmente (será igual ao enquadramento da saída). Caso o enquadramento seja diferente de zero, o campo valor de confronto deverá ser gerado e consequentemente ambos os campos serão gerados nos registros 1100 e 1200 (COD\_LEGAL e VL\_CONFR). |
| **Solução/Implementação:** | Foi implementado na geração dos registros referentes ao ressarcimento no Encerramento do Período de Apuração os cálculos para as Notas de Devolução de Venda. |
