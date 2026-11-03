---
article_id: 31577155473431
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 9107a8a5e92f49824b432a50c793b436dcf0653dd52b27f298d8299fa0a7e290
fetched_at: '2026-06-28T22:37:20.182602+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Schedule - Apropriação
  do Cronograma Contábil
type: support-article
updated_at: '2026-05-05T13:07:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31577155473431-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Schedule-Apropria%C3%A7%C3%A3o-do-Cronograma-Cont%C3%A1bil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31577144389911) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como configurar Apropriação do Cronograma Contábil via CNTA300?

**Ambiente**  
Esta funcionalidade estará disponível a partir da versão **12.1.2410**

**Solução**

Ao executar acessar a rotina **Manutenção de Contratos ( CNTA300 )** acesse em Outras Ações / Schedules / Apropriação Contábil

![](https://tdn.totvs.com/download/attachments/877161561/image-2024-10-21_18-24-51.png?version=1&modificationDate=1729546102570&api=v2)

A visualização dos eventos executados desta rotina serão exibidos

![](https://tdn.totvs.com/download/attachments/877161561/image-2024-10-21_18-25-41.png?version=1&modificationDate=1729546102503&api=v2)

Nesta tela também será possivel realizar a criação de uma agendamento recorrente ( clicando no botão **NOVO )**, conforme demonstrado abaixo:

Execução Única, em data/hora pre-deteminada:

![](https://tdn.totvs.com/download/attachments/877161561/image-2024-8-9_15-21-40.png?version=1&modificationDate=1729546103100&api=v2)

Execução Diária:

![](https://tdn.totvs.com/download/attachments/877161561/image-2024-8-9_15-27-5.png?version=1&modificationDate=1729546102973&api=v2)

Execução Semanal:

![](https://tdn.totvs.com/download/attachments/877161561/image-2024-8-9_15-29-4.png?version=1&modificationDate=1729546103040&api=v2)

Execução Mensal:

![](https://tdn.totvs.com/download/attachments/877161561/image-2024-8-9_15-29-50.png?version=1&modificationDate=1729546102840&api=v2)

Parametrização adicional:

![](https://tdn.totvs.com/download/attachments/877161561/image-2024-8-9_15-30-37.png?version=1&modificationDate=1729546102767&api=v2)

Após informado os dados, confirme a gravação.

![](https://tdn.totvs.com/download/attachments/877161561/image-2024-10-21_18-26-23.png?version=1&modificationDate=1729546102437&api=v2)

![](https://tdn.totvs.com/download/attachments/877161561/image-2024-8-9_15-34-42.png?version=1&modificationDate=1729546102907&api=v2)

## **DEMAIS INFORMAÇÕES**

Importante

Para realizar manutenções no agendamento criado, a principio só poderá ser feito através do configurador, na rotina Ambiente \ Schedule \ Schedule.

Importante

Esta funcionalidade estará disponível a partir da versão 12.1.2410

Importante

Para o **funcionamento**deste **recurso**, se faz necessário a configuração do **Smart Schedule**em seu ambiente conforme a documentação: [Schedule Protheus](https://tdn.totvs.com/display/public/framework/Schedule+Protheus)

***Obs1:***

**Consideração do parâmetro MV\_CNTDTIN no uso da CNTA290 pelo Schedule:**

Regra de Data (MV\_CNTDTIN): A rotina CNTA290, quando executada via Schedule, utiliza a Data Base do sistema como referência. O parâmetro MV\_CNTDTIN define quantos dias retroativos à data base o sistema deve considerar para a apropriação.

Dessa forma, tendo como referência a Data Base do Sistema no momento da execução da rotina no Schedule, serão contabilizados as parcelas do Cronograma Contabil, com data anterior a Data Base no range com dias retroativos de acordo com o parâmetro MV\_CNTDTIN.

Execução Manual vs. Automática: Na execução manual, o usuário tem a liberdade de preencher os parâmetros SX1 (incluindo datas futuras). No Smart Schedule, o processo é padronizado para evitar apropriações indevidas de períodos ainda não encerrados.

***Saiba Mais:***

[DT Smart Schedule GCT - Apropriação do Cronograma Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=877161561)

[Apropriação do Cronograma Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=234610742)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
