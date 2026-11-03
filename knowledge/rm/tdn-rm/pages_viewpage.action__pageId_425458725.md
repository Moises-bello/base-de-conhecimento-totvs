---
content_hash: d79cb9ac6da438453bc1e2d4f267ada8d775cb2a29b3ac64afe0b661faaac35b
fetched_at: '2026-06-29T00:09:31.802342+00:00'
page_id: '425458725'
product: rm
source: tdn-rm
title: Gerar Certificados / Diplomas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458725
version: 35
---

---

# Descrição

Este processo tem por objetivo gerar diplomas, certificados (extensão, competências, atividade ofertada) e registro das solenidades.

# Execução do processo

Para execução do processo de geração de certificado/diploma/solenidade é necessário selecionar uma das abas disponíveis para execução na tela principal do módulo, que são conforme abaixo.

| Ensino Superior | Ensino Básico |
| --- | --- |
|  |  |

## Diplomação

Apenas para o **ensino superior.**

Ao selecionar a aba de diplomação será necessário preencher o(s) filtro(s) para buscar os alunos e após isso selecioná-los para execução.

### Diploma

A opção **Diploma** traz o tipo da via com três opções: primeira, segunda e apostila.

Alguns campos informados no processo serão atualizados na aba Diploma do Curso/Habilitação do aluno, com isso os seguintes campos abaixo tela serão bloqueados nesta aba mencionada.

* Data de conclusão do curso
* Data de colação de grau
* Registro de conclusão
* Livro de registro
* Página de registro
* Nº do processo registro diploma
* Instituição diploma
* Data de emissão do diploma
* Data de registro do diploma
* Data de emissão do histórico final

Atenção

Nos casos em que a instituição de ensino **não atua como registradora do diploma**, os campos **Registro de Conclusão, Livro de Registro, Página de Registro e Nº do Processo de Registro do Diploma** não serão atualizados automaticamente na habilitação do aluno.

Essas informações dependem do retorno da instituição registradora do diploma para que possam ser incluídas no sistema.

Após o recebimento dos dados, eles devem ser inseridos no diploma gerado do aluno. A partir dessa atualização, os campos correspondentes serão refletidos automaticamente na habilitação do aluno.

A partir da versão **12.1.2310** os campos **Instituição de registro e Instituição de emissão** passa a ter um comportamento diferente conforme abaixo.

O campo **instituição de registro**passa a ter dois campos **Registro em outra IES**e **Registro na própria IES**. Ambos são condicionados pela seleção de alunos. Se for selecionados alunos onde o campo de **registro em outra IES**na  estiver parametrizado para **sim** o campo **Registro em outra IES**irá aparecer e será obrigatório no registro do livro, caso contrário se o campo **registro em outra IES**na  estiver parametrizado para **não**, o campo **Registro em outra IES não** irá aparecer e sim o campo **Registro na própria IES** (instituição do MEC) que ficará disponível. Caso for selecionados alunos onde o campo de **registro em outra IES**na  estiver parametrizado para **sim**e outros alunos com este campo como **não**, os **dois**campos irão aparecer, porém o campo **Registro na própria IES** (instituição do MEC) sempre ficará somente leitura e o campo **Registro em outra IES**sempre aberto para selecionar uma .

