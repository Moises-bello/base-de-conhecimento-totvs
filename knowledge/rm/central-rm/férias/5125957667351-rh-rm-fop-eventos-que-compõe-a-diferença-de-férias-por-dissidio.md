---
article_id: 5125957667351
category: Férias
content_hash: 71d99ee4a6ec4a702469adb015c7be1ade27929e3da2dbc0bad817ee5fa7e9ce
fetched_at: '2026-06-28T22:46:56.316647+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP - Eventos que compõe a diferença de férias por dissidio
type: support-article
updated_at: '2025-01-20T21:45:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5125957667351-RH-RM-FOP-Eventos-que-comp%C3%B5e-a-diferen%C3%A7a-de-f%C3%A9rias-por-dissidio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:08:20 min** **Dúvida**Quais os eventos  compõem o processo de diferença de férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, basta verificar as informações abaixo sobre quais eventos são utilizados no processo de diferença de férias e suas parametrizações.  
  
Códigos de Calculo que são utilizados no processo da Diferença de Férias por Dissidio:  
  
[Código de Cálculo 45 - Dif. Férias Pagas no Mês](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452718398)  
Provento do tipo valor.  
O sistema calculará a diferença do aumento salarial, ocorrido no período de gozo das férias e o resultado da diferença de férias será lançado no evento de CC 45. O evento de CC 45 tem que incidir INSS e FGTS, pois deve compor as bases de cálculo do mês. Independente se a diferença for calculada por dissídio sim ou não, o evento fará parte das bases de Cálculo de INSS e FGTS, pois o mesmo está sendo feito no mês de pagamento das férias. Quando é férias de meses anteriores, o sistema não lança este evento.  
  
[Código de Cálculo 59 - Diferença de Abono de Férias](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452718362)  
Provento do tipo valor. O sistema calculará a diferença decorrente do aumento salarial efetuado no período de gozo das férias. O sistema recalculará as férias com o novo salário e pagará a diferença de abono pecuniário neste código de cálculo.  
  
[Código de Cálculo 79 - Diferença 1/3 Férias Pagas Mês](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452718622)  
Provento do tipo valor. O sistema calculará a diferença de 1/3 de férias, ocorrida com aumento salarial dentro do período de gozo das férias.  
  
[Código de Cálculo 80 - Diferença Férias Próximo Mês](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452718961)  
Provento do tipo valor. O sistema calculará a diferença decorrente do aumento salarial efetuado no período de gozo das férias e pagará a diferença das férias do próximo mês neste evento.  
  
[Código de Cálculo 81 - Diferença 1/3 Férias Próximo Mês](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452718619)  
Provento do tipo valor. O sistema calculará a diferença decorrente do aumento salarial efetuado no período de gozo das férias e pagará a diferença de 1/3 de férias do próximo mês neste evento. Este evento somente será lançado para funcionário com férias repartidas.  
  
[Código de Cálculo 86 - Diferença Férias Pagas Mês Anterior](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452718395)  
Provento do tipo valor. O sistema lançará o valor da diferença das férias pagas, proporcional, no mês anterior.  
  
[Código de Cálculo 87 - Diferença 1/3 Férias Pagas Mês Anterior](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452718625)  
Provento do tipo valor. O sistema lançará neste evento a diferença de 1/3 de férias pagas, proporcional, no mês anterior, Código de Cálculo 77, decorrente do aumento salarial efetuado no período de gozo das férias.

[Código de Cálculo 88 - Diferença Outros Eventos Férias](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452719641)  
Provento do tipo valor. O sistema lançará o valor da diferença de outros eventos referente as férias pagas em meses anteriores. Neste caso todos os eventos, Provento/Desconto, serão acumulados neste evento podendo ficar com o valor final negativo.  
   
Caso seja necessário a discriminação, o evento com código de cálculo 88 também poderá ser inserido como Desconto do tipo valor.  
   
O cálculo considerará da seguinte forma:  
01 – No momento do cálculo somente evento provento é encontrado no cadastro de eventos, será considerado o evento que for encontrado primeiro e será lançado o valor dos proventos e descontos de outros eventos lançados nas férias para as quais foram calculadas diferenças. Veja que este cálculo poderá retornar negativo caso os descontos sejam maiores que os proventos.  
   
02 – No momento do cálculo evento provento e evento desconto são encontrados no cadastro de eventos, será considerado o evento provento para o valor dos proventos e será considerado o evento descontos para o valor dos descontos, portanto será discriminado o evento de código de cálculo 88 – Diferença Outros Eventos Férias lançados nas férias para as quais foram calculadas diferenças.  
  
[Código de Cálculo 110 - INSS de Diferença Salarial de Férias](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452718218)  
Desconto do tipo valor. Este evento será utilizado na diferença de férias por dissídio. Este evento será o desconto de INSS referente a base de diferença de dissídio e terá as mesmas incidências do INSS Férias.  
  
[Código de Cálculo 111 - Base de FGTS de Diferença Salarial Férias](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452719694)  
Base de cálculo do tipo valor sem incidência. Este evento será utilizado para o cálculo de diferença de férias dissídio. Este evento será o somatório da diferença calculada dos eventos de férias, que tenham incidência em INSS.  
  
[Código de Cálculo 116 - Estorno Base INSS Dissídio Retroativo Férias](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452718644)  
Base de cálculo do tipo valor.  
Este evento será utilizado para o cálculo de diferença de férias dissídio. Este evento será o somatório da diferença calculada dos eventos de férias, que tenham incidência em INSS e terá incidência em estorno de inss. Exemplo: 1/3 de Férias.  
  
[Código de Cálculo 132 - Diferença INSS Férias Próximo Mês](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452718408)  
Desconto do tipo valor. Caso a opção **Deduz INSS Integral (inclui mês seguinte)** do menu **Configurações** **| Parametrizador | Férias | Desconto de INSS**, estiver confirmada, o valor da diferença de férias será proporcionalizado no evento com código de cálculo 03 - INSS e no evento com o código de cálculo 132, centro e trinta e dois, no lançamento das férias, caso estas sejam partidas.  
  
[Código de Cálculo 176 - Diferença de 1/3 de Abono de Férias](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452718628)  
Provento do tipo valor, cadastramento obrigatório no momento do cálculo da diferença de férias.  
  
[Código de Cálculo 197 - Dif. Pensão Alimentícia Férias](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=452718419)  
Desconto do tipo valor e Est. Calc. IRRF de Ferias. Este evento permite a utilização de fórmulas para o cálculo. Este código de cálculo será lançado automaticamente no movimento do funcionário houver um cálculo de diferença de férias e nas férias do funcionário a ser calculado a diferença existir o CC113 - Pensão Alimentícia de Férias. Será gerado um movimento de pensão para o dependente como Dif. de Férias, Movimento =5, e registrado no cadastro do dependente  em **Cadastros | Funcionários | Base de Cálculo | Dependentes | pasta Movimento da Pensão**.  
  
**Saiba Mais**  
[RH - RM - FOP - Códigos de Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412890806807-RH-RM-FOP-C%C3%B3digos-de-C%C3%A1lculo)
