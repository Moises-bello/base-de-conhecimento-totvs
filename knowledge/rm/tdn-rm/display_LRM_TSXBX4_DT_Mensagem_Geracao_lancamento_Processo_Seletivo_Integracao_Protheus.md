---
content_hash: 7f2f129d047723c939f93013e12caea42ad95da82997d2c65fa9df75a236df94
fetched_at: '2026-06-29T00:06:01.849989+00:00'
page_id: '198940974'
product: rm
source: tdn-rm
title: TSXBX4_DT_Mensagem_Geracao_lancamento_Processo_Seletivo_Integracao_Protheus
type: documentation
url: https://tdn.totvs.com/display/LRM/TSXBX4_DT_Mensagem_Geracao_lancamento_Processo_Seletivo_Integracao_Protheus
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Processo Seletivo* |
| **Função:** | *Mensagem de Geração de Lançamento no Processo Seletivo quando integrado ao Protheus* |
| **Situação/Requisito:** | Ao gerar um lançamento pelo processo seletivo utilizando a integração com Protheus de Mensageria, não estava sendo carregado corretamente  as informações de Item Contábil e Classe de Valor, com isso este conteúdo não estava sendo incluído na mensagem enviada para o Protheus. |
| **Solução/Implementação:** | A consulta que recuperava a informação não estava retornando o valor de Item Contábil e Classe de Valor do campo correto!  A tabela SPSPROCSELINTPROTHEUS possui quatro campos:  (IDITEMCONTABIL e IDITEMCONTABILPROTHEUS) e (IDCLASSEVALOR e IDCLASSEVALORPROTHEUS)  Na integração antiga com o Protheus através de trigger, o Item Contábil e Classe de Valor são armazenados nos campos IDITEMCONTABIL e IDCLASSEVALOR.  Já na integração através de Mensageria, são gravados nos campos IDITEMCONTABILPROTHEUS e IDCLASSEVALORPROTHEUS.  A consulta executada pela integração com mensageria estava retornando os valores dos campos da integração antiga.    Foi ajustado a consulta para retornar os campos corretos. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.7* |
