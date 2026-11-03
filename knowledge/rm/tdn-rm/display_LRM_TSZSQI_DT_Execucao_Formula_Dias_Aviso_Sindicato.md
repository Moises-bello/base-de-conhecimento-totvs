---
content_hash: e44354b0d5a74e6989449a935291db7949b430e3258d9df900305121e0e1cf57
fetched_at: '2026-06-29T00:06:06.925743+00:00'
page_id: '201733397'
product: rm
source: tdn-rm
title: TSZSQI_DT_Execucao_Formula_Dias_Aviso_Sindicato
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZSQI_DT_Execucao_Formula_Dias_Aviso_Sindicato
version: 3
---

# RESCISÃO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Rescisão* |
| **Situação/Requisito:** | *Ao executar a fórmula de cálculo de dias de aviso prévio previstas pelo sindicato, não estava sendo verificado o preenchimento do campo de Data de Demissão/Data de Cálculo da rescisão, fazendo com que o cálculo fosse feito de forma incorreta.* |
| **Solução/Implementação:** | *Aplicada uma validação antes de executar o cálculo da fórmula, para não permitir o cálculo sem que todas as informações necessárias estejam preenchidas.* |
| **Chamados relacionados:** | TSZSQI |
| **Versões/Release:** | *11.82.41.* |
