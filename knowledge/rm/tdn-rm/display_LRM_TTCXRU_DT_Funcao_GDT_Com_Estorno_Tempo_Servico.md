---
content_hash: 4f66d5f27c91a403268a613742e3f41fc3b4d0a64e06df826e48614ce93720ed
fetched_at: '2026-06-29T00:06:05.746463+00:00'
page_id: '201726909'
product: rm
source: tdn-rm
title: TTCXRU_DT_Funcao_GDT_Com_Estorno_Tempo_Servico
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCXRU_DT_Funcao_GDT_Com_Estorno_Tempo_Servico
version: 1
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
| **Chamados relacionados:** | *TTCXRU* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
