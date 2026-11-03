---
content_hash: f41a7dc6f6247999c5277a44bba94d535dd5df4121777b08ed97c7783edef977
fetched_at: '2026-06-29T00:09:34.832402+00:00'
page_id: '425459256'
product: rm
source: tdn-rm
title: TOTVS Educacional x EAD (WebEnsinoAMS) - Turma/Disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459256
version: 6
---

**Turma/Disciplina**

---

A entidade Turma pode ser sincronizada do TOTVS Educacional para o WebEnsino.  
  A integração da entidade Período Letivo/Turma Disciplina do TOTVS Educacional será integrada com a entidade Turma do WebEnsino. Essa integração permite todos os tipos de operações, veja abaixo:

|  |  |
| --- | --- |
| **TOTVS EDUCACIONAL** | **WEBENSINO** |
| Inclui no TOTVS Educacional | Inclui no WebEnsino |
| Altera no TOTVS Educacional | Altera no WebEnsino |
| Exclui no TOTVS Educacional | Exclui no WebEnsino |

**Pré-Requisitos**

Para que a integração do Período Letivo e da Turma seja feita do TOTVS Educacional para o WebEnsino, são necessários uma série de cadastros:

**Incluir:**

- Período Letivo

- Curso

- Habilitação

- Matriz Curricular

- Matriz Aplicada

- Parametrização por Curso

- Disciplina

- Turma

- Turma Disciplina

Após todos os pré-requisitos estarem cadastrados, no cadastro da Turma Disciplina deverá ser indicado o período letivo, o curso e a disciplina criados anteriormente.Feito isso o sistema gera uma mensagem para o Monitor da Fila de Integração do TOTVS Business Conector indicando que alguma operação foi feita. Essa mensagem ficará com o status igual a 'Pendente' (0) até que seja executado o Agente de Envio, que permite encaminhar as mensagens do Monitor da Fila de Integração para o TOTVS ESB através de um serviço de JOB. (Podendo ser executado com certa periodicidade, conforme configurações feitas) O TOTVS ESB, por sua vez, entrega a mensagem ao destino WebEnsino contendo as mesmas informações da enviada. O status dessa mensagem muda para 'Processado com Sucesso' (1). Caso tenha ocorrido algum erro o status ficará igual a 'Erro' (99).

**Observação**

A alteração e exclusão da Turma/Disciplina são feitas no cadastro da mesma. No momento que a alteração é salva, o sistema gera a mensagem para o Monitor da Fila de Integração. No caso da exclusão, quando se exclui a Turma/Disciplina criada o sistema irá gera a mensagem para o Monitor da Fila de Integração.
