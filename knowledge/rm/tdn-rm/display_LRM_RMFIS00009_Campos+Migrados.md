---
content_hash: 919aa3c30c1756557e0a5fc8de07b1a14f5b49882ed2f455447c200d01a8d6db
fetched_at: '2026-06-29T00:09:51.742277+00:00'
page_id: '437260953'
product: rm
source: tdn-rm
title: RMFIS00009_Campos Migrados
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00009_Campos+Migrados
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** |  |
| **Versões:** |  |
| **Ocorrência:** |  |
| **Ambiente:** |  |
| **Passo a passo:** | Definição do Processo     Na versão 11.50, alguns campos complementares utilizados para geração do EFD Contribuições foram migrados para base CorporeRM. Este documento tem, por finalidade, esclarecer e mostrar ao usuário onde realizar o preenchimento dos campos e localizar os mesmos dentro do lançamento fiscal.    **Tabela de Campos Complementares**  Os campos abaixo já foram migrados desde a versão 11.40, estes são utilizados para geração do registro F100:    .    Para maiores informações destes campos, consulte a FAQ abaixo:  [Boletim Técnico - Parametrização Base de Cálculo (PIS/COFINS) Registro F100](http://tdn.totvs.com/pages/viewpage.action?pageId=73076526)    Os campos abaixo, utilizados para geração dos registros D101/105 , C120, M410/810, A170, já podem ser preenchidos nos lançamentos fiscais, também nos movimentos do RM Nucleus:          Relação Campo Complementar x Campo Nativo     Nome do campo Complementar: **INDNATFRETE** – Indicador da Natureza do Frete  Tabela: **DITEM** e **TITMMOV**  Este campo foi migrado para o Item do lançamento fiscal, para habilitar seu preenchimento é necessário que o “*CodModDoc*” (Código modelo de Documento) da espécie vinculada ao lançamento seja um dos   códigos abaixo :  • 07, 08, 8B, 09, 10, 11, 26, 27 e 57        Nome do campo Complementar: DRAWBACK - Número do Ato Concessório do regime Drawback  Tabela: **DLAF** e **TMOV**  Este campo foi migrado para o lançamento fiscal, para habilitar seu preenchimento é necessário que o lançamento se de Entrada (já que são as informações de Importação) e o Cliente/Fornecedor seja do   Exterior, junto com o CFOP 3.xxx.xx. Desta forma, o sistema habilita a aba Exterior:      Nome do campo Complementar: **NATREC** – Natureza da Receita  Tabela: **DITEM** e **TITMMOV**  Este campo foi migrado para o item lançamento fiscal, para habilitar seu preenchimento é necessário   Acessar o a aba Outros dados do Item.  Nome do campo Complementar: **TIPOCREDITO** – Tipo do Crédito PIS/COFINS   Tabela: **DITEM** e **TITMMOV**  Este campo foi migrado para o item lançamento fiscal, para habilitar seu preenchimento é necessário   Acessar o a aba Outros dados do Item.  Nome do campo Complementar: **NATBCCRED**– Código da Base de Cálculo do Crédito   Tabela: **DITEM** e **TITMMOV**  Este campo foi migrado para o item lançamento fiscal, para habilitar seu preenchimento é necessário   Acessar o a aba Outros dados do Item.      Campos não Migrados     Os campos abaixo, ainda não foram migrados para versão 11.50, seu preenchimento deve ser feito através do campo complementar, um no Cliente/Fornecedor (**INDNATRET**) e outro no lançamento Financeiro (**INDNATREC**)        **Para maiores informações:**  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)  **COMUNIDADE****[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)**  **Canais****de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal) |
| **Observações:** |  |
