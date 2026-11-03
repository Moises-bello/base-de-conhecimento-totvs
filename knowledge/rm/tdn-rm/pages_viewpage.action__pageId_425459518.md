---
content_hash: 5ada3c165f7cdb9c47363aaabc456d31fbd94e49e22800ec947edc23f1140618
fetched_at: '2026-06-29T00:09:36.771557+00:00'
page_id: '425459518'
product: rm
source: tdn-rm
title: Tipo de Atendimento - TOTVS Aprovações e Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459518
version: 64
---

**Tipo de Atendimento**

---

O tipo de atendimento foi criado para classificar o atendimento, definir etapas (situação atual do atendimento) e verificar o fluxo de etapas (passagem de uma etapa para outra) que o atendimento percorrerá no sistema.

Ele deve estar vinculado a um Grupo de Atendimentos para ser utilizado e somente atendentes com permissão liberada no perfil, poderão visualizar os tipos de atendimento.

É possível configurar por tipo de atendimento, alguns detalhes dos email que são enviados sobre atendimentos desse tipo, segue abaixo:

**Importante**: A Descrição padrão do remetente e o Assunto padrão email, sempre podem ser alterados, porém, por questões de segurança, nem todo servidor configurado no envio de email global, irá permitir a alteração do Endereço de email padrão do remetente, e nesses casos será mantido sempre o email que foi configurado nos parâmetros globais, para prevenir que uma pessoa com intenções maliciosas se passe por outra em um envio de email.

Minhas Aprovações / WhatsApp

