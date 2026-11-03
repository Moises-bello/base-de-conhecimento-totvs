---
article_id: 38393605639191
category: Ativo Fixo - Ajuste e Alteração do Bem
content_hash: ba9a393a6de394fb421ebe5a0d803468c37e68aea8dc71f1953dcf6d059db29d
fetched_at: '2026-06-28T22:41:58.801366+00:00'
product: protheus
section_id: 1500001546862
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 - Alteração
  de valores de bens já cadastrados
type: support-article
updated_at: '2026-02-19T20:25:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38393605639191-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Altera%C3%A7%C3%A3o-de-valores-de-bens-j%C3%A1-cadastrados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38393614401943)Tempo aproximado para leitura: 00:05 min

**Dúvida**  
Existe alguma forma ou rotina para realizar alterações manuais nos valores de um bem já cadastrado no Ativo Fixo?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo (SIGAATF) - Versão 12.1.7

**Solução**  
Atualmente, o Protheus não possui uma rotina nativa que possibilite a edição manual direta dos valores de um bem após a sua efetivação no sistema. Essa restrição existe para garantir a integridade dos cálculos contábeis, fiscais e o histórico de depreciação do ativo.  
  
Para corrigir valores que não estejam condizentes, existem dois procedimentos possíveis, dependendo da movimentação do bem:

1. **Processo de Baixa e Reinclusão**  
   Indicado para bens que já possuam movimentação como transferências, baixas parciais e etc, não sendo possível desclassificar.  
   * Realize a Baixa do Bem através da rotina de Baixa de Ativos (ATFA036);  
     [SIGAATF - ATFA036 - BAIXA DE ATIVO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018556171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-BAIXA-DE-ATIVO)
   * Inclua o bem novamente no sistema com os valores e saldos corretos utilizando a rotina de Inclusão (ATFA012).
2. **Processo de Desclassificação e Classificação**  
   Indicado exclusivamente para bens que ainda não possuem movimentações e foram incluídos via integração com o compras na rotina Documento de entrada (MATA103)   
   * Acesse a rotina de Classificação de Compras (ATFA240);
   * Utilize a opção de Estorno/Cancelamento para desfazer a classificação do bem;  
     [ATFA240 - Cancelamento da classificação do bem](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006848432-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Cancelamento-da-classifica%C3%A7%C3%A3o-do-bem)
   * Realize a Classificação novamente com o valor corrigido.

**Saiba Mais**  
[ATFA240 - Cancelamento da classificação do bem](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006848432-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Cancelamento-da-classifica%C3%A7%C3%A3o-do-bem)  
[ATFA036 - BAIXA DE ATIVO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018556171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-BAIXA-DE-ATIVO)
