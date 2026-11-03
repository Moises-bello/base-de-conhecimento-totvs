---
content_hash: 9e6846acea2f38674cca465a0d7d63153a4fe5b78f39e607d29464f5407d4ad6
fetched_at: '2026-06-29T00:08:52.302072+00:00'
page_id: '338376930'
product: rm
source: tdn-rm
title: Como atualizar o Dicionário de Dados do TAF?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338376930
version: 10
---

Alguns usuários relataram que após atualizar o TAF - TOTVS Automação Fiscal e acessar a tela de Monitoramento, o sistema está apresentando a mensagem abaixo:

Para corrigir  o incidente é necessário atualizar o Dicionário de Dados:

Para aplicar o dicionário de dados diferencial, utilizamos uma ferramenta  chamada UPDDISTR. A ferramente atualiza o dicionário de dados do Protheus usando as mesmas regras e funcionalidades do atualizador de versão do Protheus. 

Antes de executar o UPDDISTR você deve baixar o arquivo do Dicionário de Dados completo (SXSBRA.TXT) em nossa Central de Downloads: 

* Acesse a Central de Downloads e aplique os filtros abaixo:

* Realize o Download do arquivo que corresponde ao Dicionários de Dados (sdfbra):

Após baixar o arquivo, é necessário descompactá-lo ou copia -lo na pasta Systemload (Servidor:\totvs\TAF\systemload)

OBS: No caso abaixo o ambiente não possui o arquivo do discionário que vamos atualizar.

Extraia os arquivos que foram baixados da central de downloads e copie o arquivo "sdfbra" :

Cole o arquivo  "sdfbra" na  pasta "systemload":

Após atualizar o arquivo na pasta de instalação do TAF, é necessário rexecutar a ferramenta UPDDISTR:

* Acesse a pasta smartcliente no ambiente de instalação do TAF (servidor:\totvs\TAF\bin\smartclient) e execute o smartclient.exe informando o programa inicial UPDDISTR:

* Execute conforme os passos abaixo:

**OBS:** Caso apresente a mensagem abaixo, clique em "Unlock script" e execute o processo:
