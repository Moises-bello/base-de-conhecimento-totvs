---
content_hash: c67cc0328d3823ef581a4ad321e658dfea32e263be91d1b21a2bcab8c79c8953
fetched_at: '2026-06-28T21:35:25.062529+00:00'
page_id: '273981019'
product: fluig
source: tdn-fluig
title: Identity | Gerenciar Active Directories
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Gerenciar+Active+Directories
version: 85
---

# Falando de gerenciar Active Directories...

---

O Identity suporta a vinculação do Active Directory para importação de contas e autenticação via credenciais do AD.

A sincronização de usuários entre a empresa do Identity e o Active Directory é realizada através de uma aplicação chamada SmartSync. Os procedimentos de instalação e configuração estão disponíveis em [SmartSync](https://tdn.totvs.com/x/VIs0DQ).

Os usuários importados a partir da integração entre o Active Directory devem ser aceitos pelo administrador para que o seu acesso à empresa no Identity seja permitido. Consulte [Aceitar Usuários Pendentes](https://tdn.totvs.com/x/1L1UE) para obter informações sobre a configuração e utilização deste recurso.

Gerenciar Active Directories

## Gerenciar Active Directories

---

**01.** Acessar as configurações  e selecionar a opção **Active Directory**.

**02.** Na seção **Gerenciar Active Directories**, acionar o link **Gerenciar Active Directories**.

## Adicionar Active Directory local

---

**01**. Acessar o **Gerenciamento do Active Directory** conforme item .

**02.** Acionar **Adicionar** e selecionar a opção**Active Directory local**.

**03.** Em **Nome**, preencher o nome do diretório.

**04.** Definir se o aceite automático de usuários deve ser habilitado para este diretório.

#f2f2f2#f2f2f2

**Sim:** Ao habilitar essa opção, todos os usuários importados deste Active Directory pelo SmartSync serão aceitos e provisionados automaticamente nesse contexto do Identity.

**Não:** Ao manter a opção desabilitada, todos os usuários importados deste Active Directory pelo SmartSync serão incluídos na lista de Pendentes até que sejam manualmente aceitos para o contexto pela administração da empresa.

**05.** Acionar **Avançar.**

**06.** Acionar  para copiar o token de configuração do Active Directory.

#f2f2f2#f2f2f2

O token copiado será informado na configuração do Active Directory no SmartSync.

**07.** Acionar **Concluir**.

#f2f2f2#f2f2f2

Após a inclusão de um novo Active Directory na empresa, será apresentado o status **Não Configurado** ao lado direito do nome do Active Directory cadastrado. Esse status indica que este Active Directory ainda não é utilizado em nenhum SmartSync. Para saber como efetuar a instalação e a configuração do SmartSync, consulte [essa documentação](https://tdn.totvs.com/display/fluig/Identity+%7C+SmartSync).

#fdf7e8#fdf7e8

![](http://tdn.totvs.com/download/thumbnails/286221066/importante.png)

**IMPORTANTE!**  
É possível vincular mais de um Active Directory a uma empresa no Identity (quantos forem necessários), mas caso a autenticação seja realizada através do sAMAccountName, o usuário deverá informar o domínio antes do login, separado por uma barra invertida. Por exemplo: SP01\usuario.sobrenome.
