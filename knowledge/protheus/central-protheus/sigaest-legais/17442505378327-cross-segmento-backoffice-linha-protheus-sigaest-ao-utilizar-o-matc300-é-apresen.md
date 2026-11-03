---
article_id: 17442505378327
category: SIGAEST - LEGAIS
content_hash: 69e442579028960586aa2716f57ec524c0878f0728aa69fa8e468c4da0363f14
fetched_at: '2026-06-28T22:38:51.592844+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ao utilizar o MATC300
  é apresentado divergência na desmontagem "Sem Item Origem (RE7)"
type: support-article
updated_at: '2023-09-11T19:38:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17442505378327-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-utilizar-o-MATC300-%C3%A9-apresentado-diverg%C3%AAncia-na-desmontagem-Sem-Item-Origem-RE7
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17442536551319) Tempo aproximado para leitura: **00:02:13min** **Dúvida**Ao utilizar o MATC300 é apresentado divergência na desmontagem "Sem Item Origem (RE7)":![](https://centraldeatendimento.totvs.com/hc/article_attachments/17442067240343)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Neste caso é necessário analisar as movimentações de desmontagem, para entender se o tipo utilizado (B1\_TIPO) é contemplado nos registros K210 e K215.

No exemplo acima, se analisarmos a desmontagem vamos identificar que o item origem existe na movimentação:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17442306895127)

Porém vale lembrar que o MATC300 é um facilitador, que analisa possíveis rejeições do SPED antes da geração do txt.

Sabendo disso a validação feita nesse momento está relacionada ao tipo do produto, neste caso o PI110923 é um Produto Intermediário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17442379778711)

Ao analisarmos a documentação sobre o registro K210 (Desmontagem de Mercadorias - Itens de Origem) identificamos que no Padrão ele não considera Produtos Intermediários (N°06) [clique aqui](https://tdn.totvs.com/display/public/PROT/Registro+K210%3A+Desmontagem+de+Mercadorias+-+Itens+de+Origem):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17442440995479)

Tabela de tipos (Maiores informações [clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=259560649)):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17442515360023)

Dessa maneira deve analisar se o Tipo 06 Produto Intermediário deve ser considerado nos registros de desmontagem, caso entenda que sim, deve ajustar em uma das opções consideradas no registro K210.

Neste exemplo fizemos o ajuste no MV\_BLKTP04 que é relacionado aos Produtos Acabados adicionando o PI:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17442745337879)

É necessário também alterar o MV\_BLKTP06 (relacionado aos Produtos Intermediários) para que o PI não fique em duplicidade em dois parâmetros MV\_BLKTP\*\* distintos, nesse caso escolhemos um outro tipo qualquer, mas deve avaliar internamente qual opção preencher:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17442790583191)

Após isso ao gerar o MATC300 não é gerado mais nenhuma divergência pois os tipos existentes estão contemplados nos registros K210 e K215:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17442930264855)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
