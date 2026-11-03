---
content_hash: aa224ccb268a1ee539612a789194e83b99655c1a8846f681d8a76554d54911c7
fetched_at: '2026-06-29T00:09:09.826082+00:00'
page_id: '394210441'
product: rm
source: tdn-rm
title: DT_Layout_Processo_Seletivo_Tercerizado
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Layout_Processo_Seletivo_Tercerizado
version: 1
---

# PROCESSO SELETIVO TERCEIRIZADO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | ***TOTVS Educacional*** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Processo seletivo terceirizado | Processo seletivo terceirizado |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cadastro de processo seletivo terceirizado | Cadastro de processo seletivo terceirizado | | Cadastro de layout de importação | Cadastro de layout de importação | | Matrícula de candidato aprovado | Matrícula de candidato aprovado | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SCANDIDATOPROCSEL. |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** |  |

Processo seletivo terceirizado

## Descrição

O processo seletivo terceirizado, utilizado a integração com sistemas externos, utiliza um layout customizado para a importação de candidatos aprovados em um processo seletivo e matrícula dos mesmos como alunos no Educacional.

Mais informações no WikiHelp: <http://wikihelp.totvs.com.br/WikiHelp/EDU/EDU.processoSeletivoTerceirizado.aspx>

Inclusão de novos campos:

Para a adequação com campos já existente no cadastro do aluno, foram inclusos os campos, abaixo, no layout de importação de arquivo e no cadastro do candidato do processo seletivo terceirizado:

* Tipo de rua
* Tipo de bairro
* País
* Cor/Raça
* Grau/Escolaridade
* Situação ocupacional
* data de emissão da identidade

O novos campos serão disponibilizados no layout do arquivo, de acordo com os nomes dos campos:

* Tipo de rua: ***CODTIPORUA***
* Tipo de bairro: ***CODTIPOBAIRRO***
* País: ***PAIS***
* Cor/Raça: ***CORRACA***
* Grau/Escolaridade: ***GRAUINSTRUCAO***
* Situação ocupacional: ***CODOCUPACAO***
* Data de emissão da identidade: ***DTEMISSAOIDENT***

Os campos: tipo de rua, tipo de bairro, cor/raça, grau/escolaridade e situação ocupacional deverão receber o valor do código referente, e não o nome ou a descrição dos mesmos.

Esses campos poderão ser encontrados nos caminhos abaixo:

* Tipo de rua: ***BackOffice | Gestão Fiscal | Cadastros | Mais... | Endereço | Tipo de Rua***
* Tipo de bairro: ***BackOffice | Gestão Fiscal | Cadastros | Mais... | Endereço | Tipo de Bairro***
* Cor/Raça: ***Serviços Globais | Administração | Tabela Dinâmica | Sistema: Folha de Pagamento | INT46 - Cor/Raça***
* Gau/Escolaridade: ***Serviços Globais | Administração | Tabela Dinâmica | Sistema: Folha de Pagamento | INT09 - Grau de instrução***
* Situação ocupacional: ***Serviços Globais | Administração | Tabela Dinâmica | Sistema: Folha de Pagamento | INT06 - Código de situação***
