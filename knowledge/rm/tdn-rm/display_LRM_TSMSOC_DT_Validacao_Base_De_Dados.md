---
content_hash: d9029f30aa43463f10c58722607a2e176ac5247cea25df0de5138c24e340ecb4
fetched_at: '2026-06-29T00:06:03.233532+00:00'
page_id: '198951629'
product: rm
source: tdn-rm
title: TSMSOC_DT_Validacao_Base_De_Dados
type: documentation
url: https://tdn.totvs.com/display/LRM/TSMSOC_DT_Validacao_Base_De_Dados
version: 2
---

# VALIDAÇÃO DA BASE DE DADOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *construção e projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Validação de Base de Dados* |
| **Situação/Requisito:** | *Cliente informa que ao executar rotina de validação de base, o sistema apresenta mensagem Erro - Prioridade do evento (desconto) menor que dos códigos de cálculo 3,4,13 e 105. Inconsistência devido ao uso de insuficiência de saldo. Porém os eventos com CC3,4,13 e 105 tem prioridades informada de forma automática dentro do sistema. Os eventos em que são apresentados os erros, são todos de prioridades obrigatoriamente menores que os Códigos de Cálculos acima.* |
| **Solução/Implementação:** | *Essa consistência não faz sentido no cálculo .NET, ela será retirada.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | **TSMSOC** |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
