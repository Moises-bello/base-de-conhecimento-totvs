---
content_hash: 43acd8c8eba9fb7b04ea72136b9e856b2d3b3922f22db8cccdea21dfa63f3254
fetched_at: '2026-06-29T00:06:21.632914+00:00'
page_id: '223173940'
product: rm
source: tdn-rm
title: ER_PDI_Integracao_com_Competencias
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PDI_Integracao_com_Competencias
version: 13
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Totvs Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** |  | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** |  |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

 

## Objetivo

Disponibilizar o desenvolvimento de competências através do PDI. Também será possível gerar todo o PDI automaticamente através do mapa de conhecimento estabelecido.

## Definição da Regra de Negócio

**Req.1 - Alterações no cadastro de PDI**

O PDI (Plano de Desenvolvimento Individual) será alterado para possibilitar o desenvolvimento de competências através de metas no processo de PDI. Para isso será disponibilizado no cadastro de PDI que se encontra no caminho **RH > Gestão de Pessoas > Acompanhamento> PDI** uma série de configurações para possibilitar o desenvolvimento de competências através de metas, as quais encontram-se abaixo:

* Utiliza metas para desenvolvimento de competências
* Preenchimento de competência obrigatório
* Habilitar sugestão de competências para o funcionário
* Exibir somente competências definidas na meta
* Exibir somente competências definidas no mapa de conhecimento do funcionário
* Exibir somente competências definidas na meta e que estejam definidas no mapa de conhecimento do funcionário

**Req.2 - Alterações no cadastro de Metas**

Como o desenvolvimento de competências será através de metas também iremos criar um novo anexo chamado **"Competências Vinculadas"** que será somente leitura e somente exibirá as competências vinculadas a meta selecionada. De forma similar ao funcionamento de requisito de acesso vinculados a meta, as competências somente serão vinculadas através de processo, por isso iremos criar um processo chamado **"Vincular/Desvincular Competências a Meta"**. Este processo irá disponibilizar as competências e as metas para o usuário realizar o vínculo. O processo deve funcionar de forma similar ao processo de vinculação de requisitos de acesso, porém realizando a vinculação de competências a meta.

**Req.3 - Portal**

No portal onde se encontram as funcionalidade de PDI, também serão feitas modificações. Teremos na opção de lançamento de ações a opção de preencher também escolhendo competências. Será similar a escolha de requisito de acesso que já existe hoje no sistema, porém funcionará com competências. O Usuário só poderá lançar ações para competências ou para requisitos de acesso, para isso teremos uma opção de escolha no momento de lançamento da ação, se o usuário escolher lançar competências será carregado as opções de competências disponíveis de acordo com as configurações realizadas no PDI anteriormente.

Também será alterado no portal a opção de sugestões da ação. O menu atual irá mudar de nome para **"Carregar Sugestões de Requisito de Acesso"** e irá sugerir somente ações relacionadas com requisitos de acesso, seu comportamento não sofrerá mudanças. Será criado um novo menu chamado **"Carregar Sugestões de Competências"** que deverá sugerir as ações relacionadas com as competências, essa funcionalidade irá funcionar de forma similar ao de sugestão de requisito de acesso.

Caso as opções de competências não estejam marcadas no cadastro de PDI as opções relacionadas a competências do PORTAL não devem ser exibidas. 

**Req.4 – Vincular Questionários ao PDI**

Como analista de RH,  
Eu preciso definir dentro de um PDI, um questionário.  
Para ter informações específicas da minha empresa registradas dentro do PDI.

Regras de negócio:

    • Se já houver respostas para o questionário não deverá ser permitido remover o vínculo.

**Req.5 – Criação de ação do PDI no portal utilizando questionário**

Como usuário do portal,  
Eu preciso definir ações do meu PDI, e caso tenha um questionário vinculado, preciso responde-lo por ação respeitando as regras do questionário (obrigatoriedade e formato). No entanto, a interface precisa ser fluida e com uma experiência única, tanto para itens do próprio PDI quanto do questionário.   
Para detalhar melhor meu PDI com as informações que a empresa solicita e para que eu tenha uma boa experiência de uso com o sistema.

 

 Regras de negócio:

   • Deverá seguir as mesmas regras de edição da própria ação do PDI.

**Req.6 – Visualização dos itens de questionário na visão de ações**

Como usuário do portal,  
Eu preciso visualizar as informações descritas no questionário e da ação ao clicar em um ícone na visão de ações do meu PDI.  
Para ter acesso fácil as informações preenchidas.

Regras de negócio:

   • Este novo botão da visão deverá trazer todas as informações da ação em formato ReadOnly num modal dialog (pode ser o próprio da edição).

**Req.6 - Lançamento de Itens do PDI pelo Portal**

Como usuário do portal,  
Eu preciso acessar meu PDI e complementar informações como: competências, requisitos de acesso, prazo, questionário e objetivo.  
Para formalizar os itens que preciso desenvolver.

Regras de negócio:

   • Deverá seguir as regras já existentes no PDI.  
   • Tem que inserir competência ou requisito, se não tiver informado.  
   • Tem que conseguir preencher o questionário, para gerado pelo processo ou pela sugestão.  
   • Se vincular um questionário após já ter ações, a primeira vez que abrir a ação fará inscrição e permitirá responder o questionário.

****Req.7 -**Processo para Gerar PDI a partir de um mapa de conhecimento**

Como analista de RH,  
Eu preciso gerar um PDI a partir do mapa de conhecimento, podendo ser por requisito de acesso ou por competências.  
Para direcionar o que as pessoas da empresa deverão desenvolver.

Regras de negócio:

   • Este novo processo terá duas opções de escolha para execução: "Gerar ações do PDI para Competências" e "Gerar ações do PDI para Requisitos de Acesso" podendo ser ambos.   
   • Ambos os parâmetros deste processo somente estarão disponíveis se estiverem habilitados no PDI através dos parâmetros: "Utilizar Requisitos de Acesso", "Utilizar Competências".  
   • O processo também deve seguir as regras configuradas no PDI relativa a competências e, ou, relativas a requisito de acesso, definido o resultado de ações a serem geradas para o PDI do participante.  
   • Caso tenha mais de uma opção de requisito ou competência para a mesma ação, não deverá preencher a opção (será preenchido mais tarde pelo portal).  
   • O status da ação no PDI deverá ser criado como "Ação aguardando Complemento".

   • Caso a mesma competência/requisito esteja vinculada a N ações. deverão ser geradas todas as ações com a competência/requisito que está vinculada;  
   • Caso mais de uma competência/requisito que esteja como "a desenvolver" tenham a mesma ação, a ação deverá ser gerada sem nenhuma competência/requisito informada (isto será feito no PDI).  
   • Se não tiverem competências/requisitos associados a meta, não serão geradas as metas. Mas deverá ser registrado via LOG no processo: "Não foi gerada a competência/requisito X para a pessoa Y pois não existem metas associadas".

   • Se houverem ações status diferente de "Ação aguardando Complemento" o processo não poderá mais ser executado.  
   • O processo for executado novamente, deverão ser excluídas todas as ações e regeradas conforme regras já definidas.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| PDI | Criação | RH > Gestão de Pessoas > Acompanhamento > PDI | - |
