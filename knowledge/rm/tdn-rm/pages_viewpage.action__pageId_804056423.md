---
content_hash: c6d058177b9d22572454492164ab4196cbdff6d535e0521e0b4081cebfdabce9
fetched_at: '2026-06-29T00:11:43.367624+00:00'
page_id: '804056423'
product: rm
source: tdn-rm
title: 04 -  API - Preenchimento da Ficha Médica do candidato no TOTVS Processo Seletivo.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=804056423
version: 45
---

# Sumário

---

Sumário

# Objetivo

---

Este documento tem como objetivo exemplificar a forma de utilização da API de preenchimento da ficha médica do candidato no **TOTVS Processo Seletivo**.

Esta API possibilita incluir, atualizar ou acessar a ficha médica do candidato do **TOTVS Processo Seletivo**.

É importante ressaltar que neste modelo o aplicativo RM.Host é responsável por hospedar e expor os serviços de APIs. Veja mais sobre a [configuração clicando aqui](https://tdn.totvs.com/display/LRM/Configurando+HttpPort+e+ApiPort). 

**Recurso disponível a partir da versão 12.1.2402.**

# Pré-requisitos

---

* **Permissão**

Por questão de segurança e rastreabilidade, as requisições serão permitidas somente para um usuário cadastrado no RM, portanto é necessário conceder as devidas permissões apara o perfil do usuário que irá executar as requisições.

* **Parâmetros**

O **TOTVS Processo Seletivo** irá considerar as parametrizações referentes ao termo de consentimento de uso de imagem e voz que foram definidas no **TOTVS Educacional**, para maiores informações [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=790644488).

* No **TOTVS Processo Seletivo**, é necessário indicar que a utilização da ficha médica está habilitada para o processo seletivo. A configuração deve ser realizada em "Edição de Processo Seletivo" > Parâmetros > Matrícula > Confirmação Matrícula > **Utiliza ficha médica flexível**. Para maiores informações acesse .

Caso o parâmetro não esteja marcado, as chamadas para as APIs da ficha médica **GET**, **POST** e **PUT,**devem ter as seguintes informações no seu retorno:

# Dicas

---

A construção do modelo da ficha médica que será utilizada é realizada no **TOTVS Educacional**, no TOTVS Educacional será permitido definir um único modelo ativo por contexto, ou seja, o modelo que estiver ativo naquele contexto será o modelo disponibilizado para preenchimento em todo o RM (Portal do aluno, Portal Gestão Educacional ou Portal do TOTVS Processo Seletivo).

Para conhecer mais sobre a criação de modelos [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=799265605).

Para ter acesso a estrutura do modelo ativo e que será utilizado pela API de preenchimento da ficha médica, orientamos consumir a API abaixo:

**Máscara de Url:**  http://{domínio}:{porta}/api/educational/v1/medicalrecord/templates/{Id. Modelo}?Expand=wrapper,section,field

**Exemplo de configuração:**

**Domínio:** localhost

**Porta:** 8051

**Expand=wrapper,section,field**: indica que a requisição ira retornar os agrupadores, seções e campos.

**Id. Modelo:** Identificador do modelo da ficha médica que está ativo no contexto.

**Url Utilizada: [http://localhost:8051/api/educational/v1/medicalrecord/templates/9?Expand=wrapper,section,field](http://localhost:8051/api/educational/v1/medicalrecord/templates/5?Expand=wrapper,section,field)**

Ver resultado JSON...js1Resultado Positivo (JSON)true

# 1 - Métodos

---

      Serão apresentados 3 métodos, os quais foram implementados na API do Termo, são eles:

* GET ( Retorna a ficha médica cadastrada)
* POST (Cria nova ficha médica)
* PUT (Atualiza informações da ficha médica)

# 1.1 - GET (Retorna a ficha médica cadastrada)

---

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/ApplicantRegistries/{**Cód. da Coligada**}|{**Id. Processo Seletivo**}|{**Cód. Usuário PS** }/medicalRecord/{Id. Ficha Médica}?BranchCode={**Cód Filial**}&LevelEducationCode={**Nível de ensino**}&ResponsibleApplicantCode={**Cód. Usuário PS responsável pela operação**}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Cód. Coligada: 1,  Id. Processo Seletivo: 161, Cód. Usuário PS: 386, Id. Ficha Médica:-1, Cód. Filial: 1, Nível de Ensino:1, Cód. Usuário PS Responsável pela atualização:26**

**Url Utilizada:****<http://localhost:8051/api/educational/v1/ApplicantRegistries/1|161|386/medicalRecord/-1?BranchCode=1&LevelEducationCode=1&ResponsibleApplicantCode=26>**

Id. Ficha Médica

"Id. Ficha Médica" se passado -1 o sistema retornará  a ficha médica do modelo que esta ativo, caso contrário deverá ser passada o Id. Ficha médica do candidato (tabela SFICHAMEDICAPESSOA)

O cadastro do campo é global, ou seja, um mesmo campo cadastrado poderá ser utilizado em outros contexto ou em vários modelos do mesmo contexto.

Por exemplo: Campo cadastrado "**Qual é o seu tipo sanguíneo?**", esse mesmo campo poderá ser adicionado em outros modelos de outros contexto ou do mesmo contexto.

É importante ressaltar que o campo nasce global de forma nativa, e permite que  a informação preenchida pelo aluno também seja global, por exemplo, se o aluno preencher o campo "**Qual é o seu tipo sanguíneo?**" na ficha médica da filial 01, e depois se esse aluno for transferido para a filial 02, e a ficha médica da filial 02 usar o mesmo campo no seu modelo de ficha médica, essa informação já vai estar preenchida na ficha médica da filial 02.

O mesmo aproveitamento acontecerá, no seguinte cenário: o usuário realiza a cópia da ficha médica "**X**" para o mesmo contexto, passando a ter a ficha médica "**X Cópia**". Na sequência inativa a ficha médica "**X**",  ativa a ficha médica "**X Cópia**" e acrescenta alguns novos campos, com isso quando o aluno acessar a ficha médica o sistema vai mostrar a ficha médica ativa "**X Cópia**" e carregara os campos já preenchidos pelo aluno.

Considerando os cenários acima, podem existir casos que para o **modelo ativo no TOTVS Educacional**, o candidato ainda não possua nenhuma ficha médica preenchida, no entanto existem campos associados a esse modelo que já foram preenchidos pelo candidato em outro momento através de outro modelo, neste caso a ficha médica será retornada com os campos que já estão preenchidos e o idMedicalRecord será igual a  -1 indicando que será uma nova ficha médica.

Resultado - Usuário não cadastrado

Caso o usuário não possua nenhum ficha médica cadastrada (para o modelo ativo no RM) será retorno um objeto vazio conforme o exemplo abaixo:

**idMedicalRecord: -1** = Indica que deverá ser incluída uma nova ficha médica.

**idModel** = Sempre retorna o id. modelo que esta ativo no **TOTVS Educacional.**

js1Resultado (JSON)trueVer resultado JSON...js1Resultado (JSON)trueInformações complementares

É importante ressaltar que se um candidato já for aluno (possuir vinculo com a tabela de Pessoa) a ficha médica do candidato é a mesma do aluno, ou seja, qualquer alteração na ficha médica do candidato automaticamente reflete na ficha médica do aluno (estará alterando a mesma ficha).

# 1.2 - POST (Criar uma nova ficha médica)

---

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/ApplicantRegistries/{**Cód. da Coligada**}|{**Id. Processo Seletivo**}|{**Cód. Usuário PS** }/medicalRecord/?BranchCode={**Cód Filial**}&LevelEducationCode={**Nível de ensino**}&ResponsibleApplicantCode={**Cód. Usuário PS responsável pela operação**}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Cód. Coligada: 1,  Id. Processo Seletivo: 161, Cód. Usuário PS: 386**

**Url Utilizada:****[http://localhost:8051/api/educational/v1/ApplicantRegistries/1|161|386/medicalRecord/](http://localhost:8051/api/educational/v1/ApplicantRegistries/1|161|386/medicalRecord/-1?BranchCode=1&LevelEducationCode=1&ResponsibleApplicantCode=26)**

falseExemplo de EntradaVer resultado JSON...

Importante:

**idModel**: deve ser informado o id. modelo que esta ativo para o contexto.

js1Resultado (JSON)truefalseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

# 1.3 - PUT (Atualiza informações da ficha médica)

---

**Máscara de Url:** http://{domínio}:{porta}/api/educational/v1/ApplicantRegistries/{**Cód. da Coligada**}|{**Id. Processo Seletivo**}|{**Cód. Usuário PS** }/medicalRecord/{Id. Ficha Médica}?BranchCode={**Cód Filial**}&LevelEducationCode={**Nível de ensino**}&ResponsibleApplicantCode={**Cód. Usuário PS responsável pela operação**}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Cód. Coligada: 1,  Id. Processo Seletivo: 161, Cód. Usuário PS: 386, Id. Ficha Médica:48, Cód. Filial: 1, Nível de Ensino:1, Cód. Usuário PS Responsável pela atualização:26**

**Url Utilizada:****[http://localhost:8051/api/educational/v1/ApplicantRegistries/1|161|386/medicalRecord/48](http://localhost:8051/api/educational/v1/ApplicantRegistries/1|161|386/medicalRecord/-1?BranchCode=1&LevelEducationCode=1&ResponsibleApplicantCode=26)**

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de ResultadoVer resultado JSON...false

**Importante:**

Serão retornados somete os campos que foram atualizado, pois quando enviamos as informações para atualização podemos enviar campos que não foram modificados, por isso é retornado somente os campos que foram atualizados.

js1Resultado (JSON)true
