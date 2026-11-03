---
content_hash: a9408d51df46595c5a234a907214706bc945dd15d4401be2c9a3c5ded63f9e18
fetched_at: '2026-06-29T00:06:10.587998+00:00'
page_id: '203765143'
product: rm
source: tdn-rm
title: TTHR09_DT_CadastroFuncionario_EnvioEmail
type: documentation
url: https://tdn.totvs.com/display/LRM/TTHR09_DT_CadastroFuncionario_EnvioEmail
version: 1
---

# CADASTRO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | *Folha de Pagamento.* |
| **Função:** | *Processo "Enviar e-mails para funcionários".* |
| **Situação/Requisito:** | *Ao selecionar mais de uma linha na visão de funcionários para executar o processo "Enviar e-mails para funcionários", ocorre o erro no envio dos emails.* |
| **Solução/Implementação:** | *Foi alterado na rotina de "Enviar e-mails para funcionários", o controle da variável que armazenava o relatório a ser anexado ao email. Esta variável não estava sendo zerada para cada email enviado aos funcionários selecionados.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTHR09.* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
