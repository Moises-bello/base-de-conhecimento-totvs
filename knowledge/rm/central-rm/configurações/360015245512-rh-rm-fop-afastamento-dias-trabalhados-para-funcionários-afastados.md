---
article_id: 360015245512
category: Configurações
content_hash: 105e4337c7297ab00d982eef7d7e9f08728d23c61b455239fa0df7ff5f014977
fetched_at: '2026-06-28T22:46:49.654165+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: 'RH - RM - FOP - Afastamento: Dias Trabalhados para Funcionários Afastados'
type: support-article
updated_at: '2024-10-11T20:11:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015245512-RH-RM-FOP-Afastamento-Dias-Trabalhados-para-Funcion%C3%A1rios-Afastados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**Ao lançar o envelope de pagamento de um funcionário que foi afastado no mês competência, o evento de dias trabalhados considera um dia a menos.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre pois a parametrização do sistema está considerando apenas o mês comercial. Assim, em meses com 31 dias, o sistema irá considerar apenas os 30 dias do mês comercial.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Selecione **Configurações | Parametrizador | Folha Normal | Afastamento 1/2** e desmarque o parâmetro **Usa mês comercial para afastamentos no final do mês com 31 dias.****![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9854188652055)**2. Após realizar a parametrização corretamente, recalcule o envelope de pagamento do funcionário. O evento de **Dias Trabalhados** deverá ser recalculado e os dias de **Referência** serão calculados corretamente.  
  
**Importante**A flag do parametrizador **Usa mês comercial para afastamentos no final do mês de 31 dias**, terá impactos apenas quando o período do afastamento passa pelo dia 31 do mês que tem 31 dias. No exemplo a seguir, no mês de maio, o funcionário encerra o afastamento no dia 13, e a partir desta data os dias trabalhados serão contabilizados normalmente como mês comercial, ainda que haja este período de afastamento remanescente no início do mês.  
  
Como exemplo de situação para o comportamento da flag, veja abaixo: **![](https://totvssuporte.zendesk.com/attachments/token/JPUZ8KBPAZKdeDVhs5PB9WqL0/?name=inline-1981671092.png)​**  
Parâmetro **Usa mês comercial para afastamentos no final do mês de 31 dias** desmarcado.  
  
O funcionário afastado do dia 11/05 até o dia 31/05 teve considerado 25 dias trabalhados no mês, visto que o afastamento tipo P, nos primeiros 15 dias, são arcados pela empresa, portanto contabilizam como dias trabalhados no evento de código de cálculo 2. Desta forma, do dia 26/05 até o dia 31/05, há o afastamento, sendo 6 dias no total. Neste caso, o dia 31 do mês entrou na contabilização de dias de afastamento, e é apenas nesta situação que a flag se torna útil. Por este motivo, na descrição do cálculo, há a frase **Serão considerados 31 dias**. **![](https://totvssuporte.zendesk.com/attachments/token/0BtaknZse9mvKFyMj59daMjns/?name=inline1079130139.png)​**  
Parâmetro **Usa mês comercial para afastamentos no final do mês de 31 dias** marcado. Com o flag marcado, no entanto, o cálculo dará preferência aos dias de afastamento, mantendo os 6 dias conforme o histórico de afastamento e 24 dias trabalhados, visto que o cálculo não está mais considerando o mês como sendo de 31 dias.  
  
Normalmente, entende-se que se deve considerar o mês como comercial na folha, e apenas nos casos em que o período de afastamento passa pelo dia 31 de algum mês, é que se considera esta opção a depender da interpretação do usuário. Como o processo se trata de parametrização, não há no sistema algum mecanismo para automatizar a consideração de 31 dias de afastamento se ele está utilizando mês comercial. Se ainda assim o usuário desejar que esta situação considere 31 dias, 13 dias de afastamento e 18 dias de atestado, conforme exemplo acima, utilizando mês comercial, será necessário aplicar alguma fórmula ou forçar valor no evento.  
  
Saiba mais...

[Parametrizador Folha Normal | Afastamento 1/2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719376#:~:text=Este%20par%C3%A2metro%20somente%20ser%C3%A1%20considerado,o%20dia%2031%20do%20m%C3%AAs.&text=Marque%20este%20par%C3%A2metro%20para%2C%20quando,dias%20do%20m%C3%AAs%20como%20divisor.)

[Parametrizador Folha Normal | Afastamento 2/2](https://tdn.totvs.com/pages/viewpage.action?pageId=556879107)
