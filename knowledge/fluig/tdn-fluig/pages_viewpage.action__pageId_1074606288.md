---
content_hash: 660b0d921be939877220230c8d6211c29f3bffe8f8a067d35d8ca00aa5f51821
fetched_at: '2026-06-28T21:35:17.519312+00:00'
page_id: '1074606288'
product: fluig
source: tdn-fluig
title: Identity | Fluxo de Acesso com Certificado (WebAuthN)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1074606288
version: 36
---

# Falando de WebAuthN no Identity...

---

O **WebAuthN** (ou *Passkey*) é uma tecnologia que permite que você entre no Identity de forma muito mais rápida e segura, **sem precisar digitar sua senha** ou códigos de autenticação (MFA) toda vez que fizer login. Você pode usar a digital do seu celular, o reconhecimento facial do computador (Windows Hello/Apple FaceID) ou uma chave de segurança física.

## O que eu preciso para começar? (Pré-requisitos)

---

Antes de começar a usar, certifique-se de que seu navegador e computador estão prontos:

* **Se usa o Google Chrome:** Certifique-se de que você já tem um PIN (senha de bloqueio) cadastrado no seu computador ou gerenciador de senhas.
* **Se usa o celular (Android):** O seu celular precisa ter um bloqueio de tela configurado (PIN, desenho ou digital) e estar conectado a uma Conta Google.
* **Se usa outros sistemas:** O recurso funciona perfeitamente com o **Windows Hello** (reconhecimento facial/digital do Windows) ou **TouchID/FaceID** da Apple.

## Passo a Passo: Como cadastrar sua chave de acesso

---

Para começar a entrar no sistema sem senha, primeiro você precisa cadastrar o seu dispositivo atual (computador ou celular) dentro do Identity.

Você deve fazer este procedimento enquanto estiver logado no sistema.

**01.** Acesse o endereço de cadastro fornecido pela sua empresa. O padrão do link é:

#f2f2f2

<https://app.fluigidentity.com/ui/user-settings>

Clique no ícone do Perfil de Usuário - Segurança  - Minhas passkeys.

**02.** Clicar no botão **Cadastrar Chave.**

#f2f2f2

O seu navegador ou sistema operacional abrirá uma janelinha nativa (uma mensagem do próprio Windows, Mac ou Celular) perguntando se você deseja confirmar a identidade.

Vai aparecer a opção Salvar de outra forma, você pode clicar para escolher outra forma para criar a chave de acesso.

**03.** Digite um **PIN** no seu computador.

**04. Dê um nome para a sua chave:** O sistema dará um nome automático, mas você pode alterá-lo no campo **"Nickname"** para lembrar facilmente qual dispositivo é aquele (Exemplo: *"Notebook do Trabalho"* ou *"Meu Celular"*).

**100%true5%**

#008000#f2f2f2

**Pronto! Sua chave está cadastrada.**

## Como fazer Login sem Senha

---

Uma vez que a sua chave foi cadastrada, você pode **"Entrar com certificado"** ou digitar seu login e sua senha.

1. Vá para a tela de login padrão do Identity da sua empresa.
2. Em vez de digitar seu usuário e senha, procure e clique no botão **"Entrar com Certificado"**.
3. O seu computador ou celular vai pedir o seu PIN, ou biometria, ou FaceID (exatamente como você faz para desbloquear a tela do seu Notebook ou celular no dia a dia).
4. Assim que o dispositivo reconhecer você, o Identity abrirá automaticamente. **Você está logado!**

## Central de Gerenciamento (Listar, Alterar Nome ou Excluir)

---

Se você trocou de computador, perdeu o celular ou simplesmente quer organizar suas chaves, você mesmo pode gerenciá-las. Na sua tela de perfil do Identity, você encontrará a área de **Gestão de Passkeys**:

* **Listagem:** Você verá uma lista com todas as chaves que já cadastrou.
* **Editar Nome:** Se quiser mudar o nome de identificação da chave, basta clicar no campo de edição da chave e alterar o **"Nickname"**.
* **Excluir/Revogar:** Se você perder um dispositivo, clique em **Excluir** ao lado da chave correspondente. Isso impede imediatamente que aquele dispositivo consiga acessar sua conta.

**100%true5%**

## Recados Importantes para o Atendimento (Dicas de Suporte)

---

**Atenção com mudanças no MFA:** O cadastro da chave tira uma "foto" das regras de segurança do usuário naquele momento. Se o usuário cadastrou a chave quando a empresa **não** exigia o segundo fator de autenticação (MFA), e depois a empresa passou a exigir, o acesso dele continuará entrando direto sem pedir o MFA.

**Solução do suporte:** Para que a nova regra de segurança funcione para esse usuário, oriente o cliente a **excluir a chave antiga e cadastrar uma nova**.

Atenção

**Celular Android não exibe a opção de login?** Se o cliente tentar usar no Android e a tela de autenticação não aparecer, verifique se o celular dele tem um PIN ativo na tela de bloqueio e se há uma conta Google logada no aparelho. Sem isso, o Android bloqueia o recurso por segurança.
