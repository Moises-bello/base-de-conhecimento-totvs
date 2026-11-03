---
article_id: 40036202370071
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 30130b28463028dcd2001927a91c058355422fe87bbe3fc91b4697c53e162205
fetched_at: '2026-06-28T22:41:48.497486+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAATF - ATFA240 - Erro
  na classificação em lote: O campo Historico (N3_HISTOR) não foi preenchido'
type: support-article
updated_at: '2026-04-27T15:29:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40036202370071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Erro-na-classifica%C3%A7%C3%A3o-em-lote-O-campo-Historico-N3-HISTOR-n%C3%A3o-foi-preenchido
---

O erro no processamento da classificação em lote na rotina ATFA240 ocorre porque o campo Histórico (N3\_HISTOR) não está preenchido no cadastro do grupo de bens (ATFA271). Para resolver, acesse ATFA271, localize o grupo, preencha o histórico do bem e salve. Após isso, execute novamente a classificação em lote para concluir com sucesso.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40036202359703) Tempo aproximado para leitura: **5 min**  
  
**Dúvida**  
Ao tentar realizar a classificação de bens em lote na rotina Classificação de Compras (ATFA240), o sistema apresenta um log de erro de processamento indicando que o campo Histórico (N3\_HISTOR) não foi preenchido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40036173342999)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo (SIGAATF) - a partir da versão 12  
  
  
**Solução**  
Este incidente ocorre porque o campo referente ao histórico do bem não está configurado no cadastro do grupo de bens associado (ATFA271). Para que o processamento em lote seja concluído com sucesso, é necessário preencher essa informação.

**Passos**

1. Acesse a rotina de Grupo de Bens (ATFA271).

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40036173343767)
2. Localize o grupo de bens que está sendo utilizado na classificação e clique em **Alterar**.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40036173344663)
3. Na tela de configuração do grupo, preencha as informações obrigatórias referentes ao histórico do bem.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40036173346071)
4. Após confirmar as alterações, execute novamente a rotina de classificação em lote.

**Saiba mais:**  
[ATFA240 - Classificação em Lote](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11989934209687-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Classifica%C3%A7%C3%A3o-em-Lote?source=search)
