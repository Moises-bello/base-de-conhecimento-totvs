---
content_hash: 507efb4b71e2aebafb0bf22e9e3fdce9b6bf322e36eeb1c30709d7280d767122
fetched_at: '2026-06-29T00:11:38.371500+00:00'
page_id: '784772167'
product: rm
source: tdn-rm
title: 02.02 Dados cadastrais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=784772167
version: 2
---

Este passo tem como objetivo permitir que os dados do candidato e dos responsáveis do candidato sejam cadastrados ou atualizados conforme as definições do cadastro de pessoa, pois ao efetuar a matrícula os dados dos usuários do processo seletivo são cadastrados ou atualizados como uma pessoa do sistema, este passo utilizará a definição de campos obrigatórios exatamente como no cadastro de pessoa.

Os campos em negrito no cadastro de pessoa definem quais campos são obrigatórios e estes serão refletidos na atualização de dados cadastrais através da matrícula pela Central do candidato, ou seja, campos obrigatórios do cadastro de pessoa também serão obrigatórios nesta etapa (destacados com **\***), porém o cadastro de pessoa possui inúmeros campo mas somente os campos abaixo serão utilizados para a atualização de dados cadastrais do candidato e de seus responsáveis:

1. **Identificação**
   * Nome
   * CPF
   * Estado Natal
   * Naturalidade
   * Data de Nascimento
   * Estado Civil
   * Sexo
   * Nacionalidade
   * e-mail
   * Telefone Residencial
   * Telefone Celular
2. **Endereço**

   * CEP
   * Tipo de Rua
   * Logradouro
   * Número
   * Complemento
   * Tipo de Bairro
   * Bairro
   * Estado
   * Cidade
   * País
3. **Documentos**

   * CPF
   * Carteira de identidade
   * Emissão
   * Órgão emissor
   * Estado Emissor
   * Passaporte
   * Emissão
   * Data de Validade

A atualização sempre será exibida para os dados do candidato, para os responsáveis será exibida conforme definição dos parâmetros:

Inclusão de pai e mãe

A partir das versões 12.1.31.**250**, 12.1.32.**189**, 12.1.33.**116** e superiores,  o usuário logado que está realizando a matrícula, poderá incluir no cadastro do candidato, até 2 pais ou 2 mães, de acordo com a parametrização realizada.

Ao cadastrar uma nova filiação na matrícula via central, o usuário deverá informar o tipo daquela filiação, se é pai ou mãe.

Importante

Á partir das versões 12.1.2502.**256**, 12.1.2506.**216** e 12.1.2510.**143**, caso o candidato e sou seus responsáveis possuam cadastro como pessoa, os dados de unicidade não poderão ser alterados. Ficará disponíveis para alteração somente somente se o candidato e o responsável, seja ele qual for, não exista como pessoa no TOTVS RM.
