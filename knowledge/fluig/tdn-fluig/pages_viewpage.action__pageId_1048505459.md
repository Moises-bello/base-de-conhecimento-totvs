---
content_hash: 46595924c210e7e54d35fdd7f7158be47230ef5cb192474ca5f6d58f872bf496
fetched_at: '2026-06-28T21:35:17.363284+00:00'
page_id: '1048505459'
product: fluig
source: tdn-fluig
title: Identity | Configuração e Uso do MFA por e-mail
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1048505459
version: 49
---

Esta página tem como objetivo orientar o usuário e o administrador sobre os procedimentos de configuração, utilização e recuperação do MFA no TOTVS Identity.

75%

5.\*ndice

25%

trueIdioma

# Falando em disponibilizar o MFA por e-mail no Identity...

---

Os procedimentos necessários para disponibilizar o MFA por e-mail no Identity são detalhados nos itens abaixo.

# Visão Geral

---

A autenticação multifator (MFA) adiciona uma camada extra de segurança ao processo de login, exigindo não apenas a senha, mas também uma verificação adicional via aplicativo **My Safe ID** ou **E-mail**.

**Seleção do Método de Autenticação**

Na tela inicial de configuração, o usuário deve escolher entre as duas abas disponíveis:

MFA1Aplicativo

**Aplicativo:** Recomendado para maior segurança e agilidade via notificações *push* ou códigos temporários (TOTP).

E-mail

**E-mail:** Utilizado para receber códigos numéricos diretamente na caixa de entrada cadastrada.

---

# MFA de Ponta a Ponta: do Cadastro à Recuperação de Acesso

---

Esta seção detalha o ciclo de vida do MFA no TOTVS Identity: do cadastro e fluxos de login à recuperação de acesso e gestão multi-empresas, unindo segurança e continuidade.

MFA\_e-mailCadastro de MFA por Usuário

Ao acessar o Identity pela primeira vez após a ativação da obrigatoriedade, ou ao realizar a configuração voluntária, siga o passo a passo:

1. Acesse o menu **Meu Perfil** > **Segurança**.
2. Clique em **Autenticação Multifator** e selecione **Autenticação Multifator**.
3. Escolha o método de sua preferência: **Aplicativo** ou **E-mail**.
4. Habilite o MFA conforme as regras do seu grupo de acesso.

1000true800

**Permissão por E-mail:** Marque a caixa **"Permitir que os usuários dos grupos ativem a autenticação multifator por e-mail"** no topo da página.

Dica

* Note que ao ativar para o grupo "**Everyone**", todos os usuários da plataforma serão solicitados a configurar o MFA no próximo acesso.
Processo de Login (Fluxos de Autenticação)

### Login com MFA por Aplicativo

1. Insira seu e-mail e senha na tela de login.
2. Abra o aplicativo **My Safe ID** no seu smartphone.
3. Faça a leitura do QRCode ou digite o código gerado no campo solicitado.

---

### Login com MFA por E-mail

1. Insira suas credenciais de acesso.
2. O sistema enviará um **código de verificação** para o e-mail cadastrado.
3. Insira o código recebido para concluir o acesso.

---

### 1. Solicitação do Código

Após inserir suas credenciais de acesso (e-mail e senha), o sistema apresentará a tela de seleção de método.

* Selecione a aba **E-mail**.
* Clique no botão **Enviar código**. O sistema encaminhará uma chave de verificação para o endereço de e-mail cadastrado na plataforma.

### 2. Verificação do E-mail

Acesse sua caixa de entrada e localize a mensagem enviada pelo TOTVS Identity.

* O código de autenticação possui **6 dígitos**.

Atenção

* O código tem validade de **10 minutos**. Caso expire, será necessário solicitar um novo envio.

### 3. Validação do Acesso

Retorne à tela de login do Identity para concluir a autenticação.

* No campo **Código de autenticação**, insira a sequência recebida por e-mail.
* Clique em **Ativar autenticação** para finalizar o login.

Dica

Caso não localize o e-mail em sua caixa de entrada, verifique a pasta de **Spam** ou utilize a opção **Reenviar código**.

---

### Login com MFA Habilitado (App e E-mail)

Caso o usuário possua ambos configurados, o sistema apresentará a opção padrão. O usuário poderá clicar em **"Utilizar outro método de autenticação"** para alternar entre o código do App e o código por E-mail.

Gestão de E-mail do MFA

### Template de E-mail do MFA

O administrador pode personalizar o visual do e-mail de autenticação em:

* **Painel de Controle** > **Configurações** > **Templates de E-mail**.
* Procure pelo template: `MFA - Código de Verificação`.
Recuperação de Acesso

### Perdeu o acesso do aplicativo (My Safe ID)?

Se você trocou de celular ou excluiu o app:

1. Utilize um **Código de Recuperação** (gerado no momento da configuração inicial).
2. Caso não possua o código, entre em contato com o administrador do Identity da sua empresa para solicitar o **Reset do MFA**.

### Perdeu o acesso ao E-mail?

1. O administrador da conta deverá atualizar o e-mail de contato no cadastro do usuário.
2. Após a atualização, o MFA poderá ser enviado para o novo endereço.
Desativação de MFA (Usuário Logado)

Se o usuário desejar remover a obrigatoriedade (e a política da empresa permitir):

* **Aplicativo:** Acesse Perfil > Segurança > Aplicativo Autenticador > **Remover**.
* **E-mail:** Acesse Perfil > Segurança > E-mail de Verificação > **Desabilitar**.
* *Nota: Será necessário confirmar a identidade através de um código antes de Desabilitar.*

Imagem

Multi-empresas com MFA

Para usuários que possuem acesso a múltiplas empresas (Contextos):

* O MFA configurado em uma empresa é válido para o seu usuário (identidade única).
* Se empresas diferentes possuírem políticas de MFA distintas, o sistema exigirá a configuração que atender ao nível mais alto de segurança exigido entre elas.

## Documentações relacionadas

---

* [Configuração de Políticas de Segurança](https://tdn.totvs.com/display/fluig/Identity)
* [Guia do Aplicativo My Safe ID](https://tdn.totvs.com/display/fluig/Identity+%7C+Multi-Factor+Authentication)
* [Identity | Multi-Factor Authentication](https://tdn.totvs.com/display/fluig/Identity+%7C+Multi-Factor+Authentication)
* [Fazer login com autenticação multifator (MFA)](https://tdn.totvs.com/display/fluig/Identity+%7C+Login#Identity|Login-Fazerlogincomautentica%C3%A7%C3%A3omultifator(MFA))
* [Identity | Validação do MFA desvinculado do Login](https://tdn.totvs.com/pages/viewpage.action?pageId=1048504602)
* Identity | API de validação de MFA
* [Identity | API de validação de MFA por E-mail](https://tdn.totvs.com/pages/viewpage.action?pageId=1060219992)
