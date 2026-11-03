---
content_hash: c50da5535febc54b23f4446ecdf41efb502d5939b67a19af0035c9de7d820cfa
fetched_at: '2026-06-29T00:09:33.850655+00:00'
page_id: '425459065'
product: rm
source: tdn-rm
title: Processo Seletivo Terceirizado
type: documentation
url: https://tdn.totvs.com/display/LRM/Processo+Seletivo+Terceirizado
version: 5
---

Nesta tela, será utilizada para cadastrar o processo seletivo que a instituição utilizará para matricular os alunos novos.   
Existe um aba de "Layout de importação" onde o usuário poderá montar o layout com os dados do seu candidato para serem importados para o sistema. Campos obrigatórios do Layout de importação: - Inscrição - Nome - Data de nascimento - Cidade de nascimento - UF de nascimento - Pai - Mãe - Código do curso - 1º opção - Pontuação - 1º opção - Classificação - 1º opção - Data de nascimento do Pai - Data de nascimento da Mãe - Cidade de nascimento do Pai - UF de nascimento do Pai - Cidade de nascimento da Mãe - UF de nascimento da Mãe  
   
Exemplo de layout de importação: 18001;CRISTIANO;19011972;BELOHORIZONTE;MG;TPD;09950;01;aluno@totvs.com.br;PAI;MAE;22071971;22061984;Belo Horizonte;Belo Horizonte;MG;MG;brasileira  
Existe um aba de "Habilitações Oferecidas" onde o usuário poderá informar para qual período letivo e matriz curricular que os alunos serão matriculados.  
**Observações:**  
O campo "Nacionalidade" configurado no layout de importação do processo seletivo deverá ser utilizado com o nome no feminino. Exemplo: Brasileira, Argentina, Espanhola, Norte-Americana, Italiana....  
O campo "Período" configurado no layout de importação matricula o aluno nas disciplinas do período informado.  
Exemplo de layout de importação com o campo "Período":  
18001;CRISTIANO;19011972;BELOHORIZONTE;MG;TPD;09950;01;aluno@totvs.com.br;PAI;MAE;22071971;22061984;Belo Horizonte;Belo Horizonte;MG;MG;brasileira;**2**  
   
O último campo **(2)** é referente ao "Período" portanto esse aluno será matriculado nas disciplinas do 2º Período do curso.  
   
Quando esse campo não existir no layout de importação ou estiver vazio o processo de importação será executado matriculando o Aluno no 1º período do curso.  
   
Caso o responsável já esteja cadastrado no cadastro de pessoas, o sistema utilizará do cadastro já existente. Levando isto em consideração, o sistema irá identificar a pessoa conforme a regra de unicidade informada na parametrização geral do RH.

Quando executar o processo de matrícula, o sistema validará o CPF e Nome do responsável financeiro informado. Caso o nome esteja diferente (ex: Acento, nome diferente e Maiúsculo e minúsculo(Oracle)) e o CPF igual ao Cliente fornecedor já cadastrado, o sistema informará que o responsável já existe e não permitirá a matricula do candidato.

Caso já exista uma pessoa cadastrada no cadastro de pessoas, de acordo com a regra de unicidade parametrizada no gestão de pessoas, o sistema utilizará do cadastro já existente. Levando isto em consideração, existe o parâmetro "Atualizar pessoa existente", que caso seja marcado ira atualizar os dados da pessoa já cadastrada.  
   
O campo Número de inscrição somente poderá conter dígitos, portanto será removido automaticamente caracteres especiais como: pontuação, acentos e letras, etc. Ao matricular o candidato, no processo seletivo terceirizado, o sistema irá gravar o campo "Nacionalidade" do "Responsável financeiro" do aluno com o valor default "Brasileira", caso não seja informado nos dados do candidato.  
   
Foram inclusos os campos abaixo, no layout de importação de arquivo e no cadastro do candidato do processo seletivo:

* Tipo de rua
* Tipo de bairro
* País
* Cor/Raça
* Grau/Escolaridade
* Situação ocupacional
* Data de emissão da identidade

Os campos: Tipo de rua, Tipo de bairro, Cor/Raça, Grau/Escolaridade, e Situação Ocupacional deverão receber o valor do código referente, e não o nome ou a descrição dos mesmos.  
Esses campos poderão ser encontrados nos caminhos abaixo:

* Tipo de rua: BackOffice\Gestão Fiscal\Cadastros\Mais...\Endereço\Tipo de rua
* Tipo de bairro: BackOffice\Gestão Fiscal\Cadastros\Mais...\Endereço\Tipo de bairro
* Cor\Raça: Serviços Globais\Administração\Tabela Dinâmica\Sistema: Folha de Pagamento\IN46 - Cor\Raça
* Situação ocupacional: Serviços Globais\Administração\Tabela Dinâmica\Sistema: Folha de Pagamento\INT06 - Código de situação.

**Geração de lançamentos**

Na matrícula de processo seletivo terceirizado é possível cadastrar o contrato, responsável financeiro, plano de pagamento e gerar os lançamentos por parcela e cota ou por data inicial e final.

**Lista de Espera**

Durante o processo de matrícula, se o sistema estiver parametrizado para utilizar a matrícula na lista de espera, o usuário pode habilitar que os alunos sejam inseridos na lista, caso não haja vagas disponíveis na turma/disciplina.
