---
content_hash: 418c4143552c55dd975c515afa86f1f03968770ea0697bbd736f917bf852ba5d
fetched_at: '2026-06-29T00:11:32.228610+00:00'
page_id: '745748802'
product: rm
source: tdn-rm
title: cópiaTOTVS Educacional x EAD (WebEnsinoAMS) - Disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=745748802
version: 1
---

**Disciplina**

---

**TOTVS Educacional →** **WebEnsino**  
    
 A integração da entidade Disciplina do TOTVS Educacional será integrada com a entidade Curso do WebEnsino. Essa integração permite todos os tipos de operações, veja abaixo:

|  |  |
| --- | --- |
| **TOTVS EDUCACIONAL** | **WEBENSINO** |
| Inclui no TOTVS Educacional | Inclui no WebEnsino |
| Altera no TOTVS Educacional | Altera no WebEnsino |
| Exclui no TOTVS Educacional | Exclui no WebEnsino |

**Pré-Requisitos** Para que a disciplina seja enviada para o WebEnsino deve ser feito no TOTVS Educacional algumas configurações dentro do cadastro do Curso.

Incluir:

- Habilitação

- Matriz Curricular

- Disciplina Optativa/Eletiva

Todos esses cadastros serão sincronizados para o WebEnsino através do TOTVS ESB (gerando mensagem no Monitor da Fila de Integração e sendo enviada pelo Serviço Agente de Envio).

Veja o relacionamento abaixo:

          \* Habilitação => Série

         \* Matriz Curricular => Matriz

         \* Disciplina Optativa/Eletiva => Disciplina (Essa disciplina também pode ser obrigatória)

Após todos os pré-requisitos serem cadastrados, dentro do cadastro de Disciplina Optativa/Eletiva deverá ser informada a disciplina que deseja integrar com o WebEnsino. Feito isso o sistema gera uma mensagem para o Monitor da Fila de Integração do TOTVS Business Conector indicando que alguma operação foi feita. Essa mensagem ficará com o status igual a 'Pendente' (0) até que seja executado o Agente de Envio, que permite encaminhar as mensagens do Monitor da Fila de Integração para o TOTVS ESB através de um serviço de JOB. (Podendo ser executado com certa periodicidade, conforme configurações feitas) O TOTVS ESB, por sua vez, entrega a mensagem ao destino WebEnsino contendo as mesmas informações da enviada. O status dessa mensagem muda para 'Processado com Sucesso' (1). Caso tenha ocorrido algum erro o status ficará igual a 'Erro' (99).

**Observação:**

A alteração na Disciplina é feita no cadastro da mesma. No momento que a alteração é salva o sistema gera a mensagem para o Monitor da Fila de Integração. Já a exclusão da Disciplina é feita através do cadastro de Disciplina Optativa/Eletiva. No momento que a Disciplina é excluída desse cadastro o sistema gera a mensagem para o Monitor da Fila de Integração.

---
