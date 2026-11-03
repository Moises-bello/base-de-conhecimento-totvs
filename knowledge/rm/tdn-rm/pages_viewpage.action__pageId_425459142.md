---
content_hash: a97c3a858c60456ecbb06c7ed8bd96af04164dbd825132ab2decc4eb51495e9c
fetched_at: '2026-06-29T00:09:34.106678+00:00'
page_id: '425459142'
product: rm
source: tdn-rm
title: Módulo de Diplomações / Certificações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459142
version: 55
---

---

# **Descrição**

Este módulo contempla toda a parte de gerenciamento de diplomas e emissão dos mais diversos certificados, como por exemplo: Certificados de Extensão, Competência, Controle das solenidades da formatura.

É possível emitir um certificado de duas formas: via cadastro manual aluno por aluno ou via processo para vários alunos. É importante frisar que os certificados possuem  como emitido, não emitido, não retirado, anulado e cancelado.

## Emissão manual de certificado

A emissão de certificado para um aluno de forma manual é feita via cadastro, localizado no menu Atividades Acadêmicas | Certificados. Nesta tela é possível emitir um certificado para o aluno de forma manual, basta preencher os campos pertinentes à emissão e salvar.

O campo "Nome do aluno" serve para armazenar o nome do aluno no momento do cadastrado ou geração do certificado/diploma. Portanto ele nunca poderá ser alterado. Se houver mudança nesse nome no cadastro do aluno, deverá ser feita uma nova geração do certificado/diploma.

Os tipos de certificados disponíveis são os listados abaixo.

| Ensino Superior | Ensino Básico |
| --- | --- |
|  |  |

Nesta tela possui a aba **d****ados do** **certificado**, válido apenas para o **ensino superior**, que contém os dados do registro em livro, conforme é mostrado abaixo. É possível informar se irá registrar no livro ou não. Se efetuar o registro, os campos: livro, número do processo, as instituições e a data de registro são obrigatórios o seu preenchimento, caso não deseje registrar em livro os campos: número do processo, as instituições e a data de registro **não** são obrigatórios.

Vale lembra que a tabela **SREGISTROLIVRO** não é mais utilizada para armazenar os dados referente ao registro do livro, a tabela **SCERTIFICADO** que armazena estes campos.

#### Tipos de certificado

##### Certificado

Utilizado para geração de certificado manual para o aluno, pessoa, ou professor.

A partir da versão **12.1.2310**na aba **Dados do certificado** os campos **Instituição de registro e Instituição de emissão** passa a ter um comportamento diferente conforme abaixo.

