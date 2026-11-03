---
article_id: 37400227875991
category: Materiais - Compras (SIGACOM)
content_hash: 9223893ab690353f8315c7b912a1c6857be35285d16d99b969a7bac2a9f3b0d7
fetched_at: '2026-06-28T22:41:25.313704+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotinas do Processo
  Legado de Cotação estão bloqueadas
type: support-article
updated_at: '2026-01-28T10:36:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37400227875991-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotinas-do-Processo-Legado-de-Cota%C3%A7%C3%A3o-est%C3%A3o-bloqueadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37400227867031) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao acessar as Rotinas Descontinuadas do Antigo Processo de Cotação ( MATA131/ MATA150 /MATA161 ) na release 2410 o sistema gera Alerta ***"Essa rotina foi descontinuada e sua manutenção foi encerrada em 01/01/2026."*** e não permite acessar as rotinas, fica bloqueado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37400197547799)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - 12.1.2410  
  
  
**Solução**  
Para solucionar esse bloqueio indevido e liberar as rotinas para utilização, será necessário aplicar o Pacote abaixo.

O pacote pode ser acessado no endereço: 12.1.2310:<https://r.totvs.io/p/1232063> ; 12.1.2410:<https://r.totvs.io/p/1232061> ; 12.1.2510:<https://r.totvs.io/p/1232062> ;

**Obs**. Não esqueça de fazer backups devidamente e aplicar inicialmente em base de teste homologação.

Segue abaixo documentação da issue.

[DMANMAT02-55198 DT MATA131/MATA150/MATA160/MATA161 Legislação - Atender o processo de impostos via rotina legado](https://tdn.totvs.com/pages/viewpage.action?pageId=1028945359)

**Obs2:**

Para a release **12.1.2410,** a TOTVS não prestará serviços de suporte técnico e atualização, que incluem modificações, correções e aperfeiçoamentos técnicos.

Já para a release **12.1.2510** as rotinas passam a ficar bloqueadas (inacessíveis).

Para maiores informações referente as datas de bloqueio, por favor, acesse a documentação abaixo.

[**Prorrogação do bloqueio de uso das rotinas: Geração da Cotação / Atualização da Cotação / Análise da Cotação do módulo de Compras do TOTVS Backoffice da Linha Protheus**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36811980103575-Prorroga%C3%A7%C3%A3o-do-bloqueio-de-uso-das-rotinas-Gera%C3%A7%C3%A3o-da-Cota%C3%A7%C3%A3o-Atualiza%C3%A7%C3%A3o-da-Cota%C3%A7%C3%A3o-An%C3%A1lise-da-Cota%C3%A7%C3%A3o-do-m%C3%B3dulo-de-Compras-do-TOTVS-Backoffice-da-Linha-Protheus)

Gera Cotação <https://tdn.totvs.com/pages/releaseview.action?pageId=863908608>

Atualiza Cotação <https://tdn.totvs.com/pages/releaseview.action?pageId=863908677>

Analisa Cotação <https://tdn.totvs.com/pages/releaseview.action?pageId=863908735>

***Saiba Mais:***

[Prorrogação do bloqueio de uso das rotinas: Geração da Cotação / Atualização da Cotação / Análise da Cotação do módulo de Compras do TOTVS Backoffice da Linha Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36811980103575-Prorroga%C3%A7%C3%A3o-do-bloqueio-de-uso-das-rotinas-Gera%C3%A7%C3%A3o-da-Cota%C3%A7%C3%A3o-Atualiza%C3%A7%C3%A3o-da-Cota%C3%A7%C3%A3o-An%C3%A1lise-da-Cota%C3%A7%C3%A3o-do-m%C3%B3dulo-de-Compras-do-TOTVS-Backoffice-da-Linha-Protheus)

[Cross Segmentos - Backoffice (Linha Protheus) - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
