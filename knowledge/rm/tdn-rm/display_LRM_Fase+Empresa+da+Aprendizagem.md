---
content_hash: 9085822707950d39375cd24d12416b9c3abd2e50ec517989c650e496f1b6bb66
fetched_at: '2026-06-29T00:10:42.735595+00:00'
page_id: '547256368'
product: rm
source: tdn-rm
title: Fase Empresa da Aprendizagem
type: documentation
url: https://tdn.totvs.com/display/LRM/Fase+Empresa+da+Aprendizagem
version: 21
---

A Gestão da Fase Empresa de Aprendizagem possibilita a inserção, acompanhamento e desenvolvimento dos alunos na Fase Empresa da Aprendizagem, objetivando o alcance do perfil profissional de conclusão definido para o curso, por meio de avaliação técnico-pedagógica do SENAI.

Os cadastros essenciais à configuração da Fase Empresa de Aprendizagem e todas as informações relacionadas são vinculadas ao Módulo TOTVS Educacional l Educacional

# **Disciplina - Exclusiva Fase Empresa**

# A Disciplina exclusiva da Fase Empresa deve ser cadastrada considerando:

* **Campo Estágio:** Carga Horária Total
* **Opção Exclusiva:** Estágio

# **Matriz Curricular - Exclusiva Fase Empresa**

A Carga Horária da Disciplina exclusiva da Fase Empresa deve ser aplicada ao Campo Complementar: Carga Horária Estágio da Matriz Curricular

A disciplina exclusiva da Fase Empresa deve ser associada à Matriz Curricular como uma Disciplina Optativa/Eletiva

A disciplina da Fase Empresa da Aprendizagem será cadastrada com o campo "Tipo de Disciplina" com a opção "Optativa" (todas as disciplinas Optativas pertencem ao período/módulo 0 (zero) da Matriz Curricular)

# **Período Letivo - Exclusivo Fase Empresa**

O Período Letivo exclusivo da Fase Empresa deve ser criado conforme Máscara Padrão, para que a ele estejam associados os registros específicos da contratação de aprendizes

* **AAAA/FE**

Quando o SENAI for emitir os relatórios de Produção, será utilizado esse Período Letivo como parâmetro

# **Parametrização por Curso - Exclusiva Fase Empresa**

A Parametrização por Curso deverá associar a Matriz Curricular (que comtemple a Disciplina Optativa/Exclusiva da Fase Empresa) ao Período Letivo Padrão (Exclusivo Fase Empresa AAAA/FE)

# **Cadastro de Turma - Exclusiva Fase Empresa**

Para cada contrato da Fase Empresa da Aprendizagem, haverá a necessidade de criar uma Turma e Turma/Disciplina de acordo com o contrato estabelecido, conforme os exemplos a seguir.

* **Situação I:**Suponhamos que uma empresa estabeleça um contrato com o SENAI que compreenda 05 vagas (onde os  os alunos realizarão a Fase Empresa nos mesmos dias da semana e horários). Assim, deve-se criar uma Turma e Turma/Disciplina, para que a instituição de ensino realize a gestão sobre as contrações, como também medir produção de desses 05 alunos.
* **Situação II:**Suponhamos que uma empresa estabeleça um contrato com o SENAI que compreenda 05 vagas, onde os  os alunos realizarão a Fase Empresa em diferentes horários e dias da semana . Assim, deve-se criar uma Turma" e Turma/Disciplina para cada aluno, de modo que a instituição de ensino realize a gestão sobre as contrações, como também medir produção de desses 05 alunos.

Não é possível associar uma mesma disciplina várias vezes em uma mesma Turma. Uma vez criada uma Turma/Disciplina, é necessário cadastrar outra nova Turma para associar a mesma Disciplina utilizada na outra Turma cadastrada anteriormente

O usuário deve informar o Período Letivo Padronizado (AAAA/FE) da Fase Empresa da Aprendizagem e a Matriz Aplicada associada à Parametrização por Curso e no Campo: Nome Reduzido, aconselha-se vincular o Nome Fantasia da Empresa contratante

# **Cadastro de Turma/Disciplina - Exclusiva Fase Empresa**

O cadastro da Turma/Disciplina deve compreender o vínculo de:

* **Disciplina Optativa/Eletiva (Exclusiva da Fase Empresa)**
* **Etapas**
* **Avaliações**
* **Planos de Aula (Considerando a Geração de Horários)**

A Gestão da Fase Empresa da Aprendizagem é realizada da mesma forma que a [Gestão de Estágio](https://tdn.totvs.com/pages/viewpage.action?pageId=668639609) demostrado no Material de Capacitação de Processos Educacionais.

O cadastro de Turmas e Turmas/Disciplinas é realizado conforme processos orientados no  Material de Capacitação de Cadastros Básicos - Tópico: Turma/Disciplina.
