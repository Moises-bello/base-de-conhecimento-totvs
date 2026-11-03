---
content_hash: 9ec4945216987bb37768ffe5c0ae00cf612f89d4f1e419f2e0326e3f6135cd43
fetched_at: '2026-06-29T00:11:29.200899+00:00'
page_id: '734371059'
product: rm
source: tdn-rm
title: Cadastro Fatores de Infecção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=734371059
version: 5
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Cadastro de Fator de Infecção**
4. **Tela Associação aos Sítios Primários**
5. **Tela Fatores de Infecção do Paciente**
6. **Tabelas utilizadas**

PainelVisão Geral

## **01. VISÃO GERAL**

Essa funcionalidade tem a finalidade de cadastrar os fatores associados a uma infecção.

É possível incluir, editar ou excluir o cadastro.

Esses fatores são associados aos sítios primários de infecção e utilizados para classificar as infecções de um determinado paciente.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

|  |  |
| --- | --- |
| **Menu/Caminho Cadastro:** | Controle de IRAS/Cadastros/Cadastros/Fator de Infecção |
| **Menu/Caminho Utilização:** | Controle de IRAS/Cadastros/Cadastros/Sítio de Infecção |
| **Menu/Caminho Utilização:** | Controle de IRAS/Paciente/Paciente/Paciente/Infecção |

Tela Cadastro de Fator de Infecção

## **03. TELA Cadastro de Fator de Infecção**

Cadastre os fatores de infecção que serão utilizados no sistema.

**Outras Ações / Ações relacionadas**

| Campo | Descrição |
| --- | --- |
| Código | Código do fator de infecção. Esse campo é gerado automaticamente pelo sistema |
| Descrição | Texto descrição do fator de infecção, limitado à 200 caracteres |

Tela Associação aos Sítios Primários

## **04. TELA****Associação aos Sítios Primários**

No cadastro do Sítio Primário é possível inserir todos os fatores relacionados ao Sítio selecionado, para isso basta utilizar a aba "Fatores de Infecção" e pesquisar os fatores.

A pesquisa pode ser feita pelo código ou descrição do fator e para selecionar um ou mais fatores para inserir basta clicar no *checkbox*do grid de pesquisa.

Tela Fatores de Infecção do Paciente

## **05. TELA****Fatores de Infecção do Paciente**

No prontuário do paciente, na aba de "Infecção" é possível associar os fatores que contribuíram para o desenvolvimento / agravamento da infecção

Para inserir um novo fator, o campo "Sítio Secundário" deverá estar preenchido, após essa etapa, ao inserir um novo fator de infecção, o sistema abrirá uma tela de busca onde os fatores podem ser pesquisados por código ou descrição.

Os fatores exibidos na pesquisa são somente os que estão associados ao Sítio Primário relacionado ao Sítio Secundário selecionado na tela.

Tabelas utilizadas

## **06. TABELAS UTILIZADAS**

* SZJFATORINFECCAO - Fatores de Infecção
* SZJXFATORINFECCAOSITIOPRIMARIO - Fatores de Infecção do Sítio Primário
