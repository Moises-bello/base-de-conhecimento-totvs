---
content_hash: a56c0cc4f316af62b0ca8a7c0ad3ed82db5c0383ed2f2dc2a20baa10fe1221ed
fetched_at: '2026-06-28T21:35:24.451474+00:00'
page_id: '269439292'
product: fluig
source: tdn-fluig
title: Criando um ambiente de homologação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269439292
version: 75
---

4.\*ndice

# Objetivo

---

O objetivo deste guia é orientar administradores e desenvolvedores na preparação de um ambiente de homologação que seja fiel ao ambiente de produção utilizado pelos usuários da plataforma. Dessa forma, ao testar novas atualizações ou desenvolvimentos, é possível simular o comportamento da plataforma, diminuindo a chance de imprevistos, perda de dados e instabilidades no ambiente de produção.

oculto

**Observação interna: Esse procedimento foi repassado para o artigo <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360027790831>**  
**Caso tenha alguma atualização aqui, lembrar de repassar pra lá.**

# Pré-requisitos

---

* Um servidor separado do ambiente de produção e que preencha os requisitos da  e .

* Cópia da base de dados do Fluig em produção.

Importante!

O gerenciamento do banco de dados é de responsabilidade do cliente. Acione sua equipe interna de TI para obter a cópia da base de dados.

