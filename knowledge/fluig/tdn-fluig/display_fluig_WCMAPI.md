---
content_hash: 05e567e0212d7c124cada56b1a6f0d8f4d0b6f3f5b14cf674b0700a27049f2a0
fetched_at: '2026-06-28T21:35:25.555279+00:00'
page_id: '286005678'
product: fluig
source: tdn-fluig
title: WCMAPI
type: documentation
url: https://tdn.totvs.com/display/fluig/WCMAPI
version: 24
---

2true.\*ndicenone

# Visão Geral

---

O `WCMAPI` é a **API JavaScript central da plataforma Fluig WCM**. Ele expõe um objeto singleton global disponível em todos os widgets, temas e formulários da plataforma.  
Por meio do `WCMAPI` você consegue:

* Saber quem é o usuário logado e qual é o tenant (empresa) ativo
* Ler o contexto da página atual (código, tipo, layout)
* Carregar dinamicamente arquivos CSS e JavaScript
* Renderizar templates FreeMarker (`.ftl`) de forma síncrona ou assíncrona
* Instanciar widgets via `loadWidgets()`
* Publicar e assinar eventos entre widgets (pub/sub)
* Realizar chamadas AJAX com autenticação JWT automática
* Validar tokens OAuth de integrações externas
* O objeto é acessível em **qualquer script carregado após este arquivo**:

jstrue

## Como Começar

---

O `WCMAPI` já estará disponível como variável global no momento em que seu widget ou tema for executado. **Não é necessário importar, instanciar ou configurar nada.**

### Dentro de um widget Fluig

jstrue

### Renderizando um template FTL no widget

jstrue {
    $('#conteudo').html(html);
    WCMAPI.loadWidgets();
});]]>

### Verificando feature flags

jstrue

## Contexto de Dados (Tenant e Página)

---

Estes valores são fornecidos automaticamente pela plataforma antes de qualquer widget ser inicializado.

**Regra fundamental:** nunca acesse ou modifique propriedades do `WCMAPI` diretamente (ex.: `WCMAPI.tenantCode`). Utilize **sempre** os métodos getter/setter correspondentes. O acesso direto às propriedades é considerado legado e pode ser removido em versões futuras.

### getTenantCode() / setTenantCode(value)

**Descrição:** Retorna ou define o código único que identifica o tenant (empresa) ativo. Preenchido automaticamente pela plataforma; raramente é necessário usar o setter em widgets.  
**Retorno de `getTenantCode()`:** `string` — ex.: `'minhaempresa'`  
**Parâmetros de `setTenantCode()`:**

* `value` (`string`): novo código do tenant

jstrue

### getTenantId() / getOrganizationId() / setOrganizationId(value)

**Descrição:** Retorna ou define o identificador numérico do tenant. `getTenantId()` é um alias para `getOrganizationId()`. Use `setOrganizationId()` para definir o valor — não existe `setTenantId()`.  
**Retorno:** `number` — valor padrão `-1` quando não há tenant carregado.  
**Parâmetros de `setOrganizationId()`:**

* `value` (`number`): identificador numérico do tenant

jstrue

### getTenantURI() / setTenantURI(value)

**Descrição:** Retorna ou define o segmento de URI do tenant usado nas URLs de páginas da plataforma.  
**Retorno de `getTenantURI()`:** `string` — ex.: `'/portal/p/minhaempresa'`

jstrue

### getTenantURL() / setTenantURL(value)

**Descrição:** Retorna ou define a URL completa do tenant (esquema + host + caminho do tenant).  
**Retorno de `getTenantURL()`:** `string` — ex.: `'https://minhaempresa.fluig.com/minhaempresa'`

### getTenantPATH() / setTenantPATH(value)

**Descrição:** Retorna ou define apenas o segmento de caminho do tenant (sem esquema e host).  
**Retorno de `getTenantPATH()`:** `string` — ex.: `'/minhaempresa'`

### getServerURL() / setServerURL(value)

**Descrição:** Retorna ou define a URL base do servidor (esquema + host), sem nenhum caminho adicional.  
**Retorno de `getServerURL()`:** `string` — ex.: `'https://minhaempresa.fluig.com'`

### getServerContextURL() / setServerContextURL(value)

**Descrição:** Retorna ou define a URL completa do contexto do servidor (esquema + host + context path do portal).  
**Retorno de `getServerContextURL()`:** `string`

### getContextPath() / setContextPath(value)

**Descrição:** Retorna ou define o context path do portal no servidor de aplicação.  
**Retorno de `getContextPath()`:** `string` — ex.: `'/portal'`

### getHomePage()

**Descrição:** Monta e retorna a URL completa da página inicial do tenant.  
**Retorno:** `string` — equivale a `getTenantURI() + '/' + getHomePageCode()`

jstrue

### getPageCode() / setPageCode(code) / getPageId() / setPageId(id) / getPageType() / setPageType(type) / getPageLayout() / setPageLayout(layoutId)

**Descrição:** Retornam ou definem informações sobre a página WCM atualmente renderizada. Os setters são utilizados internamente pela plataforma; em widgets, utilize apenas os getters.

|  |  |  |  |
| --- | --- | --- | --- |
| Getter | Setter | Retorno | Exemplo |
| `getPageCode()` | `setPageCode(code)` | `string|null` | `'home'` |
| `getPageId()` | `setPageId(id)` | `number|null` | `42` |
| `getPageType()` | `setPageType(type)` | `string|null` | `'public'` |
| `getPageLayout()` | `setPageLayout(layoutId)` | `number|null` | `3` |
| `getPageTitle()` | `setPageTitle(title)` | `string|null` | `'Início'` |
| `getParentPageCode()` | `setParentPageCode(code)` | `string|null` | `'portal'` |
| `getFriendlyURL()` | `setFriendlyURL(url)` | `string|null` | `'/inicio'` |

jstrue

### getSpaceAlias() / setSpaceAlias(value)

**Descrição:** Retorna ou define o alias (identificador curto) do espaço Fluig atual.  
**Retorno de `getSpaceAlias()`:** `string` — ex.: `'default'`

jstrue

### getSpaceId() / setSpaceId(id)

**Descrição:** Retorna ou define o identificador numérico do espaço Fluig atual.  
**Retorno de `getSpaceId()`:** `number|null`

jstrue

### getHomePageCode() / setHomePageCode(value)

**Descrição:** Retorna ou define o código da página configurada como home/landing page do tenant. Usado por `getHomePage()` para montar a URL completa.  
**Retorno de `getHomePageCode()`:** `string` — padrão `'home'`

jstrue

### getUploadURL() / setUploadURL(value)

**Descrição:** Retorna ou define a URL utilizada para operações de upload de arquivos na plataforma.  
**Retorno de `getUploadURL()`:** `string`

jstrue

### getProtectedContextPath() / setProtectedContextPath(value)

**Descrição:** Retorna ou define o context path para recursos protegidos (que requerem autenticação).  
**Retorno de `getProtectedContextPath()`:** `string`

jstrue

### getDomainId() / setDomainId(value) / getDomainName() / setDomainName(value)

**Descrição:** Retornam ou definem o identificador numérico e o nome legível do domínio atual, preenchidos pela plataforma no carregamento da página.

|  |  |  |
| --- | --- | --- |
| Getter | Setter | Retorno |
| `getDomainId()` | `setDomainId(id)` | `number|null` |
| `getDomainName()` | `setDomainName(name)` | `string|null` |

jstrue

### getDefaultDomainURL() / setDefaultDomainURL(value)

**Descrição:** Retorna ou define a URL base padrão do domínio atual.  
**Retorno de `getDefaultDomainURL()`:** `string|null`

jstrue

### getIsSAMLEnabled() / setIsSAMLEnabled(value)

**Descrição:** Indica se a autenticação SAML/SSO está habilitada para o tenant. Quando `true`, o login é delegado ao Identity Provider configurado. Use `getIsSAMLEnabled()` no lugar do acesso à propriedade `isSAMLEnabled` diretamente.

> Veja também `isIdentityEnabled()`, que é um alias para `getIsSAMLEnabled()`.  
> **Retorno de `getIsSAMLEnabled()`:** `boolean`

jstrue

### getIdpHomePageURL() / setIdpHomePageURL(value)

**Descrição:** Retorna ou define a URL da página inicial do Identity Provider (IdP), usada nos fluxos de logout com SAML ativo.  
**Retorno de `getIdpHomePageURL()`:** `string`

jstrue

### getFluigPaas() / setFluigPaas(value)

**Descrição:** Indica se a plataforma está rodando em modo PaaS (Fluig em nuvem). Quando `true`, certos recursos e caminhos específicos de PaaS são ativados.  
**Retorno de `getFluigPaas()`:** `boolean`

jstrue

### getApplicationCode() / setApplicationCode(value)

**Descrição:** Retorna ou define o código de aplicação usado para escopo de caminhos de recursos estáticos. Padrão: `'fluig'`.  
**Retorno de `getApplicationCode()`:** `string`

jstrue

### getEnvType() / setEnvType(value)

**Descrição:** Retorna ou define o identificador do ambiente de implantação, como `'production'` ou `'staging'`.  
**Retorno de `getEnvType()`:** `string`

jstrue

### getTenantLocales() / setTenantLocales(value)

**Descrição:** Retorna ou define a lista de códigos de idioma disponíveis para o tenant. Útil para renderizar seletores de idioma em widgets.  
**Retorno de `getTenantLocales()`:** `string[]` — ex.: `'pt_BR', 'en_US'.`

jstrue adicionarOpcaoDeIdioma(locale));]]>

### isFeatureEnabled(featureFlag)

**Parâmetros:**

* `featureFlag` (`string`): identificador da feature a verificar

**Retorno:** `boolean`

jstrue

### getIsEditMode() / setIsEditMode(value)

**Descrição:** Indica se a página está atualmente em modo de edição WCM. Quando `true`, a plataforma exibe controles de edição e a engrenagem dos widgets.

**Não acesse `WCMAPI.isEditMode` diretamente.** Use `getIsEditMode()` para leitura e `setIsEditMode()` para escrita.  
**Retorno de `getIsEditMode()`:** `boolean`  
**Parâmetros de `setIsEditMode()`:**

* `value` (`boolean`): `true` para ativar o modo de edição

jstrue

## Contexto da Página

---

Essas informações são fornecidas automaticamente pela plataforma no carregamento da página e devem ser tratadas como somente leitura. O uso dos setters não tem efeito no comportamento da plataforma.

### getIsPreviewMode() / setIsPreviewMode(value)

**Somente leitura** — fornecido automaticamente pela plataforma.  
**Descrição:** Indica se a página está sendo renderizada em modo de pré-visualização. Neste modo, as alterações ainda não foram publicadas e a URL geralmente contém o parâmetro `?preview=true`.  
**Retorno de `getIsPreviewMode()`:** `string` — `'true'` ou `'false'` (chega como string do FreeMarker, não como boolean nativo).

jstrue

### getPageAuthType() / setPageAuthType(value)

**Somente leitura** — fornecido automaticamente pela plataforma.  
**Descrição:** Indica o tipo de autenticação exigido para acesso à página atual.  
**Retorno de `getPageAuthType()`:** `string` — ex.: `'PUBLIC'`, `'PRIVATE'`

jstrue

### getIsResponsiveLayout() / setIsResponsiveLayout(value)

**Somente leitura** — fornecido automaticamente pela plataforma.  
**Descrição:** Indica se o layout da página atual é responsivo (adapta-se a diferentes tamanhos de tela).  
**Retorno de `getIsResponsiveLayout()`:** `boolean`

jstrue

### getIsNewBuilder() / setIsNewBuilder(value)

**Somente leitura** — fornecido automaticamente pela plataforma.  
**Descrição:** Indica se a página foi construída com o editor New Builder da plataforma Fluig. Pode ser usado para ativar funcionalidades exclusivas do New Builder.  
**Retorno de `getIsNewBuilder()`:** `boolean`

jstrue

### getPageIsInternal() / setPageIsInternal(value)

**Somente leitura** — fornecido automaticamente pela plataforma.  
**Descrição:** Indica se a página está marcada como interna, ou seja, visível apenas para usuários autenticados. Quando `true`, o acesso anônimo deve ser bloqueado. Padrão `false` quando a variável não está presente no modelo do servidor.  
**Retorno de `getPageIsInternal()`:** `boolean`

jstrue

## Usuário Atual

---

### getUserLogin() / setUserLogin(login)

