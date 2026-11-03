---
content_hash: dabaaee789e038f2c9a12d7cb9993f2f2108df3a6ebec34d18c903de2a3c99d1
fetched_at: '2026-06-29T00:11:22.141416+00:00'
page_id: '699798333'
product: rm
source: tdn-rm
title: Portal de Imóveis - Backend - Globais - Etapas do funil de leads
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=699798333
version: 17
---

Portal de Imóveis possui uma visão dos processos de venda através de um funil parametrizável.   
Este funil consiste em demonstrar o processo do Lead desde o cadastro da pessoa até a finalização da venda com sucesso ou não.  
  
**Para utilizar o funil de Leads, realiza-se a seguinte parametrização:**

---

* Em Backend, habilite para o usuário a opção para visualização de Funil de Leads.

* Ao acessar o Menu: Globais, será possível visualizar a opção de funil de Leads disponibilizada para o usuário;

**Incluindo as Etapas para o Funil do Lead:**

---

* Informe a descrição do Funil e em seguida preencha as informações necessárias para criação das Etapas deste funil.  
  Ao clicar em Adicionar Etapas é possível incluir cada uma das etapas e vincular estas ao mapeamento de situações da pessoa.
* Cada uma destas etapas será representada na visão do Funil indicando a qual etapa este lead encontra-se.  
  Por este motivo é necessário mapear as Situações da Pessoa que será representada na etapa.  
  Ao final selecione o Empreendimento ao qual será associado a este registro.

* Após clicar em Salvar, o mesmo ficará disponível para utilização.

**Sincronizando Funil do RD Station com o Portal de Imóveis:**

---

* Ao acessar o cadastro do funil do lead é possível sincronizar as colunas do CRM do RDStation. Isto proverá que os funis existentes no RD Station sejam enviados para o Portal de Imóveis.  
  Para realizar esta parametrização acesse: Globais > Funil de Leads.   
  Após realizar a inclusão do Funil do Lead, selecione o empreendimento que será associado a este funil e clique em **Sincronizar etapas RD Station CRM.**
* Será apresentado na visão o nome do funil (existente no RD Station CRM) que será sincronizado com o Portal de imóveis, neste nosso exemplo abaixo o sistema apresenta o nome: Funil Padrão, que refere-se ao funil existente em nossa base de dados.
* Selecionando o funil, será apresentada uma mensagem na tela para o usuário, onde o mesmo será informado que esta integração não possibilita alterações nas etapas:

  ###### \*Este funil está integrado com o RD Station CRM: Funil Padrão Não é possível realizar alterações nas etapas sincronizadas no Portal de Imóveis.
* #### Observe que ao realizar a importação de um funil do RD Station os dados do Funil e as informações referentes ao Mapeamento de Situações da Pessoa (são parametrizadas automaticamente) não sendo possível serem alteradas pelo usuário. Em seguida, clique em Salvar. Todas estas etapas são importadas do Funil já existente no RD Station.

  Observação
  + ***Situação de entrada do Lead (RDStation)*: Ao realizar a inclusão de um novo Lead através do RD Station,** quando este cadastro estiver marcando como oportunidade (o mesmo será inserido no Portal de Imóveis com uma situação padão (informada neste campo)  
    **Mais informações acesse: [Situação Cadastro Pessoas](https://tdn.totvs.com/pages/viewpage.action?pageId=592282478)**

  #### 

  ### Funcionalidade: Parâmetro de Etapa "Sem Contato (Sem Atendimento)" no Funil de Leads Integrado ao RD Station

  Foi criada uma funcionalidade que permite definir uma etapa específica no funil de leads, integrado ao RD Station, como **"Sem Contato (Sem Atendimento)"**. Essa etapa indica que o corretor ainda **não iniciou o atendimento ao lead**.

  Essa definição é essencial para que a **roleta de vendas do PI** saiba se deve redistribuir o lead para outro corretor após o tempo limite configurado.

  #### Regras de funcionamento:

  + **Apenas uma etapa por funil de leads** pode ser marcada como "Sem Contato (Sem Atendimento)".
  + Caso **nenhuma etapa** esteja marcada como tal em um funil do RD Station, a **roleta de vendas seguirá a lógica padrão** do PI para identificar se o lead está em atendimento ou não.

  #### Objetivo da funcionalidade:

  Quando a roleta de vendas do PI distribui um lead para um corretor:

  + O corretor será **atualizado automaticamente** tanto na negociação do **RD CRM** quanto como **dono do lead no RD Marketing**.
  + A roleta funcionará da seguinte forma:

    1. **Se o lead foi atendido** (ou seja, a negociação **não** está na etapa definida como "Sem Contato"):

       - O lead **não será redistribuído** após o tempo limite da roleta.
    2. **Se o lead não foi atendido** (ou seja, a negociação permanece na etapa definida como "Sem Contato"):

       - O lead **será redistribuído para outro corretor** após o tempo limite.
       - O novo corretor será atualizado na negociação do **RD CRM**, no dono do lead no **RD MKT**, e também no **Cadastro de Pessoas**.
* Neste momento O registro será exibido com o status **"Integrado com RD Station CRM"**.  Isto fará que o usuário veja o ***[Funil de Leads](https://tdn.totvs.com/pages/editpage.action?pageId=699798402)***, baseado no modelo importado do RD Station, indicando em que etapa o lead se encontra no processo comercial.

Observações:

No RD Station, para que o usuário possa visualizar o Funil Padrão existente, acese RD Station CRM

Observe o Funil com suas respectivas colunas que foram importadas para o Portal de Imóveis

**Receber lead do RD Station com a sua situação igual a etapa de funil:**

---

* Quando o RD Station estiver configurado com um fluxo de campanha que insere o lead em alguma etapa do funil ao ser marcado como oportunidade e ao receber um lead do RD Station através do WEBHOOK, neste momento, o lead é salvo no Portal de Imóveis em sua etapa configurada no RD.

  Este processo é válido quando a etapa já estiver sincronizada no Portal de Imóvel.

  Caso a etapa não vier no lead, então o sistema utilizará a situação de entrada configurada em cada funil do Portal de Imóveis.

  Para realizar esta integração, no RD Station, acesse em Marketing o Menu: Relacionar > Automação de MArketing

* Ao realizar um novo Fluxo , clicando em Editar, seleciona opção: Foram marcados como oportunidade;
* Em seguida, ao clicar em Ações selecione a opção; Ações:
* Selecione a opção: Criar Oportunidade no CRM;
* E realize as parametrizações necessárias nas mesmas:

  Informando: O nome do funil que será utilizado para realizar esta parametrização,

  Etapa: Neste campo será necessário informar qual é a etapa que será atribuída a este Lead quando o mesmo for marcado como uma oportunidade.

  Após selecionar as opções clique em Salvar e Ativar.
* Ativar Fluxo de Automação;
* Ao marcar este Lead como Oportunidade, observe que o mesmo será enviado para o Funil do Portal de imóveis no mesmo fluxo ao qual foi selecionado no RD Station.
