---
article_id: 14503163187991
category: Encargos
content_hash: 7198cd2c05189f5ae69336612983df6aaf3f7223c5ecb82467db3dca4c85dd3a
fetched_at: '2026-06-28T22:46:52.336379+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Geração do encargo TIPO 4 - Provisão de férias
type: support-article
updated_at: '2024-10-11T19:34:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14503163187991-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-encargo-TIPO-4-Provis%C3%A3o-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como gerar encargo TIPO 4 - Provisão de férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para a geração desse encargo é necessário anteriormente gerar o histórico de provisão para a chapa do funcionário em encargos | Geração do Histórico de provisão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14498089585175)

Verifique o cadastro em Encargo | cadastro | encargos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14498129641623)

Verifique o código ativo vinculado ao encargo, pois na hora de gerar o encargo será necessário selecionar o mesmo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14498299976471)

Após acesse: Encargos | Geração dos encargos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14498306288151)

Log da geração:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14498343380887)

O calculo que o sistema irá realizar para chegar ao valor é mês atual subtraindo do mês anterior:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14502912071703)

Caso no cadastro do encargo estiver com o parâmetro **provisão acumulada** marcado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14504593824279)

Ao gerar o encargo o mesmo é levado o valor cheio :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14504634026391) 

**Saiba mais**  
[Encargos - Folha de Pagamento](https://tdn.totvs.com/display/public/LRM/Encargos+-+Folha+de+Pagamento)
