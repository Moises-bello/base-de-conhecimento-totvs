---
article_id: 19678134661399
category: Financeiro
content_hash: 01a92527cc2443402d2b5d5ebe2463e41dc370298262426b5f4dbbde95b783e8
fetched_at: '2026-06-28T22:38:03.255411+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Geramos os impostos
  de PCC individualmente, porém deveria ser agregado. O que fazer?
type: support-article
updated_at: '2023-12-14T18:28:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19678134661399-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Geramos-os-impostos-de-PCC-individualmente-por%C3%A9m-deveria-ser-agregado-O-que-fazer
---

**Causa**

Geramos os títulos com os impostos de PCC de forma individual, porém deveria ser agregado. O que fazer?

**Solução**

Para ser gerado de forma agregada o PCC ajuste o parâmetro **MV\_RNFAGRE**

**Conteúdos validos:**

**0=**Não agregar (padrão)**;**

**1=**Agregar PIS, COFINS e CSLL (CSRF)**;**

**2=**Agregar IR, PIS, COFINS e CSLL (COSIRF);

  
**Saiba mais:**

https://centraldeatendimento.totvs.com/hc/pt-br/articles/17887265370647?source=search  
   
**Observação importante:**  
O sistema acatará apenas para os títulos novos. Caso o título já tenha sido baixado, temos 3 opções:  
   
1º Deverá cancelar a baixa, baixar novamente e rodar o Extrator Fiscal.  
   
2º  Realizando o ajuste dos campos FKF\_REINF e FK2\_REINF =2 executar o Extrator Fiscal novamente (caso seja apenas um título)  
   
How To:  
<https://www.youtube.com/watch?v=IJRr2gXQykY>

3º Temos também a opção de gerar o TXT pelo extrator, conforme imagem abaixo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19678109811479)

E importar pela rotina (TAFA500)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19678134598679)**

Informe o caminho do arquivo e o Layout, confirme

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19678086695959)**

Clique em continuar

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19678109824919)**

Conforme a mensagem de arquivo processado e pode finalizar.

**Saiba mais:**

[FAQ - 0021 - Como são tratadas as retenções dispensadas por ser inferior a R$ 10,00?](https://tdn.totvs.com/pages/releaseview.action?pageId=804053851)

[Fique por dentro das atualizações Reinf Protheus](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro#Eventos--839875140)

[How To - Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19775578473751)
