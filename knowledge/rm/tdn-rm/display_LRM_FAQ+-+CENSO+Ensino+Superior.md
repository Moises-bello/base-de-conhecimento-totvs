---
content_hash: f1b6f123daed08a3b95df57920408f307b13b23c64bf6460805215569e11fdb5
fetched_at: '2026-06-29T00:08:30.334432+00:00'
page_id: '272422982'
product: rm
source: tdn-rm
title: FAQ - CENSO Ensino Superior
type: documentation
url: https://tdn.totvs.com/display/LRM/FAQ+-+CENSO+Ensino+Superior
version: 14
---

FAQ - Frequently Asked Question

Nesta documentação estão as duvidas mais realizadas por usuários realizadores do CENSO.

Dúvidas

### 1 - A data de referência é igual pra todos?

A data de referência é sempre o último dia do ano de referência do censo. Ex.: O censo do ano é referente a 2023, então a data deve ser 31/12/2023.

### 2 - No CENSO é enviada a carga horaria cursada pelo aluno?

Sim, desde o censo referente à 2015 o MEC exige essa informação.

### 3 - Essa carga horaria só é gerada após a analise curricular ou o processo de preparação realiza este calculo?

O processo de preparação do censo realiza o calculo.

### 4 - E sobre o campo PARFOR e LICENCIATURA que deve ser criado como campo complementar?

Não é necessário a criação de nenhum campo complementar, atualmente esses campos já são criados na estrutura do TOTVS Educacional.

### 5 - Sobre o cadastros do anexo da filial, os campos são únicos para educação profissional e superior, porém as informações são diferentes para cada contexto. Como proceder?

Neste caso, será necessário realizar o censo por nível de ensino, informando os dados para todos os níveis.

### 6 - Para quem utiliza o sistema somente para informar os alunos, todos os dados de filial e curso também devem ser parametrizados? E as informações de estrutura e turmas, devem ser informadas?

Caso utilize o sistema somente para informar os aluno, todos os dados de filial/nível de ensino e curso dever sim estar parametrizados. O mesmo acontece com as estruturas e turmas.

### 7 - Sobre as datas: Vamos considerar 01/01 a 31/12 mesmo nos casos em que o período letivo terminou em 03/2024?

Não, neste caso o próximo período letivo deve estar com a data inicial 01/04/2024 para que os alunos do próximo censo não apareçam. Após a alteração, deverá utilizar a data 31/03 como data de referência.

**8 - Professor XXXX possui vínculo com turma, mas não é regente, conteudista ou coordenador. Verificar vínculo para envio no censo?**

Essa mensagem ocorre pois no caminho  Currículo e oferta | turma/disciplina | anexos | professores |  guia: Dados do Censo não foi definido a atuação do docente em cada turma, conforme exigências do Censo Escolar/SISTEC.
