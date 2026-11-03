---
article_id: 360006823411
category: Materiais - Compras (SIGACOM)
content_hash: 2168a190ecd60585c2718a2158385082bf6b0596725ab1bd326cc7cbaf5440a2
fetched_at: '2026-06-28T22:41:07.371408+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  Como configurar a
  Alçada por item de pedido e entidade contábil ?
type: support-article
updated_at: '2026-05-20T16:47:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823411-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-a-Al%C3%A7ada-por-item-de-pedido-e-entidade-cont%C3%A1bil
---

**Dúvida**  
Como configurar a Alçada por item de Pedido de Compras e Entidade Contábil?  
  
**Ambiente**  
Protheus – Compras – A partir da versão 12.17  
  
**Solução**

Assistam nosso vídeo com a configuração com o passo a passo.

How To | MP-SIGACOM Alçada Por EC Para IP Na Prática #TOTVS Backoffice (linha Protheus)

<https://www.youtube.com/watch?v=9-CqjYnCQx0>

Webinar | Tira dúvidas - Fluxo de alçadas (PC x IP) #TOTVS\_Backoffice\_Linha\_Protheus:

[Webinar | Tira dúvidas - Fluxo de alçadas (PC x IP)](https://www.youtube.com/watch?v=tktv4rmQwbI)

**Alçada por item de pedido e entidade contábil**

Configurações obrigatórias:

- Parâmetro ***MV\_APRPCEC=T*** (Habilitar Alçada por Entidade Contabil) e ***MV\_ALTPDOC=T*** (Habilitar Aba "Tipos de Documentos" do Grupo de Aprovação)

- Cadastro de aprovadores rotina MATA095 informação do valor disponível para aprovação e se diário, semanal ou mensal e moeda.

- Cadastro do perfil de aprovação rotina COMA210 informar range de aprovação para o bloqueio do pedido, valor mínimo e máximo e a moeda.

- Cadastro do Grupo de aprovação  rotina MATA114  na Aba "Cadastrais" informar o(s) aprovador(es) que participarão do grupo, nível, tipo de aprovador se é apenas um vistador ou aprovador, limite automático se sim ira validar o range informado no perfil de aprovação para o bloqueio como não bloqueara qualquer valor, Tipo de liberação Usuário, Nível ou Documento e o perfil de aprovação.

- Na Aba "Tipos de Documentos" flegar a opção Item pedido.

- Na Aba "Entidades Contábeis" informar o centro de custo, conta contábil, classe de valor e/ou item contábil que fará parte de seu grupo para aprovação.

- Incluir o Pedido de Compras com Item informando a(s) mesma(s) Entidade(s) Contabil(s) informada na Aba respectiva do Grupo de Aprovação cadsstrado.

***Obs1:***

Ao incluir o pedido o sistema validara o bloqueio de acordo com os valores definidos no range do perfil de aprovação e deverá conter as informações cadastradas em seu grupo como centro de custo e ou entidade contábil e ou classe de valor e ou item contábil.

***Obs2:***

Estando os pedidos com os dados em que caia em um processo de bloqueio por alçada, qualquer alteração que for feita no pedido, ele retornará para o inicio da alçada, independente da alteração que for realizada, mesmo que apenas se clique em "Alterar" e posteriormente "Salvar" sem realizar nenhuma alteração. Pelo conceito do sistema, não há como se alterar está característica no padrão do sistema.

***Obs3:***

A visualização da tabela SCR mostrará apenas por aprovação mas na opção de LOg de Aprocação do "Outras Ações->Aprovac" da rotina será distribuído por linhas de acordo com a quantidade de aprovadores. Ex.:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411520417047)

Porém na liberação do MATA094 será agrupado os itens por aprovador.

Isso ocorre pois para ativar Entidade Contábil selecionamos "item pedido" no tipo de documento no grupo de aprovação.

Trata-se do funcionamento correto do sistema, pois caso seja diferente a Entidade Contábil de cada item , cada aprovador receberá o seu item para liberar.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411520423703)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411520438423)

***Obs4:***

No uso da alçada de Pedido por Entidades Contábeis, a rotina de Aprovação do Pedido traz em sua Tela Principal apenas as entidades contábeis referente ao processo de alçada, ou seja, traz as entidades contábeis do Grupo de Aprovação de alçada no qual o documento foi envolvido, e não todas as entidades contábeis que foram inseridas no Pedido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39625616580759)

No caso, para se ver todas as entidades contábeis do Pedido, pela rotina de Aprovação de Documentos, a possibilidade existente é através da opção Visualizar->Documento Emitido" da imagem abaixo, estando posicionado do Pedido em questão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39625616583703)

Onde então se visualiza o documento, podendo se ver não somente as entidades contábeis da alçada, mas sim todas as entidades do Pedido, inclusive da opção de Rateio.

**Obs5:**

Existe alguma maneira de configurar o sistema, para que o próximo nível de aprovação, só visualize os documentos para serem aprovados quando todos os itens do pedido forem aprovados?

**R:**O comportamento do sistema para alçada por centro de custo é por item do pedido, não temos nenhum processo no padrão do sistema que só apareça o documento para outro nível somente quando todo os itens do pedido forem aprovados.  
  
Caso queria ver a possibilidade de personalização temos os pontos de entrada abaixo:  
  
MTALCFIM - Permite customizações do usuário para a aprovação ou não de documentos  
[https://tdn.totvs.com/x/0Ntc](https://tdn.totvs.com/x/0Ntc%20)  
  
[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Pontos de Entrada no Controle de Alçadas - MATXALC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053600534-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-Entrada-no-Controle-de-Al%C3%A7adas-MATXALC)  
  
[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Pontos de entrada disponíveis na rotina Liberação de Documentos - MATA094 / MATA097](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006472091-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-entrada-dispon%C3%ADveis-na-rotina-Libera%C3%A7%C3%A3o-de-Documentos-MATA094-MATA097)  
  
Ou caso tenha interesse em falar com o product owner do produto somente através de nossa [**Central Colaborativa TOTVS**](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics) com a sugestão de melhoria.

***Saiba Mais :***

[PCOM09012 - Configuração alçada versão 12.1.14, 12.1.16 e 12.1.17](http://tdn.totvs.com/pages/viewpage.action?pageId=286209197)

[Controle de Alçadas - FAQs](https://tdn.totvs.com/pages/viewpage.action?pageId=270095502)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar o controle de alçada padrão (Sem Entidades Contábeis) ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006822671)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Trilha de Videos Controle de Alçadas no Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9058852149399-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Trilha-de-Videos-Controle-de-Al%C3%A7adas-no-Compras?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
