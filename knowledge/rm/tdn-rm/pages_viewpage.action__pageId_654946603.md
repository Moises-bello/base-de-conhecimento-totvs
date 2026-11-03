---
content_hash: 83dbfd8641d1b6b4b6a0b8836260d7d2b0cb12640ad9f26c9cfe5e53be31ab48
fetched_at: '2026-06-29T00:11:12.578284+00:00'
page_id: '654946603'
product: rm
source: tdn-rm
title: Integração de Exames Layout TOTVS - Diagnóstico de Imagem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=654946603
version: 42
---

sumarioVisão Geral

## **01. VISÃO GERAL**

Esse documento irá demostrar a configuração do TOTVS Saúde para realização de integração de exames laboratoriais utilizando o Layout TOTVS.

Configuração da unidade de atendimento

## **02.****CONFIGURAÇÃO DA UNIDADE DE ATENDIMENTO**

1. Selecionar a unidade de atendimento para realizar a configuração na aba de integrações acessando o caminho Cadastros > Unidade de Atendimento clicar no botão editar do registro.

2. Selecionar a aba Integrações e na opção de **Diagnóstico de Imagem** selecionar a opção Layout TOTVS.

Importante

A configuração de Integração é dependente do tipo da Unidade de Atendimento. Ou seja, se a unidade for de **Diagnóstico de Imagem** e a integração estiver configurado como **Layout TOTVS** para **Laboratório**, a integração não será realizada.

Configuração dos parâmetros de endereços de envio e cancelamento de exames

## **03. Configuração dos parâmetros de endereços de envio e cancelamento de exames**

Além de atribuir o layout TOTVS na unidade de atendimento é necessário também realizar a configuração dos endereços de envio e cancelamento. Essa configuração deve se realizada no **Ambiente > Parâmetros >** **Gestão Hospitalar** no RM**.**

Ao abrir a o Assistente de Implantação de Processos, clique em avançar e será apresentado à lista de processos e suas parametrizações:

Temos dois caminhos a seguir, a parametrização de Diagnóstico de Imagem ou Laboratoriais. Ambas telas apresentarão os mesmos campos.

Dentro da opção **Unidade Diagnóstico > Integrações > Diagnóstico de Imagem > Layout TOTVS**.

Ao avançar, chegamos na tela com os campos da parametrização:

Explicação dos campos e seus respectivos funcionamentos:

API Envia Pedido de Exame

## **API Envia Pedido de Exame**

Aqui deve ser informado um endereço de envio (URL) válido para que o RM consiga enviar o pedido de exame.

API Cancelamento de Pedido de Exame

## **API Cancelamento de Pedido de Exame**

Aqui deve ser informado um endereço de envio (URL) válido para que o RM consiga realizar o cancelamento do pedido de exame.  Se o check de **enviar cancelamento integração** estiver desmarcado ao cancelar o pedido de exame o sistema irá cancelar no RM mas não irá enviar a requisição de cancelamento, este parâmetro é utilizado nos casos onde o cancelamento é feito de forma manual sem auxilio de integração.

**Sobre os headers das requisições:**

Para ambas as requisições acima, no header da requisição será enviado um campo com dois possíveis nomes: **token** ou **Authorization**, no qual a API deve estar preparada para receber. Exemplo abaixo:

URL Token e Usuário/Senha

## **URL Token e Usuário/Senha**

Caso a integração utilize token de autenticação o endereço de autenticação por token deve ser informado no campo **URL Token**.

Essa URL Token nada mais que é um endereço que deve ser fornecido pelo pacs para que o sistema possa enviar o usuário e senha configurado na parametrização e assim obter como resultado um token de autenticação, que o sistema vai usar posteriormente para fazer as requisições de Envio e Cancelamento.

O formato esperado para a URL Token deve ser uma URL Completa (exemplo: "[https://exemplolayouttotvs.com/auttoken](https://exemplolayouttotvs.com/auttoken%7Chttps://exemplolayouttotvs.com/auttoken)") ou uma URL relativa, caso o client esteja configurado pra isso (exemplo: "/auttoken").

Caso eu **não preencha** o URL Token, o RM entende que a autenticação usada será somente por usuário e senha, e coloca no header da requisição (no envio de pedido de exame, por exemplo) essa informação de autenticação.

Caso eu **preencha**a URL Token da maneira correta, o sistema faz a requisição para o pacs para obter esse token por meio do usuário e senha informados, e assim colocar esse token no header da requisição desejada (no envio de pedido de exame, por exemplo).

