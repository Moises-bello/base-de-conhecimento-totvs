---
content_hash: dce4f7d17c4f50b5057d0f710c62e860103ef6886204e77b7eb429a8adf148b8
fetched_at: '2026-06-29T00:05:54.321787+00:00'
page_id: '1077776236'
product: rm
source: tdn-rm
title: 8 - Gatilhos de automação - Exemplo 2 :  
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1077776236
version: 1
---

## **Gatilho de automação - Exemplo 2:**

### Neste segundo exemplo iremos criar uma automação de Fluxo que possibilitará o *Envio automático de um Lead para o Portal de imóveis assim que o mesmo for selecionado como uma oportunidade.*

* Para que a Automação seja configurada acesse sua conta do RD Station Marketing:**<https://app.rdstation.com.br/dashboard>**  
  Ao acessar a página, clique o menu: Relacionar e selecione a opção Automação de Marketing, este menu possibilitará o usuário possa ter aceso as atividades para inclusão de ações que podem ser realizadas de forma automatizadas no sistema.;

* Selecione a opção: Criar Fluxo;

* Informe um nome para este Fluxo de Automação, como exemplo: Envia Lead para o Portal de Imóveis, em seguida clique em continuar;

* No painel apresentado a esquerda selecione as opções para que seja montada as instruções de acordo com as ações definidas:  
  **- Todos Leads que:** (esta opção informa que na ação será utilizados todos os Leads inseridos no sistema);  
  **- Campo do Lead:**Campo ao qual a automação irá percorrer  
  **- Integração no Portal de Imóveis:***(refere-se ao nome do campo personalizado que foi configurado no Tópico 1 deste material).***- é igual a SIM:** Trata-se da condição do filtro que irá realizar a ação, ou seja, quando for selecionado SIM então o gatilho realizará uma determinada ação.
* Em seguida clique na opção + destacada na tela;

* Observe que neste momento serão apresentadas outras ações para serem selecionadas, navegue nas ações e localize: Enviar Leads para Integração, em seguida marque esta ação e arraste a mesma na direção do símbolo + conforme a seta indicada na imagem;

* Após arrastar esta atividade na tela, uma guia será apresentada na lateral para que seja informado o Link que possui as informações do Webhook que irá sincronizar este gatilho com o Portal de Imóveis. Para relembrar como realiza esta parametrização veja logo abaixo uma imagem dos parâmetros do Portal de imóveis onde é informada a chave ToKen e em seguida com esta chave é criada a URL para ser utilzada nesta parametrização;

URL Webhook

**Veja como criar o Link que será utilizado na tela acima:**  
  
- URL: Nesta parte deverá ter uma atenção mais específica, observe que na primeira parte será informada o acesso ao Portal de Imóveis, em seguida para compor a URL informe o endereço: api/webhook/rdstation/ e para finalizar a chave que foi gerada no Portal de imóveis (nos parâmetros de Pessoas). Clique em “Salvar Webhook”  
Veja o exemplo detalhado:  
  
  
***Mais informações no link: [Configurações de URL](https://tdn.totvs.com/pages/viewpage.action?pageId=687737814#RDSTATION-1513287362)***

* Serão apresentadas as opções de ativação, nesta tela não precisa realizar nenhuma ação, bastando clicar em: **Ativar Fluxo;**

* Com isto concluímos a inclusão desta automação que possibilita o envio automático de um Lead para o Portal de imóveis;
