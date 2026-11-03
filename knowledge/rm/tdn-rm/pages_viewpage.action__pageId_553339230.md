---
content_hash: 8a4962db20be1c2b247bf067b157857bc1640305014b51b58762400a56be5a46
fetched_at: '2026-06-29T00:10:45.768171+00:00'
page_id: '553339230'
product: rm
source: tdn-rm
title: RascunhosProcesso de GCAD | Manual - Publicador de Pacotes - Versão Usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553339230
version: 1
---

5%90%

topo

Esse documento tem o objetivo de auxiliar a utilização do Publicador de Pacotes Manual.

## **Navegue pelos tópicos do índice abaixo:**

## **Introduçãointroducao**

Link do Publicador: **<https://suporte.totvs.com/portal/p/10098/totvs-publicador-de-pacotes>**

A publicação de pacotes na Central de *Downloads* é realizada pela área de GCAD ou time de engenharia local.

A conclusão da issue de Desenvolvimento no JIRA deve ser realizada por esses times e estes usuários devem estar configurados no papel de Analista de GCAD nos projetos do produto.

Para os times que usam API ou robô para expedição automática, é necessário criar um usuário no AD com acesso ao JIRA (liberado pela TI), e configurar este usuário com papel de Analista de GCAD para a expedição do pacote.

Para configurar o usuário com papel Analista de GCAD no JIRA, consulte o passo a passo na documentação: **[EC - JIRA - Incluir um usuário em um papel específico do meu Projeto](https://atendimento.totvs.com/hc/pt-br/articles/360012885511-EC-JIRA-Incluir-um-usu%C3%A1rio-em-um-papel-espec%C3%ADfico-do-meu-Projeto?source=search "Follow link")**

Não há um padrão estabelecido corporativamente para a descrição dos pacotes na Central de *Downloads*, o mais comum é **data-descrição\_do\_patch-versao**, permitindo que o cliente consiga identificar de forma que fique claro para o cliente do que se trata o correção ou release.

## **Acessoacesso**

Caso não tenha acesso ao Publicador de Pacotes (**<https://suporte.totvs.com/portal/p/10098/totvs-publicador-de-pacotes>**) é necessário abrir ticket através de envio de e-mail para **[ti@totvs.com.br](mailto:ti@totvs.com.br)**, informando a necessidade de acesso ao Publicador e informando a Linha, no qual terá atuação.

## **Estrutura Publicador de Pacotespublicador\_pacotes**

A estrutura Macro do Publicador de Pacotes segue a hierarquia abaixo:

## **responsabilidades**

### **Responsabilidades da criação de cada estrutura**

| **Estrutura** | **Responsável** | **Meio** |
| --- | --- | --- |
| Linha de Produto | TI | Abertura de ticket para **[ti@totvs.com.br](mailto:ti@totvs.com.br)** |
| Versão | Ciclo de Vida | Abertura de ticket para **[ciclodevida@totvs.com.br](mailto:ciclodevida@totvs.com.br)** |
| Ambiente | GCAD | GCAD responsável por cada produto |

## **Publicaçãopublicacao**

Acessar o link **<https://suporte.totvs.com/portal/p/10098/totvs-publicador-de-pacotes>**

Clicar em Pacote / Adicionar Pacote:

Campos e Tela “**Adicionar Pacote**”:

Campos destacados em **Vermelho**, são de preenchimento **obrigatório**, sendo alguns necessário atenção em seu preenchimento devido regra do Publicador de Pacotes.

**Campos:**

**Linha:** Escolher na lista a Linha desejada.

**Cód. Cliente:** Digitar o código do cliente.

Valor “0” como código significa que ficará disponível para TODOS os clientes.

**Cód. Arquivo:** Obrigatório ser o mesmo nome do arquivo a ser Publicado, com letras maiúscula, inclusive a extensão do arquivo.

**Nome do Arquivo:** Campo livre para preenchimento de acordo com necessidade.

**Descrição:** Campo livre para preenchimento de acordo com necessidade.

**Caminho do Arquivo:**

O caminho do arquivo deve ser **todo em maiúsculo**.

O nome do diretório FTP criado por TI já é a raiz no caminho a ser informado, seguido do nome do arquivo.

Ex.: Diretório criado PLATAFORMAFISCALVAREJO, logo o caminho será /PLATAFORMAFISCALVAREJO/PACOTEVERSAOWXYZ.TXT

**Tamanho Arquivo:** Informar o tamanho **EXATO** do arquivo em **bytes**

**Caminho Doc. Técnica:** Campo livre para preenchimento de acordo com necessidade.

**Dt. Publicação:** Data da Publicação.

**Dt. Expiração:** Data de Expiração da Publicação.

**Tipo:** Preencher conforme necessidade.

**Plataforma:** Preencher conforme disponibilidade.

**Categoria:** Preencher conforme necessidade e disponibilidade.

**Idioma:** Preencher conforme necessidade e disponibilidade.

**Versão:** Preencher conforme disponibilidade.

**Ambiente:** Preencher conforme disponibilidade.

Exemplo da tela preenchida:

Após os campos serem preenchidos corretamente, conforme instruções acima e clicar em Salvar, será gerado o link pacote.

Exemplo da telas abaixo:

Exemplo de link do pacote gerado: **<https://suporte.totvs.com/portal/p/10098/download?e=771085>**)

Exemplo da tela do link:

## **criacao\_ambiente**

## **Criação de Ambiente**

Acessar o link **<https://suporte.totvs.com/portal/p/10098/totvs-publicador-de-pacotes>**

Clicar em Ambiente / Novo Ambiente:

Preencha os campos e clique em Salvar.

Atenção ao preenchimento do campo **Código.** O valor deste campo será utilizado para a publicação automática de pacotes (webservice).

Um novo Ambiente também pode ser criado a partir de um cadastro já efetuado. Nesse caso, clique em Ambiente, selecione um ambiente previamente criado e clique em Copiar/Clonar .

Altere os campos com as informações do novo Ambiente e clique em Salvar.

**Importante**: é imprescindível o correto preenchimento do campo **Código**, pois o valor deste campo será utilizado para a publicação automática de pacotes (webservice).

5%
div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.expand-control-text {
color: #000000;
font-size: 13px !important;
font-weight:bold !important;
}
.expand-icon, .aui-icon, .aui-icon-small, .aui-iconfont-chevron-right {
color: #FF8000;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
