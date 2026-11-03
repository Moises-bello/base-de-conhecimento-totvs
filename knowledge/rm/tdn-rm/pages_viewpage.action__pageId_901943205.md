---
content_hash: 4467d928da8ebd91028447c2701d23dd0bc3a94a848a0b2dbffe38a494c5c65d
fetched_at: '2026-06-29T00:12:02.412530+00:00'
page_id: '901943205'
product: rm
source: tdn-rm
title: DT - Reoneração - Tratativa no Lançamento Financeiro e Relatório de INSS Patronal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901943205
version: 22
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Reoneração - Tratativa no Lançamento Financeiro e Relatório de INSS Patronal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | [DRHROTRM-11463](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11463) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.263
* 12.1.2406.214
* 12.1.2410.141 e superiores

## **03. SITUAÇÃO/REQUISITO**

Ajuste do Produto TOTVS Folha de Pagamento para atender à **Lei nº 14.973/2024**, que estabelece a reoneração progressiva da folha de pagamento a partir da competência de **janeiro/2025**.

*"Lei n° 14.973/2024 -* *§ 2º A partir de 1º de janeiro de 2025 até 31 de dezembro de 2027, o valor da contribuição calculada nos termos do inciso II do § 1º do art. 9º será acrescido do montante resultante da aplicação das proporções a que se referem a alínea “b” do inciso I, a alínea “b” do inciso II e a alínea “b” do inciso III do caput deste artigo.”*

## **04. SOLUÇÃO**

Realizamos ajustes nas rotinas listadas abaixo para atender à **reoneração progressiva da folha de pagamento**, conforme previsto na **Lei nº 14.973/2024**, com vigência a partir da competência de **janeiro/2025**:

* Relatório de INSS Patronal
* Lançamento Financeiro do tipo "25-Total Guia INSS DCTFWeb"

falsebodytruebody1Alíquota de Reoneração da FolhaAlíquota de Reoneração da Folha

Foi criado o valor fixo com a finalidade **"Alíquota de Reoneração da Folha"**, destinado ao cadastro do percentual que será utilizado para a reoneração do ano.

Acesse o menu Administração de Pessoal | Cálculos | Valores Fixos.

body1Empresa 100% DesoneradaEmpresa 100% Desonerada

1) Realizar a parametrização do tipo de Desoneração, para isso acesse o menu **eSocial | Período de Apuração.**

Selecione no campo "Indicativo de Substituição" a opção "Contrib. Patronal integralmente Substituída";

2) Realize o cadastro da "Alíquota da reoneração gradual da folha" para isso acesse o menu **Administração de Pessoal | Cálculos | Valores Fixos**

3) Ao atualizar o status do evento **S-1299**, o sistema guardará o retorno do evento de fechamento correspondente ao evento de retorno **S-5011**, conforme demonstrado abaixo:

4) Realizar a geração do Relatório de INSS Patronal, disponível no menu**eSocial | Conferência de Conferência de INSS Patronal.**

**Cálculo do exemplo acima:**

**Base Total de INSS: R$3.166,67 (vrBcCp20)+ R$1.000,00 (vrBcCp00) - R$500,00 (Base INSS 13) = R$3.666,67**

R$3.666,67 X 5% (ano 2025 representado pelo segundo trimestre de 2024 na produção restrita) = R$183,33 (reonerada percentual de 5%)

O valor será demonstrado no Código de Receita da "Contribuição Patronal", conforme print acima.

5) Gerar o Lançamento Financeiro do tipo "25-Total Guia INSS DCTFWeb" para isso acesso o menu **Encargos | Financeiro | Lançamentos**.

body2Empresa com Desoneração ParcialDesoneração Parcial

1) Realizar a parametrização do tipo de Desoneração, para isso acesse o menu **eSocial | Período de Apuração.**

Selecione no campo "Indicativo de Substituição" a opção "Contribuição Patronal parcialmente substituída" e preencha o "Percentual de Redução (lei 12.546/2011".

Neste exemplo o percentual preenchido foi de 50%.

2) Realize o cadastro da "Alíquota da reoneração gradual da folha" para isso acesse o menu **Administração de Pessoal | Cálculos | Valores Fixos**

3) Ao atualizar o status do evento **S-1299**, o sistema guardará o retorno do evento de fechamento correspondente ao evento de retorno **S-5011**, conforme demonstrado abaixo:

4) Realizar a geração do Relatório de INSS Patronal, disponível no menu**eSocial | Conferência de Conferência de INSS Patronal.**

**Cálculo do exemplo acima:**

**Base Total de INSS: R$2.833,33 (vrBcCp20)+ R$1.000,00 (vrBcCp00) - R$500,00 (Base INSS 13) = R$3.333,33**

R$3.333,33  X 50% (percentual informado no evento S-1280) = R$1.666,66 X 20% = R$333,33 (parte onerada)  
R$3.333,33  - R$1.666,66 = R$1.666,66 X 10% (ano 2026 representado pelo terceiro trimestre de 2024 na produção restrita) = R$166,66 (reonerada percentual de 10%)

Valor encontrado de contribuição patronal no evento S-5011: **R$499,99**

O valor será demonstrado no Código de Receita da "Contribuição Patronal", conforme print acima.

5) Gerar o Lançamento Financeiro do tipo "25-Total Guia INSS DCTFWeb" para isso acesso o menu **Encargos | Financeiro | Lançamentos**.

## **05. DEMAIS INFORMAÇÕES**

<https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-orientativa-s-1-3-01-2024.pdf>
