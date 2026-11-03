---
content_hash: fc43759bdda4335640f7d365bb5983297372f4d23af2c5f76fe656d253827a32
fetched_at: '2026-06-29T00:08:23.080993+00:00'
page_id: '269444680'
product: rm
source: tdn-rm
title: 230824_DT_Aproveitamento_Valor_ContaCorrente_Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/230824_DT_Aproveitamento_Valor_ContaCorrente_Aluno
version: 118
---

# Conta Corrente do Aluno

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Processo de Aproveitamento de Valores da Conta Corrente do Aluno |
| **Situação/Requisito:** | Acessei o cadastro de aluno e gerei um lançamento para seu contrato. Logo após procedi com a baixa do lançamento com pagamento a menor, gerando um valor de débito para o aluno em sua conta corrente. Ao executar o processo de Aproveitar Valores em Conta Corrente, verifiquei que o sistema não aproveita o valor no Campo de Valor Opcional no lançamento financeiro. O valor somente é incluído ao lançamento se o parâmetro 'Efetuar operação com valor total na próxima mensalidade' estiver marcado.  Mesmo com o parâmetro desmarcado o sistema deveria utilizar o valor da Conta Corrente no lançamento gerado. |
| **Solução/Implementação:** | Ajuste no processo de aproveitamento de valores da conta corrente do aluno para que os valores selecionados sejam aproveitados corretamente nos lançamentos gerados. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *MEDU-1293* |
| **Requisito (ISSUE):** | *N/A* |

divs
