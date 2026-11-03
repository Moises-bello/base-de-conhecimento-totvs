---
content_hash: cc6c4c56e2cd0e081cb615d477141f2bd9ad2e7509f9fa516ccde15418232883
fetched_at: '2026-06-29T00:10:45.954717+00:00'
page_id: '553900870'
product: rm
source: tdn-rm
title: Opções sobrescrever na importação de Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553900870
version: 12
---

false

**A partir das Versões:**

* 12.1.28.138 e superiores.

# Objetivo:

---

Tem como objetivo apresentar as configurações da importação do funcionário.

Importante

* Os parâmetros apresentados abaixo poderão ser utilizados conforme necessidade na importação;
* Caso realize a importação de um novo funcionário e o mesmo já possua a pessoa cadastrada e não marque o parâmetro **Sobrescrever Dados Pessoais**, a importação ocorrerá com sucesso, porém não haverá atualização de dados cadastrais.
1true1Parâmetro Sobrescrever Dados ContratuaisParâmetro Sobrescrever Dados Contratuais

Ao marcar este parâmetro o sistema irá realizar a importação verificado se o FUNCIONÁRIO já existe na base, e caso exista irá sobrescreve os DADOS CONTRATUAIS.

A verificação da existência do FUNCIONÁRIO é analisada pelos campos: Chapa e Número da Ficha de Registro dentro da coligada.

**Exemplo:**

Funcionário já está cadastrado em nossa base com a chapa: 00078.  Importação do funcionário alterando o campo NOME (dados pessoais) e o campo FUNÇÃO (dados contratuais) com o parâmetro **Sobrescrever Dados Contratuais**marcado.

O sistema irá realizar a importação com sucesso, porém irá sobrescrever somente os DADOS CONTRATUAIS do funcionário, ou seja, o campo FUNÇÃO. O campo NOME, por ser um dado pessoal, não sofrerá alteração.

2Parâmetro Sobrescrever Dados PessoaisParâmetro Sobrescrever Dados Pessoais

Ao marcar este parâmetro o sistema irá realizar a importação do funcionário verificando se a PESSOA já existe na base, e caso exista irá sobrescrever os DADOS PESSOAIS.

A verificação da existência da PESSOA é analisada pelos campos: CPF e Data de Nascimento  ou Nome e Data de Nascimento em todas as coligadas.

**Exemplo:**

Funcionário já está cadastrado em nossa base com a chapa: 00078. Importação do funcionário alterando o campo NOME (dados pessoais) e o campo FUNÇÃO (dados contratuais), somente com o parâmetro**Sobrescrever Dados Pessoais** marcado.

O sistema irá realizar a importação com sucesso, porém irá sobrescrever somente os DADOS PESSOAIS, ou seja, o campo NOME, será alterado em todas as coligadas. O campo FUNÇÃO não sofrerá alteração.
