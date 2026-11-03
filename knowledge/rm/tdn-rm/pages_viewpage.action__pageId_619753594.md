---
content_hash: 6958a258ab083cf41685d4b802f3ab145b4cab220ca4e1d193f6cfb35bf89b6d
fetched_at: '2026-06-29T00:11:03.212606+00:00'
page_id: '619753594'
product: rm
source: tdn-rm
title: Elaboração de APAC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=619753594
version: 8
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Lançamento da APAC**
3. **Lançamento da APAC - CIRURGIA BARIÁTRICA E PÓS CIR.BARIÁTRICA**
4. **Relatório Demonstrativo de APAC Magnético**
5. ****Lançamento da APAC - QUIMIOTERAPIA****
6. ****Relatório SAUREL0045 - Demonstrativo Completo de APAC Magnético.TotvsReport****
7. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Essa funcionalidade é responsável pelo preenchimento da Elaboração de APAC e a impressão do relatório de "**Demonstrativo de APAC Magnético**"**.**

## **02. LANÇAMENTO DA APAC**

Para criar automaticamente a Elaboração da APAC após salvar o registro de atendimento, deverá:

* Estar marcado em Parametros Gerais | Registro e Controle, o campo  "Utiliza cobrança de APACs?"

* Existir um registro de atendimento cujo convênio seja SUS, e neste registro marcado a opção "Cobrança APAC".

Ao acessar o menu **Faturamento => Faturamento SUS => Elaboração de APACs**será preenchido as informações específicas de cada APAC, conforme o procedimento principal.

**Tipo de APAC de acordo com o procedimento principal:**

**Medicamentos**: código do procedimento iniciado com 06.

**Nefrologias**: código do procedimento iniciado com  "0305", "0418", "0301130060", "0301130051"

**Radioterapia**: código do procedimento iniciado com "030401"

**Quimioterapia**: código do procedimento iniciado com "030402", "030403", "030404", "030405", "030406", "030407"

**Cirurgia Bariátrica**:  código do procedimento iniciado com "0301120056" (pós bariátrica), "0301120080" (pré bariátrica)

## 03. **LANÇAMENTO DA APAC - Cirurgia Bariátrica  e Pós Cir.Bariátrica**

Para Habilitar esta funcionalidade , deve conter um registro SUS, e no registro marcado a opção APAC , ao acessar o menu **Faturamento => Faturamento SUS => Elaboração de APACs**

Selecionar o registro e no campo de PROCEDIMENTO PRINCIAPAL  lançar de exemplo "0301120056" O sistema vai habilitar as seguintes abas:

## **04. RELATÓRIO DEMONSTRATIVO DE APAC MAGNÉTICO**

Antes de realizar a impressão do "**Relatório Demonstrativo de APAC Magnético**" na tela da **Elaboração de APAC** é necessário fazer a devida parametrização, acesse o menu**Opções => Parâmetros SUS => Aba : APAC => Sub Aba: Dados Gerais**, informe o campo "**Relatório Demonstrativo de APAC Magnético**" e salve o registro.

Para impressão acesse o menu **Faturamento => Faturamento SUS => Elaboração de APACs** selecione um registro de APAC  e acesse o menu **Processos** => **Impressão do demonstrativo de APAC Magnético**.

## 05. **LANÇAMENTO DA APAC - Quimioterapia**

A partir da competência 03/2022, o APAC Magnético do Datasus criou o campo "Medicamento Antinoeplasicos Administrados".

Estes campos foram inseridos também na Elaboração de APAC do Gestão Hospitalar.

**Validações realizadas no campo Medicamento Antineoplásicos:**

* Não poderá existir medicamentos repetidos.
* O primeiro campo de medicamento é obrigatório ser preenchido.
* Os códigos destes medicamentos são fornecidois pelo Datasus e não serão aceitos outros códigos. Porém habilitamos o cadastro dos mesmos para visualização e futuras manutenções, caso necessário. Veja no menu Cadastros | Outros Cadastros | SUS | Medicamento Antineoplásico (SUS).

## **06. RELATÓRIO **SAUREL0045 - Demonstrativo Completo de APAC Magnético.TotvsReport****

Este relatório foi configurado para imprimir os dados da APAC de acordo com o seu procedimento principal.

No caso de APAC de Quimioterapia, serão listados somente as informações deste tipo de APAC.

No menu Opções => Parâmetros SUS => Aba : APAC => Sub Aba: Dados Gerais, informe o campo "Relatório Demonstrativo de APAC Magnético" apontando para este novo relatório mais completo e salve o registro.

**07. TABELAS UTILIZADAS**

* SZPARAMSUS
* SZAPAC
* SZAPACPROC
* SZSUSPROCEDIMENTO
* SZATENDIMENTO
* SZUNIDATEND
* SZCADGERAL
* SZPACIENTE
* SZAPACNEFRO
* SZCREDENCIAMENTODETALHE
