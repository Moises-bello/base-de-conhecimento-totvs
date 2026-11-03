---
content_hash: 8ea8a9e7a9ffa112fe77fe7c4d00041c37c83dbace7010edd2aaf7703df4f044
fetched_at: '2026-06-29T00:11:32.295591+00:00'
page_id: '745764895'
product: rm
source: tdn-rm
title: Configurando APIs
type: documentation
url: https://tdn.totvs.com/display/LRM/Configurando+APIs
version: 1
---

Este documento busca demonstrar como encontrar as APIs e WebServices do Totvs Construção Gestão de Imóveis para consumo das funcionalidades existentes no produto.

**1 - APIs**

Para que se possa visualizar as APIs disponibilizadas pelo RM TCGI, siga os passos do link:  
[Linha RM - Integrações - O que é o Swagger?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058274033-Linha-RM-Integra%C3%A7%C3%B5es-O-que-%C3%A9-o-Swagger-)  
 [Link](https://tdn.totvs.com/pages/editpage.action?pageId=643550124)

Agora que entendemos como consultar o swagger para visualizar todas as APIs do RM, na lista apresentada abaixo na pagina, você deverá procurar por todas as APIs que contenha o início do nome com "**IMB...**":

**2 - WebServices**

No caso dos WebServices deverá ocorrer a devida configuração no host para exposição, para entender como fazer:

Após ter configurado e colocar o host para ser executado, conseguimos visualizar a lista de WebServices disponíveis através do aplicativo TotvsWSClient.exe, para configurar o aplicativo TotvsWSClient.exe segue o link:   
Configurando TOTVS WS Client  
  
Com o TotvsWSClient.exe configurado e executando podemos fazer a busca dos WS do TCGI, todos os WS terão no início do nome com "**IMB...**":

Ao selecionar o WS desejado e clicar em carregar, o sistema exibe todos os dados relacionados a tabela utilizada:
