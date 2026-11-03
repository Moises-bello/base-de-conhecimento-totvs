---
content_hash: ab33dc43adc79441c3e9c089695605cfcf37cbca47d430467318b986dcae5e74
fetched_at: '2026-06-28T21:35:30.186048+00:00'
page_id: '817648697'
product: fluig
source: tdn-fluig
title: Identity | Mensagem "Credenciais de acesso inválidas" ao realizar login
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=817648697
version: 17
---

**Dúvida**

Como proceder ao acessar o Identity e aparecer o erro "Credenciais de acesso inválidas"?

**Solução**

Esse erro ocorre ao realizar login no Identity. É um dos erros genéricos mais comuns e possui várias causas associadas. Listamos abaixo os principais motivos para que essa situação ocorra e seu, respectivos, modos de resolução:

**01. Senha do usuário incorreta:**

**a)** Caso a senha esteja incorreta, o usuário poderá fazer a redefinição, conforme a documentação: [Identity | Login | Recuperação de senha pessoal](https://tdn.totvs.com/display/fluig/Identity+%7C+Login#Identity|Login-Recupera%C3%A7%C3%A3odesenhapessoal)

**02. Usuário desativado no Identity:**

**a)** Se o usuário estiver **desativado** no Identity, também ocorrerá o erro de "Credenciais de acesso inválidas".

**b)** Se for o caso, o Administrador Corporativo deve ir em **Usuários**.

**c)** Pesquisar o e-mail do usuário na tela **Gerenciar usuários**.

**d)** Acessar o cadastro do usuário e clicar em **Mais Opções**.

**e)** Acionar **Ativar usuário**.

**03. Mecanismo de expiração de senha no Active Directory:**

**a)** O Identity respeita a configuração do Active Directory local e impede o login do usuário se a senha estiver expirada.

**b)** É necessário que o usuário defina uma nova senha no Active Directory local para efetuar o login. Saiba mais em: [Identity | Senha pessoal x senha de rede](https://tdn.totvs.com/display/fluig/Identity+%7C+Senha+pessoal#Identity|Senhapessoal-Senhapessoalxsenhaderede)

**04. Usuário preso na lista de aceitos do Active Directory:**

**a)** Com um usuário Administrador Corporativo no Identity, acesse a aba **Usuários**.

**b)** Pesquise o e-mail completo e verifique se aparece na lista de usuários do Identity **(Gerenciar usuários)**.

**c)** Caso o e-mail **NÃO** seja encontrado, acesse **Configurações**.

**d)** Clique em **Active Directory**.

**e)** Acione **Gerenciar Active Directories**.

**f)** Busque pelo e-mail do usuário dentro do Active Directory.

**g)** Por vezes, ocorre **duplicidade** na base do Identity e o usuário não aparece na listagem principal, porém, dentro do Active Directory, consta como **aceito**.

**h)** Se isso ocorrer, solicite a alteração através de um ticket na [Central de Atendimento](https://centraldeatendimento.fluig.com/hc/pt-br), através das opções **Nova Solicitação** → **Suporte Técnico**. Assim, o time de suporte moverá o usuário para pendente através das APIs disponíveis.

**05. SmartSync e/ou Active Directory indisponíveis no contexto:**

**a)** Com um usuário Administrador Corporativo no Identity, acesse **Configurações**.

**b)** Clique em **Active Directory**.

**c)** Acione **Gerenciar Active Directories**.

**d)** Verifique se as colunas SmartSync e AD estão com status **Disponível**.

**e)** Quando o usuário estiver provisionado em um Active Directory via SmartSync, é necessário que esses servidores estejam disponíveis no Identity.

**f)** Caso o SmartSync ou Active Directory estiver **indisponível**, inicie-o localmente.

**g)** Enquanto o status **Disponível** não aparecer nas configurações, ninguém da empresa conseguirá logar com a senha de rede.

**06. Valor de objectGUID divergente entre o Active Directory local e o Identity:**

**a)** Com um usuário Administrador Corporativo no Identity, acesse a aba **Usuários**.

**b)** Pesquisar o e-mail do usuário na tela **Gerenciar usuários**.

**c)** Acessar o cadastro do usuário, ir nas **informações de provisionamento** e clicar em **Mais detalhes**.

**d)** Esse é o valor de **objectGUID** que está cadastrado no **Identity**.

**e)** Para encontrar o valor de **objectGUID** cadastrado no **Active Directory local**, acesse a documentação:

**f)** Os valores de objectGUID tanto no Identity, como no Active Directory local, precisam ser **iguais**. Do contrário, é necessário forçar uma sincronização para atualizar esse valor. Saiba como em:
