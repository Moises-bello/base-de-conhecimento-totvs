---
content_hash: f1f1d1001480f14542a743242503db8413e2f63f4201c46e324ef7a6f238b420
fetched_at: '2026-06-29T00:09:34.571668+00:00'
page_id: '425459192'
product: rm
source: tdn-rm
title: TOTVS Educacional x EAD (WebEnsinoAMS) - Matrícula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459192
version: 4
---

**Matrícula**

---

A entidade Matrícula pode ser sincronizada do TOTVS Educacional para o WebEnsino, ou do WebEnsino para o TOTVS Educacional.  
     
 **TOTVS Educacional** **è WebEnsino**  
    
 A integração da entidade Matrícula em uma disciplina e-learning do TOTVS Educacional será sincronizada com a entidade Matrícula e-learning do WebEnsino. Essa integração permite todos os tipos de operações, veja abaixo:

|  |  |
| --- | --- |
| **TOTVS EDUCACIONAL** | **WEBENSINO** |
| Inclui no TOTVS Educacional | Inclui no WebEnsino |
| Altera no TOTVS Educacional | Altera no WebEnsino |
| Exclui no TOTVS Educacional | Exclui no WebEnsino |

**Pré-Requisitos** Para que a integração da Matrícula em uma disciplina e-learning seja feita do TOTVS Educacional para o WebEnsino, são necessários uma série de cadastros:

          Incluir:

- Curso

- Habilitação

- Matriz Curricular

- Matriz Aplicada

- Parametrização por Curso

- Aluno

- Curso/Habilitações

Quando todos os pré-requisitos estiverem cadastrados, no cadastro de aluno (Anexos | Curso/Habilitações), deve ser selecionada a disciplina que deseja fazer a matrícula. Acessar o menu Processos/Matricular Aluno e concluir a operação. Feito isso o sistema gera uma mensagem para o Monitor da Fila de Integração do TOTVS Business Conector indicando que alguma operação foi feita. Essa mensagem ficará com o status igual a 'Pendente' (0) até que seja executado o Agente de Envio, que permite encaminhar as mensagens do Monitor da Fila de Integração para o TOTVS ESB através de um serviço de JOB. (Podendo ser executado com certa periodicidade, conforme configurações feitas) O TOTVS ESB, por sua vez, entrega a mensagem ao destino WebEnsino contendo as mesmas informações da enviada. O status dessa mensagem muda para 'Processado com Sucesso' (1). Caso tenha ocorrido algum erro o status ficará igual a 'Erro' (99). **Observação** A alteração da situação da Matrícula integrada com o WebEnsino é feita pelo menu de 'Matrículas' do TOTVS Educacional. Acessando o processo de 'Alterar Situação da Matrícula' e concluindo a operação. No momento que o processo é concluído, o sistema gera a mensagem para o Monitor da Fila de Integração.  
     
 **WebEnsino è** **TOTVS Educacional**  
     
 A integração da entidade Matrícula do WebEnsino será integrada com a entidade Matrícula Isolada do TOTVS Educacional. Essa integração permite um tipo de operação, veja abaixo:

|  |  |
| --- | --- |
| **WEBENSINO** | **TOTVS EDUCACIONAL** |
| Inclui no WebEnsino | Inclui no TOTVS Educacional |

**Pré-Requisitos**

Para que a integração da solicitação de Matrícula seja feita do WebEnsino para o TOTVS Educacional, é necessário que algumas coisas já estejam pré-cadastradas no TOTVS Educacional: Cadastros que já deverão existir no TOTVS Educacional: - Aluno - Turma - Turma/Disciplina - Matriz Curricular Quando se solicita a Matrícula no WebEnsino o sistema gera uma mensagem que é recebida pelo TOTVS ESB e enviada para o Monitor da Fila de Integração do TOTVS Business Conector. (Todos os pré-requisitos devem estar cadastrados) Essa mensagem ficará com o status igual a 'Pendente' (0) até que seja executado o Agente de Recebimento, que permite encaminhar as mensagens do Monitor da Fila de Integração para o TOTVS Educacional através de um serviço de JOB. (Podendo ser executado com certa periodicidade, conforme configurações feitas) Feito isso o WebEnsino integrou a solicitação de Matrícula com a Matrícula Isolada do TOTVS Educacional. Acessando o cadastro de Matrícula Isolada do TOTVS Educacional, a Matrícula solicitada pelo WebEnsino estará inserida. Essa solicitação faz com que o sistema TOTVS Educacional gere uma nova mensagem, através do Monitor da Fila de Integração, de retorno para o WebEnsino informando que a solicitação foi recebida com sucesso.