Disponibilizada a possibilidade de aprovar/reprovar atendimentos via WhatsApp pelo parceiro Worknow, promovendo maior agilidade no atendimento e mais praticidade.  
Para configurar a utilização dessa funcionalidade ela é intermediada pelo serviço Worknow, verifique como habilitar e configurar: [Worknow - WhatsApp](https://tdn.totvs.com/pages/viewpage.action?pageId=1058177208)

No tipo de atendimento na aba 'Minhas Aprovações/WhatsApp' deverá habilitar a opção "*Disponível no Whatsapp*".

  

Na etapa do atendimento é necessário informar o template considerado na integração com o Worknow veja em : , selecionando o template no campo "*Template do WhatsAPP*"

A partir da  versão 12.1.28, o sistema disponibilizará o processo para "**Validar tipo de atendimento**" (no cadastro de tipo de atendimento), que permitirá ao usuário validar se o seu fluxo possui alguns requisitos básicos para uma melhor experiência ao utilizar o aplicativo Minhas Aprovações.

Esse processo fica disponível apenas para o usuário com essa permissão no perfil:

O processo verificará se o fluxo possui as seguintes características:

* Se todas as etapas possuem a finalidade informada (Aprovação ou Reprovação), pois essa informação irá determinar qual o caminho do fluxo o atendimento deverá seguir a partir da ação selecionada pelo usuário no aplicativo;

* Se o Tipo de Repasse está preenchido no cadastro de todas as etapas ;

* Se existe relatório vinculado ao tipo de atendimento ou uma etapa do tipo de atendimento (pelo menos uma etapa);

* Se pelo menos uma etapa possui a ação de conclusão.

Caso esqueça de preencher alguma das características acima, o usuário será informado ao fim do processo de Validar Tipo de Atendimento:

Obs: Independente do resultado deste novo processo , o fluxo de etapa seguirá normalmente no TOTVS Aprovações e Atendimento.

No App Minhas Aprovações o fluxo também poderá ser seguido, porém o usuário não irá aproveitar da funcionalidade de aprovar ou reprovar atendimentos com apenas um clique no botão apropriado e não terá acesso aos relatórios com dados de aprovação.

Ao habilitar a utilização do App Minhas Aprovações, o sistema já informará que é recomendado executar esse processo. Validando se seu tipo de atendimento está dentro dos requisitos necessários proporcionará uma melhor experiência aos usuários.

O gerenciamento de perfis e usuários é realizado pelo administrador.

Os procedimentos do tipo de atendimento são passos a serem seguidos no processo de fluxo de etapas e são dados apenas informativos no cadastro. Assim como a Descrição Detalhada, que permite informar o caminho que os atendimentos deste tipo deverão percorrer para concluir o fluxo. Neste campo ainda podem  ser  inseridas  informações adicionais que  são necessárias para o entendimento do fluxo percorrido pelos atendimentos do tipo cadastrado.

**Exemplo Procedimentos:**

**Referente à Manutenção de um Equipamento**

1º. Abrir atendimento (Solicitação de Conserto).

2º. Encaminhar para entendimento do responsável.

3º. Verificar e encaminhar para: Solucionado ou para Manutenção.

4º. Correção do defeito.

5º. Registrar informações referentes a manutenção realizada no equipamento.

6º. Encaminhar para o equipamento para testes .

7º. Registrar informações relativas ao teste.

8º. Encaminhar para entrega.

9º. Registrar informações sobre a entrega, por exemplo, prazo máximo de devolução.

**Exemplo Descrição Detalhada**

Após a abertura do atendimento que requer a manutenção do equipamento, o mesmo é encaminhado para o entendimento da solicitação. O supervisor avalia se realmente existe problema no equipamento, e logo após repassa para o solicitante se não houver defeito ou encaminha para o operador efetuar a manutenção. Na manutenção, o problema é corrigido e encaminhado a equipe de testes com as informações dos procedimentos realizados. A equipe de teste verifica a manutenção e avalia se não houve efeitos colaterais. Logo após o equipamento é enviado para a entrega.   
  
O tipo de atendimento pode ser associado a um modelo de atendimento, que servirá como um exemplo padrão para preenchimento dos campos, otimizando o processo e facilitando a abertura de ocorrências, sendo possível:

* Não substituir nenhum valor: Todos os campos permaneceram sem alteração.
* Substituir todos os valores atuais pelos do template:  Todos os campos serão substituídos pelo modelo, independente de estar preenchido ou não.

Substituir apenas os valores nulos pelos do template: Somente os campos nulos (em branco) serão substituídos.  
Além disso, o tipo de atendimento pode possuir um relatório Modelo de Tipo de Atendimento, criado no gerador de relatório, para imprimir as informações relativas as ocorrências que seguem determinado fluxo, de acordo com o tipo de atendimento.  
O Aceite pode ser utilizado quando for necessário exigir autorização para definir o fluxo, além de permitir a inserção do termo de aceitação para o tipo de atendimento. Se o tipo de atendimento possuir um fluxo que exija autorização de algum atendente, pode ser descrito o termo de aceitação.

Obriga selecionar tipo ou modelo de atendimento na abertura de atendimento

O **template de e-mail** têm por objetivo permitir que particularidades de cada tipo de atendimento seja tratado com precisão e maior controle do tráfego de informações que são enviadas no e-mail. Relatórios personalizados podem ser utilizados para apresentar as informações necessárias. Esta funcionalidade trabalha em conjunto à parametrização geral do sistema e respeita as regras:  
  
**E-mail de abertura de atendimentos**  
  
Ao enviar um e-mail de abertura o sistema irá verificar no tipo de atendimento inserido se existe algum relatório de e-mail personalizado, caso não exista ou o atendimento não tenha um tipo de atendimento, o sistema irá verificar nos parâmetros gerais se existe algum relatório de e-mail personalizado para abertura de atendimentos, caso não exista irá utilizar o fixo do sistema.

**E-mail de Repasse/Avançar Etapa**

·          Atendimento está inserido em fluxo de trabalho (Workflow):  
Repasse: Irá buscar a configuração de modelo de e-mail da etapa atual.  
Avanço de etapa: Irá buscar a configuração de modelo de e-mail da próxima etapa.  
·          Atendimento não está inserido em fluxo de trabalho (Workflow) ou não possui tipo de atendimento:   
Repasse: Irá buscar a configuração de modelo de e-mail para o tipo de atendimento, caso não exista busca o dos parâmetros, caso não exista utiliza o fixo do sistema.  
Avanço de etapa: Irá buscar a configuração de modelo de e-mail da próxima etapa (neste caso a primeira etapa do tipo de atendimento).  
Caso o atendimento não tenha um tipo de atendimento irá buscar o dos parâmetros, caso não exista utiliza o fixo do sistema.

**E-mail de conclusão de atendimentos:**

Ao enviar um e-mail de conclusão (Concluído Respondido), o sistema irá verificar no tipo de atendimento inserido se existe algum relatório de e-mail personalizado para conclusão de atendimentos, caso não exista ou o atendimento não tenha um tipo de atendimento, o sistema irá verificar nos parâmetros gerais se existe algum relatório de e-mail personalizado para conclusão de atendimentos, caso não exista irá utilizar o fixo do sistema.

**Configurações do aplicativo "Minhas Aprovações"**

---

**Notificar o responsável em todas as etapas do atendimento**

A partir da versão 12.1.33, estando a URL de configuração do App devidamente informada, sempre que o aprovador receber uma tarefa/atendimento para analisar, será enviada uma notificação no seu dispositivo conforme destacado abaixo:

As opções de notificações podem ser definidas no TOTVS Aprovações e Atendimento, por tipo de atendimento ou por etapa (telas abaixo) e nos dispositivos onde o App for instalado.

Por default esse parametro sempre será marcado para notificar.

Esse parametro pode ser habilitado no tipo de atendimento para todas as etapas , ou pode ser definido na própria etapa que só fica habilitada quando a opção de notificar em todas as etapas nao esteja informada.

É importante ressaltar que o sistema não notificará se o avanço for para conclusão do atendimento.

Caso o aparelho do usuário nao esteja com a permissão de notificação habilitada, ao clicar no sininho irá perguntar se deseja liberar permissão.

Para definir o número de dias que deverá manter as notificações no banco, acesse os Atendimento.]]>

**Disponível no aplicativo Minhas Aprovações**

Os tipos de atendimento que estiverem com este parâmetro marcado estarão disponíveis para atuação no App Minhas Aprovações.

---

**Anexos**

**Processos**

 

Cópia do Tipo de Atendimento

[Exportar Tipo de Atendimento](https://tdn.totvs.com/display/LRM/Exportar+Tipo+de+Atendimento)

Alterar Modelo de Email
