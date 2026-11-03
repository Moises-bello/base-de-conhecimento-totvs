---
content_hash: 835df47e780d9af9e3b14943bc53452939f9437bbfaa465dc28af969a8353c1f
fetched_at: '2026-06-29T00:06:10.649470+00:00'
page_id: '203765955'
product: rm
source: tdn-rm
title: TTGWYI_DT_Salario_Composto_Formula_Visual
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGWYI_DT_Salario_Composto_Formula_Visual
version: 2
---

# SALÁRIO COMPOSTO UTILIZANDO FÓRMULA VISUAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Salário Composto com Formula Visual* |
| **Situação/Requisito:** | Ao gravar os dados da fórmula na tela de Salário Composto, caso seja apresentado qualquer erro e o usuário clique em salvar novamente, o sistema inseria várias cópias do mesmo registro de histórico, causando erro na validação da chave primária. |
| **Solução/Implementação:** | Foi adicionada uma validação no tratamento de histórico salarial para não inserir registros duplicados na tabela. |
| **Chamados relacionados:** | TTGWYI |
| **Versões/Release:** | *11.82.41* |
