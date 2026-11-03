---
article_id: 9193964593687
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: f5492f5568225ea64585e12b1834be4c88d41f4633e05393b053999f11649c30
fetched_at: '2026-06-28T22:37:55.347497+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - FINA430 - Utilização
  da variável DATACREDITO para pagamentos via retorno CNAB
type: support-article
updated_at: '2023-10-16T20:20:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9193964593687-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-FINA430-Utiliza%C3%A7%C3%A3o-da-vari%C3%A1vel-DATACREDITO-para-pagamentos-via-retorno-CNAB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18313618468759) Tempo aproximado para leitura: **00:05:00 min****Dúvida**É possível utilizar a variável DATACREDITO no layout de retornos de pagamento via CNAB?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro  - FINA430 - Todas as versões  
  
**Solução**A variável **DATACREDITO** é utilizada para os **Arquivos de Cobrança** através da variável **dDataCred** onde é possível definir a data de disponibilidade do crédito no retorno via **Retorno de Cobranças (FINA200)**

Para pagamentos, deve utilizar a variável **DATA (Data do Pagamento do banco)**

A data da digitação(E5\_DTDIGIT) é gravada conforme data base do sistema no qual foi processado a baixa.

**Saiba mais**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - FINA420 - Existem variáveis e funções que possam ser utilizadas na configuração de CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004894128)

**Estruturação CNAB**  
[Estrutura dos arquivos de configuração CNAB](https://tdn.totvs.com/pages/releaseview.action?pageId=327329139)

**Pontos de entrada tratamento do retorno**  
[F200VAR - CNAB Receber - Manipular variáveis no processamento do retorno](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=235308494)  
[F430VAR - Permite manipulação das Variáveis Private durante a baixa CNAB (Pagar)](https://tdn.totvs.com/pages/viewpage.action?pageId=641447402)
