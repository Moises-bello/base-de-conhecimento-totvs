---
content_hash: f69dc1898bae6123107a288962dea7b78ffc57488e4177bed5f481c0f976e8c2
fetched_at: '2026-06-29T00:06:04.725091+00:00'
page_id: '200910706'
product: rm
source: tdn-rm
title: TTBGG0_DT_Avisos_Automaticos
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBGG0_DT_Avisos_Automaticos
version: 1
---

# AVISOS AUTOMÁTICOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Avisos Automáticos* |
| **Situação/Requisito:** | *Ao enviar avisos automáticos agrupados por chefes e selecionando Tipo de Montagem Fórmulas, ocorre erro.* |
| **Solução/Implementação:** | *Ajuste em rotina de avisos automáticos quando *agrupados por chefes e selecionando Tipo de Montagem Fórmulas. Foi adicionada validação de retorno da sentença sql para não acessar linhas inexistentes. Foi ajustado verificação de controle de agrupamento por chefes afim de recuperar os e-mails necessários.** |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTBGG0* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