**Descrição:** Retorna ou define o login (identificador único) do usuário autenticado.  
**Retorno de `getUserLogin()`:** `string|null` — `null` se o usuário não estiver autenticado.

jstrue

### getUserId() / setUserId(id)

**Descrição:** Retorna ou define o identificador numérico do usuário autenticado.  
**Retorno de `getUserId()`:** `number|null`

jstrue

### getUserCode() / setUserCode(code)

**Descrição:** Retorna ou define o código do usuário (equivalente ao login na maioria dos casos).  
**Retorno de `getUserCode()`:** `string`

### getUserFirstName() / setUserFirstName(value) / getUserLastName() / setUserLastName(value) / getUser() / setUser(value)

**Descrição:** Retornam ou definem as partes do nome do usuário autenticado.

|  |  |
| --- | --- |
| Getter | Setter |
| `getUserFirstName()` | `setUserFirstName(value)` |
| `getUserLastName()` | `setUserLastName(value)` |
| `getUser()` | `setUser(value)` |

jstrue

### getUserEmail() / setUserEmail(email)

**Descrição:** Retorna ou define o e-mail do usuário autenticado.  
**Retorno de `getUserEmail()`:** `string`

### getUserLocationId() / setUserLocationId(id) / getUserLocationCode() / setUserLocationCode(code) / getUserLocationUrl() / setUserLocationUrl(url)

**Descrição:** Retornam ou definem informações sobre a localização (unidade/empresa) associada ao usuário.

jstrue

### getLocale() / setLocale(value) / getLocaleDisplayName() / setLocaleDisplayName(value)

**Descrição:** Retornam ou definem informações sobre o idioma configurado para o usuário.

|  |  |  |
| --- | --- | --- |
| Getter | Setter | Exemplo |
| `getLocale()` | `setLocale(value)` | `'pt_BR'` |
| `getLocaleDisplayName()` | `setLocaleDisplayName(value)` | `'português (Brasil)'` |

jstrue

### getTimezone() / setTimezone(value)

**Descrição:** Retorna ou define o identificador de fuso horário IANA configurado para o usuário.  
**Retorno de `getTimezone()`:** `string|null` — ex.: `'America/Sao_Paulo'`

jstrue

### isAdmin()

**Descrição:** Verifica se o usuário atual possui privilégios de administrador da plataforma Fluig.  
**Retorno:** `boolean`

> **Atenção:** Esta operação é **síncrona** e faz uma chamada ao servidor. Evite utilizá-la em loops ou em caminhos críticos de renderização.

jstrue

### isIdentityEnabled()

**Descrição:** Indica se a autenticação SAML/SSO está habilitada para o tenant.  
**Retorno:** `boolean`

## Contexto do Usuário

---

Essas informações são fornecidas automaticamente pela plataforma no carregamento da página e devem ser tratadas como somente leitura.

> Disponíveis apenas quando `WCMAPI.getUserIsLogged()` retorna `true`.  
> Para os métodos completos de acesso aos dados do usuário (login, email, nome etc.), consulte a seção [Usuário Atual](https://tdn.totvs.com/pages/viewpage.action?pageId=1060213081#WCMAPIAtualiza%C3%A7%C3%A3odadocumenta%C3%A7%C3%A3o-usu%C3%A1rio-atual).

### getUserType() / setUserType(value)

**Somente leitura** — fornecido automaticamente pela plataforma.  
**Descrição:** Retorna o tipo de conta do usuário autenticado, conforme cadastrado na plataforma.  
**Retorno de `getUserType()`:** `string` — ex.: `'interno'`, `'externo'`

jstrue

### getIsMobileAppMode()

**Somente leitura** — fornecido automaticamente pela plataforma.  
**Descrição:** Indica se a plataforma está sendo executada dentro de um aplicativo móvel Fluig. O valor é determinado em tempo de renderização pelo servidor e não muda após o carregamento da página.  
**Retorno:** `boolean` — `true` se executando dentro do app móvel

jstrue

## Sessão e Autenticação

---

### getUserIsLogged() / setUserIsLogged(value)

**Descrição:** Retorna ou define se o usuário está autenticado na sessão atual. O setter aceita `boolean` ou as strings `'true'`/`'false'` para compatibilidade com valores vindos de templates JSP/FreeMarker.  
**Retorno de `getUserIsLogged()`:** `boolean`

jstrue

### getIsStateless() / setIsStateless(value)

**Descrição:** Indica ou define se a plataforma está operando em modo stateless (sem sessão HTTP, apenas JWT). Nesse modo, as verificações de sessão e o ping de keep-alive são desativados automaticamente.  
**Retorno de `getIsStateless()`:** `boolean`

jstrue

### extendSession()

**Descrição:** Reinicia os contadores de expiração da sessão. Deve ser chamado em resposta a interações do usuário para evitar logout por inatividade.  
Internamente, agenda:

* Um aviso após **28 minutos** de inatividade
* O logout forçado após **29 minutos** de inatividade
* Não tem efeito no modo stateless ou quando cookies SAML estão presentes.

jstrue {
    WCMAPI.extendSession();
});]]>

### login(user, password)

**Descrição:** Autentica o usuário com login e senha. Em caso de sucesso, recarrega a página; em caso de falha, exibe um alerta nativo do navegador.  
**Parâmetros:**

* `user` (`string`): login do usuário
* `password` (`string`): senha em texto plano

**Retorno:** `boolean|*` — `true` em caso de sucesso

> A senha é transmitida em texto plano para o `WCMSpaceAPI`. Certifique-se de usar HTTPS.

jstrue

### logoff()

**Descrição:** Encerra a sessão do usuário e redireciona para o endpoint de logout da plataforma. A operação é imediata e irrecuperável — o usuário será redirecionado para a tela de login.

jstrue WCMAPI.logoff());]]>

### hasPermissionToChangePermission(callback)

**Descrição:** Verifica de forma assíncrona se o usuário logado tem o direito de gerenciar permissões na plataforma (recurso `PermissionsAdmin` com ação `execute`).  
**Parâmetros:**

* `callback` (`Function`): chamado com `(err, result)` onde `result.content` é `boolean`

**Retorno:** `jqXHR` — o objeto de deferred do jQuery

jstrue {
    if (result?.content) {
        $('#btn-gerenciar-permissoes').show();
    }
});]]>

