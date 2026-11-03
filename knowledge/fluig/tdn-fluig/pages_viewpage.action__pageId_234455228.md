---
content_hash: 2ee6f8fb041af43894ae60a4e18f7bd7f188de4b3023005da022c5993f7b7115
fetched_at: '2026-06-28T21:35:21.502700+00:00'
page_id: '234455228'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Aplicativos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=234455228
version: 21
---

.\*ndice

# Falando de aplicativo...

---

A plataforma possibilita abrir qualquer tipo de aplicativo, como: Word, Excel, browsers de navegação como também ERPs como Protheus, EMS, Logix.

Para que a plataforma permita o acesso a diversos aplicativos, é necessário que eles estejam previamente cadastrados e parametrizados na plataforma.

O primeiro passo para a utilização de aplicativos dentro da plataforma é definir as informações do adapter que será necessário para a execução do aplicativo e sua linha de comando para execução. Já no segundo passo, são definidos os parâmetros do aplicativo. A definição desses parâmetros permite que a plataforma envie informações que permitam acesso ao aplicativo, como, por exemplo, usuário e senha, definição de diretório de trabalho, etc.

Importante!

Devido a necessidade de execução de applets, este recurso não tem seu funcionamento como esperado. Os applets são uma tecnologia depreciada e por este motivo foram descontinuados pelos navegadores no geral.

## Ver aplicativos

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Parâmetros técnicos**.

**03**. Clique em  **Aplicativos**.

**04.** Veja os aplicativos existentes.

## Adicionar aplicativo

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Parâmetros técnicos**.

**03**. Clique em  **Aplicativos**.

**04.** Clique em **Adicionar**.

**05.** Insira o código do aplicativo que deseja incluir.

#f2f2f2#f2f2f2Todos os campos devem ser preenchidos. É pré-requisito de um aplicativo o cadastro de um adapter para ele.

**06.** Insira a descrição do aplicativo que deseja incluir.

**07.** Selecione o adapter.

**08.** Insira a linha de comando.

#f2f2f2#f2f2f2Nesse campo devem ser informados os comandos necessários para a execução do aplicativo.Inserir a linha de comando do aplicativo para definir parâmetros que serão substituídos pelos valores informados no cadastro de parâmetros. Os parâmetros devem ser definidos no formato {$PARAM\_Nome do Parâmetro} e devem ser cadastrados na aba "Parâmetros".Parâmetros variáveis do Fluig podem ser utilizados para a linha de comando também como para o valor de um parâmetro cadastrado. 

**09.** Na tabela **Parâmetros**, clique em **Adicionar**.

**10.** Insira o nome do parâmetro que deseja incluir.

**11.** Insira o valor para o parâmetro que está sendo incluído.

#f2f2f2#f2f2f2

Inserir o conteúdo a ser assumido pelo parâmetro. Esse conteúdo pode ser um valor diretamente fixo ou uma variável de ambiente do Fluig. 

**12.** Assinale se deve ter variável por usuário.

#f2f2f2#f2f2f2Quando assinalado, determina que o parâmetro é variável por usuário, permitindo ao usuário a possibilidade de entrar com o cadastro dos valores desse parâmetro. Essa configuração pode ser alterada na funcionalidade Parâmetros do Usuário em Preferências do Usuário. 

**13.** Assinale se deve ter formato para senha.

#f2f2f2#f2f2f2Quando assinalado, determina que o parâmetro será solicitado em tela no formato de senha, sem que o valor do mesmo seja apresentado em tela.

**14.** Clique em **OK**.

**15.** Clique em **Salvar**.

#f2f2f2#f2f2f2Os aplicativos são utilizados na inclusão de documentos aplicativos, na importação de menu Fluig, tendo um campo para selecioná-lo.

## Editar aplicativo

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Parâmetros técnicos**.

**03**. Clique em  **Aplicativos**.

**04.** Selecione o aplicativo que deseja editar.

**05.** Clique em **Editar**.

**06.** Altere as informações do cadastro do aplicativo.

#f2f2f2#f2f2f2Não é permitido alterar o código do aplicativo.

**07.** Clique em **Salvar**.

## Excluir aplicativo

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Parâmetros técnicos**.

**03**. Clique em  **Aplicativos**.

**04.** Selecione o aplicativo que deseja excluir.

**05.** Clique em **Remover**.

**06.** Clique em **OK**.

Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
