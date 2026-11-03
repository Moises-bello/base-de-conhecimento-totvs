---
article_id: 1500011581022
category: RH - Leitura e Apontamento
content_hash: 609159fb20fc9a43df5ee0eaa1910293464fdc154a380e394904496e0e5d1fee
fetched_at: '2026-06-28T22:44:45.992260+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Não foi encontrado o período no calendário de marcações.
  Acerte a data base do sistema
type: support-article
updated_at: '2025-10-07T20:06:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011581022-RH-Linha-Protheus-PON-N%C3%A3o-foi-encontrado-o-per%C3%ADodo-no-calend%C3%A1rio-de-marca%C3%A7%C3%B5es-Acerte-a-data-base-do-sistema
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32150552754455) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Na Leitura/Apontamento, o sistema gera *log*: Não foi encontrado o período no calendário de marcações. Acerte a data base do sistema.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018674542)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução****1.** Verifique o Período de Apontamento em: **Atualizações > Cadastro de Ponto > Períodos de** **Apontamentos > Mod.Per.Apont. > Apenas Visualizar > Salvar**, conforme registrado no **MV\_PONMES.** A **Data Base** deve estar dentro do período em que a leitura será realizada. Por exemplo, se houver dois períodos abertos e a leitura for para um período retroativo ao processamento, use como data base o último dia do período correspondente.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32150552755351)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20680658035223)  
  
**2.** A [**Troca de Turno**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671) do funcionário é **importante** para a [**montagem do calendário**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016361412). No momento do [**Fechamento Mensal**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004103232-RH), é gerado um registro de Troca de Turno aos funcionários com o primeiro dia do novo período.  
Funcionários **sem nenhuma Troca de Turno** ou que tenham uma Troca de Turno muito **anterior ao período de apontamento aberto**, poderá ter erro na montagem do calendário.  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20678001332247)****Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
[RH - Linha Protheus - PON - Como funciona a Troca de Turno dos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671-RH-Linha-Protheus-PON-Como-funciona-a-Troca-de-Turno-dos-funcion%C3%A1rios)
