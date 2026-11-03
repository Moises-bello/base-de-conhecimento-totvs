---
article_id: 25973311333271
category: Financeiro - Contas a Receber
content_hash: 7ebef5757ab734b39eea3954477202b56e43add18e1ca60fcfe596c8897e1f18
fetched_at: '2026-06-28T22:38:13.986740+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA191 - Como habilitar
  a opção de compensar o cheque
type: support-article
updated_at: '2024-08-28T19:30:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25973311333271-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA191-Como-habilitar-a-op%C3%A7%C3%A3o-de-compensar-o-cheque
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25976367986455)** Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**

Como habilitar a opção de compensar o cheque na rotina de cheques recebidos?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

Por meio do parâmetro **MV\_SLDBXCR**, é possível gerar o **movimento bancário de títulos a receber** somente quando o **cheque for compensado**. Para ativar essa funcionalidade, deve-se configurar o parâmetro **MV\_SLDBXCR** com o valor "**C**". Com essa configuração, o botão "**Compensar**" será habilitado na rotina "**Cheques Recebidos**", conforme ilustrado na imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25973311324695)

**Saiba Mais**

[Cheques recebidos](https://tdn.totvs.com/display/PROT/Cheques+Recebidos+-+FINA191)
