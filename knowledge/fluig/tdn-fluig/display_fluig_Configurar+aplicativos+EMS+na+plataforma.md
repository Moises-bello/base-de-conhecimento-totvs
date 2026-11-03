---
content_hash: 47d9e1c709d7812c581ac024a1f87d31f05931f27b421ba206faf46c4fad3942
fetched_at: '2026-06-28T21:35:29.393196+00:00'
page_id: '74645637'
product: fluig
source: tdn-fluig
title: Configurar aplicativos EMS na plataforma
type: documentation
url: https://tdn.totvs.com/display/fluig/Configurar+aplicativos+EMS+na+plataforma
version: 29
---

# Índice

true.\*ndicenone

Atenção!

Devido a necessidade de execução de applets, este recurso não tem seu funcionamento como esperado. Os applets são uma tecnologia depreciada e por este motivo foram descontinuados pelos navegadores no geral.

### Configuração de Aplicativo EMS no TOTVS Fluig Plataforma

---

Para executar os programas do EMS é necessário configurar o Adapter e Aplicativo.

### Cadastrando o Adapter

---

Primeiro, é necessário cadastrar um adapter que utilize o arquivo emshradapter.jar. Para isso somente é necessário adicionar um novo adapter e no campo Arquivo JAR informar o trecho abaixo:

A funcionalidade ***Adapter*** está disponível no menu **Painel de Controle**, no agrupador **Desenvolvimento**.

### Cadastrando o aplicativo

---

Depois do adapter cadastrado, é necessário criar o aplicativo que vai executar o EMS.

Clique em adicionar e informe o código do aplicativo e descrição, selecione o adapter do EMS e no campo linha de comando informe o trecho abaixo:

Nota

Para bancos unificados deve-se criar um novo arquivo de alias, onde neste arquivo deverá ser alterado o comando RUN, informando o valor: **men/men906za.p**.

E na linha de comando do aplicativo deve ser informado o parâmetro **–p** com o caminho do novo arquivo de alias. **Exemplo abaixo:**

No cadastro do aplicativo é necessário também adicionar sete parâmetros na tabela **Parâmetros**, para incluir um parâmetro basta clicar no botão **Adicionar**.

Os parâmetros cadastrados devem ser configurados conforme tabela a seguir:

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Valor** | **Variável por Usuário** | **Formato Senha** |
| **company** | 1 (Empresa do EMS, normalmente é 1) | Não | Não |
| **ininame** | Informar o caminho do arquivo INI utilizado no atalho do EMS. Ex: \\servidor\ems\scripts\progress.ini | Opcional. Se o caminho for o mesmo para todos os usuários não há necessidade de ser variável. | Não |
| **password** | Informar a senha do usuário do EMS | Sim | Sim |
| **path\_PROGRESS** | Informar o caminho do diretório de instalação do Progress® na máquina do usuário. Exemplo: C:\dlc101b | Sim | Não |
| **pf** | Informar o caminho do arquivo PF utilizado no atalho do EMS. Ex: \\servidor\ems\scripts\ems.pf | Opcional. Se o caminho for o mesmo para todos os usuários não há necessidade de ser variável. | Não |
| **product** | Informar o produto que será executado (EMS2, EMS5 ou HR). Para o EMS2.04 usar EMS2. | Não | Não |
| **user** | Informar o usuário de acesso ao EMS | Sim | Não |

Nota

Os parâmetros devem estar com o código exatamente como descrito na coluna **Parâmetro** da tabela acima, respeitando **maiúsculas** e **minúsculas**.

Para garantir que a linha de comando está corretamente configurada, pode-se fazer um teste simples no Executar do Windows®. Substitua os parâmetros da linha de comando pelos valores reais e execute-o.

**Por exemplo, altere:**

De:Para:

### Publicando um Aplicativo

---

Para configurar um programa do EMS será necessário publicar um novo aplicativo abaixo de uma pasta.

 

Deve ser selecionado o aplicativo EMS configurado anteriormente e no campo **Parâmetros** deve ser informado a constante **Program:** com o caminho do programa EMS que será executado.

**Exemplo:**

 Publicado o aplicativo, será criado o link na pasta selecionada e ao clicar no link será aberto o programa informado nos parâmetros do aplicativo.

### Configurando os parâmetros variáveis

---

Como alguns parâmetros são variáveis, cada usuário deve acessar as **Preferências do Usuário** e configurar estes parâmetros. Por exemplo o caminho do Progress®, usuário e senha do EMS.

### Third Party Trademarks

---

JavaScript is a trademark of Oracle Corporation.

Microsoft and Windows are registered trademarks of Microsoft Corporation in the United States and/or other countries.

Java is a trademark of Oracle and/or its affiliates. Other names may be trademarks of their respective owners.

Progress and OpenEdge are trademarks or registered trademarks of Progress Software Corporation or one of its subsidiaries or affiliates in the U.S. and other countries.

Any other third party trademarks are the property of their respective owners.
