---
content_hash: 34ca099acdb338f19f0a78ca6487c6cd0554eb6415f74504f89d0452bd9d910f
fetched_at: '2026-06-29T00:11:40.839343+00:00'
page_id: '795084236'
product: rm
source: tdn-rm
title: Avanço Físico (F6)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=795084236
version: 20
---

**Forma de utilização do apontamento de avanço físico**

Este parâmetro define a forma como o sistema lida com o registro do avanço físico. Você tem à disposição as seguintes opções:

1. **Progresso da tarefa**: Esta é a opção padrão para o registro de avanço físico. Quando selecionada, o progresso indicado em um novo apontamento substituirá o valor existente. Por exemplo, se uma tarefa estiver com um apontamento de avanço físico de 30% e um novo apontamento for feito com um percentual de 50%, o progresso total registrado para essa tarefa será atualizado para 50%; Para mais detalhes acesse:
2. **Trabalho realizado no apontamento**: Quando selecionada, o progresso indicado em um novo apontamento de avanço físico será somado ao valor existente. Por exemplo, se uma tarefa estiver com um apontamento de avanço físico de 30% e um novo apontamento for feito com um percentual de 50%, o progresso total registrado para essa tarefa será atualizado para 80%. Para mais detalhes acesse:

**Obrigatória a inclusão de foto no apontamento de Avanço Físico**

Quando este parâmetro estiver habilitado, o aplicativo Minha Obra exigirá que o usuário anexe pelo menos uma foto ao realizar um apontamento de avanço físico. Caso nenhuma foto seja adicionada, o apontamento não poderá ser salvo. Quando desabilitado, a inclusão de fotos permanece opcional, mantendo o comportamento atual do sistema.

**Considerar saldo da tarefa no Avanço Físico**

Este parâmetro, quando marcado, afeta diretamente o cálculo do saldo relacionado à tarefa. O saldo passa a ser calculado da seguinte forma:

Saldo = Quantidade da Tarefa - Quantidade Concluída na Tarefa - (Quantidade Planejada na Tarefa - Desconto)

Se algum item da folha tarefa tiver sido adicionado ou apontado com esse parâmetro marcado, ele não mais poderá ser desmarcado, a seguinte mensagem é apresentada nessa situação:

**Atenção:**  
Caso esse parâmetro não esteja marcado será utilizado a quantidade total da tarefa na planilha de atividades.

**Atualizar o PERT/ Cronograma automaticamente ao sincronizar e ao salvar o apontamento de Avanço Físico**

Com este parâmetro habilitado o usuário tem a possibilidade de atualizar as informações do PERT de forma automática, através do sincronismo de apontamentos originados do coletor móvel ou através da edição de apontamentos do item da Folha Tarefa.

Este parâmetro somente poderá ser alterado se não existirem Folhas Tarefas com status de "Associada ao Coletor", isto é, significa que existem informações pendentes de retorno;

Quando os apontamentos forem enviados pelo coletor móvel e forem recebidos pelo TOTVS Obras e Projetos, será verificado a utilização deste parâmetro, e em caso de estar marcado, as informações da coluna Percentual Concluído do PERT serão atualizados conforme o apontamento lançado.

Ao incluir um apontamento de avanço físico pelo app deve refletir o apontamento no Pert .

Usando o mesmo apontamento de avanço físico pelo RM e o status do apontamento estiver como validado  esse apontamento será sempre refletido no  cronograma e no Pert  independente de ter parâmetro habilitado ou não.

Quando não utilizar o Pert o cockpit deverá buscar o avanço físico do cronograma executado. Neste caso, como temos a informação por período, o cockpit deverá apresentar o avanço dos últimos 4 meses.

**Campos Complementares a serem exibidos no App Minha Obra**

Permite parametrizar os Campos Complementares dos apontamentos de Avanço Físico (máximo de 5 campos), cujo preenchimento será realizado no App Minha Obra e visualizado no histórico do apontamento de avanço físico.

Este parâmetro somente estará habilitado se existirem campos complementares de Histórico de Apontamentos de Avanço Físico  cadastrado em "Cad. Gerais | Campos Complementares | Histórico de Apontamentos de Avanço Físico". Saiba mais em [Campos Complementares - TCOP](https://tdn.totvs.com/pages/editpage.action?pageId=445666380)

Após realizado o cadastro dos campos complementares, basta informá-los nesse parâmetro, e ficarão disponíveis na tela de apontamento de avanço físico no App Minha Obra para preenchimento e no sistema no histórico de apontamento de avanço físico apenas para visualização.

A ordem dos campos complementares definirá a ordem de exibição no App, ou seja, o Campo Complementar 1 será o primeiro a ser exibido na tela do apontamento de avanço físico do App Minha Obra, o Campo Complementar 2 será o segundo a ser exibido e assim, sucessivamente.

Cada parâmetro pode ser preenchido com um campo complementar e, na tela de preenchimento dos apontamentos de avanço físico do App Minha Obra, serão exibidos somente os 5 campos complementares informados nos parâmetros acima, conforme parametrizado em cada projeto, ou seja, podem ser parametrizados campos complementares diferentes em cada projeto.

A limitação da exibição dos nomes dos campos no App Minha Obra é limitada a 30 caracteres.
