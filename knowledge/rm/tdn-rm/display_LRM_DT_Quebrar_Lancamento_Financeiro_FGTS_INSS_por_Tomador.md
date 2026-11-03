---
content_hash: fa56b6cfe03b91fc2be1427f6146ffb8a2c503ad2022397b7a172f50562348cd
fetched_at: '2026-06-29T00:06:14.688098+00:00'
page_id: '210048832'
product: rm
source: tdn-rm
title: DT_Quebrar_Lancamento_Financeiro_FGTS_INSS_por_Tomador
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Quebrar_Lancamento_Financeiro_FGTS_INSS_por_Tomador
version: 3
---

# QUEBRAR O LANÇAMENTO FINANCEIRO FGTS E INSS POR TOMADOR/CEI

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Funcionários* | *Geração SEFIP; Guia de INSS* | |
| **Versões/Release:** | *12.1.6* |

## Descrição

Os processos Geração SEFIP e Guia de INSS geram lançamentos para o Totvs Gestão Financeira caso parametrizados para tal. Pode ser gerado um lançamento financeiro por Tomador/CEI.

## Procedimento para Utilização

Um funcionário pode trabalhar em um ou mais Tomadores, ou em diferentes CEIs de um mesmo Tomador durante um mesmo período de apuração. Essa indicação é feita através do “Rateio Tomadores”, no cadastro de funcionários

Nessas situações, ao gerar o SEFIP e/ou a Guia de INSS, caso parametrizado, deverão ser gerados um lançamento por Tomador, ou por Tomador/CEI.

## **Parametrização Lançamentos Financeiros:**

1- Acessar através do menu **Encargos / Cadastros Financeiros / Parâmetros**

2- Inserir um novo registro, ou editar um registro existente onde o Tipo do Lançamento Financeiro (aba Identificação), seja igual a 15 (FGTS Conforme SEFIP).

3- Acessar a aba Parâmetros e no item Agrupamentos, escolher entre Tomador ou Tomador/CEI.

› A opção Tomador indica que na geração do SEFIP irá gerar um lançamento financeiro por Tomador, mesmo que o funcionário tenha trabalhado em mais de um CEI do Tomador.  
› A opção Tomador/CEI indica que na geração do SEFIP irá gerar um lançamento por Tomador/CEI. Caso o funcionário tenha trabalhado em mais de um CEI de um mesmo Tomador, será gerado um lançamento para cada  CEI.

## **Geração do SEFIP:**

1-  Acesse através do menu **Encargos / Sefip / Geração SEFIP**

2-  Avançar a primeira etapa, marcar para salvar o perfil ao final caso deseje gravar a parametrização.

3-  O código de recolhimento deve ser 155, a modalidade do SEFIP deve ser Branco. Avançar.

4- Informar os dados do responsável e avançar.

5- Informar as opções de geração de arquivo conforme desejado e avançar.

6- Selecionar a(s) coligada(s) desejada e clicar no terceiro botão da esquerda para a direita (Adicionar parâmetros a coligada), será aberto o formulário de parâmetros específicos da coligada. Acessar a aba Lançamento Financeiro e marcar a opção Gerar lançamentos financeiros. Clicar em Ok, e depois Avançar.

7-  Executar

8- Opcionalmente visualizar os lançamentos gerados através do menu **Encargos / Lançamentos / Lançamentos (RM Fluxus).**

## **Guia de INSS**

1- Acessar através do menu **Encargos / Guia de INSS / Guia de INSS**

2- Avançar a primeira etapa, marcar para salvar o perfil ao final, caso deseje gravar a parametrização.

3-  Configurar as seguintes opções:

 › Tipo de Guia: Folha.

 › Informar os percentuais para cálculo.

 › Marcar a opção Movimento por tomador, a opção Construção Civil e informar o Código de Pagamento GPS somente terceiros.

 › Avançar

4-  Em opções de impressão informar o Código do relatório. Avançar.

5- Avançar.

6- Selecionar a(s) coligada(s) desejada e clicar no terceiro botão da esquerda para a direita (Adicionar parâmetros a coligada), será aberto o formulário de parâmetros específicos da coligada. Acessar a aba Lançamento Financeiro e marcar a opção Gerar lançamentos financeiros, informar o código da parametrização criado no item Parametrização dos Lançamentos Financeiros. Clicar em Ok, e depois Avançar.

7- Executar.

8- Opcionalmente visualizar os lançamentos gerados através do menu **Encargos / Lançamentos / Lançamentos (RM Fluxus).**

Na visão de lançamentos **Encargos / Lançamentos / Lançamentos (RM Fluxus)** procurar pelos campos CNPJ Tomador e CEI Tomador para identificar a qual a Tomador ou Tomador/CEI o lançamento pertence.

Na edição dos lançamentos, ir até a aba Integração Folha para verificar os valores desses campos, eles são somente leitura, não podem ser modificados.
