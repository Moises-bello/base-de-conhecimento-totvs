---
article_id: 41272424196887
category: Faturamento - Integrações
content_hash: c2d6ab1dbd62c11edd7b732daccafaf1e96ec6f453b59936ace23f8c30ff6ce1
fetched_at: '2026-06-28T22:38:26.639694+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Aviso "Parâmetro MV_SPEDCOL
  não está configurado para utilizar TOTVS Colaboração"
type: support-article
updated_at: '2026-06-18T12:56:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41272424196887-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Aviso-Par%C3%A2metro-MV-SPEDCOL-n%C3%A3o-est%C3%A1-configurado-para-utilizar-TOTVS-Colabora%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41272424178839) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
No log da integração EDI, saiu esse aviso "Aviso "Parâmetro MV\_SPEDCOL não está configurado para utilizar TOTVS Colaboração", como resolver?

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**  
O erro ocorre por conta de o ambiente o parâmetro MV\_TCNEW estar com o valor "6" e o parâmetro MV\_SPEDCOL não está "S"

Nessa configuração, o sistema não faz nada, não puxando o arquivo para gerar o pedido de venda, que é o objetivo;

Avaliem trocar o conteúdo desses parâmetros, necessários para o funcionamento do MA411JOB!

Documentação de implantação com modelo de valor nos parâmetros: [DI\_Integração\_TOTVS\_Colaboração\_2\_0\_EDI\_de\_Vendas](https://tdn.totvs.com/x/vwJdDg)

**OBS 1:** É obrigatório ter TOTVS\_COLAB\_ONDEMAND

**OBS 2:** Esse aviso tende a ocorrer na implantação

**Saiba mais:**  
[DI\_Integração\_TOTVS\_Colaboração\_2\_0\_EDI\_de\_Vendas](https://tdn.totvs.com/x/vwJdDg)
