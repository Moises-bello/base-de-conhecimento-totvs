---
content_hash: 488f0a438372943268d18d084f93e7b004dec960354ceeb86648f61edbe8166c
fetched_at: '2026-06-29T00:09:28.138462+00:00'
page_id: '423938670'
product: rm
source: tdn-rm
title: Controladas 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938670
version: 6
---

Versão 12.1.2302

A partir da versão 12.1.2302, os cadastros de "Controladas" e "Eventos Societários" serão descontinuados do sistema e substituídos por Grupos Empresariais.  
Para mais informações consulte a documentação a seguir :

O cadastro de controladas serve para que o sistema consiga identificar quem serão as controladas de determinada controladora. Três campos devem ser preenchidos neste cadastro, sendo eles: Coligada controlada, % da participação acionária e % da Consolidação. Ainda existe um quarto campo (Inativa), onde o usuário poderá utilizar caso queira descartar os dados de determinada controlada para geração da ECD. Importante: Caso o usuário inative uma coligada, esta não terá nenhuma participação no conglomerado econômico, ou seja, não haverá nenhum registro na ECD referenciando tal empresa.   
   
A controlada será uma "coligada" previamente cadastrada no sistema, e representará uma das empresas que faz parte do conglomerado econômico.  
   
Quando uma **controlada** é cadastrada, o sistema entende automaticamente que a **controladora** é a coligada corrente em que o usuário está operando, sendo a controladora responsável por gerar a ECD.  
   
Importante  
O percentual de consolidação será levado em consideração no momento em que o processo for executado, os saldos das contas serão calculados proporcionalmente ao % de consolidação cadastrado para determinada controlada.

Veja Também

* K100 - Código do País

* [Cálculo Saldo Consolidado](http://tdn.totvs.com.br/pages/viewpage.action?pageId=423938856)
* [Eventos societários](http://tdn.totvs.com/x/U6sEGw)
