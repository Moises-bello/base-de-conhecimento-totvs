---
content_hash: 044cc8332aaef83d4fd0342d72a3155a2cf22c1e86c4088c368dafa9d4d5f22c
fetched_at: '2026-06-29T00:11:38.761783+00:00'
page_id: '784772495'
product: rm
source: tdn-rm
title: 02.10 Validação de inadimplência (Débitos Financeiros)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=784772495
version: 4
---

**Regra válida a partir da versão 12.1.2302.**

A validação de inadimplência na matricula via central do candidato levará em consideração as definições da parametrização da matricula online do portal do aluno no TOTVS Educacional.

Mais informações acesse:

* [Parâmetros TOTVS Educacional](https://tdn.totvs.com/pages/viewpage.action?pageId=425458610)
* [Matrícula Ensino Básico](https://tdn.totvs.com/pages/viewpage.action?pageId=315906289)
* [Matrícula Ensino Superior](https://tdn.totvs.com/pages/viewpage.action?pageId=354471723)

A matricula via Central do Candidato não consideração a opção “Validar inadimplência de aluno na matricula pelo portal” definida na situação de matricula.

**Comportamento:**

Caso os parâmetros citados anteriormente esteja habilitado, então na etapa de preenchimento dos dados do **responsável financeiro** será verificado ser existe algum débito financeiro vinculado ao CPF informado para o responsável financeiro.

Entende-se como débitos financeiros, parcelas com lançamentos financeiros vencidos (em aberto) para alunos em que o responsavel financeiro tenha o mesmo CPF informado no responsável financeiro  da matricula via central do candidato.

Caso exista algum débito financeiro para o CPF informado será aplicada a regra conforme a parametrização.

**Opção "Alertar alunos" marcada:**

**Opção "Bloquear alunos" marcada:**

Ignorar Validação de Débitos Financeiros (Geral)

É possível **ignorar a validação de débitos financeiros** em matrículas realizadas pela **Central do Candidato** via portal do TOTVS Processo Seletivo.

Para isso o parâmetro "**Não verificar débitos na Matrícula pela Central de Candidatos**" deverá ser marcado, o mesmo  está disponível nos parâmetros do TOTVS Educacional (RM Portal → Matrícula → 4/6)

É importante ressaltar que a **abrangência deste parâmetro é por contexto**, sendo aplicado a todas as matrículas do contexto realizadas pela **Central do Candidato**.  
Além disso, ele **sobrepõe as demais parametrizações**, conforme mencionado no início.

Importante

Este parâmetro está disponível à partir da versão 12.1.2406.101

Ignorar Validação de Débitos Financeiros (Por Área de interesse ofertada)

Através dos **parâmetros de perfil de usuário**, disponíveis no **cadastro da área de interesse ofertada** do Processo Seletivo, é possível permitir que uma área receba matrículas **mesmo que o aluno esteja inadimplente**. Para isso, basta marcar a opção **“Matricular alunos inadimplentes”**.

Para mais informações, consulte a documentação:  

Conforme as imagens acima é apresentada ao usuário uma mensagem padrão, no entanto nos parâmetros do TOTVS Educacional é possível definir uma mensagem customizada que irá substituir a mensagem padrão.

Parâmetros:

Exemplo:
