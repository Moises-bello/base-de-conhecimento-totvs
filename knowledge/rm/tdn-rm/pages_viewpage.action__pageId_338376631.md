---
content_hash: 2166e860339bee5c909894b2878cdd4b42af2d8562b833ec07ffe605229d896b
fetched_at: '2026-06-29T00:08:52.287780+00:00'
page_id: '338376631'
product: rm
source: tdn-rm
title: Serviço Rest
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338376631
version: 21
---

Os serviços Rest identificarão a base de dados a ser utilizada através da tag **DefaultDB**, que informa o Alias que será utilizado no acesso. Essa tag deve existir no arquivo de configuração do Host (RM.Host.Service.exe.config ou RM.Host.exe.config).

xmlExemplo de utilização da tag DefaultDBtrue]]>

A variável ***<ALIAS\_DO\_BANCO\_RM>*** deverá ser substituída pelo nome do alias cadastrado para acesso ao banco de dados.

xmlExemplo de config com a tag DefaultDB.true










  







]]>Atenção

Para que o sistema carregue corretamente os parâmetros no momento de utilização do Rest, é necessário que sejam inclusas as informações do contexto no Headers: **Coligada, Filial, Tipo de curso e Código do Sistema**.

Exemplo de uso no **Postman**:

Importante

Liberação de acesso a porta do Host Service

Caso o Host utilizado seja o **RM.Host.Service.exe** é necessário a execução do comando, abaixo, para liberação da porta configurada na tag **HttpPort**, via prompt de comando:

* Adicionar

**netsh http add urlacl url=http://+:8051/ user=NetworkService**

* Apagar

**netsh http delete urlacl url=http://+:8051/**

* Exibir

**netsh http show urlacl**

A porta **8051** é padrão no sistema e caso seja alterada na tag **HttpPort** no arquivo de configuração do Host, precisa ser alterada no link acima.

Documentações REST

Documentações de apoio da Framework para utilização de REST para execução de Processos.

Antiga API: 

RestProcess - <https://tdn.totvs.com/x/WBJnF>

Nova API:

Job Execution - <https://tdn.totvs.com/x/1gp7GQ>

Job Schedule - <https://tdn.totvs.com/x/e0F0GQ>

## **Páginas:**
