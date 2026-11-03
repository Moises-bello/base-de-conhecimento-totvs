---
content_hash: 1923cb12e9e7c6268f168a71cb1a8272153ff5673992dbd6425cc746e41f6824
fetched_at: '2026-06-29T00:06:11.362868+00:00'
page_id: '203768405'
product: rm
source: tdn-rm
title: TTDOTS_DT_Mensagem_Erro_Calculo_Exibe_Metodo_Classes
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDOTS_DT_Mensagem_Erro_Calculo_Exibe_Metodo_Classes
version: 1
---

# MENSAGEM DE ERRO NO CÁLCULO EXIBE MÉTODOS E CLASSES DO CÓDIGO FONTE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cálculo de Rescisão* |
| **Situação/Requisito:** | *Ao realizar uma rescisão com data de pagamento no mês atual, e no mesmo período o funcionário já possui movimentação que incide em IRRF com data de pagamento no próximo mês, é exibida uma mensagem de erro, informando tal situação.*  *Mas o texto da mensagem está vindo com os métodos das classes de código.* |
| **Solução/Implementação:** | *Ajuste no log para que seja exibido somente o texto da mensagem direcionada ao usuário, e não traga os nomes dos métodos das classes em nível de código.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTDOTS* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
