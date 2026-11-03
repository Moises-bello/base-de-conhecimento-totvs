---
content_hash: 0946961aa5415fd3e5ddf009c9b0406122047a9b4c250e4bffafb48728aa1f34
fetched_at: '2026-06-29T00:06:10.491778+00:00'
page_id: '203763399'
product: rm
source: tdn-rm
title: ER_Integracao_Elearning_RMVitae_FluigLMS
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Integracao_Elearning_RMVitae_FluigLMS
version: 13
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** | R\_RH\_RHU008 | **IRM1** | PCREQ-7461 |
| **Requisito1** | PCREQ-7720 | **Subtarefa1** | PDR\_RH\_RHU008-18 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

    

## Objetivo

Extensão da integração de e-learning já existente entre Vitae e LMS para Fluig LMS.

## Definição da Regra de Negócio

*Está sendo estendida no TOTVS Gestão de Pessoas a integração com Sistemas de e-learning.**Atualmente a integração está disponível para EPM e LMS. Nesta versão está sendo disponibilizada a integração com Fluig LMS.*

*A nova integração tem o Identificador 1018, definido de acordo com a planilha de integrações de Framework. Um novo item estará disponível no configurador do TOTVS Integração para carregar os dados necessários, como mensagens e parâmetros.*

*Este configurador deve carregar na base de dados:*

| Tabela | O que será carregado |
| --- | --- |
| HCIntegracao | Um registro para a nova integração |
| HCTransformacao | Um registro para cada mensagem (getcourses, user, enrollment, score) |
| HCMapaIntegracao | Um registro vinculando cada mensagem à nova integração |
| HCParametros | Um registro com o parâmetro INT\_RHU\_FLUIG\_LMS\_PROFILE\_USER |

*Esta nova integração tem as seguintes características:*

*Envio de usuário:*

1. *Deve ser adotada a versão 4.003 da mensagem User.*
2. *Além de CODPESSOA, deve ser enviado CODUSUARIO.*
3. *Deve ser acrescida a informação PAPEL, contida no valor no parâmetro INT\_RHU\_FLUIG\_LMS\_PROFILE\_USER, cadastrado para a integração,*
4. *A mensagem só deve ser enviada se o ERP não estiver integrado com Identity.*

*Envio de matrícula:*

1. *Se integrado com Identity, ao invés de CODPESSOA deve ser enviado o Identificador do Identity (e-mail).*

*Retorno de notas:*

1. *No mensagem Score, ao invés de CODPESSOA, quando não integrado com Identity; caso contrário o Identificador do Identity.*
2. *Essa informação chegará no campo/elemento CODPESSOA, que deve ser tratada no recebimento.*
3. *Quando usando Identity, deve buscar o CODUSUARIO do identity e em seguida o CODPESSOA do usuário.*

**Resumo das informações trafegadas entre os sistemas**

 

GetUser

|  |  |  |
| --- | --- | --- |
| **DADO NO RM** | **CAMPO XML ORIGINAL VITAE** | **CAMPO XML TRANSFORMADO PARA ENVIO** |
| VCURSOS.CODELEARNING | <CODELEARNING> opcional | Code |

 

User

|  |  |  |
| --- | --- | --- |
| **DADO NO RM** | **CAMPO XML ORIGINAL VITAE** | **CAMPO XML TRANSFORMADO PARA ENVIO** |
| VCURSOS.CODCOLIGADA | <CODCOLIGADA> | ListOfUnit/Unit/ParentCode |
| PPESSOA.NOME | <NOME> | Name |
| PPESSOA.CODIGO | <CODPESSOA> | InternalId e Code |
| PPESSOA.EMAIL | <EMAIL> | CommunicationInformation / Email |
| HCPARAMETROS.VALORSTR (para a integração com o LMS cujo NOMECOLUNA = INT\_RHU\_FLUIG\_LMS\_PROFILE\_USER) | <PAPEL> | ListOfRoles / Role / Code |
| PPESSOA.CODUSUARIO | <CODUSUARIO> | Login |

 

Enrollment

|  |  |  |
| --- | --- | --- |
| **DADO NO RM** | **CAMPO XML ORIGINAL VITAE** | **CAMPO XML TRANSFORMADO PARA ENVIO** |
| VTREINAMENTOELEARNING. CODCOLIGADA | <CODCOLIGADA> | UnitCode e InternalId |
| VTREINAMENTOELEARNING. CODELEARNING | <CODELEARNING> | CourseInternalId |
| VTREINAMENTOELEARNING. CODPESSOA | <CODPESSOA> | UserCode e UserInternalId |
| VTREINAMENTOELEARNING. CODMATRICULAELEARNING | <CODMATRICULAELEARNING> | InternalId |

 

Score

|  |  |  |
| --- | --- | --- |
| **CAMPO XML ORIGINAL LMS** | **CAMPO XML TRANSFORMADO PARA RM** | **DADO NO RM** |
| EnrollmentInternalId | <CODCOLIGADA> | VTREINAMENTOELEARNING. CODCOLIGADA |
| EnrollmentInternalId | <CODMATRICULAELEARNING> | VTREINAMENTOELEARNING. CODMATRICULAELEARNING |
| Date | <DTMATRICULA> | VTREINAMENTOELEARNING. DTMATRICULA |
| CourseCode | <CODELEARNING> | VTREINAMENTOELEARNING. CODELEARNING |
| UserInternalId | <CODPESSOA> | VTREINAMENTOELEARNING. CODPESSOA |
| ApprovalStatus | <STATUS> | VTREINAMENTOELEARNING. STATUS |
| PreTestScore | <SCOREPRETESTE> | VTREINAMENTOELEARNING. SCOREPRETESTE |
| PosTestScore | <SCOREPOSTESTE> | VTREINAMENTOELEARNING. SCOREPOSTESTE |

 

***Configuração de integração***

*Após executar o configurador, algumas informações devem ser complementadas no RM:*

* *URL do web service*
* *Usuário e senha de autenticação*
* *Valor do parâmetro *INT\_RHU\_FLUIG\_LMS\_PROFILE\_USER**

**Funcionalidades**

**A utilização do TOTVS Gestão de pessoas continua a mesma para o usuário:**

1. **No RM, cursos e-learning devem ser relacionados com os e-elearnings do Fluig LMS.**
2. **A matrícula em e-learnings deve ser feita pelo próprio usuário no Painel de Aprendizagem.**
3. **O usuário acessa o Fluig LMS para executar os e-learnings.**
4. *Após a execução do e-learning, a nota do pós-teste é enviada para o RM.*
5. *A mensagem recebida deve ser processada na Fila de Mensagens da Integração.*
6. *O RM recebe a nota e se aprovado, o usuário recebe o requisito de acesso vinculado.*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
