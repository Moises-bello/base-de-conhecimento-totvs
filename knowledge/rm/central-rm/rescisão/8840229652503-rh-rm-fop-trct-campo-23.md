---
article_id: 8840229652503
category: Rescisão
content_hash: 21b7f868dcfc9d858d551d4d2c5941cc83512323909fca6cc13fff0abadab0f1
fetched_at: '2026-06-28T22:46:54.321666+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - TRCT: Campo 23'
type: support-article
updated_at: '2024-09-16T19:53:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8840229652503-RH-RM-FOP-TRCT-Campo-23
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:10 min  
  
Dúvida**  
Campo 23 do TRCT em branco?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Acessar **Rescisão | TRCT Portaria 1621/2010  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8839852432919/mceclip0.png)**

Neste campo associe a fórmula criada para o calculo da remuneração do mês anterior. Ficando a critério do cliente definir junto ao sindicato qual o valor a ser demonstrado.  
  
Exemplo de formula para o calculo do campo 23:  
  
MV(MESDT(DTD)-1,ANO,'INFORME O EVENTO DE REMUNERAÇÃO') +   
  
MV(MESDT(DTD)-1,ANO,'INFORME O EVENTO DE REMUNERAÇÃO') +   
  
MV(MESDT(DTD)-1,ANO,'INFORME O EVENTO DE REMUNERAÇÃO') +   
  
MV(MESDT(DTD)-1,ANO,'INFORME O EVENTO DE REMUNERAÇÃO')   
  
**Observação**  
Nesta fórmula o sistema irá buscar o valor da competência anterior nos eventos informados em 'INFORME O EVENTO DE REMUNERAÇÃO'  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8840003008919/mceclip1.png)  
  
**Importante**  
O suporte padrão não presta auxílio na criação ou manutenção de fórmulas. Para estes casos, verifique a possibilidade de contratar nossa equipe de consultoria tarifada.  
  
**Saiba mais**  
Para mais informações sobre as parametrizações do TRCT, [clique aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=42042615).
