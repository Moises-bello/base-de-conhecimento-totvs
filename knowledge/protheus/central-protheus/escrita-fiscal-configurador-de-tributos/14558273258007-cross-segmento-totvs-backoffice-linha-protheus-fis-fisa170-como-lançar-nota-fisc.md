---
article_id: 14558273258007
category: Escrita Fiscal - Configurador de Tributos
content_hash: eef7346a3f6fec8bc26a3f20090298e60f66aa01615e5acc7eb0896f5c505c1d
fetched_at: '2026-06-28T22:39:17.491254+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como lançar
  nota fiscal de entrada de óleo diesel TAG15 no MATA103?
type: support-article
updated_at: '2024-11-14T13:44:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14558273258007-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-lan%C3%A7ar-nota-fiscal-de-entrada-de-%C3%B3leo-diesel-TAG15-no-MATA103
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26346040893975) Tempo aproximado para leitura: **00:06:00min** **Dúvida**Como lançar a nota fiscal de entrada de óleo diesel TAG15 no MATA103??  
  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**A nota fiscal de entrada será lançada com a configuração na rotina FISA170. Abaixo as configurações necessárias:  
   
No configurador / Base de dados   
Alterar o tamanho dos seguintes campos:  
   
SD1  
D1\_PICM   
![](https://totvssuporte.zendesk.com/attachments/token/2zMud7GvWUFEcFZdwNeqAqkRb/?name=image.png)

D1\_ALIQSOL  
![](https://totvssuporte.zendesk.com/attachments/token/EHKf6eqOhwcrxrGkNCo2RcMr8/?name=image.png)  
   
D1\_VINUT  
![](https://totvssuporte.zendesk.com/attachments/token/wRyukceIDETg2eEIqAUK3YS1Y/?name=image.png)  
   
   
CD2  
CD2\_ALIQ   
![](https://totvssuporte.zendesk.com/attachments/token/gtW2joSKqdooC91ieME3LUp1e/?name=image.png)  
   
F28  
F28\_ALIQ  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14873881687447)  
   
Após as configurações, o MATA103 e FISA170 estão prontos para receber as alíquotas diferenciadas.

Verifique o parâmetro:

Para que o valor da alíquota não seja arredondado no pedido de venda/Doc. Entrada, altere o parâmetro **MV\_DECALIQ**para **.T.**   
 

FISA170  
   
Regras Fiscais

Cadastros  
Tributos  
   
![](https://totvssuporte.zendesk.com/attachments/token/TPoQzOaYHhqSr5dZILtXcKmAw/?name=image.png)  
   
Esses tributos são padrões dentro do sistema, vamos usar o ICMS para ICMS monofásico e ICMS ST para o ICMS ST monofásico.  
   
Perfis   
   
Perfil do produto  
   
![](https://totvssuporte.zendesk.com/attachments/token/ipbi0VDKsJCfdyEi4zGSgXQo9/?name=image.png)  
   
O produto PB6DH está cadastrado na SB1  
   
![](https://totvssuporte.zendesk.com/attachments/token/vWKj44j3gCnKzxXfPfbzXFM9i/?name=image.png)  
   
Perfil de Operação  
   
![](https://totvssuporte.zendesk.com/attachments/token/p1vqjJKTW8uvrTJCJI0ixKGE5/?name=image.png)  
Vamos usar o Perfil 000013 já vem como cadastro padrão se precisar de outro CFOP que não está listado nesse cadastro incluir  
   
Perfil de Participante  
   
![](https://totvssuporte.zendesk.com/attachments/token/WuaItIg7MMBT50drrxFManVrE/?name=image.png)  
   
O fornecedor 000023 está cadastrado no SA2  
![](https://totvssuporte.zendesk.com/attachments/token/RhnThM46VJX2dZLaRDb8Gjb7R/?name=image.png)  
   
Perfil Origem e destino  
   
![](https://totvssuporte.zendesk.com/attachments/token/vGbiDfVntAfdj2eZhGXXBrVl7/?name=image.png)  
   
Regra de Calculo de Documento Fiscal  
   
Regra de base de calculo   
   
000023 - ICMS Monofásico  
   
![](https://totvssuporte.zendesk.com/attachments/token/KKm7id2wh00IjA0bw9vy85irB/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/5qNybQYNasmS2iMv1V8SP4GGd/?name=image.png)  
   
000024 - ICMS ST Monofásico  
   
![](https://totvssuporte.zendesk.com/attachments/token/08THrkPkvwKwvWwGU4Jo6b81F/?name=image.png)  
A formula será inserida manualmente  
   
![](https://totvssuporte.zendesk.com/attachments/token/vMoP77nMfm4WmrVdTbPlm1POU/?name=image.png)  
   
Regra de Alíquota  
   
000023 - ICMS Monofásico  
   
![](https://totvssuporte.zendesk.com/attachments/token/e8RPu70XAwzF1hQmXushD6flE/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/XInQlq8CsATghHZdnK4zR8vho/?name=image.png)  
   
000024 - ICMS ST Monofásico  
![](https://totvssuporte.zendesk.com/attachments/token/yArqy4BSYs3l4b4ZTtY2CZLeU/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/Bs94R5heG29olZEGWIzwbAvuK/?name=image.png)  
   
Regra de Escrituração do Tributo  
   
000023 - ICMS Monofásico  
   
![](https://totvssuporte.zendesk.com/attachments/token/M6M1V4tbleEdBDn2MryjvvQid/?name=image.png)  
   
000024 - ICMS ST Monofásico  
![](https://totvssuporte.zendesk.com/attachments/token/kFn2DI1gD4a9uIDWNoZzkCZQ1/?name=image.png)  
   
Regra de Calculo  
   
000023 - ICMS Monofásico  
   
![](https://totvssuporte.zendesk.com/attachments/token/cuFL3OW6UMWZu4pWhVfgj4PQN/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/TEiBTqAXwanbsuWSqZZxdiZnB/?name=image.png)![](https://totvssuporte.zendesk.com/attachments/token/cat0PBNRfwMBNPm5AEx9b709G/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/4oGarpMRRzAC5A1OvzexQyXxz/?name=image.png)  
   
000024 - ICMS ST Monofásico  
   
![](https://totvssuporte.zendesk.com/attachments/token/QuHGS9nNALXYBdX01riKcAJS0/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/LYIytoclSRyri7ybuJSeCpyUU/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/BFnRtRNHahc3wbLwONGawMdIF/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/2Ju3HM6zN1oMyIbRENDwQxOln/?name=image.png)  
   
Calculo do Óleo Diesel S10  
 

|  |  |
| --- | --- |
| qbcMono | 129.459 |
| adRemICMS | 0,9456 |
| vICMSmono/  DIESEL | 122.416,43 |
| qbcMonoReten | 17.653,500 |
| adRemICMSReten | 0,31516848 |
| vicmsmonoret | 5.563,83 |
|  |  |

   
Valores da nota fiscal  
   
![](https://totvssuporte.zendesk.com/attachments/token/q304iVVMNHBFXsllxQIoExmVq/?name=image.png)  
TES  
   
![](https://totvssuporte.zendesk.com/attachments/token/N772WJ2pqaim5j8an623OXJIJ/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/4NLTSd8Pc8ZpWujFUCtaT6Lon/?name=image.png)  
   
Lançamento do documento de entrada no MATA103  
   
![](https://totvssuporte.zendesk.com/attachments/token/hqABMD0gI9sCNKbpbZi8JZAJf/?name=image.png)  
   
Após a gravação da nota fiscal veja CD2  
   
![](https://totvssuporte.zendesk.com/attachments/token/m7uXvcvuZwUkERDtEwsa1UlST/?name=image.png)  
   
O XML vai buscar as informações da CD2 de acordo com a CD2\_CST  
   
Para emissão de nota fiscal precisa configurar a CD6 no MATA926.  
[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota Técnica 2023.001](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12928311594903-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-T%C3%A9cnica-2023-001?source=search)
