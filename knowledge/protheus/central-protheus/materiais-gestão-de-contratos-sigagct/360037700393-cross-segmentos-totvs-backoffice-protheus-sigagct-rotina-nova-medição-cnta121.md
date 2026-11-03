---
article_id: 360037700393
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: ae94db7139ba608ab4aa57b7e5b44991d9a8cac24a6f14a76d56aaf1a9c00e0b
fetched_at: '2026-06-28T22:37:20.166651+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Rotina Nova Medição
  CNTA121
type: support-article
updated_at: '2026-06-15T13:38:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037700393-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Rotina-Nova-Medi%C3%A7%C3%A3o-CNTA121
---

A rotina CNTA121 substitui a descontinuada CNTA120 para medição em contratos no Protheus a partir da versão 12.1.17, suportando planilhas semi-fixas, recorrentes e de serviço. Informações antes gravadas apenas na tabela CND agora são distribuídas em outras tabelas. A integração com o módulo PCO usa o lançamento 000355, e a geração de pedidos de venda ocorre por medição de cada parcela prevista.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41232334114327) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Rotina Nova Medição CNTA121

**Ambiente**

Protheus - Gestão de Contratos -  A partir da versão 12.1.17.

**Solução**

Com a Descontinuidade da rotina anterior de medição CNTA120, passa a ser utilizada a rotina atual de medição CNTA121.

A Rotina ***CNTA121*** possui a possibilidade de uso de alguns tipos específicos de contrato disponibilizados desde a Release V12.1.17.

* Contratos com [Planilhas Semi-Fixas](https://tdn.totvs.com/display/public/PROT/Planilha++Semi-fixa).
* Contratos com [Planilhas Recorrentes](https://tdn.totvs.com/display/public/PROT/Planilha++Recorrente).
* Contratos com [Planilhas de Serviço](https://tdn.totvs.com/pages/releaseview.action?pageId=274630153).

Estes tipos de planilha devem ser medidos exclusivamente pela nova rotina de Medição.

***Importante:***

Com o advento da nova rotina de Medição CNTA121 algumas informações que, na rotina CNTA120, eram gravadas apenas na tabela CND passaram a ser gravadas em outras tabelas acessórias.

Em ***Saiba Mais*** segue artigo de "***Ciclo de Vida - CNTA120***"  que mencionam as tabelas de estrutura de dados que são gravados na CNTA121 em substituição dos que eram gravados apenas na tabela CND na Medição.

***Observação:***

Com a conversão do fonte para MVC, alguns pontos de entrada existentes devem ser convertidos para pontos de entrada padrão MVC. Para consultar a lista DE-PARA dos pontos de entrada disponíveis na nova rotina, acesse: <https://tdn.totvs.com/pages/releaseview.action?pageId=274840426>

***Obs1:***

Os lançamentos de Integração da Medição do Gestão de Contratos com o Módulo de PCO são realizados pela configuração do lançamento do PCO 000355.

Apesar deste lançamento do PCO mencionar a função CNTA120 (acesso da rotina pelo menu descontinuado), a função ainda é usada internamente pelo sistema, e ainda assim continua este mesmo lançamento 000355 o que deve ser configurado para que ocorra a integração da nova rotina CNTA121 com o módulo SIGAPCO.

**Obs2:**

Existe a possibilidade de gerar pedidos de venda em lote através da Medição no módulo Gestão de contratos/ Protheus?

**R:**Por padrão, a única forma de gerar todas as parcelas é realizar a medição de cada uma das parcelas previstas no cronograma financeiro. Dessa forma, todos os pedidos de venda serão gerados e, consequentemente, será possível prosseguir com a inclusão dos documentos de saída.

Caso tenha interesse em sugerir uma melhoria segue o canal de nossa central colaborativa [**Central Colaborativa TOTVS**](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics), localizada em nosso [**Portal do Cliente**](http://suporte.totvs.com/). É um espaço que você poderá sugerir melhorias, acompanhar a evolução das solicitações já realizadas, comentar, seguir, votar em sugestões feitas por outros clientes e muito mais!

Para conhecer mais sobre as suas **funcionalidades** clique [**AQUI**](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=13)e assista o nosso vídeo ou acesse nosso artigo [**Central Colaborativa - Funcionalidades Disponíveis**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27733078485399-Central-do-Cliente-TOTVS-Central-Colaborativa-Funcionalidades-Dispon%C3%ADveis)**​**.  
 Você pode acompanhar as suas **sugestões** e **comentários** clicando [**AQUI**](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)**.**  
 Acompanhe as **Novidades da Release** clicando [**AQUI**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360009734433-Ciclo-de-Vida-Relat%C3%B3rio-de-Releases).

​

***Saiba Mais:***

* [Ciclo de Vida - CNTA120](https://tdn.totvs.com/pages/releaseview.action?pageId=543090098)
* [Nova Medição - CNTA121 - Gestão de Contratos - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=353284981)
* [CNTA120 - Medição - Descontinuada em 04/04/2022](https://tdn.totvs.com/pages/viewpage.action?pageId=608149730)
* [MP - SIGAGCT - Pontos de entrada para rotinas de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-MP-SIGAGCT-Pontos-de-entrada-para-rotinas-de-Medi%C3%A7%C3%A3o)
* [MP - SIGAGCT - Como fazer para as Medições Automáticas ( CNTA260 ) serem geradas pela Rotina Nova Medição (CNTA121) ? - MV\_CT26021](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034124234-MP-SIGAGCT-Medi%C3%A7%C3%B5es-autom%C3%A1ticas-geradas-n%C3%A3o-podem-ser-visualizadas-na-rotina-CNTA121-%C3%A9-apresentado-o-Help-Op%C3%A7%C3%A3o-indispon%C3%ADvel-para-medi%C3%A7%C3%B5es-realizadas-com-a-rotina-de-medi%C3%A7%C3%A3o-padr%C3%A3o-)
* [GCT0084\_Nova\_Medição\_Versão\_BETA](https://tdn.totvs.com/pages/viewpage.action?pageId=274840426)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT- Data de Aviso sobre a rotina Medições CNTA120 que será descontinuada em Abril de 2022](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5145957380887-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Data-de-Aviso-sobre-a-rotina-Medi%C3%A7%C3%B5es-CNTA120-que-ser%C3%A1-descontinuada-em-Abril-de-2022)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
