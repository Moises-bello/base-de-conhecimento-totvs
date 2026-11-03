---
article_id: 37510994120343
category: Financeiro - Smart View
content_hash: 1171010bf9877e6967f2a1306bb85550953b4f33753759c8fa1e286f1271e0d8
fetched_at: '2026-06-28T22:37:44.882911+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - EFD CONTRIBUIÇÕES -
  Registro de origem Financeiro duplicado no Smartview e na tabela CL2
type: support-article
updated_at: '2026-01-07T19:45:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37510994120343-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-EFD-CONTRIBUI%C3%87%C3%95ES-Registro-de-origem-Financeiro-duplicado-no-Smartview-e-na-tabela-CL2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37510994106647) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Smartview - Conferencia Efd Contribuição F100 - demonstra registro duplicado, quando é processado periodos parciais no mesmo mês    
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Esse comportamento no Smartview foi observado e está relacionado à forma de utilização da rotina. Não se trata de um erro no sistema, mas sim de uma característica do seu funcionamento conforme o uso realizado.

O arquivo EFD Contribuições possui exclusivamente uma periodicidade de entrega de dados **mensal**, ainda que a a rotina permita a geração em blocos por períodos por exemplo, o alerta para reprocessamento e deleção da tabela **CL2** só acontecerá se for identificado que o mesmo bloco de informações e períodos está sendo apurado novamente, o sistema não faz comparações ou tenta identificar o que consta em um bloco de informações diferentes para **impedir essa possível duplicidade de registro**  
  
Um dos pontos de gatilho desse reprocessamento é o campo **CL2\_PER** que é gravado com a data inicial de processamento (Data De  na rotina da apuração Pis/Cofins), assim se informado o período inicial diferente em outro processamento, não será apresentada a opção de reprocessamento pois o sistema entende que está sendo executado outro período, caso haja necessidade de geração desta forma, é possível caso seja realizado um controle do usuário/analista fiscal para os períodos em que serão quebrados os dados, pois atualmente não há um controle nativo no sistema.

Assim, para correta geração dos dados e também aplicação do reprocessamento caso haja necessidade é **obrigatório** **que o período inicial do processamento seja o mesmo informado anteriormente**.
