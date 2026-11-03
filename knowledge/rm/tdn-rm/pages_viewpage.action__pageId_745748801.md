---
content_hash: 93a2c245a39fed0b43f554593de220e9235bd89be3f0086fea7a59c52acafef0
fetched_at: '2026-06-29T00:11:32.225553+00:00'
page_id: '745748801'
product: rm
source: tdn-rm
title: cópiaTOTVS Educacional x EAD (WebEnsinoAMS) - Avaliação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=745748801
version: 1
---

**Avaliação**

---

**AMS è TOTVS Educacional è WebEnsino**  
    
 No sistema AMS serão cadastradas todas as avaliações que ficarão disponíveis, através de um webservice, dentro do TOTVS Educacional.

|  |  |  |
| --- | --- | --- |
| **AMS** | **TOTVS EDUCACIONAL** | **WEBENSINO** |
| Inclusão da Avaliação   (Disponibiliza para o Totvs Educacional através de webservice) | Cadastro das Avaliações de acordo com a Turma/Disciplina.   (Envio para o WebEnsino através do TOTVS ESB) | Avaliação recebida do TOTVS Educacional e disponibilizada para os usuários correspondentes a Turma/Disciplina. |

**Pré-Requisitos**

Para que a integração da Avaliação seja feita do TOTVS Educacional para o WebEnsino, são necessários uma série de cadastros:

          Incluir:

- Curso

- Habilitação

- Matriz Curricular

- Matriz Aplicada

- Parametrização por Curso

- Aluno

- Curso/Habilitações

- Turma

- Turma/Disciplina

O professor deverá primeiramente cadastrar a prova e suas questões no sistema AMS. No TOTVS Educacional acessar o cadastro de Turma/Disciplina - Anexos: Avaliações, e vincular as as provas criadas no AMS ao cadastro de Avaliações, onde poderão ser preenchidas todas a informações necessárias para o WebEnsino, como:

- Código da Etapa

- Valor

- Código da Prova (Avaliação e Pesquisa)

Quando se cadastra uma nova Avaliação no TOTVS Educacional o sistema gera uma mensagem que ficará no Monitor da Fila de Integração do TOTVS Business Conector. (Todos os pré-requisitos devem estar cadastrados) Essa mensagem ficará com o status igual a 'Pendente' (0) até que seja executado o Agente de Envio, que permite encaminhar as mensagens do Monitor da Fila de Integração para o WebEnsino através de um serviço de JOB. (Podendo ser executado com certa periodicidade, conforme configurações feitas) Feito isso o TOTVS Educacional integrou o cadastro da Avaliação para o WebEnsino. (Essa avaliação integrada para o WebEnsino deverá estar disponível para os usuários vinculados a essa Turma/Disciplina)

---