* Cópia do(s) [volume(s)](http://tdn.totvs.com/pages/viewpage.action?pageId=233766796) do Fluig em produção.

* Cópia da [pasta de instalação](http://tdn.totvs.com/x/b0sxE) do Fluig em produção (incluindo os *kits* e *widgets* personalizados na pasta appserver/apps).

# Fazer uma nova instalação

---

* Faça o *download* do pacote de instalação do Fluig no [Central do cliente](https://suporte.totvs.com/portal/p/10098/download#000035). Esse pacote deve estar na mesma atualização da base de dados copiada, ou seja, se o ambiente de produção estiver na **Update  1.6.5-190326**, a instalação no ambiente de homologação deve ser feita com essa mesma *release*. 

  Atenção!

  Caso você não tenha o pacote de instalação de mídias anteriores necessário para instalação, ficará de responsabilidade de cliente o processo de atualização da plataforma. Disponibilizaremos somente os pacotes de releases atuais no Portal de cliente para download.
* Execute o *wizard* de instalação, conforme a documentação ( / ), mas fique atento no momento de configurar o banco de dados para informar corretamente os dados de acesso **da cópia** da base de produção e não da base original. O mesmo é valido para o serviço de cache, que não deve ser compartilhado.

* Verifique também o número de licenças disponíveis no servidor de licenças, pois cada usuário ativo no ambiente de homologação consumirá uma licença.

* Após concluir a instalação, inicie os serviços do Fluig.

# Configurar a plataforma

---

Uma vez instalado o Fluig no ambiente de homologação, é necessário ajustar os dados da base copiada da produção com os dados do novo ambiente.

## Acessar o Painel de controle

---

* Acesse o Fluig no endereço que foi configurado durante a nova instalação e autentique-se com o administrador da plataforma (wcmadmin). É provável que ocorram redirecionamentos para o endereço de produção, visto que a base de dados ainda está configurada com estas informações. Se isso ocorrer, cole a URL de homologação novamente na barra de endereços do navegador.

Nota:

Caso esteja integrado ao TOTVS Identity, verifique  como acessar a plataforma com o usuário wcmadmin.

* Para acessar o Painel de Controle do wcmadmin, informe http://[fluig\_homologacao]/portal/p/wcm/cpaneladmin na barra de endereços do navegador.

## Ajustar endereço de acesso

---

Para ajustar o endereço de acesso, siga os passos da documentação [ARQ - Como alterar a URL de acesso do Fluig?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27663603084567-Fluig-Plataforma-CON-Como-alterar-a-URL-de-acesso-a-plataforma)

## Ajustar caminho do volume

---

Os volumes são utilizados pelo Fluig para armazenar os documentos, artigos, formulários, *templates* e demais arquivos publicados na plataforma. O(s) volume(s) copiados do servidor de produção para o de homologação precisam ser configurados no Painel de Controle para que a nova instalação do Fluig possa localizá-los.

* Crie uma nova pasta vazia no sistema operacional do servidor de homologação.

* Acesse o Painel de Controle do wcmadmin e selecione a opção **Volumes**.

* Selecione o volume que deseja ajustar e clique em **Editar**.

* No campo **Diretório Físico**, informe o caminho completo da pasta criada, inclusive com o nome do diretório e salve a alteração.

* Copie os arquivos salvos dentro do volume copiado do ambiente de produção para a nova pasta informada como volume no Fluig.

Fique por dentro!

Para visualizar mais detalhes e informações, acesse nossa documentação sobre .

## Configurar Fluig Analytics

---

Levando em consideração que o banco de dados replicado veio com as informações de integração do ambiente de produção é muito importante que seja alterada para o projeto de homologação ou desabilitada neste momento, pois o envio de dados configurado com o projeto de produção no ambiente de homologação irá sobrescrever as informações do ambiente de produção causando conflito.

Lembrando que o Fluig permite integrar apenas uma empresa (*tenant*) por projeto no Fluig Analytics, portanto caso você ainda não possua um projeto de homologação, é preciso solicitar via ticket para o atendimento Fluig a criação deste projeto. Siga os passos descritos na página  para solicitar o projeto e habilitar a integração.

## Verificar parâmetros

---

Acesse o menu **Painel de Controle** e o recurso **Configuração do sistema**. Na aba **Parâmetros** da plataforma verifique as informações em todos campos. Altere o que for necessário, de acordo com o novo servidor do Fluig.

Fique por dentro!

Para visualizar mais detalhes e informações, acesse nossa documentação sobre .

## Configurar TOTVS Identity

---

Levando em consideração que o banco de dados replicado veio com a integração habilitada ou mesmo, que se queira habilitar a integração com o TOTVS Identity homologação, será necessário atualizar ou incluir as informações de integração neste momento.

Para isso, é imprescindível ter as informações do  do TOTVS Identity para posteriormente seguir os passos descritos na página .

## Configurar autenticação integrada

---

Criando o ambiente de homologação usando a replicação do banco de dados da aplicação de produção, as informações da tela de Autenticação Integrada da plataforma estarão preenchidas, portanto será necessário ajustá-las realizando uma nova configuração da autenticação integrada para o ambiente de homologação.

Siga os procedimentos informados na página . Recomendamos que seja gerado um novo Token de autenticação. Além disso, é preciso criar um novo arquivo 'remote\_auth.asp' e salvá-lo em um novo diretório do IIS, porém, não é necessário reconfigurar o(s) navegador(es).

## Copiar os *widgets* personalizados

---

Caso faça uso de *kits* ou *widgets* personalizados no ambiente de produção, é necessário copiá-los manualmente para a pasta [instalação\_fluig]/appserver/apps no ambiente de homologação.

Importante!

Copie apenas os *widgets* personalizados ou adquiridos via Fluig Store. Os demais *widgets* são padrão do Fluig e estarão na nova instalação automaticamente.

# OAuth Providers

---

Caso possua integrações REST configuradas em seu ambiente de produção através do cadastro OAuth Provider e OAuth App, é necessário editar e revisar os apontamentos de URL de todos os OAuth Provider cadastrados em seu novo ambiente de homologação.

Para realizar esta análise é preciso estar logado com um usuário **administrador**. Acesse o menu **Painel de Controle**, localize o agrupador **Parâmetros técnicos** e acione o recurso **OAuth Provider**.

Fique por dentro!

Para visualizar mais detalhes e informações, acesse nossa documentação sobre .

# Serviços

---

As integrações JDBC e REST cadastradas em seu ambiente através do ícone Serviços devem ter suas URL de apontamentos revisadas.

As integrações SOAP cadastradas como serviços em seu ambiente são mais sensíveis a mudanças como esta, pois além do cadastro no banco também têm alguns arquivos que são gerados no servidor. Portanto, caso a URL dos serviços SOAP de homologação sejam diferentes das de produção, as mesmas devem ser **excluídas e recadastradas**.

Para realizar estas verificações é preciso estar logado com um usuário administrador. Acesse o menu **Painel de Controle**, localize o agrupador **Desenvolvimento** e acione o recurso **Serviços**.

Fique por dentro!

Para visualizar mais detalhes e informações, acesse nossa documentação sobre .

# Reiniciar o Fluig

---

Uma vez concluídos todos os passos acima, para que as alterações sejam aplicadas, reinicie os serviços do Fluig na seguinte ordem : 1º fluig\_Indexer, 2º fluig\_RealTime, 3º fluig.

Quando a plataforma estiver no ar, pode-se usar os mesmos logins e senhas do ambiente de produção para autenticar-se no ambiente de homologação.

$("b:contains('oculto')").parent().parent().hide();
]]>
