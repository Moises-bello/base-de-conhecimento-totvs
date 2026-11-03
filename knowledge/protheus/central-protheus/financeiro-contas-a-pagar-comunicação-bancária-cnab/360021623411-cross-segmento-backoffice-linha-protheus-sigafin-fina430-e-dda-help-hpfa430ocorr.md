---
article_id: 360021623411
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 6e057c655819ce90229e7fd3317da6b1e4a6a42adf4a33aff561b74f842bed52
fetched_at: '2026-06-28T22:37:55.005491+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA430 e DDA - Help
  HPFA430OCORR
type: support-article
updated_at: '2025-03-28T11:15:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021623411-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA430-e-DDA-Help-HPFA430OCORR
---

**Dúvida**Na recepção de um arquivo, está sendo apresentado o Help: HPFA430OCORR  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9193419330199)  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Validar no **arquivo de retorno**, qual a ocorrência que não está sendo validada, utilizando as posições designadas no arquivo de configuração  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30990742828567)**Verificar na rotina **Ocorrências CNAB (FINA140)**, se possui a ocorrência para o banco utilizado, do tipo  **P - Contas a Pagar.** Caso não tenha, criar uma ocorrência com este tipo  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30990737850263)  
  
Verificar também os **Parâmetros de Banco (FINA130)**, para confirmar se o **tamanho da ocorrência** está correto e após reprocessar o arquivo  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30990737853207)

**Saiba Mais**  
[Conciliação DDA (FINA260 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312165346)  
[Ocorrências Cnab (FINA140 - SIGAFIN)](https://tdn.totvs.com/pages/viewpage.action?pageId=312166855)  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como funciona Debito Direto Autorizado (DDA) no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018249171)
