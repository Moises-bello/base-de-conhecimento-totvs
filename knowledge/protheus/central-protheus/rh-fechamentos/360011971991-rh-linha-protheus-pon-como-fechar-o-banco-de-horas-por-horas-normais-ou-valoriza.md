---
article_id: 360011971991
category: RH - Fechamentos
content_hash: 62f7a21c422a9d7a540cb461fcee60268cc5983f91950e99be23fab8b7390593
fetched_at: '2026-06-28T22:44:48.877485+00:00'
product: protheus
section_id: 32419231682455
source: central-protheus
title: RH - Linha Protheus - PON - Como fechar o Banco de Horas por horas normais
  ou valorizadas
type: support-article
updated_at: '2025-06-05T14:28:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011971991-RH-Linha-Protheus-PON-Como-fechar-o-Banco-de-Horas-por-horas-normais-ou-valorizadas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32102245286039) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida:**Como realizar o fechamento do Banco de Horas por horas normais ou valorizadas?  
 **Ambiente:**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução:  
1.** No modulo do Ponto eletrônico certificar se o funcionário possui lançamentos de Banco de Horas, em **Atualizações> Lançamentos> Banco de Horas**.  
  
**2.** Para realizar o fechamento do banco de horas acessar em **Miscelânea> Fechamento> Banco de Horas**.   
Lembrando que o fechamento do Banco de Horas não valida o **MV\_PONMES**, portanto, o processo poderá ser executado de qualquer período de apontamento, fechado ou aberto;  
  
**3.** Nos parâmetros da rotina de Fechamento de Banco de Horas selecionar as perguntas conforme exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32102245288215)  
Dessa forma, teremos um fechamento apenas da coluna de Saldo das Horas Normais. E para fechar a coluna de Saldo Valorizado, juntamente com a de Saldo, alterar o parâmetro **"Utilizar Horas" para a opção VALORIZADAS.**  
  
4. Para verificar o resultado do fechamento após o calculo mensal do ponto, acessar através da rotina **Atualizações> Lançamentos> Resultados.****Saiba mais:**[RH - Linha Protheus - PON - Como efetuar o fechamento do banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013670411-RH-Linha-Protheus-PON-Como-efetuar-o-fechamento-do-banco-de-horas)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