Para funcionar corretamente essa requisição de busca ao token, o cliente deve estar preparado para receber no body da requisição, os campos de **UserName e Password** (Case Sensitive), contendo justamente os dados preenchidos nos campos de usuário e senha. Exemplo abaixo:

Identificador da Integração

## **Identificador da Integração**

Campo de texto básico visual para facilitar e definir qual integração se trata a parametrização.

Com essas configurações o sistema está apto para realizar o envio de exames de imagem no layout TOTVS.

Realizar a intergração de exames

## **04. REALIZAR A INTEGRAÇÃO DE EXAMES**

Com as configurações de integração definidas, a integração pode ser realizada atravez dos seguintes locais de solicitação de exames:

* **Atravez do  no RM:**
  + Basta incluir o exame no pedido de exame no RM e o botão Finalizar ficará disponível, essa botão dispara a comunicação entre TOTVS Saúde e o endereço de envio configurado.
* **Atravez da  no Prontuário do Paciente:**
  + Ao incluir um exame na prescrição médica e a unidade de atendimento do exame estiver configurada para o layout totvs, ao "Liberar" a prescrição, será enviado o pedido de exame para o RM e realizado a comunicação entre TOTVS Saúde e o endereço de envio configurado;
  + Existe a configuração "Utiliza Aprazamento / Checagem" no cadastro de unidade de atendimento (Cadastros => Unidade de Atendimento => Prontuário Eletronico => Prescrição Médica), onde se estiver marcada a prescrição médica após liberada só irá enviar a solicitação de exame para o RM após realizado o aprazamento, desta forma a integração será realizada após ser liberado o aprazamento;
* **Atravez da  no Prontuário do Paciente:**
  + Ao incluir um exame na solicitação de exame e a unidade de atendimento do exame estiver configurada para o layout totvs, ao "Finalizar" a solicitação, será enviado o pedido de exame para o RM e realizado a comunicação entre TOTVS Saúde e o endereço de envio configurado;

Nesse envio o TOTVS Saúde irá gerar uma JSON contendo as seguintes informações:

