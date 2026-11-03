---
content_hash: dc5bab6afcfd0e2a82dd3f048739b87cd73a26cd53803fa7933233a54ab9aad4
fetched_at: '2026-06-28T21:35:25.094446+00:00'
page_id: '274004323'
product: fluig
source: tdn-fluig
title: Tokens em certificados
type: documentation
url: https://tdn.totvs.com/display/fluig/Tokens+em+certificados
version: 20
---

Importante!

A partir de **Abril de 2025**, o [suporte](https://totvscst.zendesk.com/hc/pt-br/#home) ofertado ao LMS será descontinuado. Não havendo mais evoluções após este período. O LMS não estará mais disponível para acesso nos ambientes a partir da **próxima release** do TOTVS Fluig Plataforma, prevista para o primeiro semestre de 2025.

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é apresentar todos os *tokens* que podem ser utilizados ao configurar um certificado.

# *Tokens* em certificados

Os certificados – que podem ser associados a trilhas, treinamentos ou disciplinas para serem emitidos pelos alunos quando eles concluem esses itens com êxito – suportam *tokens* pré-cadastrados que são substituídos pelos valores que são dinâmicos, de acordo com cada matrícula. A seguir é exibida a lista de *tokens* disponíveis para utilização:

| Objeto | Descrição | Atributos | Exemplo de utilização |
| --- | --- | --- | --- |
| User | Usuário | *name*  *lastname*  *fullName*  *username*  *birthday*  *email* | **Nome**: ${user.name}  **Sobrenome**: ${user.lastname}  **Nome completo**: ${user.fullName}  **Usuário**: ${user.username}  **Data de nascimento**: ${user.birthday?date}  **Email**: ${user.email} |
| Tenant | Empresa | *name*  *domain* | **Nome**: ${tenant.name}  **Domínio**: ${tenant.domain} |
| Enrollment | Matrícula | *dateEnroll*  *dateConclusion*  *scoreClass*  *userRA* (quando utilizada integração com o RM)  *finalScore* | **Data de matrícula**: ${enrollment.dateEnroll?date}  **Data de conclusão**: ${enrollment.dateConclusion?date}  **Nota final (Turma)**: ${enrollment.scoreClass}  **Registro acadêmico**: ${enrollment.userRa}  **Nota final (Turma/Trilha/Treinamento)**: ${enrollment.finalScore} |
| EnrollableItem | Treinamento/Trilha | *name*  *workload*  *objective*  *cost* | **Nome**: ${enrollableItem.name}  **Carga** **horária**: ${enrollableItem.workload}  **Objetivo**: ${enrollableItem.objective}  **Custo**: ${enrollableItem.cost} |
| NormalClass | Turma | *name*  *classInitialDate*  *classFinalDate*  *cost* | **Nome**: ${normalClass.name}  **Data** **inicial**: ${normalClass.classInitialDate}  **Data** **final**: ${normalClass.classFinalDate}  **Custo**: ${normalClass.cost} |
| Discipline | Disciplina | *nome*  *objective*  *ementa*  *methodology*  *coordinator*  *workload*  *scoreApprove* | **Nome**: ${discipline.name}  **Objetivo**: ${discipline.objective}  **Ementa**: ${discipline.ementa}  **Metodologia**: ${discipline.methodology}  **Coordenador**: ${discipline.coordinator.fullName}  **Carga horária**: ${discipline.workload}  **Pontuação de aprovação**: ${discipline.scoreApprove} |

Como utilizar datas?

Existem algumas formas de utilização para as datas que podem ser exibidas nos certificados.

**Exemplo:**Data de matrícula: ${enrollment.dateEnroll**?date?string("dd-MM-yyyy")**}Resultado: **10-12-2017**

**Exemplos de formatos válidos:**

* **dd-MM-yyyy**
* **dd-MM-yyyy hh:mm**
* **hh:mm**

# Exemplo de certificado utilizando *tokens*

A seguir é exibido um exemplo de certificado que utiliza *tokens* para composição do seu conteúdo.

Onde e como crio um certificado?

Você pode conferir o passo a passo para criação e configuração de um certificado no .

0.5falsecertificadosfadetrue1Criação do certificado2Certificado emitido pelo aluno
