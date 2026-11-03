---
article_id: 360018358172
category: Meu RH - Login
content_hash: 06b31887f9cbd3bc9c1b6bbe4b6f69bc96fdbb11248b8e14f19928848de0af17
fetched_at: '2026-06-28T22:47:27.322565+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Como criar usuários para acesso ao Meu RH
type: support-article
updated_at: '2026-03-06T20:48:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018358172-RH-RM-Meu-RH-Como-criar-usu%C3%A1rios-para-acesso-ao-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24083522332951) Tempo aproximado para leitura: 00:01:55 min**  
  
**Dúvida**  
Como criar e dar permissão de acesso aos usuários no Meu RH.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.17  
  
**Solução**  
Para conceder as permissões de acesso ao Meu RH, siga os passos abaixo:

Acesse a rotina **Inclusão de Usuário para Acesso ao RM Portal**, que permite criar ou atualizar usuários de acesso ao Meu RH para um ou mais funcionários.

É importante observar que a permissão será criada para o módulo em que a rotina estiver sendo executada. Por exemplo:

* Se estiver no módulo **Folha de Pagamento**, a permissão será criada para esse módulo.
* Caso esteja em outro módulo, como **Gestão de Pessoas**, a permissão será criada apenas para esse módulo.

Para acessar o **Meu RH** é obrigatório que os funcionários possuam permissão no **módulo de Folha de Pagamento**.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6445340194199)

Selecione um código de acesso ao banco de dado**s** e o Perfil referente ao módulo que o funcionário deverá ser vinculado. Informe a **data de início**, que determinará a partir de quando o funcionário terá acesso ao Meu RH.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6775675917847)  
  
Nos parâmetros, escolha quais configurações serão utilizadas para a definição do usuário e da senha dos funcionários.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38802120654743)

Detalhes sobre os parâmetros:

* O **código do grupo** possibilita selecionar o grupo de quiosque que foi criado em "**Parâmetros do RM Portal**".
* O parâmetro **"Usuário deve alterar a senha no próximo login"** serve para forçar a troca da senha de um usuário. Assim, na próxima vez que o usuário logar no sistema será solicitado a troca da senha.
* Se o parâmetro **"Definir CPF como senha default"** estiver selecionado, a senha gerada será o CPF do usuário.
* Caso **nenhum parâmetro esteja marcado**, o sistema utilizará o **último nome** do usuário como senha.
* Ao selecionar **"Utilizar número da coligada e chapa para código de acesso"**será feita a união dos códigos para criação do usuário.
* O parâmetro **"Utiliza CPF para código de acesso"** foi disponibilizado para que o sistema crie o usuário utilizando o número de CPF cadastrado para o funcionário. Caso não defina CPF como senha default ou não exista CPF cadastrado para o funcionário, quando utilizar CPF como senha default, o sistema incluirá a chapa como código de acesso e a senha será o último nome do funcionário com letras maiúsculas.
* Ao marcar o parâmetro **"Atualizar permissões para usuário existente",** caso o funcionário já possua um usuário vinculado, o sistema irá atualizar os dados abaixo:
  + Código de acesso ao banco
  + Perfil
  + Validade
  + Código do Grupo
  + Usuário deve alterar senha no próximo login
  + Definir CPF como senha default e
  + Núm. de dias para Forçar a Troca de Senha

Após realizar a inclusão do usuário para o funcionário, será necessário definir **q**uais outros módulos ele poderá acessar. Para isso, siga os passos abaixo:

**01.** Acesse **Serviços Globais | Segurança | Usuários** e selecione o sistema Folha de Pagamento. Depois edite o cadastro do usuário utilizado;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014126132)  
  
**02.** Acesse a aba **Segurança**e verifique qual perfil está associado ao usuário;  
  
![01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014038032)  
  
**03.** Em seguida acesse Perfis e altere o sistema para Folha de Pagamento. Edite o perfil que está associado ao usuário na aba Acesso a Menus. O menu Portal RH (Portal), deverá esta habilitado.  
  
![01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014047451)  
  
**04.** Caso o funcionário utilize o ponto através do Meu RH, será necessário que seu usuário possua permissões no modulo de **Automação de ponto.**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6445735344535)  
  
Caso deseje **incluir permissões para os perfis dos funcionários de forma global**, utilize a rotina [**Cópia de Permissão de Usuários**.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016447572-Framework-Linha-RM-Frame-C%C3%B3pia-de-permiss%C3%A3o-de-usu%C3%A1rios-para-um-ou-v%C3%A1rios-usu%C3%A1rios)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6776964384535)

**Saiba mais**  
Parâmetros de inclusão de usuários, acesso o link: [Inclusão de usuário para acesso ao RM Portal](https://tdn.totvs.com/pages/releaseview.action?pageId=452719492#:~:text=A%20inclus%C3%A3o%20de%20usu%C3%A1rio%20para,estiver%20cadastrado%20para%20o%20funcion%C3%A1rio)

Como utilizar Automação de Ponto através do Meu RH acesse o link: [RH - RM - Meu RH - Como Habilitar a Inserção de Batidas por Geolocalização Portaria 373/2011](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020815391--RH-RM-Meu-RH-Como-Habilitar-a-Inser%C3%A7%C3%A3o-de-Batidas-por-Geolocaliza%C3%A7%C3%A3o-Portaria-373-2011?source=search)
