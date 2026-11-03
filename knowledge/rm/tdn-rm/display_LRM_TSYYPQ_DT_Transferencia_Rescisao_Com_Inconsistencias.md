---
content_hash: d840b680dcd9e0e236bded7de821b37db40d1b3dd5e93c4e699c2407eb0441cd
fetched_at: '2026-06-29T00:06:11.269977+00:00'
page_id: '203767265'
product: rm
source: tdn-rm
title: TSYYPQ_DT_Transferencia_Rescisao_Com_Inconsistencias
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYYPQ_DT_Transferencia_Rescisao_Com_Inconsistencias
version: 1
---

# TRANSFERÊNCIA DE FUNCIONÁRIO COM INCONSISTÊNCIAS NO CÁLCULO DA RESCISÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão por Transferência* |
| **Situação/Requisito:** | *Quando é realizada rescisão com o tipo 6 - Transferência com ônus, e ocorre alguma inconsistência que interrompe o cálculo, é exibida a mensagem de erro e não demite o funcionário.*  *Porém realiza a transferência criando um novo registro. Com isto, o funcionário fica com dois cadastros ativos e nenhum com a rescisão calculada.*  *Um exemplo é quando se trabalha com regime caixa, em que o funcionário já possui movimentação que incide em IRRF com data de pagamento no próximo mês, e a rescisão tem data de pagamento no mês atual.* |
| **Solução/Implementação:** | *Ajuste para que só seja processada a transferência do funcionário se a execução do cálculo da rescisão for finalizada sem erros, e a situação do funcionário for alterada para demitido.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSYYPQ* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
