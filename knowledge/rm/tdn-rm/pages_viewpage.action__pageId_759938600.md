---
content_hash: f064e63a8831ac145d23c7ffe09266e126f5503044fc72dee8301c2224aff470
fetched_at: '2026-06-29T00:11:33.420458+00:00'
page_id: '759938600'
product: rm
source: tdn-rm
title: PI - Resumo Proposta - Solicitar Aprovação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=759938600
version: 30
---

É importante destacar que a nova proposta estará disponível para novos clientes a partir da versão 12.1.2306.

**Introdução:**

---

Esse processo é útil para gerenciar propostas que precisam ser aprovadas por um supervisor ou gerente antes de serem finalizadas. O processo começa quando um gerente recebe uma proposta que foi reprovada e precisa ser aprovada.   
Em seguida, o gerente acessa a proposta e pode visualizar um resumo dos dados da proposta. Com base nesses dados, o gerente pode decidir se aprova ou reprova a proposta.

Para garantir que o supervisor ou gerente seja notificado sobre a proposta, é necessário enviar um e-mail ao finalizar a proposta. Esse e-mail será enviado para o supervisor com as informações em seu corpo que é parametrizado em um Reports (através dos parâmetros do TOTVS Incorporação) , juntamente com informações adicionais sobre o motivo pelo qual a proposta foi aprovada ou reprovada.

## **Pré requisitos:**

---

**Sobre as configurações necessárias para o envio de e-mails:**

* É necessário que os parâmetros de envio de e-mail estejam configurados no sistema. Para configurar acesse: ***[Envio de e-mails - Linha RM](https://tdn.totvs.com/display/LRM/Envio+de+email+-+LINHA+RM)***
* Realizar a importação dos relatórios: ***TCGIRELPI0001 -*** *Corpo de E-mail para Solicitação de Aprovação de Proposta e* ***TCGIRELPI0002 -*** *Corpo de E-mail para Forçar Aprovação de Proposta*(através do RM Reports) estes relatórios estão disponível acessando o ***[TOTVS Compartilhamento](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento)***
* Para que os e-mails possam ser enviados corretamente é importante que o SUPERVISOR E CORRETOR possuam seus e-mails cadastrados em seus respectivos usuários no Portal de imóveis no caminho (backend | Usuários)

**Sobre as configurações no portal de imóveis:**

* Para a situação da proposta REPROVADA, é necessário habilitar a opção "Permite forçar aprovação" no Backend | Globais | Situação da Proposta. Essa opção permitirá que o SUPERVISOR realize a aprovação de uma proposta reprovada.
* Para permitir que o supervisor autorize propostas reprovadas, acesse o Backend, vá para Usuários, selecione Grupos e edite o grupo associado ao usuário Supervisor. Marque a opção "Autorizar proposta reprovada". Isso dará ao supervisor a capacidade de autorizar propostas reprovadas.
* A proposta deverá estar com sua situação reprovada para que este processo possa ser realizado.

## **Parametrizando o sistema:**

---

Para que o sistema realize o envio de email será necessário realizar as seguintes parametrizações:  
  
**1) Realizar a parametrização dos relatórios nos parâmetros do TOTVS Gestão de Imóveis.** Estes relatórios imprimem o resumo da proposta no corpo do email enviado para o supervisor e para o corretor.  
Esta tela é dividida em duas seções: *"Dados para solicitar aprovação"* (referente aos dados enviados pelo corretor para o e-mail do supervisor) e *"Dados para forçar a aprovação"* (referente ao e-mail enviado pelo supervisor para o corretor).  
Para informar os relatórios nesta tela Acesse no backoffice o módulo Gestão de Imóveis e em seguida acesse: Ambiente | Parâmetros | Gestão de imóveis | Portal de Imóveis, nesta tela apresentada preencha os campos: Nome do remetente, email do remetente e em seguida informe os relatórios conforme instruções na imagem. 

falseObs:

***As informações sobre como baixar e importar esses relatórios no sistema estão descritas nos pré-requisitos deste material.***

**2) Associando um usuário supervisor no cadastro do corretor:**

Para parametrizar um usuário supervidor para o corretor no Portal de Imóveis, siga os seguintes passos:

* Acesse no Portal de Imóveis - backend;
* Clique em "Usuários";
* Selecione o corretor que deseja parametrizar (e edite seu cadastro);
* Ao acessar o cadastro editado, informe um supervisor para o corretor no campo "supervisor".
* Certifique-se de que o corretor selecionado tenha um e-mail cadastrado no sistema;

Ao seguir esses passos, o sistema estará configurado para enviar um e-mail automaticamente para o supervisor quando uma proposta for reprovada. Isso permitirá que o supervisor tome conhecimento do status da proposta e tome as medidas necessárias para forçar a aprovação ou reprovar a proposta

## **Realizando o processo na prática:**

---

Para que o e-mail seja enviado, foi realizado pelo corretor a inclusão de uma proposta que foi salva com sua situação reprovada.   
Este exemplo abaixo demonstra um % de desconto de 5% que possibilitará esta proposta ficar reprovada;

Após validar os dados, você observará uma informação indicando que este plano encontra-se reprovado.  
Em seguida foi selecionado a opção "próximo" para que a página do "Resumo da proposta" fosse apresentada.  
  
  
Ao acessar a tela "Resumo da proposta", será exibida a opção **"Solicitar aprovação"**.   
Ao selecionar essa opção, uma tela com o nome "Observação" será aberta, permitindo que o usuário preencha uma mensagem, ao final clique em Enviar solicitação.

As informações inseridas no campo mensagem serão impressas no corpo do e-mail enviado para o supervisor responsável pelo corretor.   
Dessa forma, o supervisor terá acesso às informações relevantes sobre a proposta reprovada e poderá tomar as medidas necessárias para a aprovação da mesma.  
  
***OBS: Para configurar uma proposta para Aprovação \ reprovação de VPL acesse: [Alçada de aprovação](https://tdn.totvs.com/pages/viewpage.action?pageId=763255907)***

## **Visualizando o processo de Aprovação ou reprovação de Propostas:**

---

Após o processo de "Solicitar aprovação" (demonstrado na última imagem acima), será enviado um e-mail para o supervisor.  
  
Quando o supervisor acessar esse e-mail, veja que será disponibilizado um link de acesso à proposta. Ao clicar nesse link, o supervisor será direcionado para realizar seu login no portal de imóveis para acessar a página da proposta no sistema.

Imediatamente será acessada a tela de resumo da proposta onde o suporvisor poderá visualizar as informações da proposta e validar os dados.   
Isso permitirá que o supervisor tenha acesso fácil e rápido às informações relevantes sobre a proposta reprovada e tome as medidas necessárias para a aprovação da mesma.  
  
Ao clicar Autorizar Proposta Reprovada será apresentado o campo mensagem que após ser preenchido bastará o supervisor clicar em enviar solicitação para que o email possa ser direcionado para o corretor.

O corretor irá receber um email informando que a proposta encontra-se aprovada pelo supervisor

falseObs:

***Caso o Supervisor acesse novamente o Link para aprovação da Proposta (no momento da realização do processo) o sistema irá informar para o mesmo que a proposta já encontra-se aprovada conforme imagem:***
