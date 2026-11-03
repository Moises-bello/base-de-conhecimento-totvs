---
content_hash: 91343af939ab49d57fdea4f978debd48edeb3f763598e524c952296b2ccffd51
fetched_at: '2026-06-29T00:11:49.671133+00:00'
page_id: '836072696'
product: rm
source: tdn-rm
title: Integração com WhatsApp/RD Conversas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=836072696
version: 35
---

Olá, você está na página de Integração com o WhatsApp.

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de Utilização**

PainelVisão Geral

## **VISÃO GERAL**

A integração com WhatsApp permite que o paciente possa fazer os **A****gendamentos de consultas** 100% via WhatsApp e automatizada..

Alem disso é possível configurar e agendar **Confirmações de consulta** periódicas, onde será enviado uma mensagem de confirmação ao paciente , para que ela possa confirmar ou cancelar o agendamento.

**O que é preciso para funcionar?**

1. Uma conta ativa no  **RD Conversas By Tallos,** e com numero de WhatsApp disponível para uso.
2. Um ambiente do  **RM,** de preferência usando o CLOUD da TOTVS.
   1. Para os clientes não estão em ambiente CLOUD, e preciso alinhar com o time de RD Conversas By Tallos, para mais orientações de como se comunicar com as APIs do RM.
3. {Confirmação de consulta} Será preciso um ambiente do **RM,**3 camadas.
Agendamento de consulta

## **Configurar o agendamento de consulta:**

**Premissas:**

1. Considerando que a conta e número de Whatsapp do **RD Conversas by Tallos**, esteja OK
2. Considerando que tenha um Ambiente **RM** em CLOUD e OK

Com estes pontos de premissa superados o que mais iremos precisar?

1. Importar fluxo de agendamento de consulta.
2. Apontar para meu ambiente - Trocar URLs + Token de usuário
3. Customização é possível?

## **Importar fluxo de agendamento de consulta:**

Para facilitar a implantação, já deixamos um arquivo para importação de um fluxo pré definido, desta forma otimizando o tempo de construção de todo o fluxo.

**Qual o arquivo preciso baixar?**

E preciso baixar os arquivos abaixo:

