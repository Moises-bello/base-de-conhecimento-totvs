---
content_hash: 04d7b409c64f83392cb57185497872db08a8cd834559e4730c46744825de96e3
fetched_at: '2026-06-29T00:06:18.731748+00:00'
page_id: '219686317'
product: rm
source: tdn-rm
title: TTIRIP_DT_Provisao_Ferias_Mes30_Admitido17
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIRIP_DT_Provisao_Ferias_Mes30_Admitido17
version: 1
---

# PROVISÃO DE FÉRIAS EM MESES DE 30 DIAS PARA ADMITIDO NO DIA 17

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Provisão de Férias* |
| **Situação/Requisito:** | *Na provisão de férias do cálculo Delphi existia o parâmetro de execução do processo "Considera avo em mês 30 dias p/ admitido dia 17".*  *Na migração para o cálculo .Net foi verificado que o comportamento com o parâmetro desmarcado fazia a provisão ficar inconsistente.*  *Assim ele foi retirado do sistema, e o comportamento passou a ser sempre considerar o avo, ou seja, com o parâmetro marcado.*  *Mas agora cliente solicitou que não seja considerado o avo em mês 30 dias para admitido dia 17 na provisão de férias.* |
| **Solução/Implementação:** | *Para não haver confusão com o parâmetro antigo, foi criado no Parametrizador, pasta Férias/Controle, o parâmetro "Provisão de Férias desconsidera o avo em mês 30 dias para admitido dia 17", com o comportamento contrário.* |
| **Chamados   relacionados:** | *TTIRIP* |
| **Versões/Release:** | *11.82.42* |
