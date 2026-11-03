---
content_hash: 7d381faed0e14b981ec48607e11e819a0a76b8b08c756f7ccf5bd29dc00cf8f0
fetched_at: '2026-06-29T00:08:50.303499+00:00'
page_id: '334334035'
product: rm
source: tdn-rm
title: Como incluir para todos os funcionários da coligada os dados no campo “Tipo
  de Rua”, sem a necessidade de editar cada registro.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334334035
version: 2
---

### Alteração Global Campos Cadastro Funcionário – Inclusão de dados no campo Tipo de Rua

Nas versões anteriores o processo de "Alteração Global dos Campos" apresentava apenas as opções relacionadas ao cadastro dos funcionários. Com a liberação das implementações do terceiro pacote de adequações ao eSocial, foram disponibilizadas opções para atender aos campos da tabela PESSOA.

Entre elas esta a opção para alterar a informação do campo Tipo de Rua do Endereço de Funcionários. Esta funcionalidade visa facilitar a alteração do campo, com o recurso de alteração para vários funcionários, de acordo com a seleção definida.

Para executar a alteração, o usuário deverá selecionar no campo Dados a serem alterados, a nova opção "Dados Pessoais". Serão listados os campos possíveis de serem alterados: Bairro, Rua, Tipo de Bairro além da opção Tipo de Rua.

**Atenção!** Antes de realizar alteração na base de produção faça um backup da sua base de dados e realize testes na sua base de dados teste.

Veja um exemplo da fórmula a ser utilizada na Alteração Global do campo Tipo Rua. A fórmula abaixo deverá ser alterada de acordo com a necessidade dos clientes e relativamente com o campo que desejar alterar:

**Código: TipoRua**

**Descrição: Alteração Tipo Rua do Endereço dos funcionários**

**Texto:**  
DECL NOMERUA, TIPORUA;  
SETVAR(NOMERUA, TABPESSOA('RUA', 'S'));  
SE SUBSTR(NOMERUA, 1, 4) = 'RUA ' OU SUBSTR(NOMERUA, 1, 4) = 'Rua ' OU SUBSTR(NOMERUA, 1, 2) = 'R ' OU SUBSTR(NOMERUA, 1, 3) = 'R. '  
ENTAO  
SETVAR(TIPORUA, 1)  
SENAO SE SUBSTR(NOMERUA, 1, 3) = 'AV ' OU SUBSTR(NOMERUA, 1, 4) = 'AV. ' OU SUBSTR(NOMERUA, 1, 4) = 'AVE ' OU SUBSTR(NOMERUA, 1, 5) = 'AVE. ' OU SUBSTR(NOMERUA, 1, 8) = 'AVENIDA '  
ENTAO  
SETVAR(TIPORUA, 6)  
SENAO  
SETVAR(TIPORUA, ' ')  
FIMSE;  
TIPORUA

**OBS:** A nomenclatura utilizada na fórmula para definir os Tipos de Rua deve esta de acordo com o patrão que foi utilizado no cadastro de endereços dos funcionários.
