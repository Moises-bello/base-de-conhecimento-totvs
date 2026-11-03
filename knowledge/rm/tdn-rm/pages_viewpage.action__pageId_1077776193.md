---
content_hash: 1827b036c283a422f3707c075b72f877d01131f1a086b24bdde1a5a49636e943
fetched_at: '2026-06-29T00:05:54.313827+00:00'
page_id: '1077776193'
product: rm
source: tdn-rm
title: '6 - Incluindo Gatilhos de automação  - Exemplo 1:'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1077776193
version: 1
---

## **Gatilhos de automação - Exemplo 1 :**

---

Neste primeiro exemplo iremos criar uma automação de Fluxo que possibilitará o *Envio automático de um Lead para o CRM assim que o mesmo for incluído pelo usuário na base de Lead*;  
  
**Envio automático de um novo Lead para o CRM**

* Para que a Automação seja configurada acesse sua conta do RD Station Marketing: **<https://app.rdstation.com.br/dashboard>**  
  Ao acessar a página, clique o menu: Relacionar e selecione a opção Automação de Marketing, este menu possibilitará que o usuário possa ter aceso as atividades para inclusão de ações que podem ser realizadas de forma automatizadas no sistema.;

* Selecione a opção: Criar Fluxo;

* Informe um nome para este Fluxo de Automação, como exemplo: Entrada de Leads, em seguida clique em continuar;

* No painel apresentado a esquerda selecione as opções para que seja montada as instruções de acordo com as ações definidas:  
  - Todos Leads que (esta opção informa que na ação será utilizados todos os Leads inseridos no sistema);  
  - Foram marcados como oportunidade  
    
  *Ou seja, esta atividade que foi criada irá validar todos os Leads incluídos no sistema que possuem a opção Oportunidade Marcada*

* Em seguida clique na opção + destacada na tela;

* Observe que neste momento serão apresentadas outras ações para serem selecionadas, navegue nas ações e localize: Criar Oportunidade no CRM, em seguida marque esta ação e arraste a mesma na direção do símbolo + conforme a seta indicada na imagem;

* Após arrastar e soltar, observe que a ação ficará associada com a outra atividade já criada e outras opções para seleção serão apresentadas para serem preenchidas.  
  - Criar a oportunidade no funil: Selecione o Funil existente no site que receberá esta automação;  
  - Na etapa: Informe a etapa a qual esta automação será iniciada. Isto indicará a automação este lead ao ser inserido na base de Lead (onde no cadastro é informado este funil e esta etapa) neste momento este Lead será incluído automaticamente para o CRM.  
  - Atribuir para uma pessoa: Informar um usuário que receberá as oportunidades  
    
  Ao final clique em Salvar e Ativar.

* Serão apresentadas as opções de ativação, nesta tela não precisa realizar nenhuma ação, bastando clicar em: Ativar Fluxo;

* Com isto concluímos a inclusão desta automação que possibilita o envio automático de um novo Lead para o CRM;

Observações:

A utilização desta automação dispensa a necessidade da parametrização do Webhook.   
Para maiores informações referentes a este recurso acesse a página:  [Parâmetros > Webhook](https://tdn.totvs.com/pages/viewpage.action?pageId=687737814#RDSTATION-1513287362)

URL Webhook

**Veja como criar o Link que será utilizado na tela acima:**  
  
- URL: Nesta parte deverá ter uma atenção mais específica, observe que na primeira parte será informada o acesso ao Portal de Imóveis, em seguida para compor a URL informe o endereço: api/webhook/rdstation/ e para finalizar a chave que foi gerada no Portal de imóveis (nos parâmetros de Pessoas). Clique em “Salvar Webhook”  
Veja o exemplo detalhado:  
  
  
***Mais informações no link: [Configurações de URL](https://tdn.totvs.com/pages/viewpage.action?pageId=687737814#RDSTATION-1513287362)***

* Serão apresentadas as opções de ativação, nesta tela não precisa realizar nenhuma ação, bastando clicar em: **Ativar Fluxo;**

* Com isto concluímos a inclusão desta automação que possibilita o envio automático de um Lead para o Portal de imóveis;
