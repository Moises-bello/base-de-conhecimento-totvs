---
content_hash: 09557e2f6f3ecfa53b71cfef8470af3d3714f53b7598f8862fa87957a32102ab
fetched_at: '2026-06-29T00:11:04.242295+00:00'
page_id: '625762670'
product: rm
source: tdn-rm
title: FAQ - Meu eduCONNECT
type: documentation
url: https://tdn.totvs.com/display/LRM/FAQ+-+Meu+eduCONNECT
version: 95
---

**Bem-vindo(a) à Central de Ajuda do Meu eduCONNECT!**

Sabemos que o seu tempo é valioso e que a tecnologia deve ser uma facilitadora na sua jornada educacional. Por isso, preparamos este espaço para ajudar você a resolver dúvidas e solucionar pequenos imprevistos de forma rápida, simples e autônoma.

Neste guia, reunimos as respostas para as perguntas mais frequentes dos nossos usuários e o passo a passo para você aproveitar ao máximo todas as funcionalidades do aplicativo escolar.

Quais são os pré-requisitos para utilização do TOTVS Educa Mobile?

Antes de prosseguir com as soluções apresentadas neste FAQ, é fundamental garantir que o seu ambiente esteja configurado corretamente e que todas as dependências iniciais estejam validadas.

Por favor, verifique se todos os pré-requisitos foram atendidos seguindo a documentação oficial do sistema:   
  
