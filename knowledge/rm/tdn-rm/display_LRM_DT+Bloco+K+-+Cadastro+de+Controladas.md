---
content_hash: d9e3f987096768897045614af62d8a39b29a92277719b9a94f1039c5b50971aa
fetched_at: '2026-06-29T00:08:53.226770+00:00'
page_id: '344463960'
product: rm
source: tdn-rm
title: DT Bloco K - Cadastro de Controladas
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Bloco+K+-+Cadastro+de+Controladas
version: 7
---

# Cadastro de Controladas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Gestão Contábil*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cadastro de controladas | CtbControladaAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | SPED Contábil | CtbSpedContabilProcessAction | |  |  | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A.* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *CONTROLADORIA01-1091; CONTROLADORIA01-1596* |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *SQLSever / Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows.* |

## Descrição

Com o objetivo de gerar o bloco K100, que identifica as empresas que fazem parte da escrituração contábil consolidada, foi disponibilizado o cadastro de controladas. Considera-se controlada a sociedade na qual a controladora é titular de direitos de sócio que lhe assegurem, de modo permanente, preponderância nas deliberações sociais e o poder de eleger a maioria dos administradores.

**Cadastro de controladas**

No módulo contábil o cadastro está disponível no menu "Obrigação Acessórias → Bloco K".

Ele é composto pelos seguintes campos:

* Coligada controlada: Campo obrigatório que irá listar todas as coligadas cadastradas, com exceção da zero e da corrente.
* Percentual da participação acionária: Campo obrigatório composto por quatro casas decimais, não podendo ser superior a 100.
* Percentual da consolidação: Campo obrigatório composto por quatro casas decimais, não podendo ser superior a 100.
* Inativa: Indica se a controlada foi inativada. Se esta opção estiver marcada a coligada controlada será desconsidera pelas rotinas que envolvem a geração do bloco K.