## Ambiente

---

Essas informações são fornecidas automaticamente pela plataforma no carregamento da página e devem ser tratadas como somente leitura. Elas refletem a configuração da instância no momento da renderização.

### getVersion() / setVersion(value)

**Somente leitura** — fornecido automaticamente pela plataforma.  
**Descrição:** Retorna a versão da plataforma Fluig. Útil para lógica condicional baseada em versão ou para exibição em painéis de diagnóstico.  
**Retorno de `getVersion()`:** `string` — ex.: `'1.7.0'`

jstrue

### getFluigVersion() / setFluigVersion(value) / getFluigInstanceVersionName() / setFluigInstanceVersionName(value) / getFluigVersionBuild() / setFluigVersionBuild(value) / getFluigVersionStatus() / setFluigVersionStatus(value) / getFluigVersionStatusInfo() / setFluigVersionStatusInfo(value)

**Somente leitura** — disponível apenas quando informações detalhadas de versão estiverem configuradas na plataforma.  
**Descrição:** Informações detalhadas da versão da instância WCM, mais granulares do que `getVersion()`. Se não estiverem configuradas, os métodos retornam string vazia.

|  |  |  |
| --- | --- | --- |
| Getter | Setter | Exemplo de retorno |
| `getFluigVersion()` | `setFluigVersion(value)` | `'2.0.0-260417'` |
| `getFluigInstanceVersionName()` | `setFluigInstanceVersionName(value)` | `'Voyager'` |
| `getFluigVersionBuild()` | `setFluigVersionBuild(value)` | `'788'` |
| `getFluigVersionStatus()` | `setFluigVersionStatus(value)` | `'0'`, `'1'` |
| `getFluigVersionStatusInfo()` | `setFluigVersionStatusInfo(value)` | texto descritivo |

jstrue

### getNocodeActive() / setNocodeActive(value)

**Somente leitura** — fornecido automaticamente pela plataforma.  
**Descrição:** Indica se o módulo No-Code está ativo para o tenant atual. Quando `true`, funcionalidades de criação de aplicações sem código estão habilitadas. Padrão `false` quando a variável não estiver presente no modelo do servidor.  
**Retorno de `getNocodeActive()`:** `boolean`

jstrue

### getGoogleAnalyticsEnabled() / setGoogleAnalyticsEnabled(value) / getGoogleAnalyticsAccount() / setGoogleAnalyticsAccount(value)

**Somente leitura** — fornecidos automaticamente pela plataforma.  
**Descrição:** Indicam se o Google Analytics está ativo e qual é o ID da conta configurada para o tenant. Use em conjunto para inicializar o rastreamento.

|  |  |  |
| --- | --- | --- |
| Getter | Setter | Retorno |
| `getGoogleAnalyticsEnabled()` | `setGoogleAnalyticsEnabled(value)` | `boolean` |
| `getGoogleAnalyticsAccount()` | `setGoogleAnalyticsAccount(value)` | `string`, ex.: `'UA-XXXXX-Y'` |

jstrue

## Interface (UI)

---

Essas informações são fornecidas automaticamente pela plataforma no carregamento da página e devem ser tratadas como somente leitura. Refletem a configuração visual do tema ativo e as funcionalidades de edição de texto do tenant.

### getThemeId() / setThemeId(id)

**Somente leitura** — fornecido automaticamente pela plataforma.  
**Descrição:** Retorna o identificador numérico do tema aplicado à página atual. Chega como string do FreeMarker; converta com `parseInt()` se necessário.  
**Retorno de `getThemeId()`:** `string` (número como string) — ex.: `'3'`

jstrue

### getColorMenu() / setColorMenu(value) / getColorBackground() / setColorBackground(value)

**Somente leitura** — fornecidos automaticamente pela plataforma.  
**Descrição:** Retornam as cores definidas pelo tema ativo — a cor do menu de navegação e a cor de fundo da página, respectivamente. Úteis para personalização dinâmica de componentes que precisam combinar com o tema.

|  |  |  |
| --- | --- | --- |
| Getter | Setter | Descrição |
| `getColorMenu()` | `setColorMenu(value)` | Cor do menu de navegação, ex.: `'#003366'` |
| `getColorBackground()` | `setColorBackground(value)` | Cor de fundo da página, ex.: `'#f5f5f5'` |

jstrue

### getImageBackground() / setImageBackground(value) / getImageLogo() / setImageLogo(value)

**Somente leitura** — fornecidos automaticamente pela plataforma.  
**Descrição:** Retornam as URLs das imagens configuradas no tema ativo — imagem de fundo da página e logotipo exibido no cabeçalho. Vazios quando não configurados.

|  |  |  |
| --- | --- | --- |
| Getter | Setter | Descrição |
| `getImageBackground()` | `setImageBackground(value)` | URL da imagem de fundo da página |
| `getImageLogo()` | `setImageLogo(value)` | URL do logotipo do cabeçalho |

jstrue

### getIsDisabledRichEditor() / setIsDisabledRichEditor(value)

**Somente leitura** — fornecido automaticamente pela plataforma.  
**Descrição:** Indica se o editor de texto rico (rich editor) foi substituído pelo editor simples (simple editor) para o tenant. Quando `true`, o `loadJS` troca automaticamente caminhos contendo `'richeditor'` por `'simpleeditor'`.  
**Retorno de `getIsDisabledRichEditor()`:** `boolean`

jstrue

### getEnableRichEditorSanitizer() / setEnableRichEditorSanitizer(value)

**Somente leitura** — fornecido automaticamente pela plataforma.  
**Descrição:** Indica se a sanitização XSS está ativa no editor de texto rico. Quando `true`, o conteúdo gerado pelo usuário passa por sanitização antes de ser salvo, prevenindo a injeção de scripts maliciosos.  
**Retorno de `getEnableRichEditorSanitizer()`:** `boolean`

jstrue

## Carregamento de Recursos (CSS e JS)

### loadCSS(path)

**Descrição:** Injeta dinamicamente um arquivo CSS no `<head>` da página, evitando duplicatas.  
**Quando usar:** sempre que um widget ou componente precisar de um arquivo CSS específico.  
**Parâmetros:**

* `path` (`string`): URL ou caminho do arquivo CSS

jstrue

### loadJS(path, callback)

