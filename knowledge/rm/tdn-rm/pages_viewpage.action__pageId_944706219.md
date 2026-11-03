---
content_hash: 96eec24c1c4426e9020e6c5d0a0f940d5ffd16bd1e49120bcae4148cad6db024
fetched_at: '2026-06-29T00:12:09.308560+00:00'
page_id: '944706219'
product: rm
source: tdn-rm
title: 03 - Gestão de mensagens
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=944706219
version: 44
---

# Sumário

---

Sumário

# Gestão de mensagens

---

A Gestão de Mensagens tem como objetivo permitir que os usuários e os responsáveis por aprovações acompanhem e visualizem as mensagens processadas. Além disso, essa funcionalidade oferece recursos adicionais, como visualização dos detalhes da mensagem, edição, aprovação, reprovação, uso como modelo, exclusão, entre outros.

Para que o item “**Gestão de mensagens**” seja exibido, é necessário que a permissão esteja devidamente habilitada no perfil do usuário autenticado.

Exemplo da tela de "Gestão de mensagens"

Status da Mensagem – Definições

* **Aprovação pendente:**  
  Indica que a mensagem foi criada e enviada por um usuário, e está aguardando aprovação de um dos responsáveis definidos na regra de comunicação vinculada ao tipo da mensagem.
* **Reprovado:**  
  Indica que a mensagem foi analisada e reprovada por um dos aprovadores configurados na regra de comunicação associada ao tipo da mensagem. Mensagens reprovadas não seguem para envio.
* **Agendado:**  
  Indica que a mensagem está programada para envio em uma data e horário futuros. Neste status, a mensagem já passou pelo processo de aprovação, quando aplicável.
* **Aguardando processamento:**  
  Indica que a mensagem está na fila de processamento, aguardando início do envio. Este status é comum em mensagens que não foram agendadas, mas enviadas imediatamente.
* **Em processamento:**  
  Indica que o processo de envio da mensagem está em andamento.
* **Parcialmente processado:**  
  Indica que parte da mensagem foi processada e enviada com sucesso, enquanto outra parte apresentou erros durante o envio.  
  Este cenário é comum quando a mensagem é direcionada a múltiplos contextos. Por exemplo, se o público-alvo inclui alunos das filiais 01 e 02, o sistema executará dois processamentos independentes (dois JOBs). Caso um JOB finalize com sucesso e o outro apresente falha, o status da mensagem será atualizado para **“Parcialmente processado”**.
* **Enviado:**  
  Indica que a mensagem foi processada e enviada com sucesso.
* **Erro de processamento:**  
  Indica que ocorreu uma falha durante o processamento.
Mensagens com Data de Expiração

Algumas categorias permitem o envio de mensagens com data de expiração. Nesses casos, a coluna "**Data de Expiração**" estará preenchida, indicando até quando o conteúdo ficará disponível para visualização na linha do tempo do aplicativo.

