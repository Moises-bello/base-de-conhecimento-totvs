---
content_hash: 415d6878f685d153aabc62b3f67ef3a5a9b0a45c11af72d5b9358bc252e933ea
fetched_at: '2026-06-29T00:09:35.380151+00:00'
page_id: '425459335'
product: rm
source: tdn-rm
title: TOTVS Educacional x EAD (WebEnsino e AMS) - Curso
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+Educacional+x+EAD+%28WebEnsino+e+AMS%29+-+Curso
version: 5
---

**Curso**

---

**TOTVS Educacional →** **WebEnsino**  
    
 A integração da entidade Curso do TOTVS Educacional será integrada com a entidade Categoria do WebEnsino. Essa integração permite todos os tipos de operações, veja abaixo:

|  |  |
| --- | --- |
| **TOTVS EDUCACIONAL** | **WEBENSINO** |
| Inclui no TOTVS Educacional | Inclui no WebEnsino |
| Altera no TOTVS Educacional | Altera no WebEnsino |
| Exclui no TOTVS Educacional | Exclui no WebEnsino |

O Curso deverá ser incluído no respectivo cadastro.

Feito isso quando se inclui, altera ou exclui um Curso através do TOTVS Educacional, o sistema gera uma mensagem para o Monitor da Fila de Integração do TOTVS Business Conector indicando que alguma operação foi feita.

Essa mensagem ficará com o status igual a 'Pendente' (0) até que seja executado o Agente de Envio, que permite encaminhar as mensagens do Monitor da Fila de Integração para o TOTVS ESB através de um serviço de JOB. (Podendo ser executado com certa periodicidade, conforme configurações feitas)

O TOTVS ESB, por sua vez, entrega a mensagem ao destino WebEnsino contendo as mesmas informações da enviada. O status dessa mensagem muda para 'Processado com Sucesso' (1). Caso tenha ocorrido algum erro o status ficará igual a 'Erro' (99).
