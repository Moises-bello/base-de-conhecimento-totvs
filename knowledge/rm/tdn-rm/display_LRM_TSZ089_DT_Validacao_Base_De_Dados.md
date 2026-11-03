---
content_hash: 084b915ea4dd8c9e7959f504996aa981ab8f964c6fc8825ed98a13d6e4c99b31
fetched_at: '2026-06-29T00:06:03.459041+00:00'
page_id: '198954592'
product: rm
source: tdn-rm
title: TSZ089_DT_Validacao_Base_De_Dados
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZ089_DT_Validacao_Base_De_Dados
version: 1
---

# VALIDAÇÃO DA BASE DE DADOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Totvs Folha de Pagamento* |
| **Função:** | *Validação de Base de Dados* |
| **Situação/Requisito:** | *Cliente informa que ao executar rotina de validação de base, o sistema apresenta mensagem Erro - Prioridade do evento (desconto) menor que dos códigos de cálculo 3,4,13 e 105. Inconsistência devido ao uso de insuficiência de saldo. Porém os eventos com CC3,4,13 e 105 tem prioridades informada de forma automática dentro do sistema. Os eventos em que são apresentados os erros, são todos de prioridades obrigatoriamente menores que os Códigos de Cálculos acima.* |
| **Solução/Implementação:** | *Essa consistência não faz sentido no cálculo .NET, ela será retirada.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | **TSZ089** |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
