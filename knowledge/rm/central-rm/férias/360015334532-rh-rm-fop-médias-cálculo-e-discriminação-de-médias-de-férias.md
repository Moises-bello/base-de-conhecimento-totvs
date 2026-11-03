---
article_id: 360015334532
category: Férias
content_hash: 9f599b9d07d0cba58a8c5617ceec6c3b8dd9545126c1328db7d9c6fd0e92b01d
fetched_at: '2026-06-28T22:46:56.477063+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Médias: cálculo e discriminação de médias de férias'
type: support-article
updated_at: '2024-10-04T18:37:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015334532-RH-RM-FOP-M%C3%A9dias-c%C3%A1lculo-e-discrimina%C3%A7%C3%A3o-de-m%C3%A9dias-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como parametrizar um evento específico para o pagamento de médias de férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de pagamento - Todas as versões  
  
**Solução**Para parametrizar as médias discriminadas siga os passos abaixo:  
  
1. Acesse: **Administração de pessoal | Eventos | Eventos** e cadastre novos eventos com os seguintes códigos de cálculo:  
  
Código de Cálculo 0 - Média de XXXX de Férias  
Código de Cálculo 0 - Diferença Média de XXXX Férias  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9978592545559)  
  
O código XXXX utilizado acima representa eventos de horas-extras, comissões ou adicionais.  
  
2. Acesse: **Administração de Pessoal | Sindicatos** e depois acesse a aba **Férias**.Na aba inferior **Eventos p/ pagamento de Média de Férias**, é necessário parametrizar os grupos de médias e informar os eventos para pagamento das médias específicas.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9978761085591)  
  
Para que o pagamento das médias ocorra separadamente em um evento específico, informe um grupo de médias a partir do grupo 1. Isso é necessário, pois ao informar o grupo 0 as médias serão somadas ao evento de pagamento de férias com código de cálculo 38.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9978805418135)  
  
3. Após parametrizar os grupos de médias nos **Eventos p/ pagamento de Média de Férias**, é necessário informar a incidência de média no cadastro dos eventos pagos ao funcionário. Acesse: **Administração de Pessoal | Eventos | Eventos** edite o evento que deseja informar a incidência das médias e vá em **Anexos | Eventos de Média**.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9978880473239)  
  
Cadastre a incidência em férias e o grupo de média utilizado, conforme explicado nos passos anteriores. Lembrando que este evento deverá estar lançado e com valores no período estabelecido nas parametrizações da média de férias para que as médias sejam corretamente lançadas. Desta forma, ao calcular as férias para o funcionário, o evento informado para pagamento de médias do grupo 1 será lançado no recibo de férias.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9978883209111)
