---
content_hash: 9c3aa8a2a4fa6224ce64ec804c3b48967cab98fbf69d96c0438988d61ad7f0c7
fetched_at: '2026-06-29T00:11:32.220563+00:00'
page_id: '745748798'
product: rm
source: tdn-rm
title: cópiaTOTVS Educacional x EAD (WebEnsino e AMS) - Professor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=745748798
version: 1
---

**Professor**

---

**TOTVS Educacional →** **WebEnsino**  
    
 A integração da entidade Professor do TOTVS Educacional será integrada com a entidade Professor do WebEnsino. Essa integração permite todos os tipos de operações, veja abaixo:

|  |  |
| --- | --- |
| **TOTVS EDUCACIONAL** | **WEBENSINO** |
| Inclui no TOTVS Educacional | Inclui no WebEnsino |
| Altera no TOTVS Educacional | Altera no WebEnsino |
| Exclui no TOTVS Educacional | Exclui no WebEnsino |

Para que essa integração seja feita com sucesso é preciso acessar o cadastro de usuários e inserir um login (usuário/senha) para o Professor que irá ser integrado.

O Professor deverá ser incluído, no respectivo cadastro, e o usuário criado deverá ser informado. É necessário também que seja indicado no cadastro desse Professor o CPF, pois sem essas duas informações a integração não é concluída.

Feito isso quando se inclui, altera ou exclui um Professor através do TOTVS Educacional, o sistema gera uma mensagem para o Monitor da Fila de Integração do TOTVS Business Conector indicando que alguma operação foi feita.

Essa mensagem ficará com o status igual a 'Pendente' (0) até que seja executado o Agente de Envio, que permite encaminhar as mensagens do Monitor da Fila de Integração para o TOTVS ESB através de um serviço de JOB. (Podendo ser executado com certa periodicidade, conforme configurações feitas)

O TOTVS ESB, por sua vez, entrega a mensagem ao destino WebEnsino contendo as mesmas informações da enviada. O status dessa mensagem muda para 'Processado com Sucesso' (1). Caso tenha ocorrido algum erro o status ficará igual a 'Erro' (99).
