---
content_hash: 4eb470692e36a532739f2e1ec41302783855f4afadc9729325d72b4171876226
fetched_at: '2026-06-29T00:05:47.155039+00:00'
page_id: '1008214254'
product: rm
source: tdn-rm
title: DT - S-1210 - Tratativa para funcionário expatriado de férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1008214254
version: 5
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | S-1210 - Tratativa para funcionário expatriado de férias |
| País: | Brasil |
| Issue: | [DRHROTRM-14968](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14968 "View this issue") |

## **02. LIBERAÇÃO**

  Lembrando que, será a partir dos patches:

* 12.1.2502.225
* 12.1.2506.175
* 12.1.2510.106 e superiores

## **03. SITUAÇÃO/REQUISITO**

As informações relacionadas ao residente ou domiciliado no exterior são registradas apenas na tela principal do cadastro do funcionário.

Com isso, ao gerar o evento S-1210, os dados de identificação fiscal (NIF) são informados apenas por competência, o que impede a definição desses dados por período. Essa limitação dificulta o atendimento a situações em que as informações do NIF variam entre diferentes períodos.

## **04. SOLUÇÃO**

No menu Administração de Pessoal | Funcionários | Anexos | Folha de Pagamento | Dados do Residente ou Domiciliado no Exterior, foi criada a nova aba **Dados do Residente ou Domiciliado no Exterior no Período.**

Essa aba deve ser utilizada para informar períodos em que o funcionário teve tributação diferenciada, permitindo o registro dos dados de identificação fiscal (NIF) por período.

**Importante**: Para habilitar a aba **Dados do Residente ou Domiciliado no Exterior no Período** é necessário a execução dos scripts pendentes no RM.Atualizador.exe

**Exemplo:**

* + Competência atual: **05/2025**
  + O funcionário teve cálculo de férias referente a 20 dias nessa competência, com retenção de IRRF.

Porém, ao lançar as férias no período 1, o salário registrado não atingiu a base para retenção de IRRF. Como esse período apresenta tributação diferenciada, foi realizado o cadastro desse período na aba **Dados do Residente ou Domiciliado no Exterior no Período**.

No menu Administração de Pessoal | Funcionários | Anexos | Folha de Pagamento | Dados do Residente ou Domiciliado no Exterior

Na aba **Identificação**, foi preenchido o campo **Forma de Tributação** com a informação **"Retenção do IRRF - alíquota padrão"**, conforme demonstrado abaixo:

Na aba **Dados do Residente ou Domiciliado no Exterior no período**, foi preenchido o campo **Forma de Tributação** com a informação **"Não retenção do IRRF - isenção estabelecida em convêncio."**, conforme demonstrado abaixo:

Ao gerar o XML do evento S-1210, no **<ideDmDev>1**, as informações foram geradas conforme dados preenchidos na nova aba **Dados do Residente ou Domiciliado no Exterior no período**

No **<ideDmDev>08052025**, as informações foram geradas conforme dados preenchidos na aba **Identificação**.

**Importante:**  
Na geração do evento S-1210, o sistema buscará primeiro as informações cadastradas na aba **Dados do Residente ou Domiciliado no Exterior no Período**. Caso não haja dados nessa aba para o período em questão, o sistema utilizará as informações registradas na aba **Identificação**.

## **05. DEMAIS INFORMAÇÕES**

* [Dados do Residente ou Domiciliado no Exterior](https://tdn.totvs.com/display/LRM/Dados+do+Residente+ou+Domiciliado+no+Exterior)
