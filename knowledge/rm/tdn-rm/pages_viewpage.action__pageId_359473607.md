---
content_hash: fa8f2ecc6e090404976ae4a6676cfb64ded9998bc47304e974cc7324cdf60806
fetched_at: '2026-06-29T00:08:58.118450+00:00'
page_id: '359473607'
product: rm
source: tdn-rm
title: 'TAF/TSS - Erro : WSCERR044 / Não foi possível POST : URL http://localhost:8091/SPEDADM.apw
  ( 999 : Invalid HTTP Connection ).'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=359473607
version: 5
---

Erros e AçõesErro

Erro : WSCERR044 / Não foi possível POST : URL <http://localhost:8091/SPEDADM.apw> ( 999 : Invalid HTTP Connection ).

Ação

Ação :

• Verifique se no arquivo appserver.ini ([diretório]/tss/bin/appserver) a tag relativa à URL de conexão do TSS está igual ao do Wizard de configuração do TAF.

Exemplo:  
  
  
No exemplo acima, está configurado como [[localhost:8080](http://localhost:8080/)], então o Wizard também deverá constar como localhost:porta.  
  
Também é possível utilizar como IP:PORTA (Exemplo: [10.172.69.81:8080]). Porém, caso o IP da máquina seja dinâmico, seja necessário alterá-lo manualmente em algum momento se houver a mudança deste.  
  
Obs.: Se houver a alteração do arquivo appserver.ini, reinicie os serviços antes de configure o Wizard novamente.

• Verifique também se os serviços do TAF e TSS estão ativos, se Proxy está liberado ou se o Firewall está bloqueando a conexão.

• Faça também um teste tentando abrir a URL no browser (caminho até porta - [http://localhost:9091](http://localhost:9091/)). Outro teste a ser feito é acessar a pasta DBAccess e rodar o executável DBMonitor.exe e testar a conexão com a base TSS..
