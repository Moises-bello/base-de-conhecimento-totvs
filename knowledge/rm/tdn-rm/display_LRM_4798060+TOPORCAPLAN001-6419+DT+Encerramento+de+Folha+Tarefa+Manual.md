---
content_hash: 8304028db2c1c48ab111c79b48bb152818d061863fc64f3e447dfdd7fe08ff4a
fetched_at: '2026-06-29T00:10:12.670309+00:00'
page_id: '454834674'
product: rm
source: tdn-rm
title: 4798060 TOPORCAPLAN001-6419 DT Encerramento de Folha Tarefa Manual
type: documentation
url: https://tdn.totvs.com/display/LRM/4798060+TOPORCAPLAN001-6419+DT+Encerramento+de+Folha+Tarefa+Manual
version: 3
---

# ENCERRAMENTO DE FOLHA TAREFA MANUAL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Obras e Projetos |
| **Função:** | Encerramento de Folha Tarefa Manual |
| **Situação/Requisito:** | Erro no momento de encerrar a folha tarefa. Apos editar o apontamento de uma folha tarefa com o status EM PROCESSAMENTO e realizar o apontamento de 50% da mesma, o sistema apresenta a mensagem que o a folha não foi apontada no momento de encerrar. |
| **Solução/Implementação:** | Folhas tarefas com status EM PROCESSAMENTO, não devem permitir alteração em percentuais de apontamento de Avanço Físico.  Abaixo o passo a passo para que uma folha tarefa manual possa ser apontada e consequentemente encerrada:  1) Criação da Folha Tarefa: Status EM PROCESSAMENTO:    2) Associação dos Itens da Folha Tarefa:    3) Alteração da Folha Tarefa: Status PRONTA PARA IMPRESSÃO:    4) Edição do apontamento, alterando para o status de VALIDADO, e consequentemente alterando o status da Folha tarefa para APONTADA. O status da folha somente é alterado se todos os apontamentos dos itens estiverem com o status de VALIDADO:      5) Encerrando a Folha Tarefa: Com a folha no status de APONTADA, basta selecionar o processo de "Encerrar Folha Tarefa": |
| **Conversores e Parâmetros:** | Não se aplica. |
| **Tickets relacionados:** | Informe o(s) chamado(s) relacionado(s). |
| **Requisito:** | Informe o requisito relacionado. |
| **Documento de Referência:** | Não se aplica. |
| **Pacote:** | Não se aplica. |
