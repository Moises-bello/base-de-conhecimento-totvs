---
article_id: 1500004324382
category: RH - Benefícios
content_hash: 070951d4688500b6f35561210a4d520317606d5501bc42ee739caa19d2b4400f
fetched_at: '2026-06-28T22:44:04.680737+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Lançamento e cálculo de coparticipação/reembolso
type: support-article
updated_at: '2025-09-26T13:30:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004324382-RH-Linha-Protheus-GPE-Lan%C3%A7amento-e-c%C3%A1lculo-de-coparticipa%C3%A7%C3%A3o-reembolso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33050511152279) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como realizar o lançamento e cálculo de coparticipação/reembolso de assistência medica/odontológica?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**

**1.** Crie as verbas de coparticipação e reembolso.   
A verba de coparticipação deve ser de **desconto** e a verba de reembolso deve ser de **provento.** Ambas as verbas **não possuem identificador de cálculo.**   
  
**2.** Após a criação da verba, realize os lançamentos em  **Atualizações> Benefícios> Plano de Saúde/ Coparticipações/reembolso.**

Selecione o funcionário e clique em **Lançamentos:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33050525240471)

Informe os dados referente a coparticipação ou reembolso;  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005362501)

Principais Campos:

**- Data Ocorrenc:** Data do lançamento ou da consulta. Campo apenas informativo;

**- Origem:** Informe se a coparticipação refere a 1-Titular; 2-Dependente ou 3-Agregado;

**- Tipo:** Informe se o lançamento se refere a 1-Assistência Médica ou 2-Assistência Odontológica;

**- Cód. Fornec.:** Informe a operadora/fornecedor do plano de saúde. Deve ser o mesmo informado no cadastro de planos ativos do titular, dependente ou agregado;

**- Sequência:** Informe a sequência do dependente ou do agregado. Campo será ativado apenas quando a origem se referir a um dependente ou agregado;

**- Nome:** Nome do Dependente ou Agregado. Este campo é preenchido automaticamente após informar a sequência. Campo apenas visual;

**- Tipo do Lançam.:** Informe se o lançamento se refere a 1-Coparticipação ou 2-Reembolso;

**- Verba Calcul.:** Informe a verba de desconto/provento que será enviada para folha de pagamento;

**- Vlr Funcion.:** Valor que será descontando ou pago ao funcionário;

**- Vlr Empresa:** Valor correspondente à empresa;

**- Compet. Pagto:** Informe o ano e o mês de competência para desconto/pagamento em folha de pagamento.

**3.** Realize o cálculo do Roteiro PLA em **Atualizações> Benefícios> Planos de saúde> Cálculo Plano de Saúde.** Nesta etapa será calculado todos os planos vinculados ao funcionário (Rotina de Planos Ativos) e coparticipações/reembolsos lançados para o período.   
  
**4.** Para conferência do cálculo, gere o relatório [GPER008](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411051523735-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-c%C3%A1lculo-assist%C3%AAncia-medica-GPER008) ou consulte o cálculo individualmente na rotina de [Consulta de Cálculo.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21293087204759-RH-Linha-Protheus-GPE-Como-consultar-o-c%C3%A1lculo-de-assist%C3%AAncia-m%C3%A9dica-individualmente)  
  
**5.** Após a conferência dos valores de coparticipação/reembolso e planos, integre o Roteiro PLA a folha de pagamento em **Atualizações> Benefícios> Plano de Saúde> Integração com a folha**

**Importante:**

* Ao gravar o lançamento, o sistema verifica se o fornecedor lançado está de acordo com o informado no plano ativo, não permitindo gravar, caso este seja diferente.
* Na integração com a folha de pagamento, o valor lançado no campo **Vlr Empresa** será somado à Verba Parte Empresa da assistência médica/odontológica. Caso a empresa não realize nenhum tipo de pagamento, seja de reembolso ou de coparticipação, este campo deve ser gravado sempre com o valor zero.

**Saiba Mais:**[RH - Linha Protheus - GPE - Documentações relacionadas a rotina de coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11301756760855-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%B5es-relacionadas-a-rotina-de-coparticipa%C3%A7%C3%A3o?source=search)  
[RH - Linha Protheus - GPE - Definir um valor limite mensal para desconto de coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15479857442327-RH-Linha-Protheus-GPE-Definir-um-valor-limite-mensal-para-desconto-de-coparticipa%C3%A7%C3%A3o)  
[RH - Linha Protheus - GPE - Importação de variáveis tabela RHO - Coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXOGZWOQU6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBp2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzU3NDM4MjA4MTQ0ODctUkgtTGluaGEtUHJvdGhldXMtR1BFLUltcG9ydGElQzMlQTclQzMlQTNvLWRlLXZhcmklQzMlQTF2ZWlzLXRhYmVsYS1SSE8tQ29wYXJ0aWNpcGElQzMlQTclQzMlQTNvBjsIVDoOc2VhcmNoX2lkSSIpMDQ1ODY5Y2UtNmMzNC00Y2NjLTlkYWItZjllMzAxOGVjMjBkBjsIRjoJcmFua2kMOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIecHJvdGhldXMgY29wYXJ0aWNpcGHDp8OjbwY7CFQ6EnJlc3VsdHNfY291bnRpAuoD--f8f55575516c7ffae21305b598ad450d6a024a19)
