---
article_id: 40305955971223
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 25fddec6e793925052a2a8e14a3ebdb2184148279563403238cb0113db6dc4ef
fetched_at: '2026-06-28T22:38:58.507053+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Log de auditoria
  para alteração de data de validade de lotes (MATA390)
type: support-article
updated_at: '2026-05-07T18:09:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40305955971223-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Log-de-auditoria-para-altera%C3%A7%C3%A3o-de-data-de-validade-de-lotes-MATA390
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40305955947671) Tempo aproximado para leitura: 00**:01:00 min**  
  
**Dúvida**  
Existe algum tipo de log ou rastreamento na rotina Manutenção de Lotes (MATA390) que registre usuário, data e hora em caso de alteração da data de validade de um lote?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque e Custos (SIGAEST) - Todas as releases  
  
**Solução**  
As rotinas de manutenção de lotes não são consideradas rotinas de processamento e, por este motivo, não gravam logs nativamente no arquivo unificado de logs (tabela CV8). No entanto, a execução desta rotina gera alterações e inclusões na tabela SD5 (Movimentação por Lote).

Para rastrear essas alterações, é necessário utilizar a funcionalidade de Audit Trail (Trilha de Auditoria) aplicada especificamente sobre a tabela SD5. Com essa configuração ativa, o sistema passará a registrar as modificações, permitindo auditorias futuras sobre quem realizou a alteração e em qual momento.

**Passos**

1. Acesse o módulo Configurador (SIGACFG).
2. Realize a implementação do Embedded Audit Trail para a tabela SD5 conforme o link da documentação: [Configurar Embedded Audit Trail](https://tdn.totvs.com/display/framework/Configurar+Embedded+Audit+Trail)
3. Após a implementação, as próximas ocorrências de alteração de validade ou manutenção de lotes serão registradas para consulta.

***Saiba Mais:***  
[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
