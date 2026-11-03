---
article_id: 40549497058199
category: ADVPL - Web Service
content_hash: e243b543ca334cd2d0aecefc9b5227667bcde071fce0700faec9e516bf5db925
fetched_at: '2026-06-28T22:40:10.555284+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL -  Restringir acesso
  a API REST Protheus
type: support-article
updated_at: '2026-06-15T13:46:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40549497058199-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Restringir-acesso-a-API-REST-Protheus
---

É possível restringir o acesso a endpoints da API REST do Protheus;

Para APIs customizadas, usa-se o parâmetro cSecurity vinculando a API a uma rotina do sistema, controlando permissões pelo ERP.

Para APIs padrão, utiliza-se o ponto de entrada LOADREST para habilitar apenas os serviços desejados, mantendo essenciais como TOKEN e HEALTHCHECK sempre ativos.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40550424982295)Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
É possível restringir o acesso a endpoints do API REST do Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - REST - A partir da versão 12.2410.  
  
**Solução**  
Ao criar o usuário no Protheus, por padrão, ele terá acesso a todas as APIs do sistema. Para restringir e gerenciar esse acesso, a configuração depende do tipo de API que está sendo requisitada.  
  
**Para APIs customizadas:**  
Você pode utilizar o parâmetro **cSecurity**. Caso informe o nome da rotina que possui relação com a API REST (por exemplo, **MATA030** ou **MATA410**), esse nome será utilizado para a validação dos privilégios do usuário no sistema. Dessa forma, as permissões configuradas no ERP para aquela rotina determinarão se o acesso à API será permitido ou não.

Exemplo de código com uma API customizada com a rotina MATA030

```
#INCLUDE "protheus.ch"
#INCLUDE "restful.ch"

WSRESTFUL TstSecApi DESCRIPTION "API de Teste de Segurança" FORMAT "application/json" SECURITY "MATA030"

	WSMETHOD GET DESCRIPTION "Retorna dados protegidos" WSSYNTAX "/TstSecApi" PATH "/TstSecApi" PRODUCES application/json

END WSRESTFUL

WSMETHOD GET WSRECEIVE WSSERVICE TstSecApi
	Local lRet := .T.
	Local cJsonRet := ""

	cJsonRet := '{"status": "sucesso", "mensagem": "O usuario autenticado possui acesso a rotina MATA030 no Protheus!"}'

	::SetResponse(cJsonRet)

Return lRet
```

**Para APIs padrões:**  
O ponto de entrada **LOADREST** é utilizado para habilitar e definir quais serviços do REST estarão disponíveis para requisição. Porém, o usuário padrão terá acessos as APIS disponíveis no sistema.  
Esse ponto de entrada intercepta chamadas de serviços e é executado antes da inicialização do ambiente.   
Para utilizá-lo na restrição, deve-se efetuar o tratamento do retorno da função, validando o parâmetro **cServiceName** (nome da classe do serviço) para habilitar apenas os serviços que pretende disponibilizar.

**Atenção**: Alguns serviços são essenciais para o funcionamento correto do sistema, sendo recomendado que permaneçam sempre habilitados: **TOKEN, HEALTHCHECK, USERS, COMPANIES, BRANCHES, SYSTEMMODULES, LANGUAGE e BRAND.**  
  
Exemplo de código com **LOADREST:**

```
User Function LoadRest()
  Local cServiceName as character
  Local cList as character
  cServiceName := PARAMIXB[1]
  cList  := "FWJWT|HEALTHCARE"
 
Return (cServiceName $ cList )
```

**Observação:**

* Disponível a partir da LIB Label 20210809.
* As APIs TLPP não passam por esse ponto de entrada.
* O do ponto de entrada **LOADREST** pode causar o mau funcionamento ou bloqueio de rotinas Angular (PO-UI), pois ele intercepta chamadas de serviços REST (via Porta Multiprotocolo - MPP) essenciais para essas aplicações.

**Saiba Mais**  
[WSRESTFUL](https://tdn.totvs.com/display/public/framework/WSRESTFUL)  
[TOTVS Backoffice Linha Protheus - ADVPL - REST com segurança](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8919254403735-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-REST-com-seguran%C3%A7a?source=search)  
[LOADREST - Ponto de entrada para habilitar os serviços do Rest](https://tdn.totvs.com/pages/releaseview.action?pageId=632104977)  
[Configurar Privilégio para controlar acesso a rotinas](https://tdn.totvs.com/pages/releaseview.action?pageId=271389653)
