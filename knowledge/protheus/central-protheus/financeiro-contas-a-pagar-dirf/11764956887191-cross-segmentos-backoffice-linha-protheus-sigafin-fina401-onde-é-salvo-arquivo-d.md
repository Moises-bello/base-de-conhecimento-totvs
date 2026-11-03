---
article_id: 11764956887191
category: Financeiro - Contas a Pagar - Dirf
content_hash: ef647129713743af5a2d25f78e8f644ff9901d1fa08fed0d7cacd678f2ff6a88
fetched_at: '2026-06-28T22:38:10.665767+00:00'
product: protheus
section_id: 1500001550482
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA401 - Onde é salvo
  arquivo da DIRF
type: support-article
updated_at: '2023-04-21T19:40:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11764956887191-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA401-Onde-%C3%A9-salvo-arquivo-da-DIRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Onde o protheus salva o log/relatório da DIRF FINA401?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Na rotina FINA401, validar a pergunta parâmetro **MV\_PAR07 (Gerar Log de Processamento?)**  
Ajustar : Gerar log de processamento ? = Sim  
  
![](https://totvssuporte.zendesk.com/attachments/token/IdXmBQ57S77vMOA0FBpILpkfx/?name=inline253849274.png)

Ao selecionar a opção para gerar o *log*, é possível avaliar todos os títulos que compõem cada mês gerado na rotina de **Manutenção de Arquivo (tabela SR4)**.  
  
Após o processamento : **Arquivo .csv gerado em \SYSTEM\DIRF**  
  
**Saiba mais**[FIN0041\_CPAG\_Geração\_de\_Dados\_para\_DIRF\_(FINA401)](https://tdn.totvs.com/pages/releaseview.action?pageId=224126168)
