---
content_hash: 972f66da08a785c03e59a6b881d79639ce624fb6f5c5da62467e67918208103b
fetched_at: '2026-06-29T00:08:40.547100+00:00'
page_id: '286224371'
product: rm
source: tdn-rm
title: 1196915 DEDUINTEGRACOES-189 DT Transferência Interna Aproveitamento Conta Corrente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286224371
version: 105
---

# Transferência Interna

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contabil |
| **Função:** | Transferência Interna |
| **Situação/Requisito:** | Ao realizar o processo de transferência interna (mudando de matriz aplicada) para um aluno que possuía débitos ou créditos na conta corrente o sistema não atualizava a matriz aplicada dos registros da conta corrente, este cenário ocorre quando na transferência o usuário opta por gerar um novo contrato.  Como a matriz aplicada da conta corrente não era atualizado, ao executar o processo de aproveitamento de valores da conta corrente o sistema não deixava continuar, pois a matriz aplicada do contrato ativo era diferente da matriz aplicada do registro da conta corrente. |
| **Solução/Implementação:** | * Realizado uma evolução no processo de transferência interna para que a matriz aplicada dos registros de conta corrente seja atualizada conforme a matriz aplicada de destino.  A matiz aplicada no registro de conta corrente será atualizado somente se o contrato de origem estiver sendo cancelado, caso contrário o registro da conta corrente permanecerá com a matriz aplicada do contrato antigo. * Habilitamos a opção de edição da conta corrente, possibilitando ao usuário alterar manualmente a matriz aplicada do registro da conta corrente. Será permitido alterar somente a matriz aplicada Será listado para a seleção somente matriz aplicada vinculada a um contrato do aluno, contrato que não esteja cancelado . |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |

divs
