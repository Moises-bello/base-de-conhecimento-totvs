---
content_hash: e4f1652d147dff05945299457aba0808eec249994d58de76ee840c6568dc73e4
fetched_at: '2026-06-29T00:12:14.241445+00:00'
page_id: '967112200'
product: rm
source: tdn-rm
title: Libportal Angular - Compartilhamento de classes e métodos utilitários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=967112200
version: 2
---

Pensando no reaproveitamento de código, e na padronização de componentes, foi criado um projeto de biblioteca chamado Libportal, o qual encontra-se no repositório do azure <https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/libportal>

Para facilitar e agilizar o desenvolvimento web com angular e PO-UI, a libportal fornece classes e métodos utilitários para usos mais comuns, como por exemplo: requisições HTTP, tratamento de dados base 64, blobs, ets.

Para adicionar a libportal a um projeto angular com PO-UI, basta seguir o passo a passo abaixo.

# **1) Incluir arquivo .npmrc no projeto**

---

No projeto precisa ser incluído um arquivo .npmrc com o conteúdo abaixo para permitir autenticação do usuário (desenvolvedor) no azure artifacts:

```
@totvs.cp:registry=https://totvstfs.pkgs.visualstudio.com/Construcao-e-Projetos/_packaging/Construcao-e-Projetos/npm/registry/  
always-auth=true
```

# **2) Instalar o autenticador do Azure Artifacts**

---

Após incluir o arquivo .npmrc, rode o comando node para instalar o **vsts-npm-auth** responsável por executar a autenticação no azure artifacts:

```
npm install -g vsts-npm-auth
```

Adicionalmente pode ser incluído no arquivo package.json um script com o comando, a fim de facilitar a execução, conforme exemplo:

# **3)** **Rodar o comando de autenticação do Azure Artifacts**

---

Após instalação, execute o comando de autenticação, com base no arquivo .npmrc, conforme abaixo:

```
vsts-npm-auth -config .npmrc
```

Será necessário criar um script para este comando, caso deseje-se executar o projeto pela IC do azure posteriormente:

# **4) Instalar os pacotes node**

---

Após execução do comando de autenticação, basta instalar os pacotes node normalmente com o comando:

```
npm install
```

# **5) Referenciar as classes da libportal no projeto angular**

---

Após instalação, para qualquer serviço ou componente que for utilizar as classes utilitárias da libportal, basta referenciar um dos pacotes do projeto e usá-lo na aplicação, conforme exemplo utilizando o pacote **@totvs.cp/ng-realestate-core**:
