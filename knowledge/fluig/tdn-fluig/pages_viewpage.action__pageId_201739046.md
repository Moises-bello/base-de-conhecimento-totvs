---
content_hash: 799941e8f730769f62ec525623a11264ae63c6e9cb2560a7a7e38022e1c826c6
fetched_at: '2026-06-28T21:35:19.336398+00:00'
page_id: '201739046'
product: fluig
source: tdn-fluig
title: Identity | Configuração do Active Directory
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201739046
version: 49
---

4true.\*ndicenone

---

A integração do Active Directory (AD) utilizando o SmartSync possibilita que o administrador gerencie determinados recursos do AD para uma melhor experiência com os usuários de sua empresa.

# Pré-requisitos

* Possuir o SmartSync instalado, configurado e em execução, conforme instruções da documentação de [Instalação do SmartSync](https://tdn.totvs.com/x/KAAXEQ)

# Gerenciar Active Directories

No Identity, as configurações relacionadas ao Active Directory são acessadas na tela [Active Directory](https://tdn.totvs.com/x/AptUE). A tela [Gerenciar Active Directories](https://tdn.totvs.com/x/W55UE) oferece mais detalhes e opções para configuração do AD e importação de usuários.

Os usuários pendentes são aqueles enviados ao Identity pelo SmartSync, mas que ainda não foram aprovados pelo administrador para terem suas contas criadas na ferramenta.

## Status do SmartSync e Active Directory

Para cada Active Directory cadastrado, o Identity apresenta o status do SmartSync e do respectivo Active Directory configurado.

O SmartSync permite a conexão de várias instâncias do Active Directory.

Quando o SmartSync utilizado tiver a versão 3.0.4 ou posterior, o Identity apresenta duas colunas de status para cada AD local.  **[Veja a imagem](https://tdn.totvs.com/pages/viewpageattachments.action?pageId=273981019&preview=/273981019/544718566)**

Os status são verificados apenas durante o carregamento inicial da página. Para atualizá-los, o administrador deve recarregar a página ou acionar **Atualizar**.

Os possíveis status neste caso são:

falsestatusSmartSync

| Status | Descrição |
| --- | --- |
| **Disponível** | Indica que existe comunicação entre o SmartSync e o Identity. |
| **Indisponível** | Indica que não existe comunicação entre o SmartSync e o Identity. |
| **Desabilitado** | Indica que o domínio do AD em questão está com opção "*Enabled*" desmarcada nas configurações do SmartSync. |
| **Não configurado** | Indica que o AD foi cadastrado no Identity, mas está pendente a configuração do SmartSync. |

AD

| Status | Descrição |
| --- | --- |
| **Disponível** | Indica que existe comunicação entre o SmartSync e o AD. |
| **Indisponível** | Indica que não existe comunicação entre o SmartSync e o AD. |
| **Desconhecido** | Indica que não existe comunicação entre o SmartSync e o Identity ou quando o SmartSync está desabilitado. |

## Informações do Active Directory

Ao clicar no ícone  localizado no canto direito de cada linha da listagem de Active Directories, o Identity apresenta a tela com as informações referentes ao AD, conforme figura abaixo.

falseinformaçãoInformações do AD

**Token:** chave utilizada para a configuração do Active Directory no SmartSync.

**DN Raiz:** configuração do SmartSync que indica o diretório raiz utilizado para sincronização dos dados entre Identity e Active Directory.

**Servidor AD:** endereço do servidor Active Directory, conforme configurado do SmartSync.

**Tipo de diretório LDAP:** AD

**Versão do SmartSync:** informa a versão do SmartSync que está executando a sincronização entre o Identity e o Active Directory.

**Última comunicação do SmartSync:** apresenta a data e hora da última comunicação realizada entre SmartSync e Identity. O Identity identifica que o SmartSync está disponível com base no recebimento da comunicação no sentido SmartSync → Active Directory.

Imagem de ExemploObservação

É possível vincular mais de um Active Directory a uma empresa no Identity, mas caso a autenticação seja realizada através do sAMAccountName, o usuário deverá informar o domínio antes do login, separado por uma barra invertida. Por exemplo: SP01\usuario.sobrenome.

# Ativação da conta

O Identity permite que os usuários usem as credenciais do AD para fazer o acesso. Dessa forma, quando a senha do AD for alterada, o usuário não terá que lembrar de duas senhas distintas.

Para que um usuário possa usufruir do Identity, primeiramente a conta precisa ser ativada. A ativação pode ser realizada de duas formas: (1) através de um *link* enviado por e-mail ou (2) informando as credenciais (e-mail e senha) do Active Directory ao fazer o login no Identity.

Saiba mais sobre essas configurações no help [Ativação de nova conta e entrar](https://tdn.totvs.com/x/sMVUE).

 ]]>