**Descrição:** Carrega dinamicamente um arquivo JavaScript com cache habilitado, evitando carregamentos duplicados.  
**Quando usar:** sempre que um widget precisar de um script externo. Prefira sempre `WCMAPI.loadJS()` em vez de `$.getScript()` dentro da plataforma — o WCMAPI garante controle de duplicatas e cache correto.  
**Parâmetros:**

* `path` (`string`): URL ou caminho do arquivo JavaScript
* `callback` (`Function`, opcional): executado após o carregamento

jstrue {
   // faça algo
});]]>

### jsBasePath()

**Descrição:** Retorna o diretório base da última tag `<script>` adicionada à página no momento da chamada. Útil para resolver caminhos relativos dentro de scripts inline de widgets que não possuem acesso a um sistema de módulos.  
**Retorno:** `string`

jstrue

## Renderização de Templates FTL

---

### convertFtlAsync(appCode, fileNameFtl, pars, callback, errorCallback)

**Descrição:** Renderiza um template FreeMarker (`.ftl`) de um aplicativo Fluig de forma **assíncrona** (não bloqueante) e entrega o HTML resultante por meio de um callback.  
CSS e JS declarados pelo template são carregados automaticamente após a resposta.  
**Parâmetros:**

* `appCode` (`string`): código do aplicativo Fluig, ex.: `'wcm_meupainel'`
* `fileNameFtl` (`string`): nome do arquivo FTL, ex.: `'view.ftl'`
* `pars` (`Object|string`): parâmetros passados ao template (serializado automaticamente se for objeto)
* `callback` (`Function`): chamado com o HTML renderizado — `callback(html)`
* `errorCallback` (`Function`, opcional): chamado em caso de erro — `errorCallback(err)`

jstrue {
        $('#meu-container').html(html);
        WCMAPI.loadWidgets();
    },
    (erro) => {
        console.error('Falha ao renderizar o template', erro);
    }
);]]>
> ✅ **Prefira este método** ao `convertFtl()` em qualquer situação onde o bloqueio da thread do navegador seja indesejável.

### convertFtl(appCode, fileNameFtl, pars, component, callback)

**Descrição:** Renderiza um template FTL de forma **síncrona** (bloqueante) e injeta o HTML resultante em um elemento da página. Também carrega os recursos CSS e JS declarados pelo template.  
**Parâmetros:**

* `appCode` (`string`): código do aplicativo Fluig
* `fileNameFtl` (`string`): nome do arquivo FTL
* `pars` (`Object|string`): parâmetros para o template
* `component` (`string|jQuery`): ID do elemento ou objeto jQuery onde o HTML será injetado. Passe `undefined` para receber o HTML como string de retorno
* `callback` (`Function`, opcional): executado após todos os recursos JS serem carregados

**Retorno:** `string` — HTML renderizado quando `component` é `undefined`; caso contrário, `""`

jstrue {
    console.log('Widget em modo de edição pronto');
});
const html = WCMAPI.convertFtl('meuApp', 'partial.ftl', { id: 10 });
$('#lista').append(html);]]>
> **Atenção:** Esta versão bloqueia o navegador durante o round-trip ao servidor. Use `convertFtlAsync()` sempre que possível.

### extractHtmlContentAndResources(html, appCode) *(interno)*

**Descrição:** Método interno utilizado por `convertFtl` e `convertFtlAsync` para separar o HTML renderizado em nós de conteúdo DOM e descritores de recursos (CSS/JS). Não deve ser chamado diretamente por widgets.

## Ciclo de Vida de Widgets

---

### loadWidgets()

**Descrição:** Inicializa os widgets presentes na página. Chamado automaticamente pela plataforma no carregamento da página e ao final de `convertFtl` / `convertFtlAsync`.  
**Quando usar:** sempre que widgets forem carregados dinamicamente — por exemplo, após injetar HTML via `convertFtlAsync`, `convertFtl` ou uma requisição AJAX.

jstrue {
    $('#container').html(html);
    WCMAPI.loadWidgets();
});]]>

### openEditMode(instId, slot) / openViewMode(instId, slot)

**Descrição:** Re-renderizam sincronamente uma instância de widget em modo de edição ou visualização, substituindo o nó DOM atual.  
**Parâmetros:**

* `instId` (`number`): ID numérico da instância do widget
* `slot` (`string`): ID do elemento slot container

jstrue

### editContent(control, instanceId)

**Descrição:** Re-renderiza um widget em modo de edição quando acionado pelo ícone de engrenagem no modo de visualização. Diferente de `openEditMode()`, este método também carrega os recursos CSS e JS declarados pelo template de edição antes de injetar o HTML.  
**Parâmetros:**

* `control` (`Element|string`): elemento DOM clicado, usado para localizar o slot pai
* `instanceId` (`number`): ID numérico da instância

### updateWidgetPreferences(instanceId, prefs)

**Descrição:** Salva as preferências de um widget para **todos os usuários** e re-renderiza o widget em modo de edição imediatamente, para que o usuário veja o resultado da configuração.  
**Parâmetros:**

* `instanceId` (`number`): ID numérico da instância do widget
* `prefs` (`Object`): pares chave/valor das preferências a salvar

**Retorno:** `boolean` — `true` em caso de sucesso, `false` em caso de falha

jstrue

### updateUserWidgetPreferences(instanceId, prefs)

**Descrição:** Idêntico a `updateWidgetPreferences()`, porém as preferências são salvas **apenas para o usuário logado**, permitindo personalização individual.  
**Parâmetros:**

* `instanceId` (`number`): ID numérico da instância
* `prefs` (`Object`): pares chave/valor das preferências

**Retorno:** `boolean`

jstrue

## Sistema de Eventos

---

O `WCMAPI` oferece um barramento de eventos pub/sub para comunicação desacoplada entre widgets e temas. Os nomes dos eventos padrão (como `WCMAPI.LISTENER_LOGIN`) são constantes injetadas pela plataforma.

### Eventos disponíveis

