---
article_id: 360012783911
category: ' RH - Funcionários'
content_hash: 2a93468635af12720a30e09163df074dd8a61bfcae466bf9ec4e498ad2460af4
fetched_at: '2026-06-28T22:44:48.192625+00:00'
product: protheus
section_id: 32419218165783
source: central-protheus
title: RH - Linha Protheus - PON - Alterar a visualização do período na rotina Exceção
  por Funcionário
type: support-article
updated_at: '2025-12-26T13:50:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012783911-RH-Linha-Protheus-PON-Alterar-a-visualiza%C3%A7%C3%A3o-do-per%C3%ADodo-na-rotina-Exce%C3%A7%C3%A3o-por-Funcion%C3%A1rio
---

**![relogio.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32096712500887)** **Tempo aproximado para leitura:****00:01:00 min**  
  
**Dúvida**  
Como alterar a visualização do período na rotina Exceção por Funcionário  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
O parâmetro se alterado, teremos uma visualização diferente quando acessarmos a rotina **Exceção por Funcionário - PONA140**.  
  
Este parâmetro não tem funcionalidade na rotina **PONA090 - Exceção por Período**.  
  
Se o parâmetro **MV\_PAPEXCE** estiver com o **conteúdo P**, indica que utilizará o conteúdo do parâmetro **MV\_PAPONTA** para composição do grid de marcações de acordo com o período de apontamento.  
  
Parâmetro **MV\_PAPEXCE** com o **conteúdo P:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30086942528791)  
  
  
Veja no cadastro de período como estão configurados os parâmetros **MV\_PAPONTA/MV\_PONMES**:  
Para saber como consultar: [RH - Linha Protheus - PON - Rotina Período de Apontamento - PONA290](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30086942530583)  
  
  
Acessando a rotina de exceções por funcionário, em **Atualizações> Cadastro de Funcionários> Exceções Por Funcionários:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30086942534679)  
  
  
Se o Parâmetro **MV\_PAPEXCE** com o **conteúdo M**, utilizará o a composição do mês (01/31):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30086917682967)  
  
  
Acessando a rotina de exceções por funcionário, em **Atualizações> Cadastro de Funcionários> Exceções Por Funcionários:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30086942537367)  
  
  
  
**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como cadastrar exceções por período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006706652-RH-Linha-Protheus-PON-Como-cadastrar-exce%C3%A7%C3%B5es-por-per%C3%ADodo)
