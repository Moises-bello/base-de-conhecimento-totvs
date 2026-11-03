---
content_hash: 43fa9ffc638b2099adc95574d7f35c250a60bd476aa22ba2dba0958af153eda0
fetched_at: '2026-06-29T00:05:53.274935+00:00'
page_id: '1068938732'
product: rm
source: tdn-rm
title: Autenticação TOTP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1068938732
version: 3
---

# **01.** **Visão Geral**

O **TOTP** (Time-Based One-Time Password), é um algoritmo que gera uma senha de uso único e temporária (normalmente válida por 30 ou 60 segundos) combinando uma chave secreta compartilhada com o horário atual do sistema.  
No ecossistema do RM, a implementação do TOTP atua como um fluxo de contingência de segurança e segundo fator de autenticação (2FA) para usuários que realizam o login utilizando o provedor de identidade **OIDC** (OpenID Connect).

# **02.** **Funcionamento do Fluxo no RM**

A tela é invocada de forma automática **logo após o login de sucesso do usuário**, sob a condição estrita de que o usuário esteja parametrizado e apto a logar via OIDC e ainda não possua uma chave secreta TOTP configurada no sistema.

Aviso Importante sobre o Cancelamento

Caso o usuário opte por clicar em "**Cancelar**" e decida não configurar o TOTP naquele momento, o sistema apresentará uma mensagem informativa alertando sobre a alta relevância da segurança desse recurso.



# **03.** **Guia de Configuração Passo a Passo**

Ao se deparar com a tela de ativação do TOTP após o login, o usuário deve seguir o roteiro abaixo composto por três etapas lógicas:

### 3.1.Download do Aplicativo de Autenticação

O usuário deve realizar o download e instalação de um aplicativo autenticador em seu smartphone ou dispositivo móvel. O sistema recomenda nativamente o aplicativo My Safe ID (disponível via instâncias da Google Play Store e Apple App Store), porém o fluxo é perfeitamente compatível com qualquer gerador de tokens de mercado, tais como Google Authenticator, Microsoft Authenticator ou extensões de navegadores homologadas.

### 3.2.Leitura do QR ou Cópia da Chave Eletrônica

O usuário deve abrir o aplicativo autenticador escolhido, acionar a opção de adicionar nova conta ("+") e realizar um dos seguintes procedimentos:

* **Leitura Óptica:** Apontar a câmera do celular para realizar a leitura do QR Code dinâmico renderizado na tela do RM.
* **Entrada Manual:** Caso possua limitações na câmera, o usuário pode copiar a Chave Eletrônica textual exibida em formato alfanuméricoe colá-la diretamente no aplicativo.

### 3.3.Inserção do Código e Ativação

Uma vez feita a leitura ou inserção da chave, o aplicativo passará a gerar códigos numéricos aleatórios de 6 dígitos que expiram periodicamente. O usuário deve:

1. Visualizar o código atual de 6 dígitos no aplicativo móvel.
2. Digitar este código no campo de entrada "Código de Autenticação" da tela do RM.
3. Clicar no botão "Ativar autenticação" para consolidar o vínculo de segurança.

# **04. Configuração do** **TOTP pelo Menu**

Além do fluxo de configuração automática no primeiro login, o sistema disponibiliza uma funcionalidade de gerenciamento centralizado diretamente no Menu "**Configurar Autenticador (TOTP)**" localizado em **Gestão →  Comunicação → Login Oidc.**

Apenas usuários com **Login OIDC ativado** poderão configurar o TOTP.

false

**Índice:**

false

**Produto:** Framework

false

**Versão:** >=12.1.2606

false

**Processo:** Autenticação TOTP

falsefalse

**Status:** Em Desenvolvimento

false

**Data:** 18/05/2026