Para mais informações sobre o funcionamento, [[clique aqui]](https://tdn.totvs.com/display/LRM/Cadastro+de+categorias).

É importante ressaltar que a **data de expiração** será preenchida somente após o processamento do envio, pois o prazo é calculado dinamicamente com base no fluxo de saída e na categoria configurada.

Para conhecer mais sobre a funcionalidade de aprovações e reprovações [clique aqui](https://jiraproducao.totvs.com.br/browse/DEDUCAPCOM-8762).

Ações Disponíveis na Gestão de Mensagens

As ações disponíveis podem ser acessadas clicando no ícone de três pontinhos localizado na linha da mensagem desejada, conforme demonstrado na imagem abaixo.

Segue abaixo a descrição do comportamento das ações disponíveis

* **Visualizar ou Editar:**  
  Disponível para o autor da mensagem quando ela estiver com status **“Pendente aprovação”**. Permite visualizar ou editar a mensagem antes que ela seja aprovada.
* **Visualizar:**  
  Disponível para o autor da mensagem e para os aprovadores. Permite consultar os detalhes da mensagem, porém sem possibilidade de edição. Esta opção estará disponível quando o status da mensagem for **diferente de “Pendente aprovação”**.
* **Usar como modelo:**  
  Permite utilizar a mensagem selecionada como base para criar uma **nova mensagem**.  
  Ao selecionar esta opção, será aberta a tela de envio com todos os dados da mensagem preenchidos conforme o modelo selecionado, possibilitando ao usuário revisar, ajustar ou alterar qualquer informação necessária.

  Importante

  A mensagem original não será alterada.
* **Cancelar:**  
  O botão **Cancelar**estará visível apenas para usuários que possuírem a permissão correspondente em seu perfil. Além disso, somente o usuário que criou a mensagem poderá cancelá-la.  
  A ação de cancelamento é permitida apenas para mensagens com os status ****"Pendente de aprovação"**, **"Agendada"**, **"Aguardando processamento"****ou ****"Em processamento".****  
  Ao cancelar uma mensagem, o sistema interrompe o agendamento e/ou o pedido de aprovação, se aplicável.  
    
  1. Mensagens com **status** igual a **"Agendada" ou "Pendente de aprovação"** ao serem canceladas, ficarão com o status **"Cancelado"**.
  2. Mensagens com **status** igual a **"Em andamento"** ao serem em canceladas terão o envio interrompido, e o status será **"Processando cancelamento..."** temporariamente, e depois do cancelamento processado passará para o status **"Cancelado parcialmente"**.

     Se o cancelamento da mensagem for acionado enquanto ela estiver com o status **"Em andamento"**, dependendo do progresso do envio, o cancelamento poderá não ser concluído. Nesse caso, o envio será finalizado e a mensagem permanecerá com o status **"Enviada"**.

     Quando a mensagem apresentar o status **"Cancelado parcialmente"**, isso pode indicar que alguns destinatários já receberam a mensagem enquanto o processamento de cancelamento estava em andamento. Essa situação é registrada no log de processamento, incluindo a informação sobre a interrupção e a lista de usuários que foram notificados.

     Recomendamos utilizar a ação **"Baixar Log de Processamento"** para consultar esses registros e verificar os destinatários impactados.

     Para os casos em que a mensagem apresentar o status **"Processando cancelamento..."**, recomendamos aguardar alguns instantes e, em seguida, acionar a opção **"Atualizar"** para que o status mais recente da mensagem seja carregado na tela. Nesse cenário, a atualização do status não é realizada automaticamente.

     Ao executar o envio de uma mensagem, é criado no **Gerenciamento de Jobs** do *rm.exe* um JOB responsável por processar o envio.  
     Em caso de cancelamento, o sistema automaticamente cancela ou interrompe a execução desse JOB.  
     No *rm.exe*, também é possível visualizar o status e os respectivos logs.

     Exemplo:

     *Job* gerado referente a uma mensagem cancelada com status **Em andamento**. Após o término do cancelamento, o status foi alterado para **Cancelado parcialmente,** e alguns destinatários já haviam recebido a mensagem antes de finalizar o cancelamento.
* **Excluir:**  
  Disponível para o autor da mensagem, permite excluir a mensagem quando ela estiver com o status **“Pendente aprovação”** ou **“Agendado”**.

  Se a mensagem estiver agendada ao excluir o JOB de execução é automaticamente cancelado no RM.
* **Aprovar ou Visualizar:**  
  Exclusiva para mensagens com status **“Aprovação pendente”** e visível apenas para usuários que estão configurados como **aprovadores** na regra de comunicação associada ao tipo da mensagem.  
  Permite visualizar os detalhes da mensagem e realizar a aprovação ou reprovação.
* **Detalhes do Agendamento:**  
  Disponível para mensagens com status **“Agendado”** ou **“Enviado”**. Permite visualizar as informações do agendamento, como data e hora programada e parâmetros utilizados.
* **Justificativa da Reprovação:**  
  Disponível para mensagens com status **“Reprovado”**. Permite consultar detalhes da reprovação, incluindo:  
  • Usuário que realizou a reprovação  
  • Data e hora da reprovação  
  • Justificativa informada pelo aprovador
* **Baixar Log de Processamento:**  
  Disponível para mensagens com status **“Enviado”**, **“Erro de processamento”**, **“Parcialmente processado”** ou **"Cancelado parcialmente"**.  
  Ao acionar esta opção, será realizado o download dos arquivos de log, que contêm detalhes do processamento da mensagem.

  Importante

  Se a mensagem foi processada para mais de um contexto (ex.: alunos das filiais 01 e 02), será gerado um arquivo de log para cada processamento. Nesse exemplo, dois arquivos de log estarão disponíveis para download.
Filtros

A funcionalidade de filtro permite ao usuário realizar consultas tanto amplas quanto específicas, com base nas informações da mensagem, como: assunto, autor, status, tipo de mensagem, se possui anexo, canal de envio, data/hora de criação ou de envio (inicial e final).

Uma boa prática para usuários aprovadores é utilizar os filtros para localizar rapidamente mensagens que estão pendentes de aprovação, seja de um autor específico ou de todas as mensagens pendentes. Além disso, é possível realizar diversas combinações dos filtros para refinar ainda mais a busca.

# Envio de Mensagem com Recorrência

---

Ao enviar uma mensagem, é possível configurá-la para **agendamento recorrente**, ou seja, a mensagem poder ser programada para ser enviada automaticamente conforme o intervalo de recorrência definido.

O agendamento com recorrência significa que o envio da mensagem se repetirá de forma periódica, podendo ser semanal, mensal, anual ou em outro intervalo configurado.

Na última etapa do processo, é possível definir se a mensagem será **agendada** e configurar a sua **periodicidade**.  
Se a periodicidade for diferente de **“Única”**, isso significa que a mensagem será agendada com **recorrência**, ou seja, será enviada automaticamente de acordo com o intervalo definido.

Execução da recorrência

Quando chega o momento da execução da recorrência, o sistema (RM) **gera uma cópia da mensagem original** e realiza o envio dessa cópia. A mensagem original permanece com o status **“Agendado”**, indicando que ela é a base da recorrência e continuará ativa para os próximos envios, conforme a configuração.

Após o processamento da recorrência, na tela de **Gestão de Mensagens**, será exibida a nova mensagem enviada (cópia gerada pela recorrência), permitindo ao usuário **consultar detalhes e baixar o log desse envio**.

Se for necessário **cancelar a recorrência**, basta excluir a mensagem que está com o status **“Agendado”** e com o indicativo de recorrência. Com isso, o sistema **cancelará automaticamente o JOB de envio recorrente no RM**.

Todo envio de mensagem na Central de Comunicação gera um **JOB de execução no RM**. No caso de mensagens recorrentes, esse JOB também fica agendado no RM até que a recorrência seja cancelada.

Exemplo de uma menagem agendada com recorrência

Para consultar os detalhes da recorrência é só acessar "Detalhes do agendamento" conforme a imagem acima.
