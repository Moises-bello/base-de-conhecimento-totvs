---
article_id: 360027342473
category: Escrita Fiscal - Impostos - ICMS
content_hash: 8752b717d6a5bf4e6a9a87181ab6fab676fdbf98a069957b8271c90b58c43f68
fetched_at: '2026-06-28T22:39:24.019285+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Redução de Base
  de Cálculo de ICMS'
type: support-article
updated_at: '2024-01-05T17:42:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027342473--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Redu%C3%A7%C3%A3o-de-Base-de-C%C3%A1lculo-de-ICMS
---

**Dúvida**

Redução de Base de Cálculo de ICMS

**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Cadastro TES:

Calc. ICMS (F4\_ICM) = S

%Red.do ICMS (F4\_BASEICM) "TES" ou %Red.do ICMS (F7\_BASEICM) "Exceção fiscal" = Informe o valor a ser calculado do ICMS próprio. No padrão, este valor é apresentado na coluna Tributada do Livro Fiscal.

Livro Fiscal ICMS (F4\_LFICM) = ISENTO/ OUTROS. Selecione uma das opções para informar onde será destacado o restante da operação Valor total da NF menos percentual informado no campo F4\_BASEICM.

Material de Consumo (F4\_CONSUMO)=NÃO

Exemplo:

%Red.do ICMS (F4\_BASEICM) = 60;

Livro Fiscal ICMS (F4\_LFICM) = ISENTO

Material de Consumo (F4\_CONSUMO) = NÃO

O valor do ICMS será dividido entre as colunas Tributado(60%) e Isento(40%)

%Red.do ICMS (F4\_BASEICM) = 60;

Livro Fiscal ICMS (F4\_LFICM) = OUTROS

Material de Consumo (F4\_CONSUMO) = NÃO

O valor do ICMS será dividido entre as colunas Tributado(60%) e Outros(40%)

**ATENÇÃO:**

**Há algumas exceções em que mesmo com redução de Base de Cálculo nenhum valor deve ser tributado para esta situação. Para isso existe o campo Material de Consumo (F4\_CONSUMO).**

Exemplos:

1º ) %Red.do ICMS (F4\_BASEICM) = 60;

Livro Fiscal ICMS (F4\_LFICM) = Isento

Material de Consumo (F4\_CONSUMO) = Sim

O valor do ICMS será dividido entre as colunas ISENTO (60%) e OUTROS (40%)

2º) %Red.do ICMS (F4\_BASEICM) = 60

Livro Fiscal ICMS (F4\_LFICM) = ISENTO

Material de Consumo (F4\_CONSUMO) = OUTROS

100% do valor será apresentado na coluna ISENTO (100%)

3º) %Red.do ICMS (F4\_BASEICM) = 60;

Livro Fiscal ICMS (F4\_LFICM) = OUTROS

Material de Consumo (F4\_CONSUMO) = SIM

O valor do ICMS será dividido entre as colunas OUTROS (60%) e ISENTO(40%).

4º) %Red.do ICMS (F4\_BASEICM) = 60;

Livro Fiscal ICMS (F4\_LFICM) = OUTROS;

Material de Consumo (F4\_CONSUMO) = OUTROS.

100% do valor será apresentado na coluna OUTROS (100%)

**Importante**

Abaixo parâmetro que poderá influenciar na gravação do valor do ICMS no campo 10 VL\_RED\_BC do registro C190 do SPED FISCAL:

1 - Preencha o parâmetro MV\_NRPRBIC conforme abaixo:

![MV.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/20351098147735)

Este parâmetro indica se na geração do registro **C190**, **campo 10 – VL\_RED\_BC** o valor da parcela referente à redução da base de cálculo do ICMS é recalculado na geração do arquivo. Se informado .**F.** *(False/*Falso) o valor é recalculado considerando percentual de redução da tabela **Processamento do SPED Fiscal (CD2)** ou do **Cadastro de TES** (SF4), forma que é feita antes da criação deste parâmetro, se informado .T.*(True/*Verdadeiro), então não se faz o recálculo e considera para geração do **campo 10**do registro **C190** o valor do campo **Vlr Isen ICM (FT\_ISENICM)** ou **Vlr Out ICMS (FT\_OUTRICM)**.

Mais informações acessar o link abaixo referente o campo VL\_RED\_BC do registro C190:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019976472-MP-FIS-SPED-FISCAL-Registro-C190-Campo-10-VL-RED-BC->
