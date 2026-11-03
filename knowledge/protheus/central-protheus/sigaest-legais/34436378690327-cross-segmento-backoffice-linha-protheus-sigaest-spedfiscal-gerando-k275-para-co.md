---
article_id: 34436378690327
category: SIGAEST - LEGAIS
content_hash: 9a3322a1697d25fa7bcf17ab6f452867ad12e1f46ab716735b4b1b0946941083
fetched_at: '2026-06-28T22:38:51.893056+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SPEDFISCAL gerando
  K275 para correções do K220 no Layout simplificado
type: support-article
updated_at: '2025-08-26T13:48:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34436378690327-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SPEDFISCAL-gerando-K275-para-corre%C3%A7%C3%B5es-do-K220-no-Layout-simplificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34436378674967) Tempo aproximado para leitura: **00:10:00 min**  
  
**Ocorrência**  
Ao gerar o SPEDFISCAL com Bloco K simplificado e possuir uma transferência de saldo de um produto para outro em um periodo anterior ao informado na geração do SPEDFISCAL o sistema está gerando o registro K275.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33 ou Superior.  
  
**Solução**  
De acordo com a validação de nosso time de produto junto a consultoria tributária no Guia Prático EFD-ICMS/IPI, versão 3.1.2, o K275 é um registro que tem o objetivo de escriturar correção de apontamento de período de apuração anterior, relativo ao Registro-filho, por tipo de Registro e por período de apuração em que o apontamento será corrigido.

Caso ocorra correção de apontamento apenas do Registro-pai (K270), este Registro não deverá ser escriturado, exceto quando a correção tiver como origem o **Registro K220 (origem 5 do Registro K270),** onde este Registro será obrigatório para identificação do item de destino, mesmo que não ocorra correção de quantidades.

Dado isso concluimos que é obrigátorio o preechimento do registro K275 sempre que houver a necessidade de correção de apontamento do registro K220 independente do tipo de layout apresentado, completo ou simplicado.  
  
Para mais detalhes acesse: [Registro K275 - CORREÇÃO DE APONTAMENTO](https://tdn.totvs.com/pages/releaseview.action?pageId=728650669)

**Saiba mais:**  
[Clique aqui e saiba mais sobre Legais/Fiscais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
