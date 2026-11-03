---
content_hash: ad8b1a0d483f13b6741c476796c4878940c301a58d07b676a6dcde2a6940aaac
fetched_at: '2026-06-29T00:11:37.945317+00:00'
page_id: '780780957'
product: rm
source: tdn-rm
title: TCGI - Cobrança - WhatsApp
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=780780957
version: 29
---

**WHATSAPP**

##### Saiba como configurar para utilizar whatsapp na cobrança.

Importante

* Será necessária a **contratação do serviço da Worknow** para utilizar a funcionalidade.    
  Entrar em contato com Worknow - <https://worknow.com.br/contato/>  
  Após contratar os serviços de whatsapp juntamente com a worknow você deverá configurar seu ambiente TOTVS para que apareça as funcionalidades Worknow no menu superior do TCGI, assim você conseguirá imputar as informações de servidor onde será enviado as mensagens do whatsapp, numero utilizado para envio como outros dados necessários no processo.
* Conforme Regra de Negócio, o templates sempre devem ser cadastrados para a coligada 1, que é a coligada centralizadora e para a filial 1.
Ativando a Integração com a Worknow e Sincronizando os Templates

---

Utilizando Templantes WorkNow/Meta - A partir da versão 12.1.2402.XXX ou superior

* Para cadastrar os templates/mensagens oficiais que deseja utilizar na cobrança para enviar aos seus compradores, os templates/mensagens deveram ser cadastradas previamente junto a WorkNow/Meta. Sendo assim, você precisará de acesso ao portal de gerenciamento da WorkNow. Em caso de duvidas entre em contato com a Worknow: <https://worknow.com.br/contato/>
* Agora poderá configurar/atualizar a integração by worknow no executar do RM.
* Sincronize os templates/mensagens oficiais
* Cadastre uma ação do tipo whatsapp, configurando os ids numéricos "{{1}}" do template/mensagen oficial, associando aos mnemônicos do TCGI [CLI]. *Exemplo*: **{{1}}:[CLI]**;
* Clique no botão incluir configuração mnemônicos, para adicionar as referências à mensagem da ação de cobrança criada.
* Não é possível de se alterar o texto da mensagem, o mesmo deve ser alterado diretamente no template da worknow.

Utilizando Mensagem cadastrada TCGI - Obsoleto, anterior à versão 12.1.2402.XXX

* Para a configuração utilize os passos a seguir:  
      1 - [como fazer download - dlls worknow](https://worknow.com.br/wikihelp/instalacao-modulos-atualizar-dlls/)  
      2 - [como utilizar dlls worknow ambiente TOTVS](https://worknow.com.br/wikihelp/instalacao-modulos-instalacao-6-passos/)  
      3 - [como configurar os dados de envio e consumo do whatsapp](https://worknow.com.br/wikihelp/workchat-parametrizacao-configuracoes-gerais/ "Follow link")

Após ter configurado o ambiente com as informações de acordo com os links acima, deverá ser criado uma ação de cobrança com o tipo de ação cobrança igual whatsapp.

Importante

O tipo de ação 'WhatsApp' somente irá aparecer na criação de uma ação, após configurar todo o ambiente TOTVS com os dados da Worknow

Ao ser disparada a ação do tipo "whatsapp" o processo irá utilizar os dados do comprador da venda para disparar a mensagem configurada na ação com o tipo whatsapp

O formato do celular deve ser preenchido com todos os valores necessários no campo celular (Ex.: 5531988776655) dos dados adicionais do cliente/fornecedor que foi associado a venda como comprador.  
  
Video demonstra o funcionamento do disparo de uma ação pelo whatsapp:
