---
article_id: 4411222614039
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: bb9bbf2d179fbbae1bbecda362309eaac7cb962a4496f7bdbca77168314dc1df
fetched_at: '2026-06-28T22:39:09.701779+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Posso alterar campos
  travados no Dicionário para alterações de tamanho e/ou decimais?
type: support-article
updated_at: '2024-01-11T20:09:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411222614039-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Posso-alterar-campos-travados-no-Dicion%C3%A1rio-para-altera%C3%A7%C3%B5es-de-tamanho-e-ou-decimais
---

**Dúvida**É possível alterar tamanho de campos ou decimais que estão travados no Dicionário?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Quando determinado campo como por exemplo **B1\_COD** ou **AH\_UNIMED** que são travados para alteração do tamanho, porém possuem **G****rupo de campos** que permitem alterações, podem ser realizadas, **somente configurando seus respectivos grupos**. Outro detalhe é que neles já vem estabelecido o tamanho Máximo e Mínimo que esses campos podem ter.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20504504744855)

 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20504504755607)

Já para campos como por exemplo o **BE\_LOCALIZ** que é travado para alteração do tamanho, e não possui um grupo de campo que permita a alteração, nesse caso, ***não*** é possível alterar. **O campo é limitado ao tamanho determinado na construção do Software**.

Qual **o impacto?**  
**Resp.:**O tamanho do campo é travado diretamente em fontes que não temos como mapear, caso alterar diretamente pela estrutura (SX3), em todas atualizações que são necessárias rodar o [**UPDDISTR**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024320152-MP-FIS-Como-Processar-o-UPDDISTR-para-atualiza%C3%A7%C3%A3o-de-dicion%C3%A1rios), **fará com que o campo retorne para o tamanho padrão automaticamente**, e os registros afetados por essa ação  não irão funcionar corretamente, impedindo as movimentações padrões e até causando error.log. Para esse tipo de alteração, ***pode ser considerada no ERP inteiro e outros campos que tenham essa trava***.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411225273879)

Também é possível sugerir uma melhoria para o campo que deseja alterar, para isso, seguem abaixo as instruções e links necessários para entrar em contato com nossa Central Colaborativa.

As sugestões de melhoria no produto não são tratadas via ticket, elas devem ser incluídas diretamente no [Portal do Cliente](http://suporte.totvs.com/). Um espaço que você poderá sugerir melhorias, acompanhar a evolução das solicitações já realizadas, comentar, seguir, votar em sugestões feitas por outros clientes e muito mais!  
  
Esse espaço é a nossa[Central Colaborativa TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics).  
Para conhecer mais sobre as suas **funcionalidades**clique **[AQUI](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=13)**e assista o nosso vídeo ou acesse nosso artigo **[Central Colaborativa - Funcionalidades Disponíveis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466814-Funcionalidades-Dispon%C3%ADveis-na-Central-Colaborativa-TOTVS)​**.  
  
Você pode acompanhar as suas **sugestões**e **comentários**clicando **[AQUI](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br).**  
Acompanhe as **Novidades da Release** clicando [AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360009734433-Ciclo-de-Vida-Relat%C3%B3rio-de-Releases).  
  
​![](https://totvssuporte.zendesk.com/attachments/token/0PPHQkcbhxphbjnq6ctEOx7Ux/?name=central+colaborativa+curto_7frame.gif)​  
  
Como alternativa, caso a melhoria seja validada, aceita pelo time de produto TOTVS e deseje a implementação da funcionalidade na versão atual ou em curto prazo, podemos direcionar essa solicitação para a nossa área de Central de Soluções que providenciará uma proposta de customização para sua empresa para atender a funcionalidade sugerida.

**Saiba Mais:**  
[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
