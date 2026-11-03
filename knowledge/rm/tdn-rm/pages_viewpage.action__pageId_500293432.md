---
content_hash: ace443eafa8c07de43493041647d1a4d9a23c685434cc5c8a17210d9eb8fa7f9
fetched_at: '2026-06-29T00:10:24.967598+00:00'
page_id: '500293432'
product: rm
source: tdn-rm
title: Como gerar as tags de remuneração outro emprego para autônomos do Totvs Gestão
  Financeira a partir da versão 12.1.26.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=500293432
version: 19
---

false

**A partir das Versões:**

* + 12.1.26

# Objetivo:

---

 A partir  da versão 12.1.26 para realizar a geração dos grupos 'infoMV' e 'remunOutrEmpr' do evento S-1200  para autônomos do Totvs Gestão Financeira, será necessário executar os seguintes passos:

As informações já cadastradas nos campos complementares serão migradas no conversor da versão 12.1.26.000.O campo complementar INDMV (Indicador de Desconto da Contribuição Previdenciária do Declarante) será levado de acordo com a data do lançamento financeiro mais recente. Os campos CNPJREMUNOUTREMPR e CODCATEG são chave no novo cadastro não podendo estar nulos, antes de executar o conversor favor validar seus cadastros.IMPORTANTE!

1true1Passo 1Passo 1

Acesse o menu Administração pessoal /Cliente e Fornecedor/Anexo /eSocial

O campo INDMV(Indicador de Desconto da Contribuição Previdenciária do Declarante) deverá ser preenchido referente aos valores do autônomo na empresa onde o cadastro está sendo realizado.

**Exemplo:**

Baseado no print abaixo, deverá informar no campo INDMV o valor igual a 1, nesse caso a base de INSS não atingiu o teto.

Remuneração do autônomo =2000,00

Desconto INSS =180

**Exemplo MOS**

Informações Adicionais

Para mais detalhes do cálculo do INDMV, acesse: , opção Exemplos de INDMV

2Passo 2Passo 2

Acesse o menu Administração pessoal /Cliente e Fornecedor/Anexo /Múltiplos vínculos Autônomos.

Este cadastro permite gerar informações para o evento [S-1200-Remuneração do Trabalhador](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719412) (eSocial) relativas ao autônomos que possui mais de um vínculo empregatício com outra(s) empresa(s).

No exemplo abaixo foi cadastrado dois vínculos. 

**Atenção:**

* O Usuário deverá preencher os campos **Tipo de Inscrição, Número de Inscrição, Código da Categoria, Competência Início, Competência Final, Salario Contribuição INSS e Valor do Desconto INSS .**
* O valor informado no campo "Salario Contribuição INSS " Não deve ultrapassar  o valor do teto.
3Passo 3Passo 3

Acesse o menu Administração pessoal/ Cliente e Fornecedor/ Anexo/ Lançamentos.

Na aba Valores | Tributos | ícone , cadastre o valor total referente a Base de INSS em outra empresa, conforme os dados cadastrados no Anexo /Múltiplos vínculos Autônomos (Passo 2). 

Atenção

Os campos **Base (%)** e **Base (Valor)** no **INSS do empregado** não devem ser zerados.

4Passo 4Passo 4

Após o cadastro dessas informações basta gerar o XML no caminho RH / folha de pagamento / eSocial / Gerar XML

Os grupos "infoMV" e "remunOutrEmpr" serão gerados considerando as informações cadastradas no anexo eSocial (Passo 1) e Múltiplos Vínculos Autônomos (Passo 2).  

Exemplo do XML com mais de um múltiplos vínculos  cadastrado.
