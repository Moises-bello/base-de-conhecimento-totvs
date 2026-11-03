---
content_hash: 103fceec2ebfea4dc3a98c743e03703494decf9d409f5d52d1fe3fae78472257
fetched_at: '2026-06-29T00:06:08.984098+00:00'
page_id: '203555644'
product: rm
source: tdn-rm
title: TTDXW1_DT_Execucao_Formula_Dias_Aviso_Sindicato
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDXW1_DT_Execucao_Formula_Dias_Aviso_Sindicato
version: 1
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
| **Chamados relacionados:** | TTDXW1 |
| **Versões/Release:** | *12.1.8.* |
