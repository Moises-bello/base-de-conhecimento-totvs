---
content_hash: 59980df0f99f93aa912844b05cc103070b17cacee22e4c52b957e42541464be9
fetched_at: '2026-06-29T00:05:59.818731+00:00'
page_id: '192096086'
product: rm
source: tdn-rm
title: TBC - Web Service ConsultaSQL
type: documentation
url: https://tdn.totvs.com/display/LRM/TBC+-+Web+Service+ConsultaSQL
version: 18
---

## **Introdução**

---

O Web Service **wsConsultaSQL**é responsável pela execução de consultas sql do sistema

## **Como funciona**

---

   Estão expostos no **wsConsultaSQL**alguns serviços, onde para consumi-los é necessário enviar através de uma requisição um envelope SOAP, passando os parâmetros de cada serviço.

 

### Serviços Disponíveis

---

RealizarConsultaSQL

Serviço responsável por executar consultas sql do sistema

1Request

Os parâmetros solicitado pelo RealizarConsultaSQL são:

codSentenca tipo **String**

codColigada tipo **Int**

codSistema tipo **String**

parameters tipo **String**

xmlRequest




wsExemplo

1

G

CODUSUARIO=MESTRE
]]>ResponsexmlResponse




mestre
Usuário Mestre
1
1997-01-01T00:00:00
oaEGFhDF
27621
1
Acesso02
2014-05-08T00:00:00
F
0
mestre@totvs.com.br
T
2015-07-14T13:48:54.417
matheus.sena
BH01
2015-07-14T13:48:54.44
mestre
2015-07-14T13:48:54
5ddcc1c2-94b4-4974-8ed3-99aeb3dee5cf
]]]]>
]]>RealizarConsultaSQLContexto

Serviço responsável por executar consultas sql do sistema, possibilitando informar um contexto para execução.

1Request

Os parâmetros solicitado pelo RealizarConsultaSQLContexto são:

codSentenca tipo **String**

codColigada tipo **Int**

codSistema tipo **String**

parameters tipo **String**

context tipo **String**

xmlRequest




wsExemplo

1

G

CODUSUARIO=MESTRE

CODCOLIGADA=1
]]>ResponsexmlResponse




mestre
Usuário Mestre
1
1997-01-01T00:00:00
oaEGFhDF
27621
1
Acesso02
2014-05-08T00:00:00
F
0
mestre@totvs.com.br
T
2015-07-14T13:48:54.417
matheus.sena
BH01
2015-07-14T13:48:54.44
mestre
2015-07-14T13:48:54
5ddcc1c2-94b4-4974-8ed3-99aeb3dee5cf
]]]]>
]]>Context

As Sentenças SQL cadastradas na Coligada Global (coligada zero) são executadas levando em consideração todas as coligadas que o usuário possui permissão.

Exemplo: Um usuário possui permissão na coligada 1 e na coligada 2 e possui filtro por perfil cadastrados em ambas as coligadas.  Ao executar uma sentença da Coligada Global o sistema irá restringir o resultado de acordo com os filtros cadastrados em ambas as coligadas.

Caso o usuário queira restringir o resultado levando em consideração apenas uma coligada específica, basta informar a coligada no contexto, conforme exemplo abaixo.

xml




wsExemplo

0

G

CODUSUARIO=MESTRE

CODCOLIGADA=1
]]>Importante saber que:

* Sentenças SQL cadastradas em uma coligada específica, por exemplo Coligada 1, sempre será executada no contexto da Coligada 1 mesmo que seja informada uma outra coligada no contexto.
* Sentenças SQL cadastradas na Coligada Global será executada preferencialmente na coligada informada no contexto.

Na dúvida consulte o quadro a seguir:

| Coligada da Sentença SQL | Coligada informada no Contexto | Coligada que será Considerada |
| --- | --- | --- |
| 0 | null | 0 |
| 0 | 1 | 1 |
| 1 | null | 1 |
| 1 | 2 | 1 |

Versões:

Disponível a partir das versões 12.1.31.273. 12.1.32.219, 12.1.33.146 e 12.1.34

  

---

**Para utilização dos Web Services através do aplicativo "Totvs Web Service Test", clique [aqui](http://tdn.totvs.com/x/yBdFCg).**

Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)

|  |  |
| --- | --- |
| **Produto** | Framework |
| **Versão** | 11.82.XX |
| **Processo** | Web Services |
| **Subprocesso** | Utilizando o Web Service wsConsultaSQL |

|  |  |
| --- | --- |
| Status do Documento: | Finalizado |
| Data: | 14/07/2015 |
| Versão: | 11.82.XX |
| Versão Anterior: | 11.82.XX |
| Autores: |  |