|  |  |
| --- | --- |
| Constante | Quando dispara |
| `WCMAPI.LISTENER_LOGIN` | Quando o usuário efetua login |
| `WCMAPI.LISTENER_LOGOUT` | Quando o usuário efetua logout |
| `WCMAPI.LISTENER_EDITMODEON` | Quando o modo de edição é ativado |
| `WCMAPI.LISTENER_EDITMODEOFF` | Quando o modo de edição é desativado |
| `WCMAPI.LISTENER_SAVEWIDGETPREFS_OPEN` | Quando o painel de preferências de widget é aberto |
| `WCMAPI.LISTENER_SAVEWIDGETPREFS_CLOSE` | Quando o painel de preferências de widget é fechado |
| `WCMAPI.LISTENER_BEFORE_SAVEWIDGETPREFS` | Antes de salvar as preferências de widget |
| `WCMAPI.LISTENER_AFTER_SAVEWIDGETPREFS` | Após salvar as preferências de widget |

### addListener(oObj, eventName, callback, listenerName)

**Descrição:** Registra uma função de callback para ser chamada quando o evento indicado for disparado. Se um listener com o mesmo `listenerName` já estiver registrado para o mesmo evento, ele será atualizado em vez de duplicado.  
**Parâmetros:**

* `oObj` (`Object`): contexto (`this`) para o callback
* `eventName` (`string`): nome do evento (ex.: `WCMAPI.LISTENER_LOGIN`)
* `callback` (`Function`): função chamada com `(eventName, data)`
* `listenerName` (`string`, opcional): nome único do listener, padrão `'DEFAULT'`

**Retorno:** `boolean` — sempre `true`

jstrue meuWidget.mostrarControlesDeEdicao(),
    'meuWidget-editmode'
);]]>

### removeListener(eventName, listenerName)

**Descrição:** Remove um listener registrado pelo nome.  
**Parâmetros:**

* `eventName` (`string`): nome do evento
* `listenerName` (`string`, opcional): nome do listener a remover, padrão `'DEFAULT'`

jstrue

### fireEvent(eventName, data)

**Descrição:** Dispara todos os listeners registrados para o evento informado. Erros dentro de callbacks individuais são silenciados para não impedir a notificação dos demais listeners.  
**Parâmetros:**

* `eventName` (`string`): nome do evento a disparar
* `data` (`*`, opcional): payload enviado para todos os listeners

jstrue {
    console.log('Documento selecionado:', data.titulo);
}, 'visualizador-docs');]]>

### containsListener(eventName, listener, varIdx)

**Descrição:** Verifica se um listener com o nome informado já está registrado para um evento. Método interno, raramente necessário em widgets.  
**Retorno:** `boolean`

## Requisições AJAX

---

O `WCMAPI` oferece métodos CRUD padronizados que já aplicam as configurações padrão da plataforma (JSON content-type, tratamento de erros, serialização automática).

> **JWT Automático:** Todas as requisições jQuery feitas na plataforma recebem automaticamente o header `Authorization: Bearer <token>` via `$.ajaxSetup()`, desde que o cookie `jwt.token` esteja presente.

### Create(options) / Read(options) / Update(options) / Delete(options)

**Importante:** Os métodos WCMAPI.Create(), WCMAPI.Read(), WCMAPI.Update() e Delete(options) estão depreciados. Use FLUIGC.ajax() ou $.ajax() que fornece uma API mais robusta e moderna.

**Descrição:** Wrappers padronizados para chamadas AJAX com os verbos HTTP correspondentes (`POST`, `GET`, `PUT`, `DELETE`). Qualquer `options.data` que seja objeto ou array é automaticamente serializado para JSON antes do envio.  
**Parâmetros:**

* `options` (`Object`): configuração jQuery.ajax. `url` é obrigatório.
  + `options.data`: payload da requisição (auto-serializado se for objeto)
  + `options.success`: callback de sucesso com a resposta parseada

jstrue {
        console.log('Post criado com ID:', resposta.content.id);
    }
});
WCMAPI.Read({
    url: `/api/public/2.0/documents/${documentoId}`,
    success: (resposta) => {
        exibirDocumento(resposta.content);
    }
});
WCMAPI.Update({
    url: `/api/public/2.0/documents/${documentoId}`,
    data: { titulo: 'Título Atualizado' },
    success: () => mostrarMensagemSucesso()
});
WCMAPI.Delete({
    url: `/api/public/2.0/documents/${documentoId}`,
    success: () => removerDaLista(documentoId)
});]]>

### callCommand(command, data, oObj, callback, errorCallback, dataType)

**Descrição:** Realiza uma requisição GET simples, prefixando o `command` com o valor retornado por `WCMAPI.getServerURL()`. O errorCallback é opcional; se omitido, erros são ignorados silenciosamente.  
**Parâmetros:**

* `command` (`string`): caminho da URL (anexado ao valor de `getServerURL()`)
* `data` (`*`): dado repassado ao callback de sucesso e erro
* `oObj` (`Object`): contexto (`this`) para os callbacks
* `callback` (`Function`): `callback(response, data)`
* `errorCallback` (`Function`, opcional): `errorCallback(xhr, textStatus, errorThrown, data)`
* `dataType` (`string`, opcional): tipo de dado esperado, padrão `'json'`

jstrue console.log('Usuário:', response)
);]]>

### readHtml(options)

**Descrição:** Atalho para fazer uma requisição AJAX com as configurações padrão da plataforma, mescladas com as opções fornecidas.

jstrue $('#container').html(html)
});]]>

### syncAjax(url)

**Descrição:** Realiza uma requisição GET síncrona (bloqueante) e retorna o texto da resposta.  
**Parâmetros:**

* `url` (`string`): URL da requisição

**Retorno:** `string|false` — texto da resposta, ou `false` se o objeto XHR não puder ser criado

> Use com extrema moderação
>
> Requisições síncronas bloqueiam completamente a thread do navegador e estão obsoletas nos padrões modernos. Este método é usado internamente apenas nos pings de keep-alive de sessão.

### failHandler(args, styleGuide) *(usado internamente)*

**Descrição:** Tratador centralizado de erros AJAX, chamado automaticamente pelo objeto padrão retornado por `ajaxRequestDefault()`. Inspeciona o Content-Type e o status HTTP da resposta para exibir a mensagem de erro correta.

* Quando `styleGuide = true`: usa componentes FLUIGC (modais e mensagens)
* Quando `styleGuide = false`: usa os componentes legados WCMC
* Raramente você precisará chamar este método diretamente.

jstrue WCMAPI.failHandler(xhr, true)
});]]>

## OAuth

---

### validateAndAuthenticateOAuth(consumerKey)

