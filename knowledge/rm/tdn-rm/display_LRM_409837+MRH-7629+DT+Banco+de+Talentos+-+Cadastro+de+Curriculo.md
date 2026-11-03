---
content_hash: ca07a41c78a3dd2ee457a4ab57f0692dfe7d4220ebd62ccf995296b8f54d9299
fetched_at: '2026-06-29T00:08:29.059891+00:00'
page_id: '272144139'
product: rm
source: tdn-rm
title: 409837 MRH-7629 DT Banco de Talentos - Cadastro de Curriculo
type: documentation
url: https://tdn.totvs.com/display/LRM/409837+MRH-7629+DT+Banco+de+Talentos+-+Cadastro+de+Curriculo
version: 113
---

# BANCO DE TALENTOS - CADASTRO DE CURRÍCULO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Rotina:** | |  | | --- | | **Rotina** | | Cadastro de currículos |  |  | | --- | | **Rotina(s) envolvida(s)** | | Cadastro de currículos | | Atualização dos dados da pessoa | | Validação de cadastros existentes por CPF | |
| **Cadastros Iniciais:** | Para a utilização do requisito será necessário parametrizar as validações por unicidade e considerar cadastro de pessoa existente quando unicidade for identificada. |
| **Parâmetro(s):** | * Configurações > Gerais > Validações   + Validar unicidade de Pessoa por CPF * Configurações > RM Portal > Banco de Talentos (Currículos)   + Considerar cadastro de pessoa existente quando unicidade for identificada |
| **Tickets relacionados** | 409837 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MRH-7629 |
| **País(es):** | Todos |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Tabelas Utilizadas:** | PPESSOA e VUSUARIOCURRICULO |

## Descrição

Esta implementação visa possibilitar o cadastro de novos currículos quando o usuário já tem cadastro de Pessoa, os dados pessoais já veem preenchidos automaticamente.

## Importante

* Para que funcione corretamente, os parâmetros precisam estar configurados corretamente.
* Se o sistema estiver configurado para permitir CPF Duplicado, e for alterar para essa nova configuração, vale ressaltar que os registros salvar anteriormente em duplicidade, serão ignorados e sempre será retornado o primeiro registro referente ao CPF Duplicado.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado.

1. Aplique o patch do chamado;

## Procedimento para Configuração

Para configurar basta seguir os passos de configuração de parâmetros abaixo:

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **parametrizador**do RM acesse:
   * Configurações > Gerais > Validações

Marque a opção Validade unicidade de Pessoa por 'CPF' e conclua o processo.

* + Configurações > RM Portal > Banco de Talentos (Currículos)

Marque a opção 'Considerar cadastro de pessoa existente quando unicidade for identificada' e conclua o processo.

## Procedimento para Utilização

* Acesse o Banco de Talentos e clique em 'Quero me cadastrar'

As validações são feitas ao preencher os Dados Pessoais.

Após preencher a nacionalidade, o campo CPF irá ser liberado, de acordo com sua região.

Assim que preencher o CPF e clicar na tela ou apertar TAB, a validação será feita. Neste caso temos 3 possibilidade de validações:

* Usuário sem cadastro nas tabelas PPESSOA e VUSUARIOCURRICULO (Usuário sem cadastro nenhum)

Neste caso o usuário irá fazer seu primeiro cadastro, então após preencher o CPF, os outros campos obrigatórios iram aparecer abaixo do CPF.

* Usuário com cadastro somente na tabela PPESSOA (Usuário já cadastrado mas sem currículo)

Neste caso o usuário possui um cadastro interno no sistema, porem não tem nenhum currículo cadastrado. Irá aparecer somente o nome do usuário mas sem possibilidade de alteração.

E uma mensagem informativa dizendo que já tem um pre cadastro e os Dados Pessoais já foram carregados.

* Usuário cadastrado nas duas tabelas PPESSOA e VUSUARIOCURRICULO (Usuário já cadastrado com currículo)

Neste caso irá aparecer somente uma mensagem dizendo que o usuário já esta cadastrado.

divs
