---
content_hash: a90be6163e3a7db7615984313e8096d9d0184017393970566e9dbf09da199a59
fetched_at: '2026-06-29T00:06:05.758750+00:00'
page_id: '201727136'
product: rm
source: tdn-rm
title: TTCYKV_DT_Log_Funcao_MINGADATA
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCYKV_DT_Log_Funcao_MINGADATA
version: 1
---

# FUNÇÃO FÓRMULA MINGADATA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Função de Fórmula* |
| **Situação/Requisito:** | *No log de cálculo da função de fórmula MINGADATA, que busca o valor do Mínimo Garantido no histórico do cadastro de Sindicato, está apresentando o valor incorreto.*  *Demonstra sempre o último Mínimo Garantido, mesmo quando na fórmula é utilizado parâmetro dia/mês/ano com uma data retroativa.*  *A mensagem incorreta não influencia no cálculo da fórmula.* |
| **Solução/Implementação:** | *Ajustar o log de cálculo da função de fórmula MINGADATA, que busca o valor do Mínimo Garantido no histórico do cadastro de Sindicato, para demonstrar o valor correto encontrado no histórico da época da data informada como parâmetro.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTCYKV* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