**Descrição:** Valida o token OAuth para uma chave de consumer e, caso o token esteja ausente ou inválido, inicia o fluxo de autorização abrindo a URL do provedor em uma nova aba.  
Use este método antes de fazer chamadas a APIs de terceiros integradas via OAuth (ex: Google Drive, Dropbox).  
**Parâmetros:**

* `consumerKey` (`string`): chave do consumer OAuth da integração

**Retorno:** `boolean` — `true` se o token é válido; `false` se o fluxo de autorização foi iniciado

jstrue

### validateOAuth(consumerKey)

**Descrição:** Verifica a validade do token OAuth **sem iniciar o fluxo de autorização**. Use quando você precisa apenas verificar o status para, por exemplo, exibir um botão "Conectar".  
**Parâmetros:**

* `consumerKey` (`string`): chave do consumer OAuth

**Retorno:** `boolean` — `true` se o token é válido

jstrue

## Atributos de Sessão no Servidor

---

### setSessionAttribute(name, value) / getSessionAttribute(name)

**Descrição:** Armazena e recupera atributos na sessão HTTP do servidor via chamadas síncronas ao `WCMSpaceAPI.SessionService`.  
**Parâmetros:**

* `name` (`string`): chave do atributo de sessão
* `value` (`*`): valor a armazenar (somente para `setSessionAttribute`)

jstrue
> **Atenção:** Não funciona em modo stateless (`WCMAPI.getIsStateless() === true`).

## Utilitários JavaScript

---

### Verificação de tipos

**Legado.** Prefira os recursos nativos do JavaScript moderno: `typeof`, `Array.isArray()`, `=== null`, `=== undefined`, etc. Evite utilizar estes métodos em novos desenvolvimentos.

|  |  |  |
| --- | --- | --- |
| Método | Equivalente nativo | Retorno |
| `isUndefined(o)` | `o === undefined` | `boolean` |
| `isNull(o)` | `o === null` | `boolean` |
| `isString(o)` | `typeof o === 'string'` | `boolean` |
| `isNumber(o)` | `typeof o === 'number'` | `boolean` |
| `isArray(obj)` | `Array.isArray(obj)` | `boolean` |
| `isObject(o)` | — | `boolean` |
| `isJSON(o)` | — | `boolean` |
| `isEmpty(o)` | — | `boolean` |

jstrue

### cloneObject(source)

**Descrição:** Cria uma cópia profunda (deep clone) de um objeto ou array simples. Não copia propriedades chamadas `'clone'` para evitar referências circulares.  
**Limitação:** Não clona corretamente `Date`, `RegExp`, `Map`, `Set` ou outras classes built-in complexas — esses são copiados por referência.  
**Parâmetros:**

* `source` (`Object|Array`): objeto ou array a clonar

**Retorno:** `Object|Array`

jstrue

### replaceAll(str, de, para)

**Descrição:** Substitui todas as ocorrências de uma substring por outra. Alternativa a `String.prototype.replaceAll()` para compatibilidade com ambientes legados. Usa abordagem iterativa em vez de regex global, evitando problemas com caracteres especiais.

jstrue

### stringify(o)

**Descrição:** Serializa para JSON e então aplica `encodeURI()`. Útil para passar objetos complexos como parâmetros de URL.

jstrue

### validateXSS(data, replace)

**Descrição:** Sanitiza um valor de string ou campo de formulário contra ataques XSS usando o utilitário `FLUIGC.utilities.preventXSS`.  
Suporta dois modos:

* **String:** recebe e retorna uma string sanitizada
* **Elemento de formulário:** recebe um elemento DOM ou jQuery com `.value`, atualiza o valor no lugar e retorna o objeto jQuery
* O parâmetro `replace` quando `true` também remove as entidades `>` e `<` do resultado sanitizado.

jstrue

### emailIsValid(email)

**Descrição:** Valida se uma string é um endereço de e-mail sintaticamente válido. Não verifica a existência do domínio.  
**Retorno:** `boolean`

jstrue

### formatDateUtc(date)

**Descrição:** Formata uma data como string localizada usando a meia-noite UTC para evitar que o deslocamento de fuso horário do cliente altere o dia exibido.  
**Parâmetros:**

* `date` (`string|number|Date`): valor de data aceito por `new Date()`

**Retorno:** `string` — data formatada conforme o locale do navegador

jstrue

### generateId()

**Descrição:** Gera uma string de identificador DOM único e incremental no formato `'wcmid<n>'`. Útil ao criar elementos dinamicamente que precisam de um atributo `id` garantidamente único na página.  
**Retorno:** `string` — ex.: `'wcmid2'`, `'wcmid3'`, ...

jstrue').attr('id', id).addClass('meu-componente');
$('body').append($div);
WCMAPI.loadJS('/meuapp/componente.js', () => {
    new MeuComponente({ target: `#${id}` });
});]]>

### getZIndex()

**Descrição:** Retorna o maior valor de `z-index` em uso por elementos absolutamente ou fixamente posicionados na página. Útil ao criar modais ou overlays que precisam aparecer acima de todo o conteúdo existente.  
**Retorno:** `number` — mínimo `1`

jstrue

### getSourceImage(imageSource, options, callback)

**Descrição:** Carrega uma imagem e corrige sua orientação com base nos metadados EXIF, entregando uma URL de dados (Base64) ao callback quando necessário. Se a imagem não tiver dados EXIF de orientação, a URL original é retornada sem processamento.  
Requer a biblioteca `blueimp-load-image` carregada na página.  
**Parâmetros:**

* `imageSource` (`string`): URL ou data URL da imagem
* `options` (`Object`): opções para `loadImage()`, ex.: {{  
  Unknown macro: { maxWidth}}}
* `callback` (`Function`): `callback(src)` onde `src` é a URL original ou o Base64 corrigido

jstrue

## Utilitários de URL

---

### \_get(name)

**Descrição:** Extrai o valor de um parâmetro de query string da URL da página atual. Retorna `null` quando o parâmetro não está presente.

jstrue

### \_getParam(url, name)

**Descrição:** Extrai o valor de um parâmetro de query string de uma URL específica (não da URL atual). Usado internamente para verificar parâmetros de versão antes de adicioná-los.

jstrue

### \_getAllParams(url)

