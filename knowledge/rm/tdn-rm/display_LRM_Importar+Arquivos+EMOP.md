---
content_hash: 3e786b09df2229e5fa9f487e8faf05ed4ec3ce5605d1a0e04f62c8be2df3e48b
fetched_at: '2026-06-29T00:09:16.086823+00:00'
page_id: '421385454'
product: rm
source: tdn-rm
title: Importar Arquivos EMOP
type: documentation
url: https://tdn.totvs.com/display/LRM/Importar+Arquivos+EMOP
version: 2
---

**Importar Arquivos EMOP**

---

A importação de Arquivos EMOP consiste em realizar a importação de Insumos, Composições ou Preços.

A funcionalidade está disponível no menu Projeto > Importações > Importar Arquivos EMOP

Para realizar a importação é necessário:  
 1 - Selecionar o tipo de Importação que será realizada  
 2 - Informar a localização e nome dos arquivos  
 3 – Importar o arquivo.  
    
 **Atenção!**

É possível importar o arquivo com a extensão \*.DBF sem a obrigatoriedade de licenças do Microsoft Office, ou seja, mesmo que o ambiente não contenha a licença, o processo importa os Insumos, Composições ou Preços normalmente.

Para migração da funcionalidade para tecnologia \*.Net foi utilizado o drive OleDB para conversão dos arquivos \*.DBF em ADO.Net, porém o mesmo será utilizado somente em ambientes locais ou em arquitetura 32 bits. Contudo, o drive não é compatível com arquitetura 64 bits.  
 Pensando nisso, foi disponibilizado no diretório de instalação o aplicativo "RM.ConvertDBToXML.exe". O aplicativo consiste em converter os arquivos \*.DBF para o formato XML.  
    
 **PARA CONVERTER O BACKUP SIGA OS PASSOS ABAIXO:**

Execute o aplicativo "RM.ConvertDBToXML.exe" que se encontra no diretório de instalação.  - Escolha o caminho onde consta os arquivos \*.DBF (Caminho Origem). - Escolha o caminho onde o novo backup em formato .XML será salvo (Caminho Destino). - Selecione "Converter" para executar o processo. - Após a conversão, os arquivos gerados podem ser utilizados normalmente pela rotina de importação citada acima.
