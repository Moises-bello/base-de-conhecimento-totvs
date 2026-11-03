---
article_id: 21080074353175
category: RH - Carol
content_hash: c037a96a80052634dcb5f0cf2c6d165863fc4a766a417d13f9f8013374a148db
fetched_at: '2026-06-28T22:44:56.582986+00:00'
product: protheus
section_id: 19035556880407
source: central-protheus
title: RH - Linha Protheus - PON - Leitura das marcações não ocorre se for utilizado
  o ID de conexão do Clock In no MV_APICLO3
type: support-article
updated_at: '2025-12-04T17:40:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21080074353175-RH-Linha-Protheus-PON-Leitura-das-marca%C3%A7%C3%B5es-n%C3%A3o-ocorre-se-for-utilizado-o-ID-de-conex%C3%A3o-do-Clock-In-no-MV-APICLO3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21080098915735) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao tentar processar a **Leitura** das marcações vindas da Carol, se for utilizado o **ID de conexão** do Clock In no **MV\_APICLO3,** os dados não são lidos e gravados.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**  
O problema ocorre se no conteúdo do parâmetro **MV\_APICLO3**, fosse informado o **ID de conexão do Clock In,** e não **clockinmobile**.  
Com isso, o campo **RR1\_CODUNI** da tabela **RR1** ficava preenchido com o ID de conexão, fazendo com que a rotina de Leitura/Apontamento não conseguisse encontrar os dados.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21080074328727)  
  
**Solução**  
Para solucionar este problema, foi feito um ajuste no Produto que está disponível no último [**Pacote de Expedição Contínua - Acumulado de RH.**](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
  
  
**Saiba Mais:**  
[Integração Protheus x Carol](https://tdn.totvs.com/pages/releaseview.action?pageId=515294516)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
