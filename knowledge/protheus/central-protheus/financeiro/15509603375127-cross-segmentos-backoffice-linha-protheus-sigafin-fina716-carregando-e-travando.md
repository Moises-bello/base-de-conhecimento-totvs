---
article_id: 15509603375127
category: Financeiro
content_hash: 7e847c2ed9e5508e5ce411d832158b686f0a2d9155f68b1168a99478893d9058
fetched_at: '2026-06-28T22:38:03.177131+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA716 - Carregando
  e travando ao acessar a rotina
type: support-article
updated_at: '2024-06-17T20:29:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15509603375127-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Carregando-e-travando-ao-acessar-a-rotina
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15509609219735) Tempo aproximado para leitura: **00:05:00min****Ocorrência**No módulo Financeiro, ao tentar realizar a abertura da rotina o sistema fica somente carregando.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois a parametrização do sistema está incorreta para o tamanho de campo numéricos da tabela SEH que é utilizada pela Rotina.   
  
**Solução**

Abra o log do **appserver** chamado console.log

E caso esteja com o erro no console.log  
**WARNING - TCSetField - Invalid field len:**  
Siga os passos abaixo:   
Verifique em sua **SX3** campos da tabela **SEH** se estão no padrão do sistema, se houve modificação no tamanho de campo do tipo numérico onde o sistema suporta somente de **1 a 16,** o sistema apresentará o problema. Segue abaixo documentação que auxilia no processo.  
  
**Saiba mais**  
[TCSetField](https://tdn.totvs.com/display/tec/TCSetField)
