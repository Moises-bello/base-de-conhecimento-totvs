---
article_id: 4414993780375
category: Folha Mensal
content_hash: d336b849f177987a37674d505b1fb934f98e06ba44e7c8d3749d46da9715f4b9
fetched_at: '2026-06-28T22:46:59.296404+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Férias Partidas: deduz INSS integral, incluindo mês seguinte'
type: support-article
updated_at: '2025-05-20T13:06:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414993780375-RH-RM-FOP-F%C3%A9rias-Partidas-deduz-INSS-integral-incluindo-m%C3%AAs-seguinte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18367464182295)Tempo aproximado para leitura: **00:01:36 min  
  
Dúvida**  
Como parametrizar sistema para descontar integral INSS férias partidas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os passos abaixo:  
  
1. Acesse: **Configurações | Parametrizador | Férias |** **Descontos** e marque as flags **Deduz integral (inclui mês seguinte)** e **Discrimina INSS no recibo de****férias.**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26408872165271)​  
  
**E****xemplo:**Lançamento das férias Inicio em Outubro e termino em Novembro:  
  
![](https://totvssuporte.zendesk.com/attachments/token/MjYJ36gfWhOLxIvh8PBZJEPii/?name=inline-140220154.png)​  
  
Envelope no mês de Outubro sobre o lançamento das férias:  
  
![](https://totvssuporte.zendesk.com/attachments/token/fnO3EAY2eo5r0gc66K8oL92Kl/?name=inline1733962199.png)​  
  
Veja que, o sistema realizou o desconto do INSS no mês corrente.  
  
Após a virada de competência para lançamento do envelope mês Novembro, sendo o final das férias, veja o envelope:  
  
![](https://totvssuporte.zendesk.com/attachments/token/5hP1IsBHkBZJCjjGPcL3iRfQX/?name=inline1230111771.png)​  
  
Ao visualizar o log de calculo, o sistema pegou como base de calculo o inss mês anterior no valor de R$284,26 que foi descontado, para abater o INSS do mês de Novembro.  
  
![](https://totvssuporte.zendesk.com/attachments/token/IInRG00kPzRgf7T4oLBVCh920/?name=inline1921301118.png)  
  
**Saiba Mais**[RH - RM - FOP - Férias: Lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007913092-RH-RM-FOP-F%C3%A9rias-Lan%C3%A7amento)  
[RH - RM - FOP - Férias: Finalizar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012328752-RH-RM-FOP-F%C3%A9rias-Finalizar-)

[Descontos](https://tdn.totvs.com.br/display/public/LRM/Descontos)
