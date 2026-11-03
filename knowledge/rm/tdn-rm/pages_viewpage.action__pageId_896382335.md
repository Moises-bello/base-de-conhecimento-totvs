---
content_hash: 604f6057c5eafa4b326b4f7b8e7b78814abb0260eb6307e290a509ad10b5c4ad
fetched_at: '2026-06-29T00:12:01.605089+00:00'
page_id: '896382335'
product: rm
source: tdn-rm
title: Processo Seletivo Terceirizado - Ensino Básico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=896382335
version: 6
---

O objetivo desse processo é importar um arquivo de dados com o resultado de um processo seletivo realizado em um outro sistema de terceiros e importar para o TOTVS Educacional.  
Para realizar o processo Acesse: Educacional | Matrícula e Avaliação | Mais | Processo seletivo terceirizado

Na aba de "Layout de importação"  o usuário monta o layout com os dados do seu candidato para serem importados para o sistema. Campos obrigatórios do Layout de importação: - Inscrição - Nome - Data de nascimento - Cidade de nascimento - UF de nascimento - Pai - Mãe - Código do curso - 1º opção - Pontuação - 1º opção - Classificação - 1º opção - Data de nascimento do Pai - Data de nascimento da Mãe - Cidade de nascimento do Pai - UF de nascimento do Pai - Cidade de nascimento da Mãe - UF de nascimento da Mãe.

Exemplo de layout de importação: 18001;CRISTIANO;19011972;BELOHORIZONTE;MG;TPD;09950;01;[aluno@totvs.com.br](mailto:aluno@totvs.com.br);PAI;MAE;22071971;22061984;Belo Horizonte;Belo Horizonte;MG;MG;brasileira

Para tipo de layout de arquivo - Separado por ponto e vírgula (CVS)- os campos são seperados por ponto e virgula. Ex. PAI;MAE;22071971;22061984;Belo Horizonte;Belo Horizonte;MG;MG;brasileira

Para tipo de layout de arquivo - Tamanho Fixo- Os campos são cadastrados de acordo com o tamanho dele sem separação. Ex. Inscrição tamanho 3 , Nascimento tamanho 10. No arquivo 00326/03/2000

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
