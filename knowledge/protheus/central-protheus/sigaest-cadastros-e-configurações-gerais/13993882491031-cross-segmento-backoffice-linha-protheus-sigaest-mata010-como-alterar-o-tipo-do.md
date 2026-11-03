---
article_id: 13993882491031
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: b2cd2b44116598a4b06582cfb6ed5a41bb08dd455fbb490eb81dba3ed253a5ae
fetched_at: '2026-06-28T22:39:09.438594+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Como alterar
  o tipo do meu produto (B1_TIPO) e os impactos?
type: support-article
updated_at: '2025-03-12T12:26:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13993882491031-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Como-alterar-o-tipo-do-meu-produto-B1-TIPO-e-os-impactos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:25 min** **Dúvida**Existe a necessidade, de efetuar alteração do tipo de cadastro do meu produto, por exemplo hoje ele tem o tipo MP, mas quero que seja MC, como alterar e quais impactos?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**Como alterar o tipo de produto?**

A alteração do tipo de cadastro do produto, pode ser efetuada, pela própria rotina de cadastro de produto, basta clicar em alterar e definir o novo tipo, após salvar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13993687439895)

**Quais impactos na alteração do tipo de produto?**

O sistema em si, não pode bloquear que o tipo de produto seja alterado, entretanto deve-se atentar o porque deseja alterar o tipo.

Em relação ao estoque, podemos dizer que vai existir um impacto para com a geração do Bloco K, pois esse é atrelado ao tipo de produto.

Demais ocasiões, devem ser avaliadas pontualmente, como: LPs que usam o tipo de produto, relatórios, consultas, são muitos pontos diversos.

**Mais eu preciso alterar o tipo de produto, oque o suporte sugere?**

Como "sugestão" : Sugerimos que seja cadastrado um novo produto com o tipo desejado, e depois efetue uma transferência entre armazéns, para cada uma dos produtos com os respectivos saldos.

Assim, você terá o histórico dos produtos antigos, e novos, e os produtos com tipo defasado, aos quais seriam alterados, basta no cadastro do produto, incluir o bloqueio do produto, para que não sejam mais utilizados.

[MP - SIGAEST - MATA010 - Como bloquear um produto no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003255781-MP-SIGAEST-MATA010-Como-bloquear-um-produto-no-Protheus-)

**Eu preciso saber, quais problemas posso encontrar com a alteração do tipo, como descubro?**

É altamente recomendado, que contatem vosso Gerente de Relacionamento na Totvs e demande um Analista in-loco para analisar seu cenário e efetuar os devidos ajustes dentro do que é possível para sua necessidade, pois esse, poderá efetuar uma avaliação de todo o seu cenário/regra de negócios, e avaliar o impacto para com esse tipo de alteração.

***Sugestão:*** Nesse cenário, é adequado **efetuar a cópia** do produto que precisa alterar o campo B1\_TIPO e no novo produto que foi copiado, ***alterar o campo B1\_TIPO conforme a necessidade***. Feito essa alteração, pela rotina ***TRANSFERÊNCIAS MÚLTIPLAS (MATA261)*** transferir o Saldo diretamente ao novo produto com o tipo desejado. Obs.: Dessa forma mantém a integridade dos dados que foram movimentados anteriormente no código evitando transtornos em entregas Fiscais entre outras.

**Saiba mais:**

*[Clique aqui para mais informações sobre a MATA010](https://tdn.totvs.com/display/public/PROT/Produtos+-+MATA010#ProdutosMATA010-PastaCadastrais)*

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de numeração automática (B1\_COD) via LicenceServer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406595504279-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-numera%C3%A7%C3%A3o-autom%C3%A1tica-B1-COD-via-LicenceServer)*
