---
content_hash: 197880b313a00e553b399c6a7b04b344f867dbe5f47e79fd7dbb04a84fee64d5
fetched_at: '2026-06-29T00:06:05.674390+00:00'
page_id: '201726371'
product: rm
source: tdn-rm
title: TSURR5_DT_Funcao_GDT_Com_Estorno_Tempo_Servico
type: documentation
url: https://tdn.totvs.com/display/LRM/TSURR5_DT_Funcao_GDT_Com_Estorno_Tempo_Servico
version: 2
---

# FUNÇÃO DE FÓRMULA GDT COM ESTORNO DE TEMPO DE SERVIÇO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Fórmula* |
| **Situação/Requisito:** | *O cálculo .Net de Anuênios na função de fórmula GDT está diferente do Delphi, quando ocorre perda de dias devido a afastamentos que estornam tempo de serviço.* |
| **Solução/Implementação:** | *No cálculo .Net a conta é feita com o número de meses, e no cálculo em Delphi é com o número de dias.*  *Com isto, dependendo da situação do funcionário, os dois cálculos podem retornar valores divergentes.*  *Deverá ser alterado no cálculo .Net para que o comportamento fique igual ao anterior, em Delphi.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSURR5* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
