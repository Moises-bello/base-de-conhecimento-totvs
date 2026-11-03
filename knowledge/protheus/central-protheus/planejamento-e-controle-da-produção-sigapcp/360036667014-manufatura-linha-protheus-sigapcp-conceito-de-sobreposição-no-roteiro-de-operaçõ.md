---
article_id: 360036667014
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a60f4278a97c016f66e1689d2bd74568a267c9de953042ae18430392b7d54f97
fetched_at: '2026-06-28T22:42:42.085695+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Conceito de sobreposição no roteiro
  de operações
type: support-article
updated_at: '2024-06-05T14:53:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036667014-Manufatura-Linha-Protheus-SIGAPCP-Conceito-de-sobreposi%C3%A7%C3%A3o-no-roteiro-de-opera%C3%A7%C3%B5es
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:05 min**  
**Dúvida**O que significa a **sobreposição** no roteiro de operações?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução** **Sobreposição** é o recurso disponível na alocação das operações através do **MATA690 - Carga Máquina**, no qual uma operação pode iniciar antes de concluir totalmente a operação anterior.  
Para isso, no **MATA632 - Roteiro de Operações**, deve ser definido se a operação pode ser sobreposta, preenchendo no campo **G2\_TPSOBRE - Tipo Sobrep** de que forma deve ser a sobreposição.  
Se o conteúdo for **Quantidade**, ao concluir a produção de uma unidade na operação anterior, dá-se início a alocação da operação atual, já se o conteúdo for **Percentual** o conteúdo registrado no campo **G2\_TEMPSOB - Tempo Sobre** é interpretado como um percentual de tempo da operação a ser executado antes de iniciar a sobreposição.  
E se o conteúdo do campo **G2\_TPSOBRE** for **Tempo**, a sobreposição iniciará depois de concluído o tempo informado no campo **G2\_TEMPSOB.**
