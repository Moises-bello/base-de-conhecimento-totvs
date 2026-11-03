---
content_hash: a09e8ff1f6e4fb0bf2a1c9d368d89bbbd5eab24b4182f31b05ce21fac78b4330
fetched_at: '2026-06-29T00:10:46.739099+00:00'
page_id: '555859524'
product: rm
source: tdn-rm
title: Relatório SUS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=555859524
version: 9
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela principal**
4. **Relatório APAC**
5. **Espelho da AIH**

## **01. VISÃO GERAL**

No Totvs Gestão Hospitalar, acessando o menu “Faturamento | Relatório SUS”, será possível imprimir os relatórios do SUS. A partir do release 12.1.29 este menu foi otimizado e migrado para ser executado através da MDI (RM.exe).

Atenção

A nova funcionalidade utiliza o RM Report e a versão anterior utilizava o antigo Gerador. Para utilizar a nova versão é necessário converter o antigo relatório para o RM Reports e ajustá-lo caso seja necessário.

Está disponibilizado um relatório padrão na pasta: C:\TOTVS\CorporeRM\ObjetosGerenciais\Relatórios

## **02. EXEMPLO DE UTILIZAÇÃO**

**Passos para a impressão do relatório SUS:**

Acessar o menu Faturamento → Relatório SUS

Será aberta a tela para o usuário selecionar o relatório que deseja imprimir e filtrar por Competência e/ou Prestador

O usuário poderá apenas visualizar o relatório ou imprimir.

## **03. TELA PRINCIPAL**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| **Tipo do relatório** | Serão listados todos os relatórios que possui o código sus e não é do tipo genérico. Campo de preenchimento obrigatório. |
| **Nome do relatório** | O nome do relatório está relacionado ao tipo do relatório, após a seleção do tipo do relatório, serão listados todos os relatórios do tipo selecionado. Campo de preenchimento obrigatório. |
| **Competência** | Mês/Ano da competência do relatório que será impresso. Campo de preenchimento obrigatório. |
| **Prestador** | O usuário pode ou não selecionar um prestador para imprimir o relatório apenas com a informação dele, caso não selecione o será impresso o relatório com todos os prestadores. |
| **Relatório do SUS** | Serão listado os relatórios do “RM Report” e o mesmo poderá conter os parâmetros com nome “COMPETENCIA\_D”, “COMPETENCIA\_S”, "COMPET" e "CODPROF".  COMPETENCIA\_D e COMPET será o campo competência concatenada com o primeiro dia do mês. Ex. 01/05/2020. |

## **04. RELATORIO APAC**

O relatório SAUREL0032 – Demonstrativo de APAC Magnetico **não está habilitado** para listar dados de Apac de **Quimioterapia**. Atualmente ele lista apenas Apac de Nefrologias.

Este relatório é o mesmo Demonstrativo de Apac, somente para tipo Nefrologia.  
Devemos renomear o relatório para o código SAUREL0045 – Laudo de Nefrologia APAC

 O Parâmetro SUS: “Relatório Demonstrativo de APAC Magnético” (**codreldemoapac**), atualmente só serve para nefrologia. E ao importar este código no RM.exe, o mesmo muda para “APAC.VT.002 - Laudo Nefro APAC”

Será necessário as seguintes alterações:  Salvar o relatório com o código SAUREL0032 – Demonstrativo APAC Magnético.

Quando a APAC for do tipo quimioterapia, o processo “Imprimir Demonstrativo de Apac magnético” deverá trazer somente dados da aba quimioterapia.

## **05. ESPELHO DA AIH**

## 

Para o espelho da AIH, a partir da versão 12.1.2310, deverá ser utilizado como modelo o relatório "**SAUREL0124 - Espelho da AIH**", disponível no TOTVS Compartilhamento.

Este relatório utiliza campos da base e portanto a execução do sistema depende disso, onde é utilizado o recurso de filtro. Portanto é necessário que os campos **SZSUSAIHPROD.CODCOLIGADA e SZSUSAIHPROD.IDAIH** estejam presentes no relatório.

 

Para imprimir o espelho da AIH, selecione as AIHs e clique no processo Espelho da AIH.
