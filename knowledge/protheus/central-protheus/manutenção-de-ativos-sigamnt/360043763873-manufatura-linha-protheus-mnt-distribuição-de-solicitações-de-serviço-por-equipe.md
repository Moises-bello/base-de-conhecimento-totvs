---
article_id: 360043763873
category: Manutenção de Ativos (SIGAMNT)
content_hash: 2baed04989a0c5e204d0d70eb9a7897a136a59513906dbf85f04e102164a0e63
fetched_at: '2026-06-28T22:42:33.137270+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Distribuição de Solicitações de Serviço
  por equipe
type: support-article
updated_at: '2021-07-05T20:55:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043763873-Manufatura-Linha-Protheus-MNT-Distribui%C3%A7%C3%A3o-de-Solicita%C3%A7%C3%B5es-de-Servi%C3%A7o-por-equipe
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)**Tempo aproximado para leitura: **00:01:15 min** **Dúvida**Como é realizada a distribuição de **Solicitações de Serviço** por equipe?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Para realizar a distribuição de **Solicitações de Serviço** para uma equipe, deve definir um responsável para a mesma em **Equipes - MNTA800**, conforme a imagem abaixo. Na aba de **Funcionários** deve informar o **Responsável - TP4\_CODRES** e os **Membros da Equipe - T1\_CODFUNC**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059405093/mceclip0.png)

Feito o processo de **Distribuição de Solicitação de Serviços** para a equipe selecionada na rotina de **Distribuição - MNTA296**, a rotina de **Atendimento - MNTA291**,deve ser acessada pelo responsável da equipe, e as solicitações de serviços podem ser visualizadas selecionando o botão **Carga da Equipe**, à esquerda da tela.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059405153/mceclip2.png)

Na tela de **Transferência**, basta selecionar o **Atendente** qual vai ser responsável pela **Solicitação de Serviço**. A partir deste momento, a solicitação é apresentada na carga do atendente escolhido, podendo ainda ser visualizada e transferida pelo responsável da equipe.  
  
**Importante**Para a realização do processo, o seguinte parâmetro deve ser configurado **MV\_NG1FAC = 1 - Indica se utiliza Facilities ou Solicitação de Serviço,** sendo **1** para **Facilities** e **2** para **Solicitação**.
