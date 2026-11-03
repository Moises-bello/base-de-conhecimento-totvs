---
article_id: 39659618075543
category: Integrações - Ahgora
content_hash: f95830ed9db05da791e7c53234b2266fd111555641c4b946951cee0204e05db3
fetched_at: '2026-06-28T22:46:39.896993+00:00'
product: rm
section_id: 36553540355351
source: central-rm
title: RH - RM - FOP - Integração RM Folha de Pagamento x Ahgora - Como forçar o reenvio
  de todos os funcionários do RM para o Ahgora?
type: support-article
updated_at: '2026-04-10T18:21:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39659618075543-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Ahgora-Como-for%C3%A7ar-o-reenvio-de-todos-os-funcion%C3%A1rios-do-RM-para-o-Ahgora
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39659661901335) Tempo aproximado para leitura: **01:25:00 min**  
  
**Dúvida**  
Como alterar o status de integração de todos os funcionários de **"Integrado"** para **"Não Integrado"** para forçar a geração de gatilhos de alteração de movimento e enviar atualizações de todos funcionários?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.2402  
  
**Solução**  
Para que o sistema gere novos gatilhos de alteração e atualize o status de integração para *"Não Integrado"* de todos funcionários, é necessário forçar um movimento de alteração. Acesse a parametrização da integração do Ahgora no RM no **Módulo: Folha de Pagamento | Configurações | Parametrizador | 06.02 - Integrações | 06.02.11 - Ahgora**  
**![image.png](https://totvssuporte.zendesk.com/attachments/token/lsMu3crvo6sZcFG73Ws7yBw7r/?name=image.png&lotus_request=true)**

Na aba **“Fórmula para localizações”**, siga os passos abaixo:

1. Inclua uma nova fórmula (pode ser qualquer uma existente).
2. Avance até a conclusão e salve.  
   ![image.png](https://totvssuporte.zendesk.com/attachments/token/8cx9yFFGmkJkGxpGAWBeYY74c/?name=image.png&lotus_request=true)

Em seguida:

3. Acesse novamente a aba **“Fórmula para localizações”**.
4. Remova a fórmula adicionada anteriormente.
5. Salve novamente.

Esse processo irá forçar uma alteração em todos os funcionários da base alterando o status para "**Não integrado**". Com isso, uma nova atualização de todos funcionários será enviada ao Ahgora na próxima execução do agendamento ou através do envio manual.

**Saiba Mais**  
[**RH - RM - FOP - Integração RM Folha de Pagamento x Ahgora- Como parametrizar a integração do RM com o Ponto Web**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36554893220631-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Ahgora-Como-parametrizar-a-integra%C3%A7%C3%A3o-do-RM-com-o-Ponto-Web)
