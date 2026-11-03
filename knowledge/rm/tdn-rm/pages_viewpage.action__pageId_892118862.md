---
content_hash: 9def547953b6289e596a216e645d7999218ed0da8c60943d37e83cdd184aef02
fetched_at: '2026-06-29T00:12:01.277065+00:00'
page_id: '892118862'
product: rm
source: tdn-rm
title: Integração de Exames Layout TOTVS - Laboratório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=892118862
version: 16
---

SumárioVisão Geral

## **01. VISÃO GERAL**

Esse documento irá demostrar a configuração do TOTVS Saúde para realização de integração de exames laboratoriais utilizando o Layout TOTVS.

## 

Configuração da Unidade de Atendimento

## **02.****CONFIGURAÇÃO DA UNIDADE DE ATENDIMENTO**

1. Selecionar a unidade de atendimento para realizar a configuração na aba de integrações acessando o caminho Cadastros > Unidade de Atendimento clicar no botão editar do registro.

2. Selecionar a aba Integrações e na opção de **Laboratório** selecionar a opção Layout TOTVS.

Importante

A configuração de Integração é dependente do tipo da Unidade de Atendimento. Ou seja, se a unidade for de **Laboratório** e a integração estiver configurado como **Layout TOTVS** para **Diagnóstico de Imagem**, a integração não será realizada.

Configuração dos endereços de envio e cancelamento de exames

## **03.****Configuração dos endereços de envio e cancelamento de exames**

Além de atribuir o layout TOTVS na unidade de atendimento é necessário também realizar a configuração dos endereços de envio e cancelamento. Essa configuração deve se realizada no **Ambiente > Parâmetros >** **Gestão Hospitalar** no RM**.**

Seguimos o passo a passo do Assistente de Implantação de Processos. Temos dois caminhos a seguir, a parametrização de Diagnóstico de Imagem e Laboratoriais:

Clique em avançar e será apresentado à lista de processos e suas parametrizações. Dentro da opção **Unidade Diagnóstico > Integrações > Laboratoriais > Layout TOTVS - Laboratoriais**.

Na aba de configurações do Layout TOTVS, deve ser informado os **endereços de envio** e **endereço cancelamento** (se o check de **enviar cancelamento integração** estiver desmarcado ao cancelar o pedido de exame o sistema irá cancelar no RM mas não irá enviar a requisição de cancelamento, este parâmetro é utilizado nos casos onde o cancelamento é feito de forma manual sem auxilio de integração) e também o **usuário** e **senha** de autenticação. Caso a integração utilize token de autenticação o endereço de autenticação por token deve ser informado no campo **URL Token**.

Com essas configurações o sistema está apto para realizar o envio de exames laboratoriais no layout TOTVS.

Realizar a integração de Exame

## **04. REALIZAR A INTEGRAÇÃO DE EXAMES**

Com as configurações de integração definidas, a integração pode ser realizada atravez dos seguintes locais de solicitação de exames:

* **Atraves do [Pedidos de exame](https://tdn.totvs.com/display/LRM/Pedidos+de+exame#Pedidosdeexame-1906526480) no RM:**
  + Basta incluir o exame no pedido de exame no RM e o botão Finalizar ficará disponível, essa botão dispara a comunicação entre TOTVS Saúde e o endereço de envio configurado.
* **Atraves da [Solicitação de Exames na Prescrição médica](https://tdn.totvs.com/pages/viewpage.action?pageId=592306460#Solicita%C3%A7%C3%A3odeExamesnaPrescri%C3%A7%C3%A3om%C3%A9dica-1906526480) no Prontuário do Paciente:**
  + Ao incluir um exame na prescrição médica e a unidade de atendimento do exame estiver configurada para o layout totvs, ao "Liberar" a prescrição, será enviado o pedido de exame para o RM e realizado a comunicação entre TOTVS Saúde e o endereço de envio configurado;
  + Existe a configuração "Utiliza Aprazamento / Checagem" no cadastro de unidade de atendimento (Cadastros => Unidade de Atendimento => Prontuário Eletronico => Prescrição Médica), onde se estiver marcada a prescrição médica após liberada só irá enviar a solicitação de exame para o RM após realizado o aprazamento, desta forma a integração será realizada após ser liberado o aprazamento;
* **Atraves da [Solicitação de Exames](https://tdn.totvs.com/pages/viewpage.action?pageId=522009904#NovaSolicita%C3%A7%C3%A3odeExames-1906526480) no Prontuário do Paciente:**
  + Ao incluir um exame na solicitação de exame e a unidade de atendimento do exame estiver configurada para o layout totvs, ao "Finalizar" a solicitação, será enviado o pedido de exame para o RM e realizado a comunicação entre TOTVS Saúde e o endereço de envio configurado;

Nesse envio o TOTVS Saúde irá gerar uma JSON contendo as seguintes informações:

* **orders.code:**Código único de documento é composto por Código da Coligada e o Número do Pedido.
* **orders.action:**Tipo de ação que dever ser realizada (I) para **Inclusão** e ( (E) para quando é o **cancelamento do pedido.**
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

Exemplo de JSON de Envio:

250

Cadastrar os resultados de exame

## **05. CADASTRAR OS RESULTADOS DE EXAME**

Os resultados dos exames são persistidos utilizando o recurso de API do: TOTVS Saúde sendo utilizando o verbo HTTP POST e enviado para o endereço **[http://DOMINIO:PORTA/api/hcg/v2/laboratory-exams-results/layout-totvs/results](http://DOMINIOPORTA)** respeitando o layout abaixo:

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
* **exam.serviceOrder:**Número do Pedido de Exame.
* **exam.examId:**Código de Exame
* **exam.sequential:**Sequencial do Exame.
* **exam.originExamId:**Código de Exame do Sistema de Origem.
* **exam.methodDescription:**Descrição do Método Utilizado no Exame.
* **exam.results.parameterName (Lista):** Nome do parâmetro
* **exam.results.result:**Resultado do Parâmetro.
* **exam.results.unitMeasurement:**Unidade de Medida.
* **exam.results.alert:**Marcação para parâmetros em status em Pânico.
* **exam.results.comment:**Comentários sobre o parâmetro.

250

Verificar o recebimento do resultado via API  
**Utilitários** **>> Integração Monitor**
