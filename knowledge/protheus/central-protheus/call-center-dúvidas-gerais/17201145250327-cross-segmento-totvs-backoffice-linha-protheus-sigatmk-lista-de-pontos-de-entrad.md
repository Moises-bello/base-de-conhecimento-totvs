---
article_id: 17201145250327
category: Call Center - Dúvidas Gerais
content_hash: d4e83ec0ec785095dc881c933f1b50abce24262ced1ca20bea03574055f1e0f7
fetched_at: '2026-06-28T22:41:26.928403+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Lista de Pontos
  de Entrada da rotina Pré-atendimento (TMKA280)
type: support-article
updated_at: '2023-09-01T12:41:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17201145250327-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Lista-de-Pontos-de-Entrada-da-rotina-Pr%C3%A9-atendimento-TMKA280
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17201136866711) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Quais os pontos de entrada existentes na rotina **Pré-atendimento para Telecobrança Ativa (TMKA280)**?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.  
  
**Solução**

Abaixo a lista com os **Pontos de Entrada** existentes na rotina de **Pré-atendimento para Telecobrança Ativa (TMKA280)**, e seus endereços de documentação no TDN:

* **TK280TB - Inclusão de botões:** Tem como objetivo a inclusão de novos botões na barra de ferramentas da rotina de Pré-Atendimento ([**https://tdn.totvs.com/x/oZJn**](https://tdn.totvs.com/x/oZJn)).
* **TK280SU5:** Ponto de entrada para substituir a pesquisa do contato relacionado ao cliente na solicitação de novo pré-atendimento (***não possui documentação no TDN***).
* **TK280NOV - Pre atendimento:** É executado antes o início de um novo pré-atendimento na rotina TMKA280, permitindo validar a execução dessa operação ([**https://tdn.totvs.com/x/n5Jn**](https://tdn.totvs.com/x/n5Jn)).
* **TK280SQL - Adição de expressão na query:** Permite adicionar uma expressão na cláusula **Where** da query de seleção dos títulos para um novo pré-atendimento (**<https://tdn.totvs.com/x/yQueCQ>**).
* **TK280COB - Processo de cobrança:** É executado antes do início do processo de cobrança, após a seleção de um cliente no pré-atendimento (TMKA280), permitindo validar a operação de cobrança ([**https://tdn.totvs.com/x/npJn**](https://tdn.totvs.com/x/npJn)).
* **TMKALTA5 - Permissão de alterações:** É executado antes da alteração do Contato, com o objetivo de permitir ou não que a alteração seja feita ([**https://tdn.totvs.com/x/vpJn**](https://tdn.totvs.com/x/vpJn)).
* **TMKALTU5 - Execução de comandos:** É chamado após a alteração do Contato, com o objetivo de executar comandos diversos após a alteração (**<https://tdn.totvs.com/x/v5Jn>**).

**Saiba Mais**

**[Pontos de Entrada - Call Center - P12](https://tdn.totvs.com/x/r52pHg)**
