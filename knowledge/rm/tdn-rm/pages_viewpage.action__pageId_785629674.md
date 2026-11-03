---
content_hash: 5cd9b491a6ac023d169668a17ed40fff30be40b9ac6f996ca49e0774e61084cf
fetched_at: '2026-06-29T00:11:38.898126+00:00'
page_id: '785629674'
product: rm
source: tdn-rm
title: 05 - API Aceite / Revogação do termo de consentimento de uso de imagem e voz
  do TOTVS Processo Seletivo.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=785629674
version: 36
---

# Sumário

---

Sumário

# Objetivo

---

Este documento tem como objetivo exemplificar a forma de utilização da API de aceite / revogação do termo de consentimento de uso de imagem e voz para o **TOTVS Processo Seletivo**.

Esta API possibilita gerar ou acessar o termo de consentimento de uso e imagem e voz para o candidato do **TOTVS Processo Seletivo**,  sendo possível  também executar o aceite ou revogação do termo.

É importante importante ressaltar que neste modelo o aplicativo RM.Host é responsável por hospedar e expor os serviços de APIs. Veja mais sobre a [configuração clicando aqui](https://tdn.totvs.com/display/LRM/Configurando+HttpPort+e+ApiPort). 

O processamento do Termo pelo portal do processo seletivo utiliza o usuário **RMProcessoSeletivo** para realizar algumas operações, portanto é necessário que este usuário exista e que ele possua todas as permissões pertinentes ao Termo.

# Pré-requisitos

---

* **Permissão**

Por questão de segurança e rastreabilidade as requisições serão permitidas somente usuários cadastrado no RM, portanto é necessário habilitar para o perfil do usuário que irá executar as requisições as devidas permissões.

* **Parâmetros**

O **TOTVS Processo Seletivo** irá considerar as parametrizações referente ao termo de consentimento de uso de imagem e voz que foram definidas no  **TOTVS Educacional**, para maiores informações [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=784761852).

* **Processo Seletivo**

É necessário indicar que a utilização do termo esta habilitada para o processo seletivo. Para maiores informações acesse .

# 1 - Métodos

---

      Serão apresentados 3 métodos, os quais foram implementados na API do Termo, são eles:

* GET ( Retorna o termo do candidato)
* POST (Enviar token)
* PUT (Aceite / revogação)

# 1.1 - GET (Recuperar / Gerar termo)

---

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/ApplicantRegistries/{**Cód. da Coligada**}|{**Id. Processo Seletivo**}|{**Cód. Usuário PS** }/termUseOfImageVoice/-1?BranchCode={**Cód Filial**}&LevelEducationCode={**Nível de ensino**}&ResponsibleApplicantCode={**Cód. Usuário PS responsável pelo aceite/revogação**}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Cód. Coligada: 1,  Id. Processo Seletivo: 161, Cód. Usuário PS: 83, Cód. Filial: 1, Nível de Ensino:1, Cód. Usuário PS Responsável pelo Aceite/Revogação:26**

**Url Utilizada: <http://localhost:8051/api/educational/v1/ApplicantRegistries/1|161|83/termUseOfImageVoice/-1?BranchCode=1&LevelEducationCode=1&ResponsibleApplicantCode=26>**

Responsável 

O cód. usuário responsável pelo aceite / revogação será o código de um dos responsáveis pelo candidato tais como: pai, mãe, responsável financeiro, responsável acadêmico ou responsável pela inscrição, podendo ser também o mesmo código de usuário do candidato.

Ver resultado JSON...js1Resultado Negativo (JSON)truejs1Resultado Positivo (JSON)trueInformações complementares

**token:** quando o **TOTVS Educacional não estiver** parametrizado para enviar o token por e-mail, a requisição sempre vai retornar um token válido que deverá ser informado ao realizar o aceite ou revogação do termo de consentimento.

*Importante: o token tem um prazo default de expiração de 60 minutos, portando a partir do momento que a requisição foi executada o aceite ou revogação devem ser realizado dentro do prazo de 60 minutos, caso contrario deverá ser feito uma nova requisição para que seja retornado um novo token.*

**consentStatus:** indica o status atual do termo, sendo: **A = "Aceite", R = "Revogado" e  P = "Pendente".**

**enableOnlyAccept:** Indica que o **TOTVS Educacional** esta parametrizado para habilitar somente a opção de "**Aceite**" para o termo.

**term:** é retornado em  Base64 no formato PDF o relatório configurado no TOTVS Educacional.

É possível executar a requisição sendo retornado as informações do termo e não retornar o relatório (**"term"**) , para isso será necessário passar como parametro na requisição o item:   **includeReport = false.**

Se um candidato já possuir um termo com status igual a "**Aceito**" ou "**Revogado**" e a instituição alterar a versão do termo, ao realizar uma nova requisição o **TOTVS Processo Seletivo**identificara que houve alteração na versão e irá gerar um novo termo com status "**Pendente**" para que seja realizado um novo "**Aceite**" ou "**Revogação**".

# 1.2 - POST (Token)

---

Quando o **TOTVS Educacional** estiver parametrizado para utilizar token de segurança (mais informações [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=425459706)) , será necessário executar esta requisição para que o token seja enviado para o e-mail do usuário do responsavel pela execução do aceite / revogação.

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/ApplicantRegistries/{**Cód. da Coligada**}|{**Id. Processo Seletivo**}|{**Cód. Usuário PS** }/termUseOfImageVoice/{**GUID**}/token?BranchCode={**Cód Filial**}&LevelEducationCode={**Nível de ensino**}&ResponsibleApplicantCode={**Cód. Usuário PS responsável pelo aceite/revogação**}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Cód. Coligada: 1,  Id. Processo Seletivo: 161, Cód. Usuário PS: 83, GUID:d3c4a091-ea4c-474a-900f-f2ecd970520e,Cód. Filial: 1, Nível de Ensino:1, Cód. Usuário PS Responsável pelo Aceite/Revogação:26.**

**Url Utilizada:**<http://localhost:8051/api/educational/v1/ApplicantRegistries/1|161|83/termUseOfImageVoice/d3c4a091-ea4c-474a-900f-f2ecd970520e/token?BranchCode=1&LevelEducationCode=1&ResponsibleApplicantCode=26>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)true

ConsentStatus =  A="**Aceite**" ou R="**Revogação**".

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

Posteriormente quando for executar a requisição PUT(Aceite ou Revogação) deverá ser informado o **token** enviado para o e-mail do usuário responsável.

# 1.3 - PUT (Aceite / Revogação)

---

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/ApplicantRegistries/{**Cód. da Coligada**}|{**Id. Processo Seletivo**}|{**Cód. Usuário PS** }/termUseOfImageVoice/{**GUID**}?BranchCode={**Cód Filial**}&LevelEducationCode={**Nível de ensino**}&ResponsibleApplicantCode={**Cód. Usuário PS responsável pelo aceite/revogação**}

**GUID:** Este é o GUID que representa o identificador único do termo que foi retornado na requisição GET.

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Cód. Coligada: 1,  Id. Processo Seletivo: 161, Cód. Usuário PS: 83, GUID:d3c4a091-ea4c-474a-900f-f2ecd970520e,Cód. Filial: 1, Nível de Ensino:1, Cód. Usuário PS Responsável pelo Aceite/Revogação:26.**

**Url Utilizada:** <http://localhost:8051/api/educational/v1/ApplicantRegistries/1|161|83/termUseOfImageVoice/d3c4a091-ea4c-474a-900f-f2ecd970520e?BranchCode=1&LevelEducationCode=1&ResponsibleApplicantCode=26>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado

O resultado é basicamente o mesmo resultado da requisição GET acrescido de algumas informações complementares, tais como: data/hora do aceite ou revogação.

Ver resultado JSON...js1Resultado (JSON)trueNotificação

Ao realizar o aceite / revogação do termo será encaminhado um e-mail de notificação para instituição conforme as parametrizações definidas no **TOTVS Educacional**. Para maiores informações [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=781854473)

Se o processo seletivo estiver parametrizado para usar o termo de consentimento de uso de imagem e voz, ao realizar a matricula do candidato no **TOTVS Educacional** será obrigatório existir para o mesmo um termo com o status de **aceito ou revogado** (isto se o sistema estiver parametrizado para permitir que o termo seja revogado).
