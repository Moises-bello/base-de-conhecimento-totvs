---
article_id: 38309763844375
category: Ativo Fixo - Ajuste e Alteração do Bem
content_hash: 062705a5a6a6af5ecfc019231c887b4eb96bb6649bf35210bd9e1b41ff433850
fetched_at: '2026-06-28T22:41:58.812294+00:00'
product: protheus
section_id: 1500001546862
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 - Alteração
  do campo Data inicio de depreciação (N3_DINDEPR) no cadastro do ativo fixo
type: support-article
updated_at: '2026-02-12T14:59:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38309763844375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Altera%C3%A7%C3%A3o-do-campo-Data-inicio-de-deprecia%C3%A7%C3%A3o-N3-DINDEPR-no-cadastro-do-ativo-fixo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38309763826071) Tempo aproximado para leitura: **05:00 min**  
  
**Dúvida**  
Como realizar a alteração do campo Data inicio de depreciação (N3\_DINDEPR) no cadastro do ativo quando os campo encontra-se bloqueado para edição?  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - 12.1.2210  
  
  
**Solução**  
O Protheus não permite o desbloqueio manual ou edição direta do campo Data inicio de depreciação (N3\_DINDEPR), quando o bem já está classificado ou possui movimentações, visando garantir a integridade dos cálculos de depreciação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38309750585111)

Para regularizar a situação, utilize uma das opções abaixo, conforme a viabilidade do seu cenário:

1. **Estorno da Classificação (Correção do bem existente)** Indicado quando é possível reabrir períodos ou reverter movimentações recentes.

   * **Verifique Movimentações:** Antes de alterar o cadastro, é necessário estornar quaisquer movimentações que o bem tenha sofrido, como Transferências, Baixas Parciais ou Ampliações.
   * **Estorno de Classificação:** Acesse a rotina **Classificação de Compras (ATFA240)** e realize a exclusão da classificação do bem. Isso retornará o ativo para o status "Pendente de Classificação".  
       
     [ATFA240 - Cancelamento da classificação do bem](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006848432-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Cancelamento-da-classifica%C3%A7%C3%A3o-do-bem)
   * **Correção:** Com os campos liberados, ajuste a data desejada.
   * **Reclassificação:** Classifique o bem novamente para que ele retome o cálculo de depreciação.
2. **Baixa e Nova Inclusão (Substituição do cadastro)** Indicado quando não é viável realizar estornos (ex: períodos fiscais já fechados ou excesso de movimentações antigas).

   * **Baixa do Ativo:** Acesse a rotina de **Baixa de Ativos (ATFA036)** e realize a baixa total do bem incorreto.
   * **Novo Cadastro:** Inclua um novo ativo no sistema contendo as datas e valores corretos desde a origem.

**Saiba Mais**  
[ATFA240 - Cancelamento da classificação do bem](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006848432-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Cancelamento-da-classifica%C3%A7%C3%A3o-do-bem)  
[ATFA036 - BAIXA DE ATIVO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018556171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-BAIXA-DE-ATIVO)
