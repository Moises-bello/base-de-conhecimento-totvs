---
article_id: 21916782695831
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 95e311364896870cf13ff33ad44b2e993199a2e9f16a5f79d8bccba70f5df672
fetched_at: '2026-06-28T22:37:56.474858+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -
  FINA200 - Como alterar a Data de Credito na baixa via retorno CNAB '
type: support-article
updated_at: '2024-03-12T17:36:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21916782695831-Cross-Segmentos-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA200-Como-alterar-a-Data-de-Credito-na-baixa-via-retorno-CNAB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21916753598871) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**

É possível mudar a data de crédito do recebimento via retorno CNAB de Cobranças FINA200?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA200 - Todas as versões  
  
**Solução**

Para o desejado, deve utilizar a variável **DATACREDITO** para os Arquivos de Cobrança **(Modelo 2 - 240 Posições)** através da variável **dDataCred** onde é possível definir a data de disponibilidade do crédito no retorno via **Retorno de Cobranças (FINA200).**

**Exemplo:**   
Variável **DATA** será gravado no campo **E5\_DATA** e a **DATACREDITO** será gravado no **E5\_DTDISPO**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21916782663447)

**Saiba mais**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - FINA420 - Existem variáveis e funções que possam ser utilizadas na configuração de CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004894128-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-FINA420-Existem-vari%C3%A1veis-e-fun%C3%A7%C3%B5es-que-possam-ser-utilizadas-na-configura%C3%A7%C3%A3o-de-CNAB)

**Pontos de entrada tratamento do retorno**[F200VAR - CNAB Receber - Manipular variáveis no processamento do retorno](https://tdn.totvs.com/pages/releaseview.action?pageId=235308494)