* **orders.code:**Código único de documento é composto por Código da Coligada e o Número do Pedido.
* **orders.action:**Tipo de ação que dever ser realizada **(I)** para **Inclusão** e **(E)** para quando é o **cancelamento do pedido**.
* **orders.identification:** Identificação da origem do Pedido de Exame
* **orders.companyId:**Código da Coligada do contexto.
* **orders.serviceOrder:**Número do Pedido.
* **orders.Type:**Tipo da integração: "I" => Diagnóstico de Imagem; "L" => Laboratorial.
* **orders.serviceOrderDate:**Data da geração do Pedido de Exame composto por data e hora.
* **orders.careUnit.code:**Código Único da Unidade da Atendimento composto por Código da Coligada do contexto e Código da Unidade de Atendimento.
* **orders.careUnit.companyId:**Código da Coligada do contexto.
* **orders.careUnit.careUnitId:**Código da Unidade de Atendimento.
* **orders.careUnit.description:**Descrição da Unidade Atendimento.
* **orders.patient.code:**Código Único do Paciente composto pelo Código da Coligada do contexto e o Código do Paciente.
* **orders.patient.companyId:**Código da Coligada do contexto.
* **orders.patient.patientId:**Código do Paciente.
* **orders.patient.medicalRegistration:**Protocolo de Atendimento do Paciente.
* **[orders.patient.name](http://orders.patient.name):**Nome do Paciente.
* **orders.patient.socialName:**Nome Social do Paciente.
* **orders.patient.cpf:**CPF do Paciente.
* **orders.patient.generalRegistration:**Número da identidade do Paciente.
* **orders.patient.gender:**Sexo do Paciente.
* **orders.patient.birthDate:**Data de Nascimento do Paciente.
* **orders.patient.motherName:**Nome da Mãe do Paciente.
* **orders.patient.address:**Endereço do Paciente.
* **orders.patient.neighborhood:**Bairro do Paciente.
* **orders.patient.city:**Cidade do Paciente.
* **orders.patient.state:**Estado do Paciente.
* **orders.patient.postalCode:**
* **orders.patient.commercialPhonePrefix:**Número DDD do telefone comercial do Paciente.
* **orders.patient.homePhoneNumberPrefix:**Número do telefone do Paciente.
* **orders.patient.weight:**Peso do Paciente.
* **orders.patient.height:**Altura do Paciente.
* **orders.medicalInsurance.code:**Código Único do registro composto pelo Código da Coligada de contexto e o Código Geral do Convênio.
* **orders.medicalInsurance.companyId:**Código da Coligada do contexto.
* **orders.medicalInsurance.medicalInsuranceId:**Código Geral do Convênio.
* **[orders.medicalInsurance.name](http://orders.medicalInsurance.name):**Nome do Convênio.
* **orders.medicalInsurance.initials:**Inicial do Convênio.
* **orders.medicalInsurance.healthInsurance:**Plano contrato no Convênio.
* **orders.practitioner.code:**Código Único do Registro composto por Código da Coligada de Contexto e o Código Geral do Médico.
* **orders.practitioner.companyId:**Código da Coligada do contexto.
* **orders.practitioner.practitionerId:**Código geral do Médico.
* **[orders.practitioner.name](http://orders.practitioner.name):**Nome do Médico.
* **orders.practitioner.boardName:**Código do conselho Profissional.
* **orders.practitioner.professionalId:**Número da Identidade Profissional.
* **orders.practitioner.professionalUf:**UF da Identidade Profissional.
* **orders.attendance.code:**Código Único do registro composto pelo Código da Coligada de contexto, Código do Paciente e Código do Atendimento.
* **orders.attendance.companyId:**Código da Coligada do contexto.
* **orders.attendance.patientId:**Código do Paciente.
* **orders.attendance.attendanceId:**Código do Atendimento
* **orders.exams.code (Lista) :**Código único do Registro composto pelo Código da Coligada do contexto, Número do Pedido, Código do Exame e Sequencial do Exame.
* **orders.exams.companyId:**Código da Coligada do contexto.
* **orders.exams.serviceOrder:**Número do Pedido.
* **orders.exams.examId:**Código do Exame.
* **orders.exams.sequential:**Sequencial do Exame.
* **orders.exams.description:**Descrição do Exame
* **orders.exams.type:**Tipo do Exame, N: Normal, U: Urgência e E: Emergência.
* **orders.exams.materialCode:**Código do Material do Exame
* **orders.exams.materialDescription:**Descrição do Material do Exame.
* **orders.exams.mnemonic:**Mnemônico do Exame.
* **orders.exams.collectionDate:**Data da Coleta do Exame.
* **orders.exams.modality:** Modalidade

### Exemplo de JSON de Envio:

150

Cadastrar os resultados de exame

## **05. CADASTRAR OS RESULTADOS DE EXAME**

Os resultados dos exames são persistidos utilizando o recurso de API do: TOTVS Saúde (para configuração e ativação das API's, ), sendo utilizando o verbo HTTP POST e enviado para o endereço [http://DOMINIO:PORTA/api/hcg/v2/laboratory-exams-results/layout-totvs/results](http://DOMINIOPORTA)

Há uma distinção no formato de envio do json entre exames de imagem e laboratoriais. Naturalmente, exames de imagem não exigirão o preenchimento dos campos de resultado e valores de referência no exame, enquanto para exames laboratoriais há essa exigência.

### Para exames de imagem, o formato do json deve ser respeitado conforme o exemplo abaixo:

150

### Já para exames de laboratório, o formato do json deve ser respeitado da seguinte maneira:

150

Explicação breve dos campos do json:

* **companyId:**Código da Coligada do contexto.
* **resultId:** Código Único do Resultado.
* **identification:**Identificação da origem do Pedido de Exame
* **processingDate:**Data de Processamento
* **resultOrigin:**Origem do Resultado.
* **action:**Tipo de ação que dever ser realizada (I) para Inclusão
* **patientId:**Código do Paciente.
* **originPatientId:**Código do Paciente no Sistema de Origem.
* **originServiceOrder:**Número do Pedido na Ordem de Serviço.
* **attendanceId:**Código do Atendimento.
* **originAttendanceId:**Código do Atendimento de Origem.
* **base64Content:** Conteúdo em Base64
* **exam**: Informações do exame
* **results:** Resultados do exame laboratorial, com campos especificando o nome do parâmetro, resultado, unidade de medida, urgência, possível comentário e valores de referência.
* **referenceValues:** Valores de referência do exame laboratorial, com campos especificando o tipo do valor, o valor em si e o valor inicial e final caso haja.

Verificar o recebimento do resultado via API  
**Utilitários** **> Integração Monitor**
