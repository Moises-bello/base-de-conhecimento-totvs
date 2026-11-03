---
article_id: 37509391969303
category: Financeiro - Cadastros
content_hash: 9c7a19ca09a2ef81dd5f9074d4ec57840b59ed8b02a0ea07d35eee3ca36e0492
fetched_at: '2026-06-28T22:37:53.074052+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Duplicidade nas rotinas
  do menu financeiro
type: support-article
updated_at: '2026-01-07T18:42:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37509391969303-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Duplicidade-nas-rotinas-do-menu-financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37509391959703) Tempo aproximado para leitura: 06**:00 min**

**Dúvida:**  
As rotinas do módulo Financeiro (SIGAFIN) aparecem duplicadas no menu para os usuários. Como corrigir esta inconsistência?

**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - 12.1.33 e superiores

**Solução:**

Essa ocorrência geralmente está relacionada à duplicidade de itens inseridos no momento da personalização do menu (.xnu) customizado do SIGAFIN. Para a correção, é necessária a limpeza e reconstrução do menu através do módulo Configurador.

**Para validação e correção, siga os passos abaixo:**

1. Acesse o módulo Configurador (SIGACFG);
2. Vá em **Ambiente > Cadastros > Menus;**  
   **![](https://centraldeatendimento.totvs.com/hc/article_attachments/37509418068631)**
3. Selecione o módulo Financeiro e clique em OK;  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37509418069015)
4. No lado direito, selecione o **menu já existente** e clique em **Remover**  
   **![](https://centraldeatendimento.totvs.com/hc/article_attachments/37509418069783)**
5. Em seguida, selecione novamente o menu existente no lado esquerdo e clique em **Adicionar**, para atualiza-lo conforme padrão disponivel!  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37509391962903)
6. Clique em Gerar e salve o arquivo com o nome desejado  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37509418070935)

**Importante**

Caso existam rotinas personalizadas inseridas manualmente no menu anterior, será necessário inseri-las novamente após a recriação.

Se preferir, é possível também remover apenas as rotinas duplicadas manualmente, navegando pela árvore do menu, sem a necessidade de refazer todo o arquivo.
