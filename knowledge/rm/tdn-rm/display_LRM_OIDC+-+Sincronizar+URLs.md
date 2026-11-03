---
content_hash: 642e458680bde9350299a3edf8a95f3d4d28633d95f1aafcf456515b9ab9952e
fetched_at: '2026-06-29T00:05:53.106159+00:00'
page_id: '1066698992'
product: rm
source: tdn-rm
title: OIDC - Sincronizar URLs
type: documentation
url: https://tdn.totvs.com/display/LRM/OIDC+-+Sincronizar+URLs
version: 3
---

# **01.** **Visão Geral**

Esta documentação detalha o processo de sincronização das URLs de redirecionamento (Redirect URIs) entre o ambiente local (On-premise) do RM e o Identity Provider (IDP) da TOTVS. Este sincronismo é vital para garantir que o fluxo de autenticação OIDC (OpenID Connect) autorize apenas origens confiáveis, evitando falhas de segurança de URL durante o login.

**Caminho:** Gestão → Comunicação → Login Oidc → Sincronizar Url's

# **02.** **Requisitos de Configuração**

Para que o RM habilite o motor de sincronismo, é mandatória a configuração da **Integração OIDC** nos **Parâmetros Globais** do sistema. O comportamento do envio é regido pelo campo interno associado à flag de login OIDC.

### 2.1. Regras de Negócio

O sincronismo só será executado se a integração estiver ativa

| **Integração OIDC** | **Comportamento do Sincronismo** |
| --- | --- |
| **Obrigatório** | O sistema tenta sincronizar as URLs automaticamente. |
| **Opcional** | O sistema tenta sincronizar as URLs automaticamente. |
| **Desativado** | O processo de sincronismo é ignorado. |

# **03.** **Infraestrutura: Credential Helper**

O sincronismo não é feito diretamente pelo Host do RM, mas sim através do **Credential Helper**. Este componente atua como um agente de comunicação segura com a nuvem TOTVS.

### 3.1. Instalação e Ativação

* O **Credential Helper** deve estar em configurado.
* Ele deve possuir as credenciais de acesso ao ambiente (tenant) para autenticar a requisição de sincronismo.

### 3.2. Liberação de Firewall (Endpoint)

Para o sucesso da operação, o servidor deve permitir tráfego de saída para o seguinte endpoint:

[URLs utilizadas](https://tdn.totvs.com/x/8dcxPw)

# **04.** **Origem dos Dados: Tabela GOIDCREDIRECTURLS**

Esta tabela possui os links a serem homologados no IDP. Todas as variações de URL (DNS interno/externo, portas e protocolos) devem estar presentes.

**Links Padrões (Exemplos):**

* `http://servidor:HTTPPort/wwwroot/smart-x-rm-ui/login-oidc-callback`
* `http://servidor:APIPort/login/oidc/callback`
* `http://servidor:APIPort/api/smart-view/oidc/token_redirect`

# **05.** **Fluxo de Sincronização**

O processo segue a seguinte ordem lógica:

1. **Processo:** Execução manual ou agendada via processo **"Sincronizar URL's"**
2. **Validação de Parâmetros:** O sistema verifica se `gparams.oidc_login` é `1` ou `2`.
3. **Leitura de Dados:** O sistema realiza o SELECT na tabela `GOIDCREDIRECTURLS`.
4. **Chamada de API:** O Credential Helper encapsula a lista de URLs e faz a chamada ao endpoint `https://api-credentialhelper.totvs.app`.
5. **Atualização no IDP:** O provedor de identidade recebe as novas URIs e atualiza a whitelist do cliente.

# **06.** **Observações Importantes**

* **Propagação:** Após o sincronismo, pode haver um breve período de propagação no IDP até que as URLs sejam efetivamente aceitas no fluxo de login.
* **Erros Comuns:** Caso o sincronismo falhe, verifique se o Credential Helper possui logs de erro de conectividade (TLS/SSL) ou se o endpoint está sendo bloqueado por Proxy.
* **Segurança:** O uso do Credential Helper garante que as chaves de API não fiquem expostas no tráfego de rede local.
false

**Índice:**

false

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Sincronizar URLs

falsefalse

**Status:** Em Desenvolvimento

false

**Data:** 22/04/2026
