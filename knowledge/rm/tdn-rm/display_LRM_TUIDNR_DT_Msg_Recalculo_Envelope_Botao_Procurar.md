---
content_hash: 5c1669f704ab1e3c668afd789f900e69c9cebf2ba94eff3cc71c7a03625f68d6
fetched_at: '2026-06-29T00:06:30.176112+00:00'
page_id: '235315105'
product: rm
source: tdn-rm
title: TUIDNR_DT_Msg_Recalculo_Envelope_Botao_Procurar
type: documentation
url: https://tdn.totvs.com/display/LRM/TUIDNR_DT_Msg_Recalculo_Envelope_Botao_Procurar
version: 2
---

# MSG DE RECÁLCULO DO ENVELOPE AO ACIONAR O BOTÃO PROCURAR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Envelope* |
| **Situação/Requisito:** | *Quando existe alguma alteração de valores ou inserção de novos eventos no envelope do funcionário, e o usuário navega para a próxima chapa, é exibida uma mensagem alertando que houve alteração de valores, e pergunta se deverá ser executado o recálculo.*  *Mensagem: "Alguns valores do envelope foram alterados manualmente . Confirma recálculo geral do envelope para este funcionário?"*  *Mas se é acionada a opção de selecionar uma nova chapa através do botão de procurar (Binóculo na parte superior da tela), esta mensagem não é exibida.*  *Dessa forma as alterações são salvas no envelope, porém os valores não são recalculados e atualizados.* |
| **Solução/Implementação:** | *Ajuste na opção de selecionar uma nova chapa através do botão de procurar do envelope, para exibir a mensagem alertando que houve alteração de valores, e se deverá ser executado o recálculo.* |
| **Chamados   relacionados:** | *TUIDNR, TUOCYV* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
