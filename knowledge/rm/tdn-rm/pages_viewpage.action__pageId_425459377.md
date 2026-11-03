---
content_hash: 1d6b02ac16c97d15f2ad6a854dac253ffefb8cb81b58fd56ee6871ef16596248
fetched_at: '2026-06-29T00:09:35.515501+00:00'
page_id: '425459377'
product: rm
source: tdn-rm
title: TOTVS Educacional x EAD (WebEnsinoAMS) - Notas/Score
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459377
version: 6
---

**Notas/Score**

---

**AMS è TOTVS Educacional / Web Ensino è TOTVS Educacional**  
    
 No sistema WebEnsino os alunos terão acesso às avaliações disponíveis para sua Turma.  Cada avaliação quando concluída irá gerar uma Notas/Score que são enviadas para o TOTVS Educacional através do TOTVS ESB. Veja abaixo:

|  |  |  |  |
| --- | --- | --- | --- |
| **AMS** | **TOTVS EDUCACIONAL** | **WEBENSINO** | **TOTVS EDUCACIONAL** |
| Inclusão da Avaliação   (Disponibiliza para o Totvs Educacional através de webservice) | Cadastro das Avaliações de acordo com a Turma/Disciplina.   (Envio para o WebEnsino através do TOTVS ESB) | Avaliação recebida do TOTVS Educacional e disponibilizada para os usuários correspondentes a Turma/Disciplina.   (Execução da Prova) | Recebimento da nota de uma avaliação feita por um determinado aluno. (Através do TOTVS ESB - Monitor da Fila de Integração) |

**Pré-Requisitos:**

Para que a integração da Nota/Score seja feita do WebEnsino para o TOTVS Educacional, são necessários uma série de cadastros:

**Incluir:**

- Curso   
- Habilitação   
- Matriz Curricular   
- Matriz Aplicada   
- Parametrização por Curso   
- Aluno   
- Curso/Habilitações   
- Turma   
- Turma/Disciplina   
- Avaliações

Quando o aluno conclui a prova o WebEnsino envia uma mensagem para o Monitor da Fila de Integração do TOTVS Business Conector (através do TOTVS ESB) informando o RA, a avaliação e a nota. (Todos os pré-requisitos devem estar cadastrados).

Essa mensagem ficará com o status igual a 'Pendente' (0) até que seja executado o Agente de Recebimento, que permite encaminhar as mensagens do Monitor da Fila de Integração para o TOTVS Educacional através de um serviço de JOB. (Podendo ser executado com certa periodicidade, conforme configurações feitas).

Feito isso o WebEnsino integrou a Nota/Score da Avaliação para o TOTVS Educacional.

**Observação:**

As notas vindas do WebEnsino chegam ao TOTVS Educacional como percentual. Esse cálculo é feito internamente no sistema.

---