**Descrição:** Extrai todos os parâmetros de uma URL e os retorna como objeto.  
**Retorno:** `Object.<string, string>`

jstrue

### getURLParameter(name) *(função global)*

**Descrição:** Extrai o valor de um parâmetro da URL atual. Diferente de `WCMAPI._get()`, esta é uma **função global** (não método do WCMAPI).

> **Atenção:** Quando o parâmetro não existe, esta função retorna a **string** `'null'` (e não `null`). Prefira `WCMAPI._get()` em novo código para evitar comparações indevidas.

jstrue

## Configurações Globais jQuery

---

### $.cachedScript(url, options)

**Descrição:** Extensão do jQuery que carrega um script com cache habilitado no navegador. Diferente do `$.getScript()` padrão (que desabilita o cache), este helper é essencial para performance em uma plataforma onde os mesmos scripts de widget podem ser solicitados em cada carregamento de página.

jstrue

## Namespace WCM

---

O objeto global `WCM` é um namespace legado mantido por compatibilidade retroativa. Ele expõe URLs de conveniência derivadas do contexto atual do `WCMAPI`.

jstrue

## Boas Práticas

---

### Use sempre getters e setters — nunca acesse propriedades diretamente

Todas as propriedades do `WCMAPI` devem ser acessadas e modificadas exclusivamente pelos métodos `get...()` e `set...()` correspondentes. O acesso direto às propriedades (ex.: `WCMAPI.userId`) é considerado **legado**, não está documentado como API pública e pode ser removido em versões futuras.

jstrue

### Use sempre o singleton `WCMAPI`

Nunca instancie `TLib` diretamente. O objeto `WCMAPI` é criado pela plataforma com uma guarda contra instanciação dupla.

jstrue

### Prefira `convertFtlAsync` ao `convertFtl`

A versão assíncrona não bloqueia a interface enquanto aguarda a resposta do servidor.

jstrue

### Sempre chame `loadWidgets()` após injetar HTML

Qualquer HTML que contenha elementos com a classe `wcm-widget-class` precisa que `loadWidgets()` seja chamado após a injeção para que os widgets sejam inicializados.

jstrue

### Use nomes únicos para seus listeners de eventos

O sistema de eventos atualiza um listener existente quando o nome já está registrado. Nomes descritivos e únicos por widget evitam conflitos silenciosos.

jstrue

### Remova listeners ao destruir widgets

Para evitar memory leaks e comportamentos indesejados, remova os listeners ao destruir ou esconder um widget.

jstrue

### Verifique o login antes de operações sensíveis

jstrue

### Sanitize inputs do usuário com `validateXSS`

Antes de inserir qualquer conteúdo gerado pelo usuário no DOM, sanitize-o:

jstrue

## Erros Comuns

---

### "WCMAPI is not defined"

**Causa:** O script do widget está sendo executado antes do `wcmapi.js` ser carregado.  
**Solução:** Verifique a ordem de carregamento dos recursos no template do widget ou tema. O `wcmapi.js` deve aparecer antes dos scripts dos widgets.

### Listener disparando múltiplas vezes

**Causa:** `addListener` está sendo chamado mais de uma vez com o nome `'DEFAULT'` (padrão quando `listenerName` não é informado), e cada chamada atualiza o listener existente — mas se diferentes widgets usam o mesmo nome, os callbacks podem se acumular.  
**Solução:** Sempre informe um `listenerName` único e específico para seu widget.

### `getURLParameter` retornando `'null'` em vez de `null`

**Causa:** Esta função global retorna a string `'null'` quando o parâmetro não existe.  
**Solução:** Use `WCMAPI._get()` que retorna o tipo nulo correto.

jstrue

### Widget não inicializa após injeção de HTML

**Causa:** `loadWidgets()` não foi chamado após a injeção do HTML.  
**Solução:**

jstrue

### Sessão expirando mesmo com o usuário ativo

**Causa:** `extendSession()` não está sendo chamado em resposta às interações do usuário, ou o interceptor foi removido.  
**Solução:** Vincule `extendSession()` aos eventos de interação de forma global no tema:

jstrue {
    clearTimeout(timerSessao);
    timerSessao = setTimeout(() => WCMAPI.extendSession(), 500);
});]]>

### Requisições AJAX falhando com 401 em modo stateless

**Causa:** O cookie `jwt.token` não está presente ou está expirado. O `$.ajaxSetup` global injeta o token automaticamente, mas ele precisa existir.  
**Solução:** Verifique se o fluxo de autenticação está renovando o JWT corretamente. Em modo stateless (`WCMAPI.getIsStateless() === true`), toda autenticação depende do token JWT.

## Dicas de Performance

---

### Evite `isAdmin()` em loops ou na inicialização

`isAdmin()` faz uma chamada síncrona ao servidor. Guarde o resultado em cache:

jstrue {
    if (ehAdmin) {
        exibirBotaoExcluir(item);
    }
});]]>

### Prefira `convertFtlAsync` para templates pesados

Templates que carregam muitos dados ou recursos devem usar a versão assíncrona para não travar a interface enquanto o servidor processa.

### Use `WCMAPI.loadJS` para scripts de widgets, nunca `$.getScript`

`$.getScript` desabilita o cache do navegador. `WCMAPI.loadJS` usa `$.cachedScript` internamente, permitindo que o navegador faça cache dos scripts entre carregamentos de página.

### Use `WCMAPI._getParam` para verificar parâmetros de versão em URLs

Ao montar URLs para recursos externos, verifique se já existe um parâmetro `v` antes de adicionar:

jstrue

### Nomeie e remova listeners para evitar memory leaks

Em widgets com ciclo de vida bem definido (criação e destruição), sempre remova os listeners ao destruir o widget para liberar memória.

### Integração com outras APIs do Fluig

O `WCMAPI` é a **porta de entrada** — use-o para obter o contexto e, a partir dele, construa chamadas para:

* **REST API pública:** `/api/public/2.0/...` — use `WCMAPI.Read()` / `WCMAPI.Create()` etc.
* **WCMSpaceAPI:** API síncrona de baixo nível (use com cautela)
* **FLUIGC:** componentes visuais do guia de estilo Fluig
* **WCMSpaceAPI.OAuthService:** para integrações OAuth, utilize os helpers `validateOAuth` e `validateAndAuthenticateOAuth` do próprio `WCMAPI`
