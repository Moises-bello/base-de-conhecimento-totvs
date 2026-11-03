---
content_hash: 0c736d5a7d76724243436315a0ca44c20a318a905f2ed504a00fb1c13f83bde0
fetched_at: '2026-06-29T00:06:05.754661+00:00'
page_id: '201727054'
product: rm
source: tdn-rm
title: TSQ374_DT_Log_Funcao_MINGADATA
type: documentation
url: https://tdn.totvs.com/display/LRM/TSQ374_DT_Log_Funcao_MINGADATA
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
| **Chamados relacionados:** | *TSQ374* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
