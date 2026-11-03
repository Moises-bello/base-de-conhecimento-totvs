---
article_id: 6350296781335
category: eSocial - Gerar XML/ Integração Evento
content_hash: 29a52ce18ff2d65b58f71f57bdf2b4adda554ecf468c376d7f8c2d5d0fb0b524
fetched_at: '2026-06-28T22:47:12.166784+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 681 na integração com governo: Identificador
  inválido. O identificador deve ser único dentro da mesma competência e Indicativo
  do tipo de guia para cada um dos recibos de pagamento de cada trabalhador.'
type: support-article
updated_at: '2024-06-26T15:06:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6350296781335-RH-RM-FOP-eSocial-Erro-681-na-integra%C3%A7%C3%A3o-com-governo-Identificador-inv%C3%A1lido-O-identificador-deve-ser-%C3%BAnico-dentro-da-mesma-compet%C3%AAncia-e-Indicativo-do-tipo-de-guia-para-cada-um-dos-recibos-de-pagamento-de-cada-trabalhador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24446217966487) Tempo aproximado para leitura: **00:02:00 min****Ocorrência** Ao transmitir o evento **S-1200, S-1202** ou **S-2299** para o governo é retornado a inconsistência **Erro código 681**  
**Descrição: Identificador inválido. Ação Sugerida: O identificador deve ser único dentro da mesma competência e Indicativo do tipo de guia para cada um dos recibos de pagamento de cada trabalhador. Localização: /eSocial/evtRemun/dmDev/ideDmDev**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6350384809879)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro geralmente ocorre para funcionário com mais de um vínculo, pois a *tag* **ideDmDev**deverá conter um identificador único para cada um dos demonstrativos de pagamento do trabalhador dentro da mesma competência.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24447278340759)

Sendo assim, no caso de funcionários que possuem múltiplos vínculos na mesma coligada e que tenham pagamentos no mesmo período, o sistema irá gerar o **ideDmDev** igual para os vínculos, gerando o erro supracitado na integração. Também será validado quando o vínculo empregatícios for em outras empresas.  
  
**Solução**  
No cadastro do funcionário que apresentou a ocorrência, aba **Parâmetros**, foi implementado o campo **Prefixo Período (eSocial)**. O valor preenchido neste campo será agregado ao valor do período na *tag***ideDmdev**, evitando assim sua duplicidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24446212410519)

Após ajustar o cadastro do funcionário, basta gerar novamente o XML e transmitir para o governo.  
  
**Saiba mais**  
Para mais informações acesse:  
 • [Como discriminar nos eventos S-1200 e S-1210 a Tag <ideDmDev> para funcionários com categorias diferentes?](http://tdn.totvs.com/pages/viewpage.action?pageId=388236245)
