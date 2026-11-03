---
content_hash: 0fc790c7d4b5fb1912ad2235587eb0edb0afffe7ddf5ac54a34643fe6bc8d469
fetched_at: '2026-06-29T00:09:32.346835+00:00'
page_id: '425458830'
product: rm
source: tdn-rm
title: Integração RM Processo Seletivo - Matrícula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458830
version: 10
---

Para matricular candidatos que foram aprovados em um processo seletivo do módulo Processo Seletivo RM é necessário que determinado processo seletivo tenha uma área de interesse ofertada vinculada a uma matriz aplicada do curso/habilitação do TOTVS Educacional.   
   
 **Utilizando o serviço:**   
Os candidatos aptos a serem matriculados no sistema são aqueles que estão na lista dos candidatos da última chamada ocorrida pelo processo seletivo em questão, ou seja, o status do candidato deve estar "Em chamada" (id interno do sistema=5).   
É permitida pelo sistema a escolha dos candidatos os quais se quer matricular.   
   
**Contexto Superior:**   
Quando o contexto do sistema é de Ensino Superior é permitido o vínculo dos acertos em provas do vestibular (Provas do Processo seletivo) às Provas de vestibular do sistema (TOTVS Educacional). Desta forma é possível, por exemplo, vincular notas de provas diferentes do candidato a uma única nota de uma prova de vestibular do sistema.   
   
**Candidatos cadastrados como alunos:**   
Logo então os candidatos selecionados são inseridos no sistema como alunos. Serão criadas também para eles matrículas de acordo com período letivo, turma e outros parâmetros selecionados. Se a situação de matrícula selecionada permitir a matrícula automática nas disciplinas assim será executado.   
   
 **Atualização interna no Sistema:**   
O ultimo passo consiste em atualizar a situação dos candidatos que foram matriculados, informando que os mesmos compareceram em chamada, ou seja, nesta integração será atualizado automaticamente no sistema o status do candidato=7, sendo desnecessário executar o processo Registrar Comparecimento em chamadas do Processo Seletivo.   
   
**Lista de Espera**   
Durante o processo de matrícula, se o sistema estiver parametrizado para utilizar a matrícula na lista de espera, o usuário pode habilitar que os alunos sejam inseridos na lista, caso não haja vagas disponíveis na turma/disciplina. 

Integração de campos complementares

Através do parâmetro "***[Copiar campos complementares do candidato para o registro de aluno e de responsável financeiro](https://tdn.totvs.com/x/-ORqIQ)***" é possível copiar as informações de um campo complementar do candidato para o cadastro de aluno.

Informações Complementares

---

[Matricular](http://tdn.totvs.com/x/Rf1bGQ)

[Desmatricular](http://tdn.totvs.com/x/SPxbGQ)

[Balanceamento de turma](https://tdn.totvs.com/display/LRM/Balanceamento+de+Turma)
