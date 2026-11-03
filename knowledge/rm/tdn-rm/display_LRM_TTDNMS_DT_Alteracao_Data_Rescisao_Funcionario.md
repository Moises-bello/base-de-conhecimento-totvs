---
content_hash: d247ff80f15eaad5b0564c80dcdef2b9a705b528399dbc724724d306d5a01a60
fetched_at: '2026-06-29T00:06:08.063885+00:00'
page_id: '201743836'
product: rm
source: tdn-rm
title: TTDNMS_DT_Alteracao_Data_Rescisao_Funcionario
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDNMS_DT_Alteracao_Data_Rescisao_Funcionario
version: 2
---

# RESCISÃO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão de Funcionários* |
| **Situação/Requisito:** | *Ao alterar a data de rescisão de um funcionário, a situação no histórico era apagada.* |
| **Solução/Implementação:** | Foi adicionada uma validação para verificar se o codigo de situação está vazio antes de efetuar o update. |
| **Chamados relacionados:** | TTDNMS |
| **Versões/Release:** | *12.1.8* |
