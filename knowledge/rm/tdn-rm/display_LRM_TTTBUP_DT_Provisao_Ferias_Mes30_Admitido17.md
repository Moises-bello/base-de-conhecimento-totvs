---
content_hash: 39b5a9482a175d910dad3e60c2acaa42bf15ff529f1c56c0ff0096e5e261a4bd
fetched_at: '2026-06-29T00:06:18.736736+00:00'
page_id: '219686324'
product: rm
source: tdn-rm
title: TTTBUP_DT_Provisao_Ferias_Mes30_Admitido17
type: documentation
url: https://tdn.totvs.com/display/LRM/TTTBUP_DT_Provisao_Ferias_Mes30_Admitido17
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
| **Chamados   relacionados:** | *TTTBUP* |
| **Versões/Release:** | *12.1.9* |
