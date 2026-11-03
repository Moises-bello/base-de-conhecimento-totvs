---
article_id: 30041040663831
category: IMPLANTAÇÃO
content_hash: fcd42e011d8f383545a44f93ef5d71f7c6b44f708dbbfef6ba84d7a70d59890f
fetched_at: '2026-06-28T22:44:33.325848+00:00'
product: protheus
section_id: 10299929290007
source: central-protheus
title: RH - Linha Protheus - MEU RH - É possível realizar o balanceamento de carga
  do serviço do Meu RH (BROKER)
type: support-article
updated_at: '2026-06-23T21:06:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30041040663831-RH-Linha-Protheus-MEU-RH-%C3%89-poss%C3%ADvel-realizar-o-balanceamento-de-carga-do-servi%C3%A7o-do-Meu-RH-BROKER
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30041040647063) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**É possível realizar o balanceamento de carga do serviço do Meu RH (BROKER)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução****Com balanceamento via *Broker* é possível dividir a carga com 2 ou mais serviços de *AppServers*,** resolvendo assim problemas de lentidão causados por muitos acessos em um curto intervalo de tempo.  
  
O Meu RH depende dos serviços de HTTP e REST, **e é possível balancear ambos.**Exemplo de construção de uma aplicação Meu RH com **5 *AppServers*: *Broker HTTP, Broker REST,* *Worker 1, Worker 2, Worker 3.*  
![](https://tdn.totvs.com/download/attachments/579452012/balanceamento-via-broker.jpg?version=4&modificationDate=1609341922227&api=v2)**

Esta aplicação, como no exemplo, funcionará com HTTPS na porta 4430 e REST na porta 9090.  
  
Logo, o Broker HTTP é quem subirá a porta 4430, e o *Broker* *REST* é quem subirá a porta 9090, então repassam às portas HTTP e *REST* dos *Workers*.  
  
**[Na versão 2410 BROKER HTTP no Binário Onça é necessário adicionar a chave MONITORING\_TYPE=CONNECTION no appserver.ini](https://tdn.totvs.com/display/tec/Balanceamento+entre+Clientes+HTTP+e+servidor+Application+Server)**

**Segue documentação de configuração dos arquivos appserver.ini para implantação do *Broker*.  
<https://tdn.totvs.com/display/NPR/0.2.3+Balanceamento+com+Broker>  
  
Saiba Mais  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
