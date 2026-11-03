---
article_id: 360060137794
category: Financeiro - Contas a Receber
content_hash: b44e3e34442730a0e699d97df6a038a0885d89e8ad12e4cc046d795093d8c33c
fetched_at: '2026-06-28T22:38:14.208371+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Linha BackOffice Protheus - SIGAFIN - FINA151 - Instrução
  de cobrança automática de baixa após liquidação
type: support-article
updated_at: '2023-02-20T16:54:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060137794-Cross-Segmentos-Linha-BackOffice-Protheus-SIGAFIN-FINA151-Instru%C3%A7%C3%A3o-de-cobran%C3%A7a-autom%C3%A1tica-de-baixa-ap%C3%B3s-liquida%C3%A7%C3%A3o
---

**Dúvida**Como gerar instrução de cobrança de baixa de títulos bancários de forma automática, ao efetuar a liquidação de títulos que já foram enviados ao banco?  
  
**Ambiente**Microsiga Protheus – Financeiro - A partir da versão 12.1.23  
  
**Solução**Para efetuar o processo, realize os seguintes passos:  
1. No configurador do Protheus (SIGACFG), inclua o parâmetro MV\_INSCOB = 1 ou igual a 0 (zero), de acordo com a necessidade.   
  
**Detalhes do parâmetro**

1.**MV\_INSCOB =2**

* **2 - Negociação**- Apenas para os processos de Fatura ou Liquidação será gerada instrução para baixa de cobrança

2. Na rotina de Liquidação ( Atualizações -> Contas a Receber -> Liquidação - FINA460), efetue o processo normalmente. Caso o título já tenha sido enviado ao banco, será apresentada a mensagem "*Caso existam títulos em cobrança bancária, deseja gerar instrução de baixa de cobrança para a instituição financeira?*". Selecione "*Sim*" para a instrução de cobrança ser gerada.  
  
**Exemplo da mensagem**  
![kcs_fina4602.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001505442/kcs_fina4602.png)

3. A instrução de cobrança de baixa será gerada de forma automática, e poderá ser enviada pela rotina de Instrução de Cobranças (Atualizações -> Comunicação Bancária -> Instrução de Cobranças).  
  
**Exemplo da instrução criada**  
![kcs_fina4603.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001505602/kcs_fina4603.png)  
 **Saiba mais  
<https://tdn.totvs.com/pages/releaseview.action?pageId=224397763>**
