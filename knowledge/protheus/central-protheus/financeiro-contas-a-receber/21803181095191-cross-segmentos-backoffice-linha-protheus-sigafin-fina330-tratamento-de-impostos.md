---
article_id: 21803181095191
category: Financeiro - Contas a Receber
content_hash: 844643fc4efae7fa82608baa0f4394f90cee08de30de5ad526487334b8de1ca5
fetched_at: '2026-06-28T22:38:14.072197+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA330 - Tratamento
  de impostos sobre Nota de Crédito do Cliente (NCC)
type: support-article
updated_at: '2024-03-06T18:47:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21803181095191-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA330-Tratamento-de-impostos-sobre-Nota-de-Cr%C3%A9dito-do-Cliente-NCC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21803195785239) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Tratamento de impostos sobre Nota de Crédito do Cliente (NCC)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA330 - Todas as versões  
  
**Solução**

Ao efetuar a **compensação de títulos a receber** (**FINA330**) de **nota de crédito ao cliente (E1\_TIPO=NCC)**, há algumas regras a serem consideras quando o(s) título(s) de contrapartida possuírem calculo de impostos:

Para os impostos calculados na **baixa** **(tipo PIS, COF, CSL, IRF, etc.)**:  
Como a **compensação da NCC** não possui fato gerador dos impostos (não houve pagamento), o valor desses impostos não serão abatidos do valor da movimentação **(E5\_VALOR)**, e o saldo da **NCC** **(E1\_SALDO)** não deve ficar com os valores desses impostos após a compensação;  
Para os impostos calculados na **emissão (tipo IR-, PI-, CO-, etc.)**:  
Nas perguntas da rotina **(tecla F12)**, a pergunta "**Considera Abatimentos/Impostos ?**" deve ser configurada para definir se os impostos calculados na **emissão (abatimentos)** devem influenciar ou não sobre o valor a ser compensado. Se configurado "**Sim**", o saldo da **NCC** deve ficar com o valor dos impostos da emissão após a compensação.

Exemplos

Pergunta "Considera Abatimentos/Impostos ?" igual a "Sim" :

* Incluir um título de R$ 10.000,00 com IR na emissão (*A1\_IRBAX=2*) e PIS/COFINS/CSLL na baixa (*MV\_BR10925=1*). O sistema irá gerar 2 registros na tabela *SE1*:

  + **1º Registro com o TIPO:** NF com valor de R$ 10.000,00 com saldo em aberto.
  + **2º Registro com o TIPO:** IR- com valor de R$ 150,00 com saldo em aberto.
* Incluir uma NCC de R$ 10.000,00;
* Na rotina de Compensação (FINA330), configurar a pergunta **"Considera Abatimentos/Impostos ?" igual a "Sim"**;
* Ainda na rotina de Compensação (FINA330), compensar o título NF com a NCC;
  + O título tipo NF ficará totalmente baixado (E1\_SALDO=0)
  + O título tipo NCC ficará com o saldo parcialmente baixado, ficando o valor referente ao abatimento/imposto (E1\_SALDO=150)

Pergunta "Considera Abatimentos/Impostos ?" igual a "Não" :

* Incluir um título de R$ 10.000,00 com IR na emissão (*A1\_IRBAX=2*) e PIS/COFINS/CSLL na baixa (*MV\_BR10925=1*). O sistema irá gerar 2 registros na tabela *SE1*:

  + **1º Registro com o TIPO:** NF com valor de R$ 10.000,00 com saldo em aberto.
  + **2º Registro com o TIPO:** IR- com valor de R$ 150,00 com saldo em aberto.
* Incluir uma NCC de R$ 10.000,00;
* Na rotina de Compensação (FINA330), configurar a pergunta **"Considera Abatimentos/Impostos ?" igual a "Não"**;
* Ainda na rotina de Compensação (FINA330), compensar o título NF com a NCC;
  + O título tipo NF ficará totalmente baixado (E1\_SALDO=0)
  + O título tipo NCC ficará com o saldo totalmente baixado (E1\_SALDO=0);
