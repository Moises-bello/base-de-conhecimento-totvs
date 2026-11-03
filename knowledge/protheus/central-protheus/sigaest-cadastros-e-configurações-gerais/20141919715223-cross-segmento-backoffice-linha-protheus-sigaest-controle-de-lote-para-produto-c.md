---
article_id: 20141919715223
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 287e0f079f0da1de2a171a554664b3219c581883f7378274d1a4409de70e58b3
fetched_at: '2026-06-28T22:39:08.178217+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Controle de lote para
  produto com validade indeterminada
type: support-article
updated_at: '2025-03-12T12:23:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20141919715223-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Controle-de-lote-para-produto-com-validade-indeterminada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20141949143959) Tempo aproximado para leitura: **00:01:40 min****Dúvida**Como configurar a validade do produto com lote, de forma indeterminada? produto com validade indeterminada.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Para esse cenário sugerimos utilizar uma data de validade longa.

Outra sugestão, no cadastro de produtos possui o campo Prazo Validade (B1\_PRVALID) veja print abaixo, onde você pode fixar a validade em dias para os produtos específicos.

![](https://totvssuporte.zendesk.com/attachments/token/SDDM1pwS29VDVHQ70VmuA8g4N/?name=inline819619856.png)  
Outra alternativa, utilizar a rotina MATA390 para efetuar a manutenção do lote para uma data de validade longa. **Exemplo: 31/12/2999**  
   
No padrão, não é possível incluir a palavra indeterminado no campo, devido o campo de controle de Lote ser do tipo DATA, onde não é possível a inclusão de dados caracteres, ou seja, se controla LOTE é obrigatório possuir a data de validade preenchida.

**Saiba mais:**

*[Documentação completa sobre controle de Rastreabilidade de Produtos no Estoque](https://tdn.totvs.com/pages/releaseview.action?pageId=367232994)*

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
