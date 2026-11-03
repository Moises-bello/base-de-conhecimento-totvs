---
content_hash: 845aa83efdab58cc8239c5e4d4324c1e545683317e4d3015d95ccdcb55744e97
fetched_at: '2026-06-29T00:09:13.595669+00:00'
page_id: '421375083'
product: rm
source: tdn-rm
title: Como gerar as tags de remuneração outro emprego para autônomos do Totvs Gestão
  Financeira?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421375083
version: 29
---

# Objetivo:

---

Para realizar a geração dos grupos 'infoMV' e 'remunOutrEmpr' do evento S-1200 para autônomos do Totvs Gestão Financeira, será necessário executar os seguintes passos:

1true1Passo 1Passo 1

Acesse o menu Backoffice | Gestão Financeira | Cadastros | Campos complementares | Lançamentos

Realize o cadastro dos três campos complementares abaixo:

Nome: CNPJREMUNOUTREMPR

Tipo: Alfanumérico

Tamanho: 18

Nome: CODCATEG

Tipo: Inteiro

Nome: INDMV

Tipo Inteiro

Caso deseje informar mais de uma remuneração outra empresa para o mesmo lançamento, deverá ser criado os campos complementares (CNPJREMUNOUTREMPR, CODCATEG) seguidos do campo "\_" e uma sequencia numérica e o novo campo VLRREMUNOE, correspondente ao campo **Base de INSS em outra empresa,** seguindo o mesmo padrão dos campos complementares (CNPJREMUNOUTREMPR, CODCATEG).

Exemplo:

Nome: CNPJREMUNOUTREMPR\_1

Tipo: Alfanumérico

Tamanho: 18

Nome: CODCATEG\_1

Tipo: Inteiro

Nome: VLRREMUNOE

Tipo: Real

Nome: VLRREMUNOE\_1

Tipo: Real

2Passo 2Passo 2

No cadastro do lançamento financeiro, serão habilitados os campos na aba "Campos Complementares". Preencha com as informações fornecidas pelo autônomo.

**Observação:**

O campo INDMV deverá ser preenchido referente aos valores do autônomo na empresa onde o cadastro está sendo realizado.

Exemplo: Baseado no exemplo do print abaixo, se estiver cadastrando o autônomo na empresa "Empregador 1", deverá informar no campo INDMV o valor igual a 1, nesse caso a base de INSS não atingiu o teto.

Informações Adicionais

Para mais detalhes do cálculo do INDMV, acesse: , opção Exemplos de INDMV

Na aba Valores | Tributos | ícone , cadastre o valor referente a Base de INSS em outra empresa, conforme os dados cadastrados na aba Campos complementares.

Caso tenha cadastrado os campos complementares (CNPJREMUNOUTREMPR, CODCATEG, VLRREMUNOE) com '\_', siga o passo a passo abaixo:

No cadastro do lançamento financeiro, serão habilitados os campos na aba "Campos Complementares". Preencha com as informações fornecidas pelo autônomo.

Na aba Valores | Tributos | ícone , cadastre o valor total referente as Bases de INSS em outra empresa cadastras no campo complementar (VLRREMUNOE), conforme os dados cadastrados na aba Campos complementares.

3Passo 3Passo 3

Após o cadastro dessas informações basta gerar o xml no caminho RH / folha de pagamento / eSocial / Gerar XML

Os grupos "infoMV" e "remunOutrEmpr" serão gerados considerando os campos complementares e o campo Base de INSS em outra empresa. Caso tenha realizado o cadastro dos campos complementares(CNPJREMUNOUTREMPR, CODCATEG, VLRREMUNOE) com "\_". o lançamento passa a desconsiderar o campo Base de INSS em outra empresa e considera o campo complementar "VLRREMUNOE".

**Atenção:**

* Em caso de mais de um lançamento financeiro para o autônomo com o campo complementar "INDMV" preenchido, será considerado sempre o maior valor para a geração do xml.   
  **Exemplo:** O campo complementar "INDMV" em um lançamento foi preenchido com o valor 2 e em outro lançamento do mesmo período foi preenchido com o valor 3, na geração o sistema irá trazer o valor 3.

Exemplo do XML com mais de um campo complementar cadastrado.

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.23 |
| 12.1.24 |
| 12.1.25 |

falsefalse

**Status:** Finalizado

false

**Data:19/10/2018**

false

**Autor:**
