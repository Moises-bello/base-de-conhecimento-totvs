---
content_hash: 24146b1905b58bb824095af3f4cc1a5777f9f4d31f38c02879cf90992c269366
fetched_at: '2026-06-29T00:10:16.477066+00:00'
page_id: '469460972'
product: rm
source: tdn-rm
title: Unidade - Processo - Cópia de Unidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=469460972
version: 27
---

Introdução

O processo de cópia de unidade tem por finalidade realizar uma cópia de uma unidade existente no sistema, respeitando parâmetros pré existentes, assim como suas subunidades e com novas configurações selecionadas durante o processo.

Procedimento para utilização

Ao clicar em processos / copiar unidade, na visão de unidades, o sistema irá exibir os campos como mostra a imagem abaixo:

Campos do processo "Copiar Unidade":Novo código inicial para:

* Unidade: Define o código inicial da Unidade que será gerada no processo.
* Número de cópias: Este campo será responsável por gerar um X número de cópias da Unidade, respeitando o código inicial definido no campo acima. Abaixo, alguns exemplos de geração de unidades para códigos do bloco numéricos e alfanuméricos:

|  |  |  |  |
| --- | --- | --- | --- |
| **Novo código inicial** | **Número de cópias** | **Unidade1** | **Unidade2** |
| 0001 | 1 | 0001 |  |
| 0001 | 2 | 0001 | 0002 |
| 1 | 1 | 1 |  |
| 1 | 2 | 1 | 2 |
| 1A | 1 | 1A |  |
| 1A | 2 | 1A1 | 1A2 |
| A1 | 1 | A1 |  |
| A1 | 2 | A11 | A12 |

Importante: O sistema irá sempre respeitar as definições dos campos **"Quantidade Unidade"** e **"Quantidade Subunidade"** do Empreendimento. O processo não permitirá a geração de novas unidades / subunidades se ultrapassarem os valores previamente definidos.

Subunidade

Este painel definirá características que devem ou não ser herdadas das Subunidades presentes na Unidade que está sendo copiada:

* Copiar Vagas
* Copiar Características
* Copiar Tabela de Preço
* Copiar Repasse
* Copiar Rateio de Centro de Custo
Situação após a cópia

* Situação para Venda: Informe a situação da Subunidade gerada para a Venda. O sistema apresentará uma lista de opções de Situações de Subunidades para a Venda já previamente cadastradas no sistema RM SGI no menu Cadastro | Tabelas Adicionais | Situação Sub-Unidade
* Situação para Aluguel: Informe a situação da Subunidade gerada para o Aluguel. O sistema apresentará uma lista de opções de Situações de Subunidades para o Aluguel já previamente cadastradas no sistema RM SGI no menu Cadastro | Tabelas Adicionais | Situação Sub-Unidade;
