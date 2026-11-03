---
content_hash: ef3ad2270d7fd91b7f0637bdb0780e354b6a53777c1c6676ce1a4374a02bbf8a
fetched_at: '2026-06-29T00:09:35.910684+00:00'
page_id: '425459427'
product: rm
source: tdn-rm
title: TOTVS Gestão de Pessoas x TOTVS e-Learning Management SUITE (LMS) - Matrículas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459427
version: 3
---

---

**Matrículas**

**Mensagem**   A mensagem "enrollment" é gerada na integração de matrículas entre o TOTVS Gestão de Pessoas e o TOTVS LMS.

O TOTVS LMS recebe as mensagens "enrollment" via EAI, processando-as e realizando as ações necessárias na sua base de dados. Para saber mais sobre EAI [clique aqui.](http://tdn.totvs.com/pages/releaseview.action?pageId=5264533) Dados que devem ser enviados pelo TOTVS Gestão de Pessoas na mensagem "enrollment":

• InternalID do usuário sendo matriculado

• CourseInternalID do Treinamento/trilha em que está sendo matriculado

Junto com a mensagem de Matrícula, é enviado a mensagem de usuários que pode ser vista aqui.

**Matrícula**

As matrículas dessa integração ocorrem somente no TOTVS Gestão de Pessoas e são replicadas para o TOTVS LMS. Ao receber a solicitação de matrícula, o TOTVS LMS define automaticamente a permissão de Execução para o Usuário no treinamento/trilha em que ele será matriculado. Essa permissão possibilita que a matrícula seja efetuada.

Quando matriculado, o aluno tem acesso à turma através do Meu Plano.

Para matricular um Aluno acesse **RH | Gestão de Pessoas | Desenvolvimento | Participante | Processos | Matricular Participantes no Curso E-Learning.**

**Observações:**

* A criação da matrícula ocorrerá do mesmo modo que acontece atualmente através das matrículas do Painel de Aprendizagem.
* O processo só poderá ser utilizado para turmas E-Learning.  As matrículas efetuadas poderão ser visualizadas através do anexo E-Learnings.
* O processo não poderá ser executado se não houver integração com LMS ativa.
* É permitido realizar matrícula de um participante mais de uma vez. Nesse caso serão incluídos novos registros nas tabelas VTREINAMENTOELEARNING e VTURMAELEARNING.
