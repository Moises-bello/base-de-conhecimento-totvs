---
content_hash: b1cb482e621c1f421a3c415d02ad224a1ff3b32a66861e4b42fe5e6b90948559
fetched_at: '2026-06-29T00:05:54.299600+00:00'
page_id: '1077776087'
product: rm
source: tdn-rm
title: '2 - Configurando Campos Personalizados no CRM:'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1077776087
version: 1
---

## **Configurando Campos Personalizados no RD Station CRM:**

---

Para configurar um campo personalizado no **RD Station CRM** acesse sua conta: **<https://crm.rdstation.com/app#/settings>**  
Ao acessar a página serão apresentados diversos menus, dentre eles o menu: Configurações, ao selecionar este menu, observe que serão listadas para o usuário opções para que o mesmo possa selecionar.

* Selecione: Campos personalizados;

* Clique em Adicionar novo campo;

* Observe que nesta tela existe um botão que ao ser selecionada irão apresentar 3 opções: Oportunidade, Empresas\Clientes e Contatos.   
  Neste nosso exemplo iremos selecionar **oportunidade;** isto refere-se que ao selecionar a opção oportunidade (este campo que iremos inserir em nosso exemplo será apresentado ao acessar a guia de oportunidades.

* Após acessar a tela com as opções a serem selecionadas observe os campos que serão preenchidos conforme a imagem abaixo.  
  - Nome do campo personalizado: Refere-se ao campo que será apresentado na tela para o usuário, com esta informação o usuário irá determinar qual será a ação ou opção que irá selecionar. Neste nosso exemplo quando este campo for apresentado no formulário de oportunidade, o usuário irá optar pelas opções a serem escolhidas SIM ou NÃO *(estas opções irão executar o gatilho com a ação automatizada) **que veremos logo a seguir nos exemplos 1 e 2 dos tópicos 4 e 6 deste material;***  
  - Campo de seleção: Selecione a opção: Escolha múltipla, que possibilita o usuário selecionar SIM ou NÃO no formulário;  
  - Tipo: Informe as palavras SIM e NÃO para que estas opções fiquem disponíveis para seleção.  
  - Visível: Indica que este campo ficará visível no formulário oportunidade, podendo ser desabilitado a qualquer momento em que não esteja sendo mais utilizado.  
    
  Ao final clique em salvar.

* Ao retornar para a tela principal, observe que o campo personalizado já encontra-se disponibilizado na opção selecionada: Oportunidades.   
  Ainda nesta tela veja que será necessário marcar a opção: **VISÍVEL** , se esta opção não estiver marcada, a mesma deverá ser marcada (conforme a imagem abaixo).  
  Ao marcar esta opção será apresentada uma mensagem de confirmação ***(Clique em sim para prosseguir);***

Para facilitar a gestão de informações, clientes na versão 12.1.2606+ possuem uma tela exclusiva para a criação de campos personalizados diretamente no RD Station CRM, sem precisar sair do Portal.

**Como criar um novo campo pelo Portal:**

* Acesse o menu Integração > Campos personalizados.
* Clique no botão **Adicionar campo**.
* Preencha as informações:
  + **Entidade:** O sistema já preenche automaticamente como "Negociação".
  + **Campo:** Selecione a informação do Portal (ex: Empreendimento, Bloco, Unidade, Data da proposta) que alimentará o RD. Dica: Ao selecionar campos como "Empreendimento", o sistema carrega as opções ativas do seu banco de dados automaticamente.
  + **Label:** Digite o nome visual do campo para o corretor no RD.
  + **Tipo:** Defina se será Texto, Data, Seleção Única ou Múltipla.
  + Também poderá definir uma **ordem** para o campo personalizado e se depois de ser salvo, ao editar, se **p****ermitir adicionar nova opção**.
* Clique em **Criar**. O campo será gerado no RD Station CRM e no PI.

**Observação**: ao criar o campo personalizado diretamente pelo RD Station CRM ele será automaticamente integrado ao Portal de imóveis.
