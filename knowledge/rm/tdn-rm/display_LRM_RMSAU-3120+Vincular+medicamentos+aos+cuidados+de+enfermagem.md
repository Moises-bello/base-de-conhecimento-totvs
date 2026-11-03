---
content_hash: 2c68d3c6c5baa88ef4fd1c0be41433cc78a98aed383a6fced7038aa1aef8d34c
fetched_at: '2026-06-29T00:08:57.752449+00:00'
page_id: '354473953'
product: rm
source: tdn-rm
title: RMSAU-3120 Vincular medicamentos aos cuidados de enfermagem
type: documentation
url: https://tdn.totvs.com/display/LRM/RMSAU-3120+Vincular+medicamentos+aos+cuidados+de+enfermagem
version: 8
---

# RMSAU-3120 Vincular medicamentos aos cuidados de enfermagem

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Vincular medicamentos aos cuidados de enfermagem |  |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Integração de cuidados com o PEP2 |  | | Cadastro de produtos |  | |
| **Parâmetro(s):** | A integração com o PEP 2 deve estar ativa |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | RMSAU-3120 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZPEPENFERMAGEMPRD |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Escreva aqui a descrição da nova implementação ou melhoria.

## Procedimento para Utilização

MedicamentosXCuidadosCadastro dos medicamentos

**Parametrizar o RM para integrar com o PEP 2**

Opções / Parâmetros / Parâmetros Gerais / Aba Integração / Aba PEP 2.0

Configurar Url principal e Url Integration PEP

**Permite vincular à cuidados de enfermagem**

No cadastro de produtos deve setar o medicamento para permitir ou não vincular em cuidados de enfermagem

Cadastro / Estoques / Produto (duplo clique no item) / Anexos / Informações TOTVS Saúde / Aba identificação II

Se configurado para integrar com PEP 2 deve mostrar o check box "Permite vincular à cuidados de enfermagem" , somente com esta opção marcada o medicamento irá aparecer na guid dos cuidados de enfermagem.

Vincular medicamentos aos cuidados de enfermagem

**Configurar o cadastro dos cuidados de enfermagem**

Cadastros / Cuidados com o paciente / Prescrição Médica / Itens de Enfermagem

Selecionar um Item do tipo Prescrição de Enfermagem

Se configurado a integração com o PEP 2 deve exibir uma aba de Medicamentos associados

Deve permitir vincular apenas itens que tenham sido marcados como  "Permite vincular à cuidados de enfermagem" .

Após adicionar os produtos pode alterar a quantidade vinculada ao cuidado (sendo 1 a quantidade default).

Integração PEP 2

**Utilizar os cuidados no PEP 2**

Através do PEP 2 > acessar o prontuário eletrônico do paciente / Prescrição Enfermagem

Clicar em + prescrição de enfermagem

Adicionar um Cuidado de Enfermagem que tenha um medicamento vinculado

Selecionar a frequência e clicar em imprimir, depois clicar em Liberar prescrição

Ao clicar na prescrição no horário prescrito (bolinha verde) deve exibir os medicamentos vinculados
