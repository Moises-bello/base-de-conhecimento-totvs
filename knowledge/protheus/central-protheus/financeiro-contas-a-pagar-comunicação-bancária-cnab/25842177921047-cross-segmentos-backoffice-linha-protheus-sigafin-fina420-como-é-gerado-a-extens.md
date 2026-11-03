---
article_id: 25842177921047
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 82e8aba4e4036e53d7496ab549d6e7581747d609332e4134266edc1953de86e0
fetched_at: '2026-06-28T22:37:56.228926+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA420  - Como é gerado
  a extensão de arquivo CNAB
type: support-article
updated_at: '2024-08-22T20:50:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25842177921047-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA420-Como-%C3%A9-gerado-a-extens%C3%A3o-de-arquivo-CNAB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25842177879703) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Como é gerado a extensão de arquivo CNAB?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**A extensão do arquivo de remessa gerado, é configurado através dos **Parâmetros de bancos** (**FINA130**).   
No campo **EE\_EXTEN - Extensão do arquivo,** isto é alguns bancos definem o nome da extensão do arquivo. Ex.: **.TXT, .SFR.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25842177885079)

Na rotina **FINA420 - Arquivo de Pagamentos**, ao gerar o arquivo de remessa, informamos somente o **nome do arquivo**, exemplo abaixo:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25842177887383)

Com isso o arquivo é gerado, já com a extensão pré-definida nos **Parâmetros de Bancos**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25842206392343)

**Saiba mais:**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Principais configurações e dúvidas para uso do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7778595184407)  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Extensão cnab](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016606051)
