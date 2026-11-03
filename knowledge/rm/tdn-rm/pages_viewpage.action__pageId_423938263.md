---
content_hash: 95421f1a063de431457e93dafc1d078eaca2c93ecc9781253fe512e9def877ae
fetched_at: '2026-06-29T00:09:26.110606+00:00'
page_id: '423938263'
product: rm
source: tdn-rm
title: TOTVS Colaboração 2.00 (Client Neogrid)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938263
version: 2
---

O TOTVS Colaboração contempla agora uma integração direta do ERP com a NeoGrid: a ferramenta Client Neogrid, um software para envio e recebimento de documentos e que deve ser instalado no servidor do cliente.   
É uma solução de integração simples e padronizada para todos os tipos de documentos e ERPs TOTVS, com foco na performance da solução para o cliente final e na agilidade de atendimento para as equipes de suporte.   
O padrão de comunicação entre os ERPs TOTVS e a NeoGrid é realizado de forma assíncrona com troca de documentos no formato XML em diretórios, sendo que há dois tipos de integração para o ERP: envio de documentos e recebimento de documentos.  
No envio de documentos, o ERP deve gerar um arquivo no diretório OUT contendo as informações de um único documento.   
O Client NeoGrid verifica os arquivos disponíveis nesse diretório e envia para o datacenter da NeoGrid. Durante a transmissão para o WebEDI, o Client NeoGrid move os arquivos da pasta OUT para a pasta TMP.   
Quando a transmissão é concluída, o arquivo é movido da pasta TMP para a pasta SENT (envio realizado com sucesso) ou para a pasta ERROR (arquivos com erro de transmissão).   
A comunicação entre o Client NeoGrid (cliente) e o WebEDI (Datacenter) é via Web Services com protocolo seguro HTTPS.  
No recebimento o Client NeoGrid monitora a existência de arquivos para download no Web EDI.   
Ao realizar o download, o arquivo é gravado no diretório IN e a situação do documento é atualizada no Web EDI.   
O ERP deve monitorar a pasta IN e, ao identificar um arquivo novo, atualizar os dados do arquivo no ERP e eliminar do diretório.   
Na linha RM, isso é feito através do Monitor de Arquivos TOTVS Colaboração.  
Para que o Client Neogrid funcione corretamente, é necessário editar o arquivo MercadorConnector.conf, que fica no diretório a ferramenta está instalada, e informar somente as Credenciais para Autorização do Cliente a Rodar os Serviços no Servidor Mercador, que são os campos conn.username, onde deve ser informado o mesmo usuário da parametrização da filial, conn.password, onde de ser informada a mesma senha da parametrização da filial e conn.senderCNPJ, onde deve ser informado o CNPJ da filial.   
Esse usuário e senha são informados pela Neogrid.  
Assim que a bat startClient do Client Neogrid é executada, o mesmo conecta com a Neogrid e já realiza os processos de busca de arquivos do ERP na basta OUT, os envia para SENT, para que sejam enviados para a Neogrid.   
Também faz o download dos recebidos na Neogrid para colocá-los na pasta IN, assim poderão ser executados pelo ERP, isso tudo de forma automática, pois o Client realiza esses processos de 5 em 5 segundos.

Informações Adicionais

* [Monitor de Arquivos TOTVS Colaboração](http://tdn.totvs.com/display/LRM/Monitor+de+Arquivos)
* [Recebimento Automático de CT-e](http://tdn.totvs.com/pages/viewpage.action?pageId=423938875)
* [Recebimento Automático de NF-e](http://tdn.totvs.com/pages/viewpage.action?pageId=423938872)
* [Recebimento Automático de Cancelamento de NF-e](http://tdn.totvs.com/display/LRM/Recebimento+Cancelamento+de+NF-e)
