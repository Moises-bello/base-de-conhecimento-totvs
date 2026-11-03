---
article_id: 360007376931
category: Gestão de Transportes (TMS)
content_hash: 62bc04fd0344a6093e92ea7600dec2927f7b45426cd2122b1f57bb0c3444d356
fetched_at: '2026-06-28T22:45:29.544791+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada F050FCTC Despreza Contratos
  de Carreteiro
type: support-article
updated_at: '2022-06-20T14:35:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007376931-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-F050FCTC-Despreza-Contratos-de-Carreteiro
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)* Tempo aproximado para leitura:** 00:00:40 min **Dúvida**Como implementar o ponto de entrada **F050FCTC** - Despreza Contratos de Carreteiro?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada  **F050FCTC** está disponibilizado na função **FA050NAT2** - Cálculo de Impostos, para desprezar contratos a serem acumulados para compor base de cálculo de **IRRF** **- Imposto sobre a Renda Retido na Fonte**, de carreteiro.  
  
**Programa Fonte**: FINA050.PRX  
  
**Sintaxe**: F050FCTC - Despreza Contratos de Carreteiro ( [ cFilOri ], [ cViagem ] ) --> lRet  
  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
| cFilOri | Caracter | Filial de origem do contrato de carreteiro. |  |  |  |
| cViagem | Array of Record | Número da Viagem do contrato de carreteiro. |  |  |  |

**Retorno:**

lRet  
           (logico)  
           Falso - Despreza contrato  
           Verdadeiro - Considera contrato

**Variáveis**:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Tipo | Escopo | Pode Alterar | Descrição |
|  | Array of Record | Global | Não |  |
