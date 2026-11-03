---
content_hash: c07151f93f097157711602d403b58606f8b88e61e35ee1b8756b89360f54ae48
fetched_at: '2026-06-29T00:09:36.286571+00:00'
page_id: '425459494'
product: rm
source: tdn-rm
title: Comunicação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459494
version: 5
---

---

Qualquer sistema de informação possui a necessidade de trocar dados com outros sistemas, e para isso existe a integração. A comunicação para que haja essa troca de informação deverá ocorrer de duas possíveis formas: Síncrona ou Assíncrona

* **Síncrona:**

A comunicação síncrona é caracterizada pela troca direta de informações (online) onde os dados ou requisições são enviados e só após um retorno é dada continuidade ou não ao processo (podendo ser esse retorno sucesso ou falha). 

* **Assíncrona:**

Caracterizada pela troca de informações entre dois sistemas, contudo os dados e ou requisições são processados de maneira off-line, geralmente utilizando rotinas SQL ou BATCH para processamento e envio dos dados. O processo de origem não aguarda um retorno para dar continuidade ou não ao processo (podendo ser esse retorno sucesso ou falha).  
   
    
 Independente da forma de comunicação, a integração dos sistemas **pode ou não** fazer uso de um ESB (Enterprise Service Bus) em sua arquitetura.   
    
 A comunicação ESB acontece quando dois ou mais sistemas trocam informações de forma síncrona ou assíncrona, onde todas as mensagens ou eventos são mediados por um Bus ou recurso similar, como Web Services. Alguns pacotes de integração utilizam o ESB na sua arquitetura, ficando nestes casos obrigatória a instalação do ByYou ESB.  
    
    
 Para mais informações acesse os links abaixo:
