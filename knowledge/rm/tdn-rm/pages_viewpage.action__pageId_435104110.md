---
content_hash: 729265a4d1dff5d80098cc3f93173b4916aba603b0bf1f6610c26d0fd2d43b39
fetched_at: '2026-06-29T00:09:45.944327+00:00'
page_id: '435104110'
product: rm
source: tdn-rm
title: TOTVS Gestão de Pessoas x TOTVS e-Learning Management SUITE (LMS) - Configuração
  e Parâmetros TOTVS LMS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104110
version: 4
---

**Configuração e Parâmetros TOTVS e-Learning Suíte - LMS**

---

**TOTVS EAI**  
    
 O EAI é uma ferramenta que permite a integração entre ERPs configurando e gerenciando a troca de mensagens estre esses. Através do EAI é possível registrar mensagens enviadas e recebidas, rastrear a execução das mensagens, gerenciar filas de execução, configurar canais de comunicação, etc. O EAI está incluído no instalador do LMS.   
 O EAI tem como objetivo criar a conexão que integrará os módulos TOTVS Educacional x TOTVS LMS.   
 Durante sua configuração são inseridas as credenciais para conexão ao TOTVS LMS e definido o Webservice de acesso ao TOTVS Educacional, permitindo a integração entre os dois sistemas.  
     
 **Configuração**

**Configurando o Console EAI**

**1** - Para executar o configurador acesse: LMS / Configurações / Console EAI

**2** - Clique em Next selecione TOTVS e-Learning Suíte - LMS no campo Host Application Preset.

**3** - Clique novamente em Next e insira um usuário e senha com permissão de acesso ao LMS e às funcionalidades básicas da integração (vide Parametrização abaixo). Os demais dados não são obrigatórios.

**4** - Após preenchimento dos dados de conexão , clique em Finish e, em seguida, em OK.

**Habilitar as mensagens da Integração**

**1** - Acesse a aba ***Configuration*** no console EAI.

**2** - Clique sobre a transação que deseja configurar e selecione, na coluna ***Mode Options***, a opção de envio da mensagem (*Send*, *Receive* ou *Both*). Para as transações *WHOIS* selecione a opção *Both*.

**3** - Após habilitar as transações, clique em ***Save Changes***.

**Adicionar o TOTVS Educacional como Aplicativo Externo**

Para que a integração conecte os sistemas é necessário que seja informado o endereço de Webservice do TOTVS Educacional e as suas credenciais de autenticação.

1 - Para isso acesse: LMS / Configurações / Console EAI.

2 - Selecione Configuration / External Application / Add New External Application.

3 - Preencha os campos:

* + **WSDL Adress:** Endereço que identifica o local onde o Webservice está instalado.
  + **Port name:** porta de acesso ao Webservice.
  + **User Id:** usuário com permissão de acesso ao Webservice
  + **Password:** Senha de acesso ao Webservice.

**4** - Selecione Next e, em seguida, Finish.

**Configurando as Rotas**

**1** - Acesse a aba ***Configuration*** no console EAI e, em seguida, a opção ***Host Application***.

**2** - Na nova tela, acesse a opção Send Routes.

**3** - Selecione, então, o Aplicativo Externo, selecione as rotas que deseja habilitar e clique em ***Save Changes***.

**Parametrização da integração**

Os seguintes cadastros devem ser efetuados no LMS:

* **Usuário da Integração:** usuário que será informado no EAI ao efetuar sua configuração inicial. Esse usuário deve possuir as permissões (perfil) necessárias para efetuar os cadastros dos dados vindos do TOTVS Educacional.
* **Perfil Professor:** Perfil referente às permissões cabíveis à professores. Esse perfil será informado no TOTVS Educacional e será enviado nas mensagens de aluno (*student*) identificando-o como tal.
* **Perfil Aluno:** Perfil referente às permissões cabíveis à alunos. Esse perfil será informado no TOTVS Educacional e será enviado nas mensagens de professor (*professor*) identificando-o como tal.
