---
content_hash: a270a6c5152f64026157c66ffc6059b17699486152c0700f74012a7209a264da
fetched_at: '2026-06-28T21:35:30.246830+00:00'
page_id: '820170215'
product: fluig
source: tdn-fluig
title: Causas de erros no envio de notificações por e-mail
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=820170215
version: 35
---

# Índice

Índice

# Objetivo

---

O objetivo desta documentação é reunir as maiores causas de erros, ao realizar o envio de notificações por e-mail, no TOTVS Fluig Plataforma.

# Pré-requisitos

---

* Servidores respeitando o [Modelo de dimensionamento](https://tdn.totvs.com/display/fluig/Modelo+de+dimensionamento).
* Plataforma de acordo com os padrões da [Matriz de portabilidade](https://tdn.totvs.com/display/fluig/Matriz+de+portabilidade).
* Ambiente em consonância com os ciclos de [Atualização da plataforma](https://tdn.totvs.com/pages/viewpage.action?pageId=73078235).
* Conferir outras [Especificações Técnicas](https://tdn.totvs.com/pages/viewpage.action?pageId=144409649) necessárias.
* Interesse em realizar a .

# Versão do Fluig anterior à 1.7.1-220607

---

**01.** Nessa versão, foram liberadas correções importantes relacionadas ao envio de notificações por e-mail.

**02.** Antes de prosseguir, é importante que atualize a versão de sua plataforma, conforme os ciclos de [Atualização da plataforma](https://tdn.totvs.com/pages/viewpage.action?pageId=73078235).

# Realizar a configuração do envio de e-mails

---

**01.** Para que a plataforma envie notificações por e-mail, essa configuração deve ser habilitada pelo administrador.

**02.** A configuração de e-mails pode ser feita de duas formas: por **empresa** ou **global**.

**03.** Por **empresa**, a configuração é feita individualmente e será aplicada apenas para a empresa em questão.

**04.** Já a **global**, será obedecida por todas as empresas cadastradas no Fluig.

**05.** Os parâmetros para cada uma das situações, você encontra na [Configuração de envio de e-mail](https://tdn.totvs.com/pages/releaseview.action?pageId=257623560).

# Habilitar o envio de e-mails

---

**01.** Por padrão o envio de e-mail na plataforma está habilitado após a instalação, porém, é possível que essa opção seja desativada por quem administra a empresa, assim, nenhum usuário receberá e-mails.

**02.** O usuário também pode desativar o recebimento de e-mails, caso desejar.

**03.** Para habilitar o envio de e-mails, siga os passos abaixo:

identificarPasso 1

* Acessar **Painel de Controle** → **Pessoas** →  **Notificações padrões para novos usuários**.

Passo 2

* Na sessão **Defina os meios de notificação disponíveis**,alterar os valores para **ON**.
* Lembrando que, as configurações realizadas nessa sessão específica, serão aplicadas **à todos os usuários**.

Passo 3

* Na sessão **Defina os padrões de configuração de recebimento de notificações para novos usuários**, definir quais notificações aparecerão para novos usuários.
* Nesse caso, **apenas novos usuários** serão afetados com as alterações realizadas nessa sessão.

## Saiba mais

---



# Configuração de notificações do usuário

---

**01.** Por padrão, todos os e-mails são habilitados para envio, porém, cada usuário pode alterá-los no seu perfil, conforme a sua necessidade.

**02.** Para conferir se um usuário específico receberá e-mails de notificação, verifique as configurações de notificação desse usuário, conforme os passos abaixo:

identificarPasso 1

* Acessar a plataforma e clicar sobre o ícone de **Notificações** no alto da tela.

Passo 2

* Acionar o botão de **Configurações** e escolher as notificações que deseja receber.

## Saiba mais

---



# Testar o envio de e-mails

---

**01.** Certifique-se de que foi realizada corretamente a . Na dúvida, mesmo que a tela esteja preenchida, reinicie os serviços do Fluig, pois a configuração só funciona após a reinicialização.

**02.** Para testar o envio de e-mail pela interface através da **Configuração global** siga os passos abaixo:

identificarPasso 1

* Acessar a plataforma com o usuário **wcmadmin**.
* Buscar o identificador **WCM → Configurações do Sistemas**.

Passo 2

* Acionar a aba **Parâmetros da plataforma** e preencher os campos de **Configuração de e-mail**.

Passo 3

* Clicar em **Testar conexão**.

**03.** Se você utiliza a **Configuração por empresa,** siga os passos abaixo para realizar o teste de conexão com o servidor de e-mails:

identificarPasso 1

* Acessar a plataforma com o usuário **wcmadmin**.
* Buscar o identificador **WCM → Empresas**.

Passo 2

* Selecionar a **empresa** desejada e clicar em **Editar**.

passo 3

* Acionar a aba **E-mail** e marcar **ON** na opção **Deseja habilitar o envio de e-mail?**

Passo 4

* Preencher os campos de **Configuração de e-mail** e clicar em **Testar conexão**.

Observação

Caso verifique alguma inconsistência após a realização dos passos **02** ou **03** acima, colete o log de erros do produto no caminho [diretório\_instalação]\appserver\standalone\log\server.log (a partir da **2.0**) ou [diretório\_instalação]\appserver\domain\servers\fluig1\log\server.log (**1.6 até 1.8.2**) e solicite a análise da equipe de Suporte através de um ticket na [Central do cliente](https://suporte.totvs.com/), opção **Abrir *ticket***.

# Testes complementares

---

**01.** Averiguar se você está recebendo e-mails de outros recursos do Fluig.

**02. Sugestões para testes:**

* Notificações de processos ao iniciar uma solicitação e selecionar o seu usuário como responsável;
* Notificações de processos na movimentação de solicitações (sem customizações quanto ao remetente);
* Notificações de documentos efetuando login com outro usuário, acessando uma pasta e compartilhando um documento para o seu usuário;
* Comentários nas publicações;
* Seguir usuários;
* Recuperação de senha pela opção *"Esqueceu sua senha?"*;
* Participação de usuários em comunidades, entre outras.

# Diagrama de processos

---

**01.** Verificar se as notificações estão habilitadas na configuração do diagrama do processo nas abas **Acompanhamento** e **Atraso**.

identificarPasso 1

# Spam

---

**01.** Em alguns situações, o servidor de e-mails detecta como***"spam"*** o e-mail enviado pelo Fluig, verifique se esse não é o seu caso.

**02.** Inclua o **remetente padrão** do Fluig na ***whitelist*** do seu servidor de e-mails.

# Envio de e-mails por datasets

---

**01.** Caso o envio de e-mails seja realizado por um **dataset**, solicite a análise da equipe de Suporte através de um ticket na [Central de Atendimento](https://centraldeatendimento.fluig.com/hc/pt-br), opções **Nova Solicitação** → **Suporte Técnico.**

**02.** Anexe ao ticket o **código de desenvolvimento** desse **dataset**.

# Templates de e-mail em múltiplas instalações

---

**01.** Caso possuam mais de um ambiente Fluig **(homologação/teste/desenvolvimento/produção)**, verifique se o template de e-mail está correto em todos os ambientes.

**02.** Os templates de e-mail utilizados pelo Fluig estão nos caminhos:

* *<volume>\templates\tplmail.*
* *<diretório de instalação do Fluig>\repository\wcmdir\templates\tplmail\TPL\_WCM\_MAIL\_TEST\_CONFIG.*

# Conflitos em configurações

---

**01.** Valide se há conflitos entre a **Configuração global de e-mail** e a **Configuração por empresa**. Caso você possua apenas **UMA** empresa cadastrada, recomendamos desabilitar o envio de e-mail por empresa e utilizar somente a **Configuração global** em:

* **wcmadmin → Painel de Controle** **→** identificador **WCM → Configurações do sistema**, (utilizar, preferencialmente, o **"Remetente Padrão"**).

# Envio de logs

---

**01.** No decorrer dos testes, colete capturas de tela *(printscreen)* ou faça vídeos durante a realização das verificações.

**02.** Caso nenhum dos passos acima solucione a situação reportada, envie o material e os logs para a equipe de Suporte através de um ticket na [Central de Atendimento](https://centraldeatendimento.fluig.com/hc/pt-br), opções **Nova Solicitação** → **Suporte Técnico**.
