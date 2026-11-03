---
content_hash: 9d141ec6ede8fd8f9ee15f5657ce18992ea303305324f28d71bd7d2857c06fed
fetched_at: '2026-06-29T00:06:24.311493+00:00'
page_id: '224116595'
product: rm
source: tdn-rm
title: TU0585_DT_Questao_Multipla_Questao_Condicional_Acao_Incorreta
type: documentation
url: https://tdn.totvs.com/display/LRM/TU0585_DT_Questao_Multipla_Questao_Condicional_Acao_Incorreta
version: 118
---

# EXECUTOR WEB

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Avaliação e Pesquisa* |
| **Função:** | *Execução de provas com questões condicionais pelo executor web.* |
| **Situação/Requisito:** | *No executor web, foi identificado que quando é executada uma prova com uma questão do tipo múltipla que possui uma questão condicional, o sistema não estava efetuando a ação correta da questão condicional, as vezes até invertendo a ação.* |
| **Solução/Implementação:** | *No momento que era criado o evento da ação condicional o sistema não estava criando o id do campo corretamente por uma incosistência na ordem das opções da questão, após efetuar o ajuste na geração do ID da opção as ações condicionais passaram a ser executadas corretamente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.10* |
| **Versão Corrigida:** | *12.1.10* |
| **Versão Expedida:** | *12.1.10* |

divs
