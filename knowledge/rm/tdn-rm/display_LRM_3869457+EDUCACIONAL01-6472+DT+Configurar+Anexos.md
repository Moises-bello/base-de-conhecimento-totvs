---
content_hash: 875e4adcda10c49479aceced934a7f87bc2faec531b7a957c248d81630d6e4a8
fetched_at: '2026-06-29T00:09:11.519828+00:00'
page_id: '407113196'
product: rm
source: tdn-rm
title: 3869457 EDUCACIONAL01-6472 DT Configurar Anexos
type: documentation
url: https://tdn.totvs.com/display/LRM/3869457+EDUCACIONAL01-6472+DT+Configurar+Anexos
version: 4
---

# CONFIGURAR ANEXOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Configurar Anexos |
| **Situação/Requisito:** | Após acessar a matrícula no período letivo do aluno e depois o anexo Configurar Anexos, selecionar a opção usuário no escopo e informar o usuário desejado, o sistema apresenta o erro:  "A seguinte exceção ocorreu no DataGridView:  System.ArgumentException: O valor de DataGridViewComboBoxCell não é válido.  Para substituir a caixa de diálogo padrão, manipule o evento DataError." |
| **Solução/Implementação:** | Foram alteradas as chamadas de alguns anexos, que não utilizam tela de visão, para que não ocorram validações incorretas na tela de configurações de anexos. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
