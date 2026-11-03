---
article_id: 4409609448599
category: Manutenção de Ativos (SIGAMNT)
content_hash: aece1b24e7c2b709caa5abf6facda0c29e450f64faa023cfa4e4a55b9f6a5c24
fetched_at: '2026-06-28T22:42:34.326473+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Plano de Acompanhamento
type: support-article
updated_at: '2021-09-28T20:30:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409609448599-Manufatura-Linha-Protheus-MNT-Plano-de-Acompanhamento
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como funciona o **Plano de Acompanhamento**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Nestas opções do menu, o usuário poderá gerar **O.S. - Ordens de serviço** de acompanhamento do contador e apontar estas **O.S.** para atualizar o contador do bem.  
  
**1. Plano -** **MNTA310**Utilizado para gerar **O.S.** para leitura ou levantamento daqueles bens que são controlados por contador. O programa irá gerar **O.S. de acompanhamento** conforme os parâmetros estabelecidos pelo usuário. Um plano gerado por este programa terá *Status* de pendente, poderá, por ação de programa posterior passar para *Status* de confirmado ou cancelado. As **O.S.** geradas também terão o *Status* de pendente, podendo passar para liberada ou cancelada pelo programa de confirmação do plano. Também neste programa o usuário poderá encerrar um plano de acompanhamento. Ao encerrar um plano o usuário estará informando para passar o *Status* do plano para terminado, sendo que as **O.S.** que neste ato estiverem em aberto, passarão a ter *Status* de cancelada.  
Nessa rotina, verifique se os bens que são controlados por contador, estão com o campo, **Período** e **Un. Acomp.** preenchidos na aba de **Contador**.  
  
**2. Confirmação - MNTA320**Confirmação de plano de acompanhamento. Para que um plano seja liberado para execução, deverá ser processado por este programa. O usuário poderá optar por liberação total ou parcial do plano. Após o processamento deste programa, o plano passará para *Status* de liberado. As **O.S. liberadas** também passarão para *Status* de liberada, e aquelas não liberadas passarão para *Status* de cancelada. Na liberação parcial o usuário poderá optar por assinalar aquelas que deseja cancelar, ou aquelas que deseja liberar, conforme a sua conveniência.  
  
**3. Retorno - MNTA390**Este processo permite o registro das informações obtidas na execução das ordens de serviço de acompanhamento. O reporte deve ser efetuado por ordem de serviço. Na janela **Retorno - Acompanhamento**, clique sobre o botão **Retorno**. Podem ser atualizadas: as informações relativas ao acompanhamento por contador constantes do arquivo de bem.   
O programa efetuará a atualização da variação/dia do contador, que servirá como base, juntamente com outras informações, para a execução do plano de manutenção.  
  
**4. Reabertura O.S. - MNTA255**Esta rotina tem como objetivo reabrir as ordens de serviço de acompanhamento que já foram finalizadas. Este procedimento permite facilitar e agilizar o processo de acompanhamento das ordens de serviço, evitando que seja necessário abrir outro plano com as mesmas descrições só para gerar uma ordem de serviço que já havia sido finalizada.