*Fluxo de agendamento de consulta: (Ultima atualização*

250  

Obs: Arquivo pode sofrer atualizações.

**Onde eu importo o fluxo, dentro do RD conversas by Tallos?**

1. Acesse a página <https://app.tallos.com.br/>(sujeito a modificação pela plataforma RD Conversas)
2. Faça Login, com suas credenciais.
3. Encontre o menu de Automação> Fluxos.(Sujeito a modificação pela plataforma RD Conversas)
4. Clique em Importar Fluxo.
5. Selecione o arquivo baixado.

Assim que importar o arquivo o fluxo irá aparecer na lista de fluxos disponíveis na lista. 

* Para que o seu fluxo já seja visível, a partir do momento que o cliente mandar um "Oi", no número disponível, basta clicar no icone , do fluxo pretendido, e informar que deseja "Aplicar no inicio", de todos canais disponíveis.

## **Apontar para meu ambiente - Trocar URLs + Token de usuário**

Agora, para que o fluxo seja direcionado e se conecte ao seu **RM**, precisamos informar as URLs de comunicação das APIs. Isso fará com que o  **RD Conversas by Tallos,** se comunique e busque as informações necessárias.

Obs: Caso não saiba qual é sua URL de comunicação, peça apoio ao time da TOTVS.

**Como trocar as URLs?**

* Clique no ícone , do fluxo pretendido.
* Irá abrir o fluxo para modificação, você pode navegar usando os comandos do mouse e botões no topo da página(sujeito a modificação pela plataforma RD Conversas)
* Encontre todos os Card(conforme exemplo), e troque onde está {Insira a informação aqui}, pela URL disponível.
* Faça isso para todos os Cards, será necessário navegar no fluxo para olhar 1 por 1.

Na caixa "POST" no final do agendamento Particular (conforme prints abaixo), devem ser incluídos na hora de implantar o fluxo, as seguintes informações, de acordo com o cadastro do ambiente do RM vinculado:

1. O código do Convênio Particular, no parâmetro “**InsuranceCompanyID”**
2. O código do Plano do Convênio Particular, no parâmetro **“InsurancePlanID**

**Como trocar o usuário?**

* Em todos os Cards, igual no exemplo anterior, onde trocamos as URLs, deve se trocar o token , no campo "Authorization"
* Para conseguir este Token, poderá pedir apoio ao time de **RD Conversas by Tallos**, ou do time da TOTVS.

Mas caso queira obter manualmente, precisamos de:

* Acessar a plataforma <https://postman.com.br/>.
* Criar uma Workspace para testes de APIs.
* Informar uma URL+ Rota, igual está configurado no **RD Conversas by Tallos.**
* Inserir usuario e senha na aba "Authorization", dentro do postman.
* E usar o recurso de Enviar do postman.
* Ao fazer isso, conferimos na Aba "Console", qual e o token de authorization, que devemos usar na plataforma  **RD Conversar by Tallos.**

## **Customização é possível?**

Sim, o  **RD conversas by Tallos,** aceita todo o tipo de modificação no fluxo, como duplicar e criação de novos fluxos.

Apenas se certifique de testar o fluxo e inserir as informações de comunicação com o as APIs do **RM** corretamente.

**Importante:** Para a utilização correta do endpoint (URL) da API de especialidades é necessário informar qual o convênio (insuranceId) utilizado para que o retorno seja o mais eficiente possível.  
Adicione &insuranceId=**ID** na URL, sendo ID o número do convênio cadastrado no sistema. 

Para saber como cada API funciona e o que configurar no  **RM** para que ela retorne corretamente, acesse a Aba de **API's RM**.

Confirmação de consulta

## **Configurar confirmação de consulta:**

**Premissas:**

1. Considerando que a conta e número de Whatsapp do **RD Conversas by Tallos**, esteja OK
2. Considerando que tenha um Ambiente **RM** em CLOUD e OK
3. O ambiente do **RM** está em 3 camadas
   1. Caso não esteja pode consultar as documentacões:

      2. <https://tdn.totvs.com.br/pages/releaseview.action?pageId=270085915>

Com estes pontos de premissa superados o que mais iremos precisar?

1. Importar fluxo de Confirmação / Cancelar agendamento
2. Apontar para meu ambiente - Trocar URLs + Token de usuário
3. Inserir parâmetros no RM
4. Executar/Programar Envio de confirmação
5. Resposta do paciente
6. Customização é possível?

## **Importar fluxo de Confirmação / Cancelar agendamento:**

Para facilitar a implantação, já deixamos um arquivo para importação de um fluxo pré definido, desta forma otimizando o tempo de construção de todo o fluxo.

**Qual o arquivo preciso baixar?**

E preciso baixar os arquivos abaixo:

*Fluxo confirma agenda: (Ultima atualização 04/06/2024)*

250

*Fluxo cancela agenda: (Ultima atualização 04/06/2024)*

250

  

Obs: Arquivo pode sofrer atualizações.

**Onde eu importo o fluxo, dentro do RD conversas by Tallos?**

1. Acesse a página <https://app.tallos.com.br/>(sujeito a modificação pela plataforma RD Conversas)
2. Faça Login, com suas credenciais.
3. Encontre o menu de Automação> Fluxos.(Sujeito a modificação pela plataforma RD Conversas)
4. Clique em Importar Fluxo.
5. Selecione o arquivo baixado.

Assim que importar o arquivo o fluxo irá aparecer na lista de fluxos disponíveis na lista. 

## **Apontar para meu ambiente - Trocar URLs + Token de usuário**

Agora, para que o fluxo seja direcionado e se conecte ao seu **RM**, precisamos informar as URLs de comunicação das APIs. Isso fará com que o  **RD Conversas by Tallos,** se comunique e busque as informações necessárias.

Obs: Caso não saiba qual é sua URL de comunicação, peça apoio ao time da TOTVS.

**Como trocar as URLs?**

* Clique no ícone , do fluxo pretendido.
* Irá abrir o fluxo para modificação, você pode navegar usando os comandos do mouse e botões no topo da página(sujeito a modificação pela plataforma RD Conversas)
* Encontre todos os Card(conforme exemplo), e troque onde está {Insira a informação aqui}, pela URL disponível.
* Faça isso para todos os Cards, será necessário navegar no fluxo para olhar 1 por 1.

**Como trocar o usuário?**

* Em todos os Cards, igual no exemplo anterior, onde trocamos as URLs, deve se trocar o token , no campo "Authorization"
* Para conseguir este Token, poderá pedir apoio ao time de **RD Conversas by Tallos**, ou do time da TOTVS.

Mas caso queira obter manualmente, precisamos de:

* Acessar a plataforma <https://postman.com.br/>.
* Criar uma Workspace para testes de APIs.
* Informar uma URL+ Rota, igual está configurado no **RD Conversas by Tallos.**
* Inserir usuario e senha na aba "Authorization", dentro do postman.
* E usar o recurso de Enviar do postman.
* Ao fazer isso, conferimos na Aba "Console", qual e o token de authorization, que devemos usar na plataforma  **RD Conversar by Tallos.**

## **Inserir parâmetros RM:**

Para funcionar a integração entre **RM** e  **RD Conversas by Tallos** e preciso inserir informações dentro do sistema para se comunicarem.

**Onde insiro os parâmetros?**

* Apenas é inserido no **RM**, dentro da plataforma do **RD Conversas by Tallos**, não e necessário.
* Os parâmetros ficam dentro de Ambiente>Parâmetros>Gestão Hospitalar>Integração WhatsApp
* Os dados devem ser obtidos junto ao **RD conversas by Tallos:**
  + Endereço base da integração
  + Endpoint
  + Token
  + ID do template(template\_message\_id)(Deve ser criado e configurado junto ao time de **RD Conversas by Tallos**)
* O dado de "Quantidade de dias anteriores a consulta", deve ser preenchido de acordo com o processo de cada cliente
  + Exemplo: Caso o cliente queira confirmar todas as agendas do dia seguinte, a data atual, então informa o numero "1", significa que vai confirmar todas as agendas 1 dia antes da data da consulta.
  + Exemplo: Caso o cliente queira confirmar todas as agendas 3 dias antes do agendamento, então informa o número "3", significa que vai confirmar todas as agendas 3 dias antes da data da consulta.
* Após todos os campos preenchidos, então basta concluir a parametrização, para salvar as informações.
* Tambem deve se alterar o fluxo dentro do  **RD conversas by Tallos**, mudando o parâmetro de ScheduleDate, para o mesmo valor que inseriu nos parâmetros do  **RM**

## **Executar/programar envio de confirmação:**

Para enviar as mensagens de confirmação por Whatsapp, e preciso agora executar ou programar o disparo do processo.

**Onde consigo executar/programar?**

* Basta ir no menu Atendimento>Outros>Integração Whatsapp
* Definir a execução, se enviar Agora, ou se programar o JOB para executar sob demanda de acordo com a parametrização escolhida.
* Ao executar, será enviado as mensagens de confirmação por Whatasapp.

**Quais agendas serão enviadas?**

* Todas as agendas que estão dentro do parâmetro de quantidade de dia informado nos parâmetros gerais.
  + Se no parametro gerais, informado o valor "1", então todas as agendas do dia seguinte serão consideradas.
* Todas as agendas que tenha numero de celular informado.
  + Caso a agenda não tenha o numero cadastrado, então não será informado.
  + Caso o número tenha algum erro onde o **RD Conversas by Tallos** não consiga mandar, também irá retornar erro
* Todas as agendas com a data de nascimento informado.
  + Dado usado para o envio da mensagem de confirmação dos dados do paciente.
  + Caso não tenha, irá dar falha ao enviar.

## **Resposta do paciente:**

o paciente tem 3 caminhos ao receber a mensagem de confirmação

1. Confirmar sua presença
2. Cancelar seu agendamento
3. Conversar com atendente

**Como o paciente confirma o agendamento?**

* Ao receber a mensagem, o paciente terá a opção **"Sim, confirmar".**
* Ao clicar, iremos exibir quais os horários do dia informado deseja confirma, para caso tenha mais de um horário no mesmo dia.
* Quando o paciente selecionar, qual a opção de confirmação, então e informado e atualizado na agenda do **RM.**

**Como o paciente cancela o agendamento?**

* Ao receber a mensagem, o paciente terá a opção **"Não, cancelar".**
* Ao clicar, iremos exibir quais os horários do dia informado deseja cancelar, para caso tenha mais de um horário no mesmo dia.
* Quando o paciente selecionar, qual a opção de cancelamento, então e informado ao usuário e retirado na agenda do **RM,** liberando o espaço da agenda.

**Como o paciente conversa com atendente?**

* Ao receber a mensagem, o paciente terá a opção **"Conversar com atendente".**
* Ao clicar, iremos direcionar ao chat para contato com um atendente humano.

## **Customização é possível?**

Sim, o  **RD conversas by Tallos,** aceita todo o tipo de modificação no fluxo, como duplicar e criação de novos fluxos.

Apenas se certifique de testar o fluxo e inserir as informações de comunicação com o as APIs do **RM** corretamente.

Para saber como cada API funciona e o que configurar no  **RM** para que ela retorne corretamente, acesse a Aba de **API's RM**.
