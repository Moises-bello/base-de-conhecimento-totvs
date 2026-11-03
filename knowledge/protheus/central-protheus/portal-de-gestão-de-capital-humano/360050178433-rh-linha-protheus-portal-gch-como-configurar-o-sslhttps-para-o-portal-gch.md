---
article_id: 360050178433
category: Portal de Gestão de Capital Humano
content_hash: 3e7e69889e062c498e5b6599f1825733f2a51a12bef5d7b55a71bf25a9787aa8
fetched_at: '2026-06-28T22:42:59.061244+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus -  PORTAL GCH - Como configurar o SSL/HTTPS para o Portal
  GCH
type: support-article
updated_at: '2022-08-03T11:12:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050178433-RH-Linha-Protheus-PORTAL-GCH-Como-configurar-o-SSL-HTTPS-para-o-Portal-GCH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:05:00 min  
  
Dúvida**Como configurar o **SSL/HTTPS** para o Portal GCH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Portal Gestão Capital Humano – Todas as versões  
  
**Solução**Para configurar o **SSL/HTTPS** para o **Portal Gestão de Capital Humano** e utilizar uma conexão segura é importante que primeiramente valide se o **acesso interno** está funcionando corretamente.  
  
[RH - Linha Protheus - PORTAL GCH - Como instalar e configurar o Portal Gestão do Capital Humano?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005517721-RH-Linha-Protheus-PORTAL-GCH-Como-instalar-e-configurar-o-Portal-Gest%C3%A3o-do-Capital-Humano-)  
  
Recomendamos a validação do certificado conforme documentação:

**[Validação de certificados](https://tdn.totvs.com/pages/viewpage.action?pageId=550327608)**  
Segue abaixo um exemplo de configuração do **Portal GCH** no **APPSERVER.INI** com a utilização de **SSL/HTTPS:**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7898767491863/mceclip1.png)  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7899382140439/mceclip6.png)  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7899001368727/mceclip5.png)  
  
**\*A configuração acima trata-se apenas de um exemplo para demonstrar as tag's utilizadas.**  
  
**Importante:** Ao configurar o Portal GCH para um **acesso externo**, primeiramente certifique-se de que os acessos através de **endereço e porta interno** estão funcionando corretamente, após funcionar realize os direcionamentos de IP e porta de **acesso externo** para os serviços do Portal.  
 **Obs.:** Vale ressaltar que o **Suporte Padrão** não tem como auxiliar nos processos relacionados à configuração de **Endereços Externos, DNS, Firewall/Antivírus e Certificado Digital**, pois tratam-se de questões internas e de infraestrutura particular de cada Empresa. Caso precise de auxílio nas questões acima sugerimos que entre em contato com nosso time de **TIS – TOTVS Infra-Service** através do e-mail **[tis.comercial@totvs.com.br](mailto:tis.comercial@totvs.com.br)**ou com o time de **HUB Plataformas.**A equipe **HUB Plataformas** é possível abrir um ticket diretamente ao grupo pela central do cliente.

**Documentações de referência:**  
[Seção [HTTPS]](https://tdn.totvs.com/pages/viewpage.action?pageId=135496188)  
[Seção [SSLConfigure]](https://tdn.totvs.com/pages/viewpage.action?pageId=6064865)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
