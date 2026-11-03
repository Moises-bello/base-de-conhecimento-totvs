---
content_hash: 76f4069482b35d72d7b4f31c88bb122977bf163d03bf2545a918933491f4ed7a
fetched_at: '2026-06-29T00:06:10.652817+00:00'
page_id: '203765974'
product: rm
source: tdn-rm
title: TTIOXT_DT_Salario_Composto
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIOXT_DT_Salario_Composto
version: 1
---

# SALÁRIO COMPOSTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Salário Composto* |
| **Situação/Requisito:** | Ao gravar os dados na tela de Salário Composto, caso seja apresentado qualquer erro e o usuário clique em salvar novamente, o sistema inseria várias cópias do mesmo registro de histórico, causando erro na validação da chave primária. |
| **Solução/Implementação:** | Foi adicionada uma validação no tratamento de histórico salarial para não inserir registros duplicados na tabela. |
| **Chamados relacionados:** | TTIOXT |
| **Versões/Release:** | *12.1.8* |