O campo **instituição de emissão** passa a chamar **Emissão na própria IES** o mesmo ficará somente leitura e preenchido automaticamente pela **Instituição do MEC**, que é definida nos parâmetros da [secretaria](https://tdn.totvs.com/display/LRM/Secretaria#Secretaria-Secretaria7/7:Par%C3%A2metrosGerais).

O intuito desta implementação é unificar as instituições registradora e emissora nos certificados e diplomas, não sendo necessário ter a instituição do MEC e instituição de ensino com os mesmos valores. Vale ressaltar que instituição emissora sempre é a própria instituição, que chamamos de instituição do MEC e instituição registradora para certificados também é a própria instituição (instituição do MEC) e para diplomas irá depender do campo **registro em outra IES**na , se não for registrado também é a própria instituição (instituição do MEC), se for registrado em outra IES será um outra instituição que é cadastrada em .

Vale ressaltar que o campo da instituição do MEC não é persistido no banco de dados, ele é carregado automaticamente no lugar do campo da  conforme regras acima.

A instituição do MEC está disponível em Atividades Acadêmicas | Censo | Instituição do MEC.

Também a partir da versão **12.1.2310**, a etapa de seleção de Assinantes do Diploma terá a seguinte apresentação:

Ao clicar no botão "Adicionar coordenador", será adicionada na lista de participantes o seguinte texto **(Coordenadores - Serão adicionados aqui os coordenadores do curso)** indicando em que posição na listagem de participantes o(s) coordenador(es) do respectivo curso do aluno será(ão) inserido(s). A ordem dos participantes na listagem pode ser alterada utilizando as setas de movimentação para cima e para baixo.

O botão "Remover" remove o item da lista de assinantes que estiver selecionado, e o botão "Limpar" remove todos os itens da lista de assinantes.

Os **coordenadores** que serão adicionados na lista de assinantes são as pessoas que compõem a comissão coordenadora da matriz aplicada do curso do aluno, que possuem a flag "Assinante do diploma digital" marcada, que possuem período de mandato vigente, e cujo **Tipo de Participação** associado a ela tenha como "Cargo do assinante do diploma digital", um desses cargos: **Coordenador de curso, Subcoordenador de curso, Coordenador de curso em exercício.**

A comissão coordenadora está disponível em Currículo e Oferta | Matrizes curriculares| Anexos | Matriz aplicada | Anexos | Comissão coordenadora:

O Tipo de participação está disponível em Atividades acadêmicas | Certificado/Diploma/Solenidade| Mais...| Tipo de participação:

**IMPORTANTE**: A legislação do Diploma Digital, exige que seus assinantes sejam informados com os seus cargos e isso é feito no sistema associando o "Cargo do assinante do diploma digital" ao "Tipo de participação" do assinante.

### Certificado

A opção de **Certificado**também traz o tipo da via, mas apenas com duas opções: primeira e segunda via.

Ao executar o processo, fica a cargo do usuário escolher se os dados inseridos no processo serão atualizados na aba Diploma do Curso/Habilitação do aluno.

Essa configuração pode ser feita também no cadastro do certificado. Ao escolher por atualizar os dados, serão bloqueados na aba diploma os campos listados abaixo.

* Data de conclusão do curso
* Data de colação de grau
* Registro de conclusão
* Livro de registro
* Página de registro
* Nº do processo registro diploma
* Instituição diploma
* Data de emissão do diploma
* Data de registro do diploma
* Data de emissão do histórico final

A partir da versão **12.1.2310** os campos **Instituição de registro e Instituição de emissão** passa a ter um comportamento diferente conforme abaixo.

O campo **instituição de registro** passa a chamar **Registro na própria IES** e o campo **instituição de emissão** passa a chamar **Emissão na própria IES**, ambos ficarão somente leitura e preenchidos automaticamente pela **Instituição do MEC**, que é definida nos parâmetros da [secretaria](https://tdn.totvs.com/display/LRM/Secretaria#Secretaria-Secretaria7/7:Par%C3%A2metrosGerais).

O intuito desta implementação é unificar as instituições registradora e emissora nos certificados e diplomas, não sendo necessário ter a instituição do MEC e instituição de ensino com os mesmos valores. Vale ressaltar que instituição emissora sempre é a própria instituição, que chamamos de instituição do MEC e instituição registradora para certificados também é a própria instituição (instituição do MEC) e para diplomas irá depender do campo **registro em outra IES**na , se não for registrado também é a própria instituição (instituição do MEC), se for registrado em outra IES será um outra instituição que é cadastrada em .

Vale ressaltar que o campo da instituição do MEC não é persistido no banco de dados, ele é carregado automaticamente no lugar do campo da  conforme regras acima.

A instituição do MEC está disponível em Atividades Acadêmicas | Censo | Instituição do MEC.

Também a partir da versão **12.1.2310**, a etapa de seleção de Assinantes do Certificado terá a seguinte apresentação:

Ao clicar no botão "Adicionar coordenador", será adicionada na lista de participantes o seguinte texto **(Coordenadores - Serão adicionados aqui os coordenadores do curso)** indicando em que posição na listagem de participantes o(s) coordenador(es) do respectivo curso do aluno será(ão) inserido(s). A ordem dos participantes na listagem pode ser alterada utilizando as setas de movimentação para cima e para baixo.

O botão "Remover" remove o item da lista de assinantes que estiver selecionado, e o botão "Limpar" remove todos os itens da lista de assinantes.

Os **coordenadores** que serão adicionados na lista de assinantes são as pessoas que compõem a comissão coordenadora da matriz aplicada do curso do aluno, que possuem a flag "Assinante do diploma digital" marcada, que possuem período de mandato vigente, e que possuem um **Tipo de Participação** associado a ela.

A comissão coordenadora está disponível em Currículo e Oferta | Matrizes curriculares| Anexos | Matriz aplicada | Anexos | Comissão coordenadora:

O Tipo de participação está disponível em Atividades acadêmicas | Certificado/Diploma/Solenidade| Mais...| Tipo de participação:

**IMPORTANTE**: A legislação do Diploma Digital, exige que seus assinantes sejam informados com os seus cargos e isso é feito no sistema associando o "Cargo do assinante do diploma digital" ao "Tipo de participação" do assinante.

### Solenidade

A **Solenidade** não traz a opção de vias. A partir desta geração, os alunos passam a constar na lista de **Alunos da solenidade** do cadastro em questão.

## Certificação

Apenas para o **ensino básico.**

Ao selecionar a aba de certificação será necessário preencher o(s) filtro(s) para buscar os alunos e após isso selecioná-los para execução.

É apresentado as opções tipo de via, tipo de certificado e data de emissão.

Ao avançar é apresentado a opção de informar os participantes assinantes deste certificado.

## Participação

Certificado emitido pela IES, para participantes de uma matriz aplicada o filtro por ser feito por curso ou curso genérico.  
O sistema permite a emissão deste para Alunos, professores e por fim Coordenadores da Matriz aplicada, ou seja, basta que uma pessoa esteja associada à matriz aplicada para ter direito a este tipo de certificado.

Através do filtro por estágio consigo visualizar quais os alunos, orientadores e participantes da banca estão aptos para gerar o certificado.

Neste processo será possível informar a origem da carga horária e o tipo de via: primeira e segunda.

No próximo passo será possível efetuar o registro no livro e tipo de participação.

## Competência

É um tipo de certificado concedido à Alunos de acordo com  estipuladas pela instituição, baseado na conclusão de disciplinas que o aluno tenha cursado, não necessariamente da sua matriz aplicada, por exemplo disciplinas isoladas. Quando utilizado, não altera os dados em Curso/habilitação | Aba Diploma, cadastro válido apenas para o ensino superior.

Ao selecionar a aba de competência será necessário preencher o(s) filtro(s) para buscar os alunos e após isso selecioná-los para execução.

Neste processo será possível informar o tipo de via: primeira e segunda.

No próximo passo será possível efetuar o registro no livro (apenas para o **ensino superior**) e tipo de participação. Caso este seja registrado no , apenas aparecerão na tela, livros que não sejam contados por curso, porque as competências não tem vinculo direto com um determinado curso, por isso, só aparecerão livros que o tipo de registro seja **contínuo**.

Após a escolha do tipo de geração será exibidos as informações para o registro no livro e tipo de participação.

## Atividade Ofertada

Certificado emitido para alunos, professores ou pessoas inscritas em uma atividade ofertada para participante ter direito a este, o mesmo deverá apenas ter cumprido a atividade em questão. Para esta funcionalidade, existe agora na tela de Atividades Ofertadas, a opção de se inscrever uma pessoa qualquer em uma atividade e não somente os alunos/Professores. Existe agora o Anexo de pessoas inscritas na tela de . (Quando utilizado, não altera os dados em "Curso/habilitação > Aba Diploma").

Ao selecionar a aba de atividade ofertada será necessário preencher o(s) filtro(s) para buscar os alunos/professores/pessoas e após isso selecioná-los para execução.

Neste processo será possível informar o tipo de via: primeira e segunda.

No próximo passo será possível efetuar o registro no livro e tipo de participação.

# Registro no livro e tipo de certificado

Neste passo é possível informar se irá registrar no livro ou não. Se efetuar o registro, os campos: livro, número do processo, as instituições e a data de registro são obrigatórios o seu preenchimento, caso não deseje registrar em livro os campos: número do processo, as instituições e a data de registro **não** são obrigatórios.

A tabela **SREGISTROLIVRO** não é mais utilizada para armazenar os dados referente ao registro do livro e sim a tabela **SCERTIFICADO**.

| Registrar no livro | Não registrar no livro |
| --- | --- |
|  |  |

Vale ressaltar a mudança de comportamento para registro no livro dos campos de **instituições (registro e emissão)** para **[certificados](https://tdn.totvs.com/pages/viewpage.action?pageId=425458725#GerarCertificados/Diplomas-Certificado)** e **[diplomas](https://tdn.totvs.com/pages/viewpage.action?pageId=425458725#GerarCertificados/Diplomas-Diploma)**.

# Segunda via de certificado/diploma

O sistema permite emitir uma segunda via do certificado/diploma, mas para isso é necessário que a primeira via do certificado/diploma já esteja gerado para o aluno.

Para que o processo encontre a primeira via do certificado/diploma, deve-se selecionar o aluno da mesma matriz aplicada e tipo de certificado, além disso, a primeira via não deve estar com a situação de cancelado.

Exemplo

Supondo que a primeira via do certificado possui um tipo de certificado preenchido. Ao gerar a segunda via deverá preencher também, se não preencher o sistema não irá encontrar a primeira via.