Se for inserir um registro novo estes campos ficarão somente leitura e serão preenchidos automaticamente pela **Instituição do MEC**, que é definida nos parâmetros da [secretaria](https://tdn.totvs.com/display/LRM/Secretaria#Secretaria-Secretaria7/7:Par%C3%A2metrosGerais).  
Se for editar este campo também irá seguir a regra acima caso os campos estiverem vazios, se já tiverem sido preenchido por uma  nada mudará para estes campos.

O intuito desta implementação é unificar as instituições registradora e emissora nos certificados e diplomas, não sendo necessário ter a instituição do MEC e instituição de ensino com os mesmos valores. Vale ressaltar que instituição emissora e registradora sempre é a própria instituição, que chamamos de instituição do MEC.

Vale ressaltar que o campo da instituição do MEC não é persistido no banco de dados, ele é carregado automaticamente no lugar do campo da  conforme regras acima.

A instituição do MEC está disponível em Atividades Acadêmicas | Censo | Instituição do MEC.

##### Diploma

Para a geração de **diploma** esta aba passa a exibir as informações da IES registradora caso a  esteja parametrizada para registro em outra IES.

Com isso os campos IES Registradora, Código do livro, Nº de registro e folha do registro no livro da IES registradora passa a atualizar os campos do curso/habilitação do aluno na aba diploma.

Mas se não for para registrar em outra IES será disponibilizado os seguintes campos abaixo.

Caso o registro em outra IES não tenha sido definido na  uma mensagem de alerta será exibida informando a necessidade desta parametrização. É importante definir este para geração de diplomas, pois caso não defina o sistema vai entender que não é para registrar em outra IES o diploma.

A partir das versões **12.1.2205.275, 12.1.2209.232, 12.1.2302.154, e 12.1.2306**, foi incluída a aba "Informações adicionais (apostilamento, ato regulatório)" no cadastro de Certificado/Diploma (disponível apenas para nível de Ensino Superior) com o respectivo campo para adição dessa informação que será utilizada no processo de geração de Diploma Digital.

Esse campo só está disponível no cadastro de Certificado/Diploma, não sendo possível inserir essa informação através do processo de Geração em lote de Certificados/Diplomas/Solenidades.

Também foram disponibilizados novos campos no cadastro de Curso do MEC (campos: Nome da Habilitação e Ênfase), para centralizar essas informações que são utilizadas no processo de geração de Diploma Digital. Para mais detalhes dessa melhoria, .

A partir da versão **12.1.2310**na aba **Dados do certificado** os campos **Instituição de registro e Instituição de emissão** passa a ter um comportamento diferente conforme abaixo.

Se for inserir um registro o campo **instituição de registro** é condicionado ao campo de **registro em outra IES**na , ou seja, se for registrado em outra IES o campo **instituição de registro** ficará disponível para seleção das , porém se não for registrado em outra IES, este campo ficará somente leitura e o mesmo será preenchido automaticamente pela **Instituição do MEC**, que é definida nos parâmetros da [secretaria](https://tdn.totvs.com/display/LRM/Secretaria#Secretaria-Secretaria7/7:Par%C3%A2metrosGerais). Já o campo **instituição de emissão**ficará somente leitura e será preenchido automaticamente pela **Instituição do MEC**, que é definida nos parâmetros da [secretaria](https://tdn.totvs.com/display/LRM/Secretaria#Secretaria-Secretaria7/7:Par%C3%A2metrosGerais).  
Se for editar estes campos também irão seguir a regra acima caso os campos **instituição de registro e emissão** estiverem vazios, se já tiverem sido preenchidos por uma  nada mudará para estes campos.

O intuito desta implementação é unificar as instituições registradora e emissora nos certificados e diplomas, não sendo necessário ter a instituição do MEC e instituição de ensino com os mesmos valores. Vale ressaltar que instituição emissora sempre é a própria instituição, que chamamos de instituição do MEC e instituição registradora para certificados também é a própria instituição (instituição do MEC) e para diplomas irá depender do campo **registro em outra IES**na , se não for registrado também é a própria instituição (instituição do MEC), se for registrado em outra IES será um outra instituição que é cadastrada em .

Vale ressaltar que o campo da instituição do MEC não é persistido no banco de dados, ele é carregado automaticamente no lugar do campo da  conforme regras acima.

A instituição do MEC está disponível em Atividades Acadêmicas | Censo | Instituição do MEC.

## Emissão em lote de certificados via processo

A emissão de certificados em lote é feito via processo, localizado no menu Atividades Acadêmicas | Certificados | Sub menu Geração de Certificados. Para mais informações sobre esta geração .

# **Validações na emissão de certificados**

Na geração de certificado/diploma somente será possível gerar certificados com matriz aplicada diferente da existente para aluno. O mesmo vale quando a geração é para o estágio, ou seja, apenas para termos de compromissos diferentes. Caso o certificado não possua matriz aplicada e o mesmo não é referente à um estágio, também somente poderá possuir um gerado. Entretanto, se os certificados existentes estiverem **anulados**, será possível gerar outro com a mesma matriz aplicada, para o mesmo tipo de estágio (termo de compromisso) e para o mesmo que não possui matriz aplicada e não é referente a um estágio.

Vale lembrar que existe um parâmetro, localizado em Configurações | Parâmetros | Secretaria | Geral 2, chamado **gerar um novo certificado para o aluno, que já possui certificado registrado para a mesma habilitação filial**, caso este parâmetro estiver marcado também será possível gerar outro certificado para a mesma matriz aplicada mesmo possuindo outro certificado **não anulado**.

Na geração de certificado/diploma somente será possível gerar certificados de atividades ofertadas diferentes para aluno,  professor ou pessoa. Se existirem certificados anulados será possível gerar outro certificado para a mesma atividade ofertada.

---

Como Fazer

 Veja Também

---
