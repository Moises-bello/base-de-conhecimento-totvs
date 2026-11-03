---
content_hash: 1bc97762282885448d87700213d3786073297bda3a1fe64d2777841f620846b7
fetched_at: '2026-06-29T00:10:26.863339+00:00'
page_id: '515287866'
product: rm
source: tdn-rm
title: Credenciamento do Prestador
type: documentation
url: https://tdn.totvs.com/display/LRM/Credenciamento+do+Prestador
version: 22
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Principais Campos**
3. **Histórico de Credenciamento**

sumarioVisão Geral

## **01. VISÃO GERAL**

## 

Cadastro onde será informado qual o credenciamento do Prestador junto ao Convênio.

Esse cadastro funciona no sistema de vigências, ou seja, somente novos cadastros com novas vigências são permitidas, dessa forma. Após a criação do cadastro será criado um histórico de credenciamento igual ao credenciamento, ele será sempre utilizado como prestador principal para unidade de faturamento do convênio.

Através do campo **Data Credenciamento**, no momento do **Faturamento para Convênio** o sistema irá buscar o cadastro vigente com base na data do item lançado na Elaboração de Contas onde o Prestador estiver informado.

Principais Campos

| Campo | Descrição |
| --- | --- |
| **Convênio** | Convênio a ser escolhido para vincular o Credenciamento. |
| **Classe** | Classe do Prestador credenciado no Convênio |
| **Credenciamento** | **Direto:**Indica que o Prestador é credenciado direto no Convênio. Desta forma, o Prestador poderá receber os honorários, dos procedimentos realizados, diretamente do Convênio.  **Indireto**: Indica que o Prestador não é credenciado ao Convênio, mas realiza procedimentos em Hospitais ou Clínicas que são credenciados. Desta forma, o Prestador receberá seus honorários, dos procedimentos realizados, através de Repasse de Honorários. |
| **Tipo de Credencial** | **CPF** do Prestador Pessoa-Física  **CNPJ** no caso de Prestador Pessoa-Jurídica.  **Código Próprio** fornecido pelo Convênio para identificação do Prestador. |
| **Identidade Profissional** | Identificação do Prestador junto ao Conselho Regional de Medicina |
| **Código Próprio** | Código fornecido pelo Convênio para identificação do Prestador. |

**Parâmetros**

Para que o sistema sempre faça o lançamento do item da Elaboração para aquele Prestador com o credenciamento **Direto como Fora da Conta**, habilitar o parâmetro em:

Ambientes> Gestão hospitalar>Faturamento > Elaboração de contas paciente 2/3

1. 1. Marcar o seguinte parâmetro:**Lançar item como "Fora da Conta" para prestadores credenciados diretamente com convênio.**
   2. Em seguida clique em <avançar>
Histórico de Credenciamento

## **02. HISTÓRICO DE CREDENCIAMENTO**

Na aba histórico é possível ver todos os credenciamentos do Prestador já registros para aquele Convênio.

Nesta mesma tela, também é permitido alterar algum campos, caso algum dado foi digitado de forma errada.

A exceção fica por conta do campo **Data Credenciamento**, se o mesmo foi digitado errado, deverá ser excluído o registro e adicionado um novo.

O histórico possui um campo adicional a unidade de atendimento, quando utilizada será considerado o credenciamento informado, dentro da guia, na tag contratado executante.

XML gerado

Abaixo exemplo  do xml gerado:

Cabeçalho:

Guia Tiss:

Alterações a partir do patch 12.1.2306.157 - Ajuste no campo Credencial do Prestador

No Menu Cadastros/Prestador/Credenciamento/Histórico de Credenciamento, o campo “Credencial” passará a chamar “Código do Prestador na Operadora” e somente será preenchido com o Código fornecido pelo Convênio para identificação do Prestador, quando o Tipo de Credenciamento for “Código Próprio”.

Caso o campo “Tipo de Credenciamento” estiver marcado como CPF/CNPJ ou Identidade Profissional, o sistema irá buscar esta informação no cadastro do prestador.

Informação tratada em:

- Autorização/Cancelamento/Elegibilidade de Guias TISS (webservice) versão 3.05 e superiores

- Faturamento de convênio TISS 3.05 e superiores

- Menu SUS/Elaboração de AIH/Procedimentos Realizados, ao selecionar o campo Documento Recebedor.
