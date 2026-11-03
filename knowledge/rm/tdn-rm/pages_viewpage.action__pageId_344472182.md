---
content_hash: 45e50fad31a9a7284c6a9ad1238d189ff370dbaf281522d4be03e6af67629e50
fetched_at: '2026-06-29T00:08:53.370975+00:00'
page_id: '344472182'
product: rm
source: tdn-rm
title: 2004276 DEDUINTEGRACOES-1473 DT Inclusão de Responsável Financeiro do Aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344472182
version: 2
---

# INCLUSÃO DE RESPONSÁVEL FINANCEIRO DO ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Inclusão de Responsável Financeiro do Aluno* |
| **Situação/Requisito:** | *Na rotina de inclusão de responsável financeiro do aluno ao clicar nos botões para cadastrar Aluno, Pai/Mãe ou Responsável Acadêmico como Responsável Financeiro o registro gerado no cadastro de cliente/fornecedor era sempre de classificação "Ambos".* |
| **Solução/Implementação:** | *Foi alterada a rotina de inclusão de cliente/fornecedor no cadastro de aluno (onde cria-se um cliente/fornecedor para o aluno, para os pais ou para o responsável acadêmico) para que o comportamento anterior fosse retornado. Cadastrando sempre como "Cliente".*  *Na rotina de inclusão de bolsas retroativas, onde é necessário que o responsável financeiro seja de classificação "Ambos" (para permitir geração de lançamentos a pagar para esse cliente/fornecedor) possui uma verificação que identifica antes de executar o assistente se existe algum contrato com responsável financeiro que é apenas "Cliente", caso encontre solicita ao usuário permissão para alterá-lo para "Ambos" durante a execução, caso o usuário não permita o assistente não é concluído.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Documento de Referência:** | *N/A* |
