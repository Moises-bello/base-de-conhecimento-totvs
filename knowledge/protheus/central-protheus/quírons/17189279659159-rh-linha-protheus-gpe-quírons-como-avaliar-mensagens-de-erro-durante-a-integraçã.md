---
article_id: 17189279659159
category: Quírons
content_hash: 318f8d6296ea8fb38d9bf5e00e108eff08519a9d2fec1b41e1c214d9bb5ebfb5
fetched_at: '2026-06-28T22:42:52.164881+00:00'
product: protheus
section_id: 9033517492119
source: central-protheus
title: RH - Linha Protheus - GPE - Quírons - Como avaliar mensagens de erro durante
  a integração
type: support-article
updated_at: '2025-04-17T11:32:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17189279659159-RH-Linha-Protheus-GPE-Qu%C3%ADrons-Como-avaliar-mensagens-de-erro-durante-a-integra%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17189296533783) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como avaliar mensagens de erro durante a integração dos dados Quírons x Protheus e Protheus x Quírons?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**As integrações entre os produtos ocorrem através de ***API's***, ou seja, o **Protheus utiliza as *API's* do Quírons** para se comunicar e atualizar suas informações, e o **Quírons utiliza as *API's* do Protheus** para se comunicar e atualizar suas informações.  
  
Uma ***API* serve para que aconteça uma comunicação entre serviços** **via** ***web,*** e com isso, podem ocorrer falhas nessa comunicação.  
Abaixo, serão listadas algumas das principais causas de falha na integração:  
  
**> 400 - *Bad Request***  
Alguma regra de negócio foi violada ou algum parâmetro está incorreto, ou seja, pode existir uma falha nas informações e *tags* passadas no arquivos *json* para integração entre os serviços das *API's.*Nestes casos, sugerimos avaliar se os serviços *REST* estão no ar/funcionais, se a URL do *REST* foi corretamente informada no Quírons e no Protheus avaliar se a URL do Quírons foi corretamente informada na rotina de Parâmetros (GPEM924), se no Quírons foi cadastrado de maneira correta a Empresa/Filial que terão integração com o Protheus, se foi alterado o compartilhamento de tabelas no Protheus após já ter executado integrações ao Quírons, pois isso pode ocasionar que os registros da tabela RJP sejam gerados com outra chave de integração (diferente da gerada anteriormente), se os campos de auditoria foram incluídos nas tabelas que tem integração com o Quírons, etc.  
  
**> 401 - *Unauthorized***  
Usuário não está autenticado, ou a autenticação é inválida, ou seja, o problema pode estar relacionado às permissões dos usuários para acesso nas *API's*. É importante avaliar se no Protheus, na rotina de Parâmetros (GPEM924), foi informado um usuário e senha de perfil Administrador do Quírons, e se o usuário Protheus que está tentando processar a integração possui perfil com permissão para se comunicar com as *API's* (geralmente perfis de Administrador). Já no Quírons, é importante avaliar se a URL e senha informadas no cadastro estão corretos e se trata de perfil de Administrador no Protheus.  
  
**> 403 - *Forbidden***  
Usuário está autenticado, mas não possui permissão para acesso, ou seja, o usuário pode ter certos níveis de acesso, mas não possui acesso a uma determinada *API* que terá que ser usada naquele momento da integração, por exemplo. Neste caso, é importante avaliar se o usuário e senha informados no Quírons são de perfil Administrador do Protheus, e no Protheus, é importante avaliar se o usuário e senha informados na rotina de Parâmetros (GPEM924) são de perfil Administrador no Quírons, bem como avaliar se o usuário que está processando a integração naquele momento, também tem perfil de Administrador.  
  
**> 404 - *Not Found***  
Não foi encontrado o recurso, ou seja, pode ser que o usuário esteja tentando utilizar um método que não é comportado pela API (por exemplo: está tentando fazer um POST mas o correto seria um GET), ou pode se tratar de uma falha no endereço da URL do *REST* Protheus no Quírons ou falha na informação da URL do Quírons no Protheus. Também pode ocorrer caso o cliente esteja tentando fazer integrações alternando ambientes, por exemplo: a integração geralmente ocorre pelo ambiente de Produção do Protheus, mas estão tentando fazer integração para o mesmo ambiente do Quírons, mas agora com o ambiente Teste do Protheus.  
  
**> 500 *- Internal Server Error***  
O servidor encontrou uma situação com a qual não sabe lidar, sendo geralmente caracterizado por erros, ou seja, pode se tratar de erros a nível de banco de dados, permissões de acesso de usuário, configurações dos ambientes, *timeout* por tentar integrar um grande volume de dados e a *API* demorar para dar um retorno, etc.  
 **Saiba Mais:**[Artigos sobre Quírons](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9033517492119-Qu%C3%ADrons)
