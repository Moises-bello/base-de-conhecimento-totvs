---
article_id: 26621279818263
category: TAF - eSocial -TSS
content_hash: 15284c7b8657f3ea56448f3c3772fe899892e90aa5595432aef9f69a4e547cf4
fetched_at: '2026-06-28T22:45:21.961342+00:00'
product: protheus
section_id: 1500001536761
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - TSS - Erro WSCERR064 / Invalid Content-Type
  return
type: support-article
updated_at: '2026-06-26T12:11:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26621279818263-RH-Linha-Protheus-TAF-eSocial-TSS-Erro-WSCERR064-Invalid-Content-Type-return
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26621268938263) Tempo aproximado para leitura: 00**:02:36 min**

**Ocorrência**Erro WSCERR064 /Invalid Content-Type return no console.log do TSS ou ao transmitir o evento  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - TSS - Transmissão de Documentos Eletrônicos - Todas as versões

**Causa**

WSCERR064 / Invalid Content-Type return (Content-Type: text/html; charset=utf-8) from "URL"  
HEADER:[HTTP/1.1 403 Forbidden]

Entre chaves será apresentado o código que corresponde algum dos problemas listados abaixo:

**400 - Bad Request (má solicitação)** - geralmente, está relacionado a algum problema no link ou pode ser gerado por uma conexão ruim.

**401 - Unauthorized -** você não tem autorização para acessar essa página. Pode acontecer se o IP for bloqueado.

**403 - Forbidden (proibido)** - normalmente ocorre no TSS quando o certificado digital da entidade ou da configuração do **appserver.ini** em **SSLCONFIGURE**está vencido.

**404 - Not Found (não encontrado) -** ocorre quando não encontra a URL desejada.

**407 - Proxy Authentication Required (autenticação de Proxy solicitada) -** na configuração do **appserver.ini** possivelmente esteja habilitado o proxy, mas é provável que não tenha sido inserido o usuário e a senha corretos. Outra possibilidade é de que a rede solicita proxy e ele não esteja configurado no **appserver.**

**408 - Request Timeout (tempo de solicitação encerrado) -** acontece quando a página que está sendo procurada demora muito para carregar e o servidor desconecta o acesso.

**Solução**  
Para solucionar essas ocorrências, valide os seguintes passos:

1. Verifique se o Certificado está na validade com o tamanho correto e configurado corretamente tanto se for Middleware ou TAF

[RH - RM - FOP - eSocial - Middleware: Certificado Digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009264782-RH-RM-FOP-eSocial-Middleware-Certificado-Digital)

[RH - Linha Datasul - eSocial - Middleware - Como configurar o Certificado Digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414078023575-RH-Linha-Datasul-eSocial-Middleware-Como-configurar-o-Certificado-Digital)

[RH - Linha Protheus - TAF - eSocial - Configuração - TSS - Certificado Digital A1 - Como Efetuar Preparação do Certificado Digital e Configurá-lo no TAF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034159554-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-TSS-Certificado-Digital-A1-Como-Efetuar-Prepara%C3%A7%C3%A3o-do-Certificado-Digital-e-Configur%C3%A1-lo-no-TAF)

2. Acesse o servidor onde está instalado o serviço TSS e abra o navegador e tente acessar a URL - <https://webservices.envio.esocial.gov.br/servicos/empregador/enviarloteeventos/WsEnviarLoteEventos.svc> com o certificado digital configurado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26621268939927)

Ele deverá abrir conforme exemplo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26621268940951)

Caso apresente a mensagem abaixo, valide junto a sua equipe de Infraestrutura para liberação da URL - https://webservices.envio.esocial.gov.br/servicos/empregador/enviarloteeventos/WsEnviarLoteEventos.svc

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26621279798935)

3. Mantenha o TSS atualizado na release 12.1.2310 com os últimos artefatos, conforme a documentação - [RH - Linha Protheus - TAF - eSocial - ATUALIZAÇÃO - Links para atualizar o TSS - Transmissão de Documentos Eletrônicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7658806742679-RH-Linha-Protheus-TAF-eSocial-ATUALIZA%C3%87%C3%83O-Links-para-atualizar-o-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos)
