---
content_hash: 723186556c24bf08ceff4e5b89837f866f91441af4a38872c0c10f0c5d530ffc
fetched_at: '2026-06-29T00:09:09.863202+00:00'
page_id: '394211657'
product: rm
source: tdn-rm
title: 3710831 DEDUINTEGRACOES-3197 DT Fórmula visual não executa processo de envio
  de mensagens
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394211657
version: 1
---

# Envio de mensagens de notificações temporais

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Envio de mensagens de notificações temporais |
| **Situação/Requisito:** | Ao executar o processo de envio de mensagens utilizando uma fórmula visual, sistema apresenta a seguinte mensagem de erro:   * + - INFORMAÇÕES SOBRE O PROCESSO \*\*\* Processamento da notificação "Pendências financeiras do aluno".  * + - AVISOS \*\*\* Mensagem de "Pendências financeiras do aluno" não parametrizada no cadastro de mensagens de notificação.   A mensagem de Notificação está parametrizada no cadastro de mensagens. |
| **Solução/Implementação:** | Identificamos que as propriedades Cód. Coligada, Cód. Filial e Cód. Nível de Ensino não estavam expostas para serem preenchidas.  Ajustamos o serviço para expor as propriedades Cód. Coligada, Cód. Filial e Cód. Nível de Ensino na atividade associada ao serviço EduMensagemNotificacoesTemporaisProcData.  Para que o serviço funcione corretamente estas propriedades devem estar preenchidas.  Observação:  No SQL (Código da sentença SQL) informado na atividade e que é utilizado para carregar informações do aluno dever ser carregado o campo "Nome", pois o mesmo será apresentado na mensagem abaixo, se o campo nome não for carregado a informação do usuário ficara em branco e no log da execução do processo será apresentada a mensagem conforme o exemplo abaixo.  Processamento da notificação "Pendências financeiras do aluno".    -> E-mail encaminhado para o usuário "". |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |
| **Documento de Referência:** |  |
| **Pacote:** | Informe o [linkdopacote] |
