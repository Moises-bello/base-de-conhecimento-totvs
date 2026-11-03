---
content_hash: 74cd51f3772bf88d0d2d34d8ab6e2cc29fa15c038174c643730cc77a2d97d808
fetched_at: '2026-06-29T00:11:32.260229+00:00'
page_id: '745750291'
product: rm
source: tdn-rm
title: cópiacópiacópiacópiaTOTVS Educacional x EAD (4) (4)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=745750291
version: 1
---

**Aluno**

---

A entidade Aluno pode ser sincronizada do TOTVS Educacional para o WebEnsino,  ou do WebEnsino para o TOTVS Educacional.  
     
 **TOTVS Educacional** **è WebEnsino**  
    
 A integração da entidade Aluno do TOTVS Educacional será integrada com a entidade Aluno do WebEnsino. Essa integração permite todos os tipos de operações, veja abaixo:

|  |  |
| --- | --- |
| **TOTVS EDUCACIONAL** | **WEBENSINO** |
| Inclui no TOTVS Educacional | Inclui no WebEnsino |
| Altera no TOTVS Educacional | Altera no WebEnsino |
| Exclui no TOTVS Educacional | Exclui no WebEnsino |

Para que essa integração seja feita com sucesso é preciso acessar o cadastro de usuários e inserir um login (usuário/senha) para o Aluno que irá ser integrado. O Aluno deverá ser incluído, no respectivo cadastro, e o usuário criado deverá ser informado (caso contrário não será integrado. A informação do usuário é obrigatória para integração). É importante também que seja indicado no cadastro desse Aluno o CPF e o seu responsável financeiro, para que as demais integrações como Boletos seja feita sem problemas. Feito isso quando se inclui, altera ou exclui um aluno através do TOTVS Educacional, o sistema gera uma mensagem para o Monitor da Fila de Integração do TOTVS Business Conector indicando que alguma operação foi feita. Essa mensagem ficará com o status igual a 'Pendente' (0) até que seja executado o Agente de Envio, que permite encaminhar as mensagens do Monitor da Fila de Integração para o TOTVS ESB através de um serviço de JOB. (Podendo ser executado com certa periodicidade, conforme configurações feitas) O TOTVS ESB, por sua vez, entrega a mensagem ao destino WebEnsino contendo as mesmas informações da enviada. O status dessa mensagem muda para 'Processado com Sucesso' (1). Caso tenha ocorrido algum erro o status ficará igual a 'Erro' (99).  
      
 **WebEnsino è** **TOTVS Educacional**  
     
 A integração da entidade Aluno do WebEnsino será integrada com a entidade Aluno do TOTVS Educacional.Essa integração permite todos os tipos de operações, veja abaixo:

|  |  |
| --- | --- |
| **WEBENSINO** | **TOTVS EDUCACIONAL** |
| Inclui no WebEnsino | Inclui no TOTVS Educacional |
| Altera no WebEnsino | Altera no TOTVS Educacional |
| Exclui no WebEnsino | Exclui no TOTVS Educacional |

Quando o WebEnsino envia um novo cadastro de Aluno para o TOTVS Educacional, o sistema gera uma mensagem que é recebida pelo TOTVS ESB e enviada para o Monitor da Fila de Integração do TOTVS Business RM Conector. Essa mensagem ficará com o status igual a 'Pendente' (0) até que seja executado o Agente de Recebimento, que permite encaminhar as mensagens do Monitor da Fila de Integração para o TOTVS Educacional através de um serviço de JOB. (Podendo ser executado com certa periodicidade, conforme configurações feitas) Feito isso o WebEnsino integra o cadastro de um novo Aluno com a entidade Aluno do TOTVS Educacional. Acessando o cadastro de Alunos do TOTVS Educacional, o novo aluno enviado pelo WebEnsino estará inserido. Essa inserção faz com que o sistema TOTVS Educacional gere uma nova mensagem, através do Monitor da Fila de Integração, de retorno contendo informações sobre o 'RA' do aluno e informando que a inserção foi feita com sucesso.
