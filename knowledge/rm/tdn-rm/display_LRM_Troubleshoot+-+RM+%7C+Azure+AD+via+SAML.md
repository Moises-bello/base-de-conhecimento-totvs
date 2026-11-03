---
content_hash: 9bf41267272c9ab8d643860add7dcdb9c17ac1d32cae8d9767a44c985039e85a
fetched_at: '2026-06-29T00:11:15.700930+00:00'
page_id: '661869891'
product: rm
source: tdn-rm
title: Troubleshoot - RM | Azure AD via SAML
type: documentation
url: https://tdn.totvs.com/display/LRM/Troubleshoot+-+RM+%7C+Azure+AD+via+SAML
version: 4
---

# Índice

---

      .\*ndice:

# Objetivo

---

       Este documento tem como objetivo como auxiliar na resolução de problemas referentes à integração do sistema RM com o Azure AD como provedor de Identidade (SAML).

# RM.exe - MDI

---

## AADSTS750054: SAMLRequest or SAMLResponse must be present as query string parameters in HTTP request for SAML Redirect binding.

       Este erro pode ocorrer ao abrir o RM.exe após realizar a integração SAML:

Este erro pode ser causado pelo erro na alteração das URL's de Location do XML, conforme explicado no 5º passo da integração SAML com o Azure AD.

### Como Corrigir

Para corrigir o erro AADSTS750054, é necessário alterar as URL's contidas nos itens **SingleSignOnService** e **SingleLogoutService**do XML baixado da Azure para a URL copiada do **MyApps** ([myapplications.microsoft.com](http://myapplications.microsoft.com)):

---

## RM não abre após o login pelo Azure AD

Caso, após inserir as credenciais de acesso no provedor (Azure AD) o RM não abra nem demonstre nenhum processo de carregamento, primeiramente confira o **EventViewer** ou **Visualizador de Eventos** do Windows. Ao acessar a aba Logs do **Windows ➝ Aplicativo (Windows Log ➝ Application)**, pode ser que seja possível ver dois novos erros, tal qual demonstrado abaixo:

Neste caso, clique em cada um dos **Erros**. Se um deles dizer a respeito do **RM**, tal qual demonstrado abaixo:

Muito provavelmente, o usuário associado ao email utilizado para logar no Azure não está com as permissões corretas.

### Como Corrigir

Verifique se as permissões e perfis associados ao usuário cadastrado no email responsável pelo login no **Azure** estão corretas e este usuário possui acesso ao sistema designado. Pode ser validado fazendo um login direto, *desativando a integração* e realizando login diretamente pela **MDI**, com **usuário e senha**.

---

# Portal - Corpore.Net

---

## Loop Infinito logo após o login com o provedor (Azure)

Caso, após inserir as credenciais de acesso no provedor (Azure AD) o portal entre em loop infinito em uma página parecida com a seguir:

O erro pode estar contido na configuração do XML inserido nos Parâmetros Globais da aplicação:

### Como Corrigir

Para corrigir a situação de loop infinito, **NÃO SE DEVE** editar as URL's contidas nos itens **SingleSignOnService** e **SingleLogoutService**do XML baixado da Azure. Estas URL's já estão corretas e ***só devem ser substituídas*** no caso de integração com a **MDI**. A alteração, principalmente caso seja feita para a URL copiada do **MyApps** (myapplications.microsoft.com) ocasionará em loop infinito na integração:

Utilizar um XML como o acima ocasionará no comportamento de loop infinito.

Dessa forma, basta baixar novamente o XML da Azure AD, remover as tags conforme instruído na documentação principal, e, SEM modificar as URL's, reimportá-lo no RM:

Já o XML acima, em que as URL's demarcadas não foram alteradas, funcionará corretamente (Possivelmente a URL correta virá com o host "https://login.microsoftonline.com")

---

## Redirecionamento para o RM.exe logo após o login com o provedor (Azure)

Pode ser que, logo após o login com o provedor, a integração SAML tente redirecioná-lo para o RM.exe (MDI) ao invés de enviá-lo para o Corpore.Net (Portal) corretamente. Isso muito provavelmente pode estar acontecendo por outra configuração que deve ser realizada APENAS no caso de configuração com a MDI:

Este erro pode estar ocorrendo pelo fato do Atributo **ExecutablePath** ter sido preenchido durante a configuração do aplicativo empresarial:

### Como Corrigir

Basta remover o Atributo **ExecutablePath** da configuração que a integração deve funcionar corretamente.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.27 e superiores

false

**Processo:** Integração SAML

falsefalse

**Status:** Finalizado

false

**Data:**