👉 **[Acessar a Documentação de Pré-requisitos]** [Documentação de Pré-requisitos](https://tdn.totvs.com/x/sgEXEQ)

Como validar a regra de parametrização?

Após validar os pré-requisitos, certifique-se de que o sistema está parametrizado de acordo com as regras de negócio e técnicas exigidas para esta operação.

A regra de parametrização deve ser conferida detalhadamente conforme a documentação oficial:

👉 **[Acessar a Documentação de Parametrização]** [Documentação de Parametrização](https://tdn.totvs.com/x/5WscEQ)

Como realizar os testes no ambiente do cliente?

Caso o cliente utilize um **App personalizado (White Label)**, é necessário isolar o problema realizando os testes cruzados descritos nas etapas abaixo. Isso ajuda a identificar se a falha está no aplicativo, na versão do ambiente (RM) ou no certificado do servidor.

Siga o roteiro de validação abaixo e compare os resultados:

#### 🟩 Etapa 1: Validação no Ambiente do Cliente

* Acesse o ambiente de produção do cliente utilizando o **App personalizado** dele e verifique se o erro persiste.

#### 🟨 Etapa 2: Validação no Ambiente de Suporte (Versão Atualizada) + App do Cliente

* Acesse o ambiente de suporte (com a versão do RM totalmente atualizada), realize o login utilizando o **App personalizado** do cliente e verifique o resultado.

#### 🟦 Etapa 3: Validação no Ambiente de Suporte (Versão Atualizada) + App Genérico

* Acesse o ambiente de suporte (com a versão do RM totalmente atualizada), realize o login utilizando o **App genérico padrão** disponível oficialmente na **Google Play** ou **Apple Store** e verifique o resultado.

> 🎯 **O que essa validação resolve?**
>
> * Se o erro ocorrer apenas na **Etapa 1**, o problema provavelmente está no ambiente desatualizado do cliente ou na cadeia de certificados do servidor dele (conforme corrigido no primeiro passo deste FAQ).
> * Se o erro ocorrer nas **Etapas 1 e 2**, mas não na 3, o problema está especificamente no pacote do **App personalizado** que precisa ser gerado novamente/atualizado.

Como validar o certificado do cliente?

Aqui está a formatação ideal para este bloco de validação externa, destacando a ferramenta da DigiCert:

### 🔍 Validação Externa da Cadeia de Certificados

Para garantir que o servidor está enviando a cadeia de certificação completa de forma correta (sem depender de downloads extras pelos dispositivos móveis), faça uma checagem externa utilizando o validador da DigiCert.

Siga os passos abaixo:

1. Acesse a ferramenta oficial:

   👉 **[Acessar o DigiCert SSL Installation Diagnostics Tool](https://www.digicert.com/help/)**
2. No campo **Server Address**, informe a URL completa do seu **TOTVS Educa Mobile** (ex: `[https://seuportal.com.br](https://seuportal.com.br)`).
3. Clique em **Check Server**.

Quais são as configurações básicas do TOTVS Educa Mobile?

Caso as validações anteriores apontem a necessidade de uma análise mais detalhada ou se precisar garantir que o serviço do **TOTVS Educa Mobile** esteja respondendo corretamente, siga as etapas abaixo:

#### 1. Ativação do Modo de Suporte no Web.config

1. No servidor onde o serviço está instalado, navegue até a pasta raiz do **TOTVS Educa Mobile**.
2. Localize e abra o arquivo `Web.config` utilizando um editor de texto (como o Notepad++ ou Bloco de Notas como Administrador).
3. Procure pela tag `<appSettings>` e altere (ou adicione, caso não exista) a seguinte chave para habilitar o modo de diagnóstico:

XML

```
<add key="SUPORTE" value="true" />
```

1. 1. Salve e feche o arquivo.

2. Verificação de Status do Serviço

1. Para confirmar se o barramento e as APIs do Educa Mobile estão ativos e respondendo adequadamente, acesse a URL de status diretamente do navegador do servidor (ou substituindo `localhost` pelo domínio correspondente se testado externamente):

   👉 **`http(s)://localhost/EducaMobile/status`**

Validação do Ambiente via Chamadas de API (URL Rewrite)

250

Uma forma eficaz de isolar se o problema é de infraestrutura do cliente (roteamento/IIS) ou da aplicação é testar os endpoints da API com e sem a regra de **URL Rewrite** ativa.

Realize os dois testes de requisição abaixo (utilizando ferramentas como Postman, Insomnia ou o próprio navegador):

#### 🧪 Teste 1: Chamada COM a regra do Rewrite

Utilize a URL padrão que passa pelo gateway/IIS do cliente:

> **URL:** `http://IP_DO_CLIENTE/EducaMobile/api/educational/v1/educonnect/parameters/GUID_DO_CLIENTE`

* **Se retornar erro nesta chamada:** O problema está na configuração do **URL Rewrite** ou nas regras de redirecionamento do IIS do cliente. A regra de Rewrite deve ser revisada e corrigida no servidor dele.

#### Teste 2: Chamada SEM a regra do Rewrite (Direto no Host)

Utilize a URL apontando diretamente para a porta onde o serviço Host do RM está rodando, contornando o IIS/Rewrite:

> **URL:** `http://IP_DO_CLIENTE:PORTA_HOST/api/educational/v1/educonnect/parameters/GUID_DO_CLIENTE`

* **Se o retorno desta chamada ocorrer normalmente:** Isso **confirma e reforça** que a aplicação (RM/Educa Mobile) está saudável e que a falha está estritamente localizada no ambiente/infraestrutura de rede do cliente (IIS/Rewrite/Firewall).

Por que ocorre o erro "Erro interno do servidor" ao autenticar no Meu eduCONNECT?

Ao tentar realizar a autenticação no aplicativo **Meu eduCONNECT**, o sistema retorna a mensagem de **"Erro interno do servidor"**.

Ao tentar isolar o problema realizando testes de requisição via **POSTMAN**, o retorno da API não vem em formato JSON estruturado, mas sim como uma **página HTML**. Isto indica que a requisição está sendo interceptada e bloqueada antes mesmo de chegar à aplicação RM.

### 🎯 Causa

Esse comportamento ocorre devido a **bloqueios de segurança e firewalls** no ambiente de rede do cliente. É muito comum em cenários onde o cliente utiliza serviços de proteção contra ataques DDoS ou proxy reverso, como o [Cloudflare](https://www.cloudflare.com/), que impedem a autenticação direta vinda de ferramentas externas ou servidores de nuvem sem a devida liberação (Whitelisting).

### 🛠️ Solução Recomendada

Para resolver o problema, é necessário que o time de infraestrutura do cliente identifique o bloqueio e adicione os IPs de saída do barramento do Meu eduCONNECT à lista de permissões (IP Allowlist).

#### Ações Imediatas:

1. **Validar com a Infraestrutura:** Acione a equipe de segurança/redes do cliente para verificar os logs do firewall ou do Cloudflare no momento exato da tentativa de login.
2. **Ambiente de Testes:** Para validações via POSTMAN, solicite que liberem temporariamente a rota de teste ou forneçam um endpoint sem a camada de bloqueio do proxy.

### 🌐 Lista de IPs para Liberação no Firewall

As requisições do Meu eduCONNECT partem de uma estrutura hospedada no Microsoft Azure. O time de infraestrutura do cliente deve liberar o tráfego de entrada para os IPs abaixo, utilizando a porta padrão de segurança:

* **Porta padrão para a API:** `443` (HTTPS)

| **API do Meu eduCONNECT** | **IPs de Saída (Outbound)** |
| --- | --- |
| `[https://educonnect.azurewebsites.net](https://educonnect.azurewebsites.net)` | `104.214.95.11`, `104.214.94.211`, `40.74.248.68`, `13.84.181.47` |
| `[https://educonnect-2.azurewebsites.net](https://educonnect-2.azurewebsites.net)` | `104.214.95.11`, `104.214.94.211`, `40.74.248.68`, `13.84.181.47` |
| `[https://educonnect-3.azurewebsites.net](https://educonnect-3.azurewebsites.net)` | `104.214.95.11`, `104.214.94.211`, `40.74.248.68`, `13.84.181.47` |
| `[https://educonnect-hml.azurewebsites.net](https://educonnect-hml.azurewebsites.net)` *(Homologação)* | `4.249.240.6`, `52.165.220.33` |

> 📌 *Nota: Embora os IPs de produção sejam idênticos para as três primeiras APIs, eles foram listados individualmente para facilitar o entendimento e permitir atualizações ou segregações futuras de forma independente.*

### ⚠️ Observações Importantes (Atenção ao tipo de APP)

* **Versão Padrão do APP:** A lista de IPs acima é válida **apenas** para os clientes que utilizam o aplicativo Meu eduCONNECT padrão (baixado direto das contas oficiais da TOTVS nas lojas).
* **App Personalizado (White Label / Loja Própria):** Se o cliente possui um aplicativo customizado com publicação própria, ele utiliza APIs exclusivas e consequentemente **IPs diferentes** dos listados acima. Nestes casos, é obrigatório contatar a equipe de desenvolvimento do APP para coletar os IPs de saída corretos.

### 💡 Contexto de Referência (Caso de Sucesso)

Em um cenário real com a estrutura **TOTVS CLOUD**, o servidor do cliente possuía uma regra estrita de *Geoblocking*, permitindo requisições originadas apenas do Brasil e da Itália. Como os servidores do Azure podem eventualmente rotear tráfego por outras regiões, o login falhava.

O problema foi solucionado de forma definitiva assim que o time de CLOUD da TOTVS recebeu as faixas de IP de saída listadas acima e as cadastrou como exceção no firewall do servidor do cliente.

Ao autenticar na parametrização do Meu eduCONNECT, o sistema exibe a mensagem:"Não foi possível estabelecer comunicação com o eduCONNECT"

👤 Regra de Usuário para Integração (Acesso Restrito)

Ao configurar a integração, a escolha do usuário utilizado no processo é crucial para evitar falhas de permissão ao salvar as configurações.

#### 🚫 Problema

O usuário utilizado para a integração **não pode ser um Responsável** (Pai, Mãe, Responsável Financeiro ou Responsável Acadêmico) de outros alunos/usuários no sistema.

Usuários vinculados como responsáveis possuem um perfil de acesso restrito no ecossistema RM. Essa restrição **impede a alteração e gravação das opções de temas do aplicativo** na aba *eduCONNECT (3/5)* dos parâmetros do sistema.

#### 🛠️ Soluções Recomendadas

Para resolver esse bloqueio de permissão, siga uma das duas alternativas abaixo:

* **Alternativa A (Recomendada):** Criar ou utilizar um usuário exclusivo para a integração (ex: um usuário de serviço/revisão técnica) que **não possua nenhum vínculo de parentesco ou responsabilidade** com terceiros no sistema.
* **Alternativa B:** Caso precise manter o mesmo usuário, acesse o cadastro dele no RM e **desvincule-o temporariamente** de todos os outros alunos/usuários. Isso removerá a trava de perfil restrito, permitindo que ele acesse e salve todas as funcionalidades necessárias na parametrização do Meu eduCONNECT.
O download de materiais ou relatórios fica travado em "loading" (carregando) no menu Acadêmico

#### 🚫 Problema

Ao acessar o menu Acadêmico no aplicativo e tentar realizar o download de materiais (seja da Instituição ou da Disciplina) ou emitir Relatórios, o sistema exibe o ícone de carregamento (*loading*) indefinidamente e o arquivo nunca é baixado no dispositivo.

### 🔍 Cenário 1: Problema na Cadeia de Certificados SSL

#### 🎯 Causa

Esse comportamento geralmente ocorre devido a falhas, expiração ou inconformidades no certificado SSL do servidor do cliente, impedindo que o dispositivo móvel estabeleça uma conexão segura confiável para transferir o arquivo.

#### 🛠️ Solução

A validação estrita do certificado é essencial para que os downloads e relatórios funcionem corretamente no TOTVS Educa Mobile. Faça a checagem seguindo os passos:

1. Acesse o site de verificação:

   👉 **[Acessar DigiCert SSL Checker](https://www.digicert.com/help/)**
2. No campo **Server Address**, informe **apenas a URL base / domínio** do cliente (remova o sufixo `/EducaMobile` ou `/TotvsEducaMobile`).

   * *Exemplo de URL do portal:* `https://portal.cliente.com.br/EducaMobile/`
   * *O que digitar no campo:* `portal.cliente.com.br`
3. Verifique no relatório gerado se o certificado é totalmente válido, se a cadeia intermediária está completa e se não há alertas de certificado expirado.

### 🌐 Cenário 2: Porta 443 explícita em ambientes TCLOUD

#### 🎯 Causa

Identificamos que em ambientes hospedados no **TOTVS Cloud (TCLOUD)**, a porta padrão utilizada para conexões seguras é a `443`. No entanto, como a porta 443 funciona como um *endpoint* virtual padrão do protocolo HTTPS, os navegadores e requisições *mobile* tendem a ignorá-la/omití-la automaticamente na escrita da URL.

Se a porta `443` for digitada de forma **explícita** nas parametrizações internas do RM, isso quebra a lógica de navegação do eduCONNECT, gerando falhas e travamentos nos downloads.

#### 🛠️ Solução

Mesmo que no painel do TCLOUD a porta do ambiente conste formalmente como 443, ela deve ser omitida das configurações da aplicação.

1. Acesse os parâmetros de configuração do sistema através do **RM.exe**.
2. Vá até a tela de configuração das URLs do **EducaMobile**.
3. **Remova a porta :443** do final do endereço do link informado.

   * *Como estava:* `https://portal.cliente.tcloud.totvs.com.br:443/EducaMobile`
   * *Como deve ficar:* `https://portal.cliente.tcloud.totvs.com.br/EducaMobile`
4. Salve as alterações e teste novamente o download pelo aplicativo.

Erro de "Falha de autenticação" no Novo Meu eduCONNECT

#### 🚫 Problema Ao tentar logar no aplicativo novo Meu eduCONNECT, o sistema apresenta a mensagem de erro "Falha de autenticação". No entanto, o login funciona normalmente no app antigo ou no Educamobile.

Abaixo estão listadas as 3 principais causas e soluções para este incidente.

### 🔍 Causa 1: Verificação de versão mínima e configuração do URL Rewrite (OBRIGATÓRIA)

#### 🚫 Problema As APIs do novo Meu eduCONNECT utilizam o novo padrão de API da TOTVS, que exige a configuração de um *URL Rewrite* no servidor. Essa exigência tem o objetivo de proteger o host e evitar que ele fique exposto externamente.

**Passo a passo para verificação do ambiente:**

1. Execute uma chamada de API no novo formato pelo navegador.

   * **Exemplo (Verbo GET):** `<URL_do_Cliente>/api/imb/v1/versions`
   * *Essa API retornará dados da versão e patch do cliente.*
2. **Análise do Retorno:**

   * **Erro 502 (Bad Gateway):** Verifique a configuração do URL Rewrite no IIS do cliente, pois ela está incorreta ou ausente.
   * **Erro 404 (Not Found):** Possivelmente o cliente está em uma versão antiga do sistema, sem os recursos e APIs necessários para o app funcionar.
   * **Retorno com Sucesso (mas ainda com erro de login):** Verifique se os patches das versões retornadas estão de acordo com o documento oficial de pré-requisitos: [Pré-requisitos Meu eduCONNECT (TDN)](https://tdn.totvs.com/pages/viewpage.action?pageId=789398485).

### 🔍 Causa 2: Problemas com o Certificado SSL (Especialmente no Android)

#### 🚫 Problema Caso o problema ocorra apenas em alguns aparelhos, principalmente no **Android 13** ou versões específicas, é altamente provável que o erro esteja relacionado à configuração do Certificado SSL do cliente.

#### Validação Geral do Certificado

Recomendamos a validação do Certificado do servidor por meio de ferramentas como o [Digicert SSL Help](https://www.digicert.com/help/) ou [Qualys SSL Labs](https://www.ssllabs.com/ssltest/).

Se o relatório apresentar baixa confiabilidade ou incompatibilidade, sugerimos as seguintes ações:

* Instalar no servidor um novo Certificado SSL atualizado, garantindo suporte ao **TLS 1.2 ou superior**.
* Desabilitar protocolos antigos e vulneráveis de SSL/TLS.
* Realizar testes com outro Certificado de uma Autoridade Confiável (caso não possuam, indicamos a emissão de um certificado gratuito para testes via [ZeroSSL](https://zerossl.com/)).

#### Erro de Revogação (CRL / OCSP)

Durante o teste no SSL Labs, pode ocorrer o seguinte erro:

> ❌ `Revocation status Validation error` ❌ `CRL ERROR: IOException occurred`

Isso indica que o celular/sistema não conseguiu verificar a lista de revogação do certificado (CRL). As possíveis causas são bloqueios de rede. **Solicite ao cliente que valide:**

1. Se o servidor possui acesso liberado à internet para a URL da CRL/OCSP indicada no certificado.
2. Se não há bloqueios de **Firewall ou Proxy** impedindo a comunicação externa do servidor.
3. Se a URL da CRL está acessível manualmente (ex: via navegador ou comando `curl`).

### 🔍 Causa 3: Cadeia de Certificação Incompleta no IIS (Ex: ZeroSSL)

**Problema:** Ao realizar o teste no Qualys SSL Labs (ex: para o domínio do cliente), o relatório apresenta a seguinte falha na seção de cadeia de certificação:

> ❌ **Chain issues: Incomplete** (Falta o certificado intermediário, ex: *ZeroSSL RSA DV SSL CA 2* ou similar). *(Aviso normal e não crítico que pode aparecer junto: Extra download Sectigo Root).*

**🎯 Causa Raiz:** Esse comportamento ocorre porque o servidor Windows (IIS) **não possui o certificado intermediário** instalado em seu repositório local. Isso faz com que o servidor não envie a "Cadeia Completa" para o celular. Sistemas rigorosos, como o Android 13, bloqueiam a conexão imediatamente ao notar a falta deste arquivo.

**🛠️ Passo a Passo para Correção (No Servidor Windows/IIS do cliente):**

1. **Download do Certificado Intermediário:** Baixe o arquivo do certificado intermediário fornecido pela sua autoridade certificadora. *(Exemplo para ZeroSSL: [Baixar ZeroSSLRSADVSSLCA2.crt](https://www.google.com/search?q=http://crt.sectigo.com/ZeroSSLRSADVSSLCA2.crt))*
2. **Instalação no Repositório Correto:**

   * Dê um duplo clique no arquivo `.crt` baixado diretamente no servidor Windows.
   * Na janela, clique em **Instalar Certificado...**
   * Selecione a opção **Máquina Local** (Local Machine) e avance.
3. **Seleção do Repositório (Item Crítico):**

   * Selecione a opção: *"Colocar todos os certificados no repositório a seguir"*.
   * Clique em **Procurar...**
   * Selecione a pasta **Autoridades de Certificação Intermediárias** (Intermediate Certification Authorities) e clique em OK.
   * Avance e clique em **Concluir**.
4. **Atualização do IIS:**

   * Abra o **Gerenciador do IIS**.
   * Vá nas **Associações (Bindings)** do site.
   * Edite a porta 443 (HTTPS). No campo do certificado, apenas **selecione o seu certificado novamente** na lista e clique em OK. Isso forçará o IIS a recarregar a cadeia completa.
   * *(Opcional)*: Reinicie o serviço de IIS pelo prompt usando `iisreset`. Refaça o teste no SSL Labs clicando em "Clear cache" para validar a correção.

Erro na Recuperação de Senha do novo Meu eduCONNECT

#### 🚫 Problema Ao tentar utilizar a funcionalidade de recuperação de senha no aplicativo novo Meu eduCONNECT, o usuário se depara com a seguinte mensagem de erro:

> ❌ *"Erro no envio de e-mail. Favor procurar a instituição."*

**Causa:** Este erro ocorre quando o sistema não consegue se comunicar com o servidor de disparo de e-mails (SMTP). Geralmente, isso é causado por configurações ausentes, credenciais inválidas ou portas bloqueadas nos parâmetros do sistema.

### 🎯 Solução: Configuração dos Parâmetros de E-mail

Para solucionar o problema de envio de e-mail de recuperação de senha, é necessário verificar e configurar corretamente os parâmetros de disparo dentro do sistema da linha RM.

**Navegue até o seguinte caminho no sistema:** 👉 `Educacional` > `Ambiente` > `Parâmetros` > `Parâmetros Globais` > `Envio de e-mails`

Nesta tela, valide rigorosamente as seguintes **configurações obrigatórias**:

#### 1. Parâmetros da Coligada Atual

Certifique-se de que todos os dados de conexão do remetente estão preenchidos de forma correta e atualizados:

* **Servidor SMTP** (Ex: *[smtp.office365.com](http://smtp.office365.com)*, *[smtp.gmail.com](http://smtp.gmail.com)*)
* **Usuário e Senha** de autenticação da conta de e-mail.
* **Porta** de comunicação (geralmente *587* ou *465*).
* **Configurações de Segurança** (marcar a opção de conexão SSL/TLS, caso exigido pelo provedor de e-mail).

#### 2. Parâmetros Globais (Quando aplicável)

Verifique qual é a origem definida para o remetente. Se a opção **"E-mail da coligada global"** estiver selecionada como remetente oficial, será estritamente necessário validar a configuração na Coligada 0 (Global) também:

* Servidor SMTP.
* Usuário e Senha de autenticação.
* Porta e configurações de conexão SSL/TLS.

> 💡 **Dica de Validação:** Após ajustar as configurações de Servidor, Porta, Usuário, Senha e SSL/TLS, utilize o recurso de "Testar envio de e-mail" (se disponível na tela de parâmetros) para garantir que o sistema conseguiu se comunicar com o provedor antes de pedir para o usuário testar novamente no aplicativo. A configuração adequada desses parâmetros é essencial para o funcionamento do fluxo de *"Esqueci minha senha"*.

Mensagens da Sala de Atendimento não chegam no iOS

#### 🚫 Problema As mensagens enviadas nas Salas de Atendimento não são recebidas pelos atendentes quando estes estão utilizando dispositivos iOS (iPhone/iPad). Em outras plataformas o recebimento ocorre, mas no iOS as mensagens em tempo real não chegam.

**Causa:** Falha na configuração da comunicação em tempo real (geralmente baseada em WebSockets/SignalR) no servidor. O sistema operacional iOS é rigoroso quanto à validação das conexões contínuas. Para que a comunicação bidirecional funcione perfeitamente, o servidor precisa estar explicitamente configurado para habilitar o tráfego em tempo real e reescrever as URLs de resposta corretamente no Proxy/IIS.

### 🎯 Solução: Ativação do RealTime e Regra de Outbound

Para que as conversas em tempo real aconteçam normalmente, duas configurações atuando em conjunto são OBRIGATÓRIAS no servidor onde a aplicação está hospedada:

#### Passo 1: Habilitar o parâmetro nos Hosts

Acesse os arquivos de configuração (`.config`) dos hosts responsáveis pela aplicação e verifique a presença da tag de ativação. É obrigatório que a seguinte chave esteja declarada com o valor `true`:

XML

```
<add key="ENABLEREALTIME" value="true" />
```

#### Passo 2: Configuração do URL Rewrite (Educamobile)

Além de habilitar a tag acima, é **OBRIGATÓRIA** a existência da regra de saída (*Outbound Rule*) no módulo de URL Rewrite do site do Educamobile no IIS. Essa regra garante que as respostas do servidor sejam reescritas com o cabeçalho correto para manter a conexão aberta no iOS.

**Adicione a regra abaixo nas configurações de URL Rewrite do IIS:**

xml













]]>

Essa regra ajusta o endereço da API utilizada para conversas em tempo real incluindo o endereço correto do Educamobile para que a conexão ponto a ponto entre dispositivo e sala de atendimento seja feita corretamente.

IMPORTANTE

A mesma já está sendo tratada nos instaladores de patches e releases a partir das versões abaixo:

* 12.1.2402.311
* 12.1.2406.301
* 12.1.2410.298
* 12.1.2502.205
* 12.1.2506.151

Caso queira inserir a regra manualmente, a mesma deverá ser incluída no web.config do Educamobile abaixo da regra de Inbound já existente.

Segue exemplo que deverá ser adaptado conforme ambiente do Educamobile configurado (Lembrando que o instalador trata a inclusão da regra)

xml
























]]>

Ao final da inclusão, ao editar a regra no URL Rewrite, a mesma ficará de forma semelhante às imagens abaixo:
