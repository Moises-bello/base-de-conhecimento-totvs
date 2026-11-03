---
content_hash: 158869e8bd9f62de5f7a1b29adb8661d503337e03a0ac7a626c7435f77a6cf63
fetched_at: '2026-06-29T00:11:32.217787+00:00'
page_id: '745748797'
product: rm
source: tdn-rm
title: cópiaTOTVS Educacional x EAD (WebEnsino e AMS) - Percentual de Completude
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=745748797
version: 1
---

**Percentual de Completude**

---

**WebEnsino è** **TOTVS Educacional**  
    
 A integração da entidade Percentual de Completude do WebEnsino será integrada com a entidade Digitação de Notas e Faltas do TOTVS Educacional. Essa integração permite dois tipos de operações, veja abaixo:

|  |  |
| --- | --- |
| **WEBENSINO** | **TOTVS EDUCACIONAL** |
| Inclui no WebEnsino | Inclui no TOTVS Educacional |
| Altera no WebEnsino | Altera no TOTVS Educacional |

**Pré-Requisitos**

Para que a integração do Percentual de Completude seja feita do WebEnsino para o Totvs Educacional, é necessário que algumas coisas já estejam pré-cadastradas no Totvs Educacional:

          Cadastros que já deverão existir no Totvs Educacional:

 - Período Letivo

-  Aluno

- Matrículas no Período Letivo

- Turma

- Turma/Disciplina

Quando se cadastra o Percentual de Completude no WebEnsino o sistema gera uma mensagem que é recebida pelo TOTVS ESB e enviada para o Monitor da Fila de Integração do TOTVS Business Conector. (Todos os pré-requisitos devem estar cadastrados) Essa mensagem ficará com o status igual a zero (0) até que seja executado o Agente de Recebimento, que permite encaminhar as mensagens do Monitor da Fila de Integração para o TOTVS Educacional através de um serviço de JOB. (Podendo ser executado com certa periodicidade, conforme configurações feitas). Feito isso o WebEnsino integrou o Percentual de Completude com a Digitação de Notas e Faltas por Etapa. Indicando o período letivo utilizado e o curso, o sistema TOTVS Educacional carrega as informações da integração com o WebEnsino.

**Observação**

A alteração ocorre da mesma forma da inclusão. Efetuando uma alteração no cadastro de Percentual de Completude do WebEnsino é gerada uma mensagem de integração para o TOTVS Educacional.

---
