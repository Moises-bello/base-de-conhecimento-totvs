---
content_hash: 103c056f1774da7d6a32edf6468d58fd264c31edfd21d63973122baed0592f72
fetched_at: '2026-06-29T00:05:54.691453+00:00'
page_id: '1080892680'
product: rm
source: tdn-rm
title: DT - Relatório de Conferência INSS - Indicativo de Suspensão da Exigibilidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1080892680
version: 10
---

## **1. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Gestão de Folha de Pagamento - RM |
| Função: | Relatório de Conferência INSS - Indicativo de Suspensão da Exigibilidade |
| País: | Brasil |
| Ticket: |  |
| Issue: | [DRHROTRM-19122](https://jiraproducao.totvs.com.br/browse/DRHROTRM-19122) |

## **02. VERSÕES**

A partir dos patches:

* 12.1.2510.XXX
* 12.1.2602.XXX
* 12.1.2606.XXX e superiores

## **03. SITUAÇÃO/REQUISITO**

Adequar o **Relatório de Conferência INSS** para atender à regra prevista no leiaute do eSocial referente ao evento S-5001, grupo infoBaseCS.

Conforme o leiaute, quando uma rubrica possui **incidência previdenciária suspensa** (códigos **91, 92, 93 ou 94**) e o processo de suspensão informado no **S-1070** possui **Indicativo de Suspensão da Exigibilidade (indSusp) diferente de 90** (decisão definitiva), o valor da rubrica deve continuar compondo as bases de cálculo da contribuição previdenciária.

Dessa forma, o Relatório de Conferência INSS deverá considerar esses eventos na Base de INSS sempre que o Indicativo de Suspensão da Exigibilidade for diferente de 90, garantindo que a conferência esteja em conformidade com as regras do eSocial e da DCTFWeb.

           

## **04. SOLUÇÃO**

Para atender à regra do leiaute do eSocial disponibilizamos o campo **Indicativo de Suspensão da Exigibilidade** em Eventos | Eventos | Anexos | Processo de Suspensão de Incidência.

false

**ATENÇÃO:**

Após a atualização da versão, é **obrigatória** a execução do **RMAtualizador.exe** para criação do novo campo **Indicativo de Suspensão da Exigibilidade**.

**1.** Para realizar a parametrização, acesse o menu Administração de Pessoal | Eventos | Eventos | Anexos | Processo de Suspensão de Incidência e informe no campo **Indicativo de Suspensão da Exigibilidade** um valor diferente de **90**.  Tipos de Indicativo de Suspensão da Exigibilidade

01 - Liminar em mandado de segurança  
02 - Depósito judicial do montante integral  
03 - Depósito administrativo do montante integral  
04 - Antecipação de tutela  
05 - Liminar em medida cautelar  
08 - Sentença em mandado de segurança favorável ao contribuinte  
09 - Sentença em ação ordinária favorável ao contribuinte confirmada pelo TRF  
10 - Acórdão do TRF favorável ao contribuinte  
11 - Acórdão do STJ favorável ao contribuinte  
12 - Acórdão do STF favorável ao contribuinte  
13 - Sentença de 1ª instância com efeito suspensivo  
14 - Contestação administrativa FAP  
90 - Decisão definitiva a favor do contribuinte  
**92 - Sem suspensão da exigibilidade**

**Importante:** Conforme as regras do eSocial, o Indicativo de Suspensão da Exigibilidade igual a **92 – Sem suspensão da exigibilidade** somente poderá ser informado quando a verba/evento estiver parametrizada com um dos seguintes códigos de **Suspensão de incidência sobre salário de contribuição em decorrência de decisão judicial (codIncCP)**:

* + - **91** – Mensal
    - **92** – 13º salário
    - **93** – Salário-maternidade
    - **94** – Salário-maternidade 13º salário

2 - Ao gerar o **Relatório de Conferência INSS** o sistema passará a considerar o valor dessa verba na da base da folha de pagamento conforme o tratamento aplicado na DCTFWeb, permitindo uma conferência consistente entre as informações.

**Importante:** O Relatório de Conferência de INSS deverá observar as seguintes regras do eSocial:

* Quando o **codIncCP** for **91, 92, 93 ou 94** e o **Indicativo de Suspensão da Exigibilidade (indSusp)** do respectivo processo no **S-1070** for **diferente de 90 (Decisão definitiva a favor do contribuinte)**, o valor deverá ser considerado na composição das bases correspondentes aos **tpValor 11, 12, 13, 14, 41, 42, 43 e 44**.

* Especificamente para rubricas com **codIncCP = 92 (13º salário)**, quando o **indSusp** for **diferente de 90**, os valores dos **tpValor 71, 72, 73 e 74** também deverão ser considerados na composição das bases dos **tpValor 51, 52, 53 e 54**, conforme definido no leiaute do evento **S-5001**.

**S-1010 - tag <codIncCP> e suas descrições:**

* + - * **91** - Mensal
      * **92** - 13º salário
      * **93** - Salário-maternidade
      * **94** - Salário-maternidade 13º salário

**S-5001 - tag <tpValor> e suas descrições:**

* + - * **11** - Base de cálculo da contribuição previdenciária normal
      * **12** - Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 15 anos de contribuição
      * **13** - Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 20 anos de contribuição
      * **14** - Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 25 anos de contribuição
      * **41** - Base de cálculo da contribuição previdenciária normal - Categorias 107 e 108
      * **42** - Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 15 anos de contribuição - Categorias 107 e 108
      * **43** - Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 20 anos de contribuição - Categorias 107 e 108
      * **44** - Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 25 anos de contribuição - Categorias 107 e 108
      * **51** - Base de cálculo da contribuição previdenciária normal - 13º salário - Lei 14.973/2024
      * **52** - Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 15 anos de contribuição - 13º salário - Lei 14.973/2024
      * **53** - Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 20 anos de contribuição - 13º salário - Lei 14.973/2024
      * **54** - Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 25 anos de contribuição - 13º salário - Lei 14.973/2024
      * **71** - Incidência suspensa em decorrência de decisão judicial - Base de cálculo - BC da Contribuição Previdenciária - CP normal - 13º salário - Lei 14.973/2024
      * **72** - Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 15 anos de trabalho - 13º salário - Lei 14.973/2024
      * **73** - Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 20 anos de trabalho - 13º salário - Lei 14.973/2024
      * **74** - Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 25 anos de trabalho - 13º salário - Lei 14.973/2024

## **04.****ASSUNTOS RELACIONADOS**

* [Processo de Suspensão de Incidência](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718749)
* [Relatório de Conferência de INSS](https://tdn.totvs.com.br/pages/releaseview.action?pageId=536721262)
