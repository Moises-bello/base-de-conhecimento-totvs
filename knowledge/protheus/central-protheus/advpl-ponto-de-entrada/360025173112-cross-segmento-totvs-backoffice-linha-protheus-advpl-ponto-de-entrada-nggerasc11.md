---
article_id: 360025173112
category: ADVPL - Ponto de Entrada
content_hash: 6912d46caf1ff3fb1ba02bf6c86bdf4201f3d9d7e9e5488ef4c1f172db3169ff
fetched_at: '2026-06-28T22:40:12.731744+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  NGGERASC11 não executa
type: support-article
updated_at: '2021-12-30T14:28:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025173112-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-NGGERASC11-n%C3%A3o-executa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Estou querendo usar o ponto de entrada [NGGERASC11](http://tdn.totvs.com/pages/viewpage.action?pageId=272403172) para alterar a descrição da observação da SC de compras. Porém parece que o ponto de entrada não é executado. Ele foi desativado ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Existe uma regra na rotina a qual avalia o parâmetro **MV\_NGMNTCP**(Indica se a numeração dos itens da solicitação de compras será a mesma. Este parâmetro sobrepõem o processo padrão de geração do compras), para que o ponto de entrada seja executado, este parâmetro deve estar com valor **N** conforme print a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024076311/mceclip1.png)
