---
content_hash: 56d7454535112a592585dc6ce77653ff568fb93a04221c14e3ce663b29f8fc94
fetched_at: '2026-06-29T00:08:52.282030+00:00'
page_id: '338376603'
product: rm
source: tdn-rm
title: WebServices
type: documentation
url: https://tdn.totvs.com/display/LRM/WebServices
version: 13
---

A integração via Web Service permite a execução de e a manutenção de .

Os serviços Web Service identificarão a base de dados a ser utilizada através da tag **DefaultDB**, que informa o Alias que será utilizado no acesso. Essa tag deve existir no arquivo de configuração do Host (RM.Host.Service.exe.config ou RM.Host.exe.config).

xmlExemplo de utilização da tag DefaultDBtrue]]>

A variável ***<ALIAS\_DO\_BANCO\_RM>*** deverá ser substituída pelo nome do alias cadastrado para acesso ao banco de dados.

xmlExemplo de config com a tag DefaultDB.true



















]]>Importante

Liberação de acesso a porta do Host Service

Caso o Host utilizado seja o **RM.Host.Service.exe** é necessário a execução do comando, abaixo, para liberação da porta configurada na tag **HttpPort**, via prompt de comando:

* Adicionar

**netsh http add urlacl url=http://+:8051/ user=NetworkService**

* Apagar

**netsh http delete urlacl url=http://+:8051/**

* Exibir

**netsh http show urlacl**

A porta **8051** é padrão no sistema e caso seja alterada na tag **HttpPort** no arquivo de configuração do Host, precisa ser alterada no link acima.
