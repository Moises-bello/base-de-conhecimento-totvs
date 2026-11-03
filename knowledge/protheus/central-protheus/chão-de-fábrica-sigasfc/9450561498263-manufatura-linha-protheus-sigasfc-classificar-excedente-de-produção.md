---
article_id: 9450561498263
category: Chão de Fábrica (SIGASFC)
content_hash: 77753ff125d3571a9cba96f806499e6dacaa8e688be48696ddceefed099738f8
fetched_at: '2026-06-28T22:42:49.798995+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: Manufatura - Linha Protheus - SIGASFC - Classificar excedente de produção
type: support-article
updated_at: '2023-08-04T12:57:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9450561498263-Manufatura-Linha-Protheus-SIGASFC-Classificar-excedente-de-produ%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:00:55 min  
  
Dúvida**Como classificar o **excedente de produção** no módulo **Chão de Fábrica**? **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12  
  
**Solução**Quando a **quantidade produzida** é maior do que a prevista através da **OP - Ordem de Produção**, o **excedente** pode ser classificado como **ganho de produção** ou **produção a maior**, porém no módulo **chão de fábrica** a tela para classificação do excedente não é exibida.  
  
Nesse caso, é necessário ativar o parâmetro **MV\_GANHOPR - Utilizado para verificar se permite o conceito de ganho de produção na inclusão do apontamento de produção** para que o sistema entenda que se trata de um ganho de produção e para que o **Protheus** classifique o excedente como produção a maior é necessário **desativar** o parâmetro **MV\_GANHOPR** e preencher o parâmetro **MV\_PERCPRM** **- Percentual da quantidade da ordem de produção que será permitido apontar a maior**.
