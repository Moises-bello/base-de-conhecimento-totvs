---
content_hash: 6e6e186a7bbf1b4305544ff86585654c53d792c868dd25718adea530a0ed8e2f
fetched_at: '2026-06-29T00:09:29.848803+00:00'
page_id: '425458312'
product: rm
source: tdn-rm
title: Cancelar inscrição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458312
version: 10
---

Por meio desse assistente UMA ou MAIS inscrições poderão ser canceladas independentemente do período de calendário em que o processo seletivo se encontrar. Mas, se o status do candidato for "Compareceu chamada" o processo irá verificar se a área de opção do candidato possui Curso/Habilitação. Se houver é porque o candidato já realizou matrícula pelo Classis. Neste caso, primeiramente deverá ser executado o processo "Desfazer matrícula" para depois ser cancelada a inscrição. Caso a área ofertada seja de cliente, a inscrição poderá ser cancelada independente do status.

**Regras específicas para o processamento do Cancelamento**:

Ocorrerá a tentativa de cancelamento do lançamento financeiro. O cancelamento da inscrição só será feito se o cancelamento do lançamento for bem sucedido.

O status da inscrição será alterado para 8, "Inscrição Cancelada". O status das opções na área ofertada será alterado para 8, "Inscrição Cancelada".

Os registros de alocação e distribuição de prova com status igual a pendente serão removidos.

Dica

Provas em andamento para candidatos que foram cancelados, podem ser concluídas executando o processo "[Finalizar provas que não foram concluídas](https://tdn.totvs.com.br/pages/viewpage.action?pageId=552085931)" para estes candidatos (no Totvs Avaliação e Pesquisa -> Prova). Após este procedimento, a prova irá para o anexo de Ranking e poderá ser removida.

Se for um processo seletivo com atividades agendadas, neste caso não é excluído o agendamento, pois o candidato pode reativar sua inscrição se o processo seletivo estiver ainda em período de inscrição.

O candidato cancelado não irá participar do processo de classificação. Caso já tenha sido classificado, o candidato não irá participar do processo de chamada.

No Portal de Inscrições o candidato que tiver a inscrição cancelada conseguirá logar normalmente, mas a inscrição cancelada não aparecerá no seu histórico de inscrições.

No processo de cancelar inscrição foi adicionado um campo motivo. Isto porque será guardado um log de inscrições canceladas.

Para este controle foi criado uma visão de inscrições canceladas/excluídas como anexo no cadastro de processo seletivo. No Portal foi feita alteração no serviço Inscrições/Resultados para que passe a ser mostrado a data e o motivo de cancelamento quando uma inscrição for cancelada.

Em versões superiores a 12.1.21 será possível cancelar a inscrição do aluno mesmo com o boleto remetido ao banco. Isto é possível devido ao novo [parâmetro](http://tdn.totvs.com/pages/viewpage.action?pageId=425458275) que se encontra disponível em: Totvs Gestão de Processo Seletivo | Aba: Parâmetros | Parâmetros do Sistema | Integração | Gestão Financeira. Basta marcar o Item: **Ao efetuar o processo de cancelamento de inscrição do processo seletivo, cancelar automaticamente remessa do boleto.**
