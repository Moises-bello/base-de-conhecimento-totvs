---
content_hash: 5f9c4fe61350d33fcbece8fac5a26743b02a9c8b46a8c6cf1c86551dbfc5ef37
fetched_at: '2026-06-29T00:05:54.281824+00:00'
page_id: '1077773072'
product: rm
source: tdn-rm
title: PI - Integração - RD Station - Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1077773072
version: 2
---

Trata-se de uma lista de parâmetros relacionados a integração do RD Station:   
Este parâmetros podem ser configurados acessando ***Backend / Integração / RD Station / Aplicativos:***

* ***Aplicativos*:** São os aplicativos possíveis de serem cadastrados e integrados com o Portal de Imóveis.

### **Parâmetros**

---

* ***RD Station - Token WebHook - Cadastro de Leads enviados pelo RD*:**Para que o RD Station envie um lead para o PVI no momento em que ele for marcado como "Oportunidade" é necessário definir um token (chave de segurança para garantir identidade) onde o RD Station enviará nas requisiçoes de cadastro lead. **informe um nome neste campo: Exemplo: portaltotvs123456 (em seguida copie esta chave)**  
    
  Na página principal do RD Station selecione a opção Integrações:  
    
    
    
  Selecione a opção de Webhooks e em seguida clique em configurar:  
    
    
    
  Selecione a opção criar Webhook preenchendo as informações do nome, URL do portal **(veja observação abaixo)** e o Gatilho oportunidade em seguida salve estas configurações.  
    
    
    
    

  - URL: Nesta parte deverá ter uma atenção mais específica, observe que na primeira parte será informada o acesso ao Portal de Imóveis, em seguida para compor a URL informe o endereço: api/webhook/rdstation/ e para finalizar a chave que foi gerada no Portal de imóveis (nos parâmetros de Pessoas). Clique em “Salvar Webhook”  
  Veja o exemplo detalhado:

OBSERVAÇÃO

Abaixo segue a parametrização do Whebhook anterior a versão 12.1.2209,  observe que os parâmetros disponibilizados encontram-se em outra Guia, conforme orientações abaixo:  
Acesse:***Backend / Integração / RD Station / Aplicativos:***

* ***RD Station - Token WebHook - Cadastro de Leads enviados pelo RD*:**Para que o RD Station envie um lead para o Portal de Imóveis no momento em que ele for marcado como "Oportunidade" é necessário definir um token (chave de segurança para garantir identidade) onde o RD Station enviará nas requisições de cadastro lead.

Para mais informações, sobre como enviar o Lead para o Portal de Imóveis, veja o vídeo abaixo do nosso How-To:

---
