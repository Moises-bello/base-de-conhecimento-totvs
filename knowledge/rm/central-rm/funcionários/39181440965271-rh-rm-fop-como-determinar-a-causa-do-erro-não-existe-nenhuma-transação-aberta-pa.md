---
article_id: 39181440965271
category: Funcionários
content_hash: ab92eaece4b72dd55837afb36b100f14fb0ec95decf8f4371caefc3553a361ec
fetched_at: '2026-06-28T22:47:03.133439+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP -  Como determinar a causa do erro "Não existe nenhuma transação
  aberta para fazer commit" ao tentar cadastrar um funcionário
type: support-article
updated_at: '2026-04-16T12:47:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39181440965271-RH-RM-FOP-Como-determinar-a-causa-do-erro-N%C3%A3o-existe-nenhuma-transa%C3%A7%C3%A3o-aberta-para-fazer-commit-ao-tentar-cadastrar-um-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39181440953751) Tempo aproximado para leitura**: 00:01:00 min**  
  
**Dúvida**  
Como determinar a causa do erro **"Não existe nenhuma transação aberta para fazer commit"** ao tentar cadastrar um funcionário?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Para corrigir o erro que ocorre ao cadastrar funcionários, é imprescindível revisar todas as fórmulas visuais e triggers associadas a esse procedimento. Esse problema surge quando o sistema detecta inconsistências nas fórmulas ou triggers, sendo necessário a validação de todas as fórmulas visuais e triggers relacionadas ao cadastro de funcionários. Abaixo, encontra-se uma documentação contendo instruções sobre como desabilitá-las. Recomenda-se realizar o procedimento em um ambiente de teste, desativando ambos os processos, e, posteriormente, verificar qual Trigger ou fórmula visual está impactando o processo e ocasionando o erro mencionado.

[RH - RM - FOP - Desabilitar triggers e fórmulas visuais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415329649943-RH-RM-FOP-Desabilitar-triggers-e-f%C3%B3rmulas-visuais)
