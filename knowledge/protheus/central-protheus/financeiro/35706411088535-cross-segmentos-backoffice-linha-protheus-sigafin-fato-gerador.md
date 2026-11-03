---
article_id: 35706411088535
category: Financeiro
content_hash: 1eab76b534370cf6017c6f92c331e22fc49a6d81f853e97b7f6b463e04a2f06b
fetched_at: '2026-06-28T22:38:02.969323+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Fato gerador
type: support-article
updated_at: '2025-10-17T18:37:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35706411088535-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Fato-gerador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35706398785687) Tempo aproximado para leitura: **00:07:00 min**  
  
**Dúvida**  
Incluí meu título no Financeiro, mas o imposto não foi deduzido automaticamente do valor total, gerando um título com o valor bruto (sem desconto do imposto).  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro  - Todas as versões

**Solução**  
A dedução automática dos impostos depende do **fato gerador** configurado no ambiente. Essa definição é controlada pelos seguintes parâmetros:

* **MV\_BX10925** → Define o momento da dedução para **Contas a Pagar**

  + Conteúdo **1** = deduz na **baixa**
  + Conteúdo **2** = deduz na **emissão**
* **MV\_BR10925** → Define o momento da dedução para **Contas a Receber**

  + Conteúdo **1** = deduz na **baixa**
  + Conteúdo **2** = deduz na **emissão**

**Quando o fato gerador estiver configurado para** ****baixa****  
O sistema fará a dedução do imposto **somente no momento em que a baixa for concluída.**

**Quando o fato gerador estiver configurado para** ****emissão****  
A dedução ocorrerá **no momento da inclusão do título.**

**📢️ Importante:**  
O parâmetro **MV\_BX10925****e MV\_BR10925**não deve ser alterado, uma vez que, no momento da implantação do ***Protheus***, foi definido como a empresa irá tratar o imposto.
