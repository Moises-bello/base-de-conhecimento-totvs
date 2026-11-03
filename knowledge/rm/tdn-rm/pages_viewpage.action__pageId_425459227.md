---
content_hash: 07343994a30c4f11884286d456fdeb90bc26bcc9c92ec749054c91247b2f17e8
fetched_at: '2026-06-29T00:09:34.706816+00:00'
page_id: '425459227'
product: rm
source: tdn-rm
title: Comunicação -  Web Services
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459227
version: 8
---

**Web Services**

---

Web Services (WS) é uma solução empregada na integração de sistemas e na comunicação entre aplicações diferentes, permitindo uma integração e comunicação mais ágil, dinâmica e segura entre os sistemas.   
    
 O TOTVS Business Conector contém Web Services que podem ser acessados por outros aplicativos para integração com a Linha RM. Eles podem ser hospedados no Internet Information Services (IIS) ou no RM. Host.  
    
 Clique nos links abaixo para mais informações:

* **Web Services do TBC**
* **Internet Information Services (IIS)**
* **RM.Host**

**Aplicativo RM.UpdateConfig**   
    
 Para hospedar os web services no IIS ou no RM.Host, serão necessárias realizar ajustes nos arquivos de configuração. Para realizar ajustes nos arquivos de configuração, pode-se fazer uso do  aplicativo RM.UpdateConfig.  
Para ver um exemplo, acesse o boletim técnico nos Recursos Adicionais.  
    
 **Configurações Importantes - RM.Host.Service**

**1. RM.Host.Service**: Quando o RM.exe estiver sendo executado utilizando o RM.Host.Service, é necessário que altere o usuário relacionado ao serviço, para isto acesse "Serviços | RM.Host.Service | Logon" e informe um usuário que tenha perfil de administrador, logo após a alteração deve se reiniciar o Host.

---

**Recursos Adicionais**

Exemplos de configurações do WebService:

[Exemplo Configuração WebService](http://api.totvs.com.br/#/) - (Acesse o menu: Integrações Legadas > Integração RM > Lista de Serviços)

Exemplo de uso do aplicativo RM.UpdateConfig:

[Usando o aplicativo RM.UpdateConfig](http://tdn.totvs.com/download/attachments/105316716/BT+-+Usando+o+aplicativo+RM.UpdateConfig.pdf?version=1&modificationDate=1385653780432)
