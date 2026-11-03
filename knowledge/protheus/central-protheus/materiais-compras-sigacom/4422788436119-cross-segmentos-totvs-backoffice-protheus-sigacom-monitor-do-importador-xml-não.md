---
article_id: 4422788436119
category: Materiais - Compras (SIGACOM)
content_hash: 0218f5573888b2dcbd5713367c2d25a1e9120d73b0d0cc3cdae1f216206f5232
fetched_at: '2026-06-28T22:41:20.209796+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Monitor do Importador
  XML - Não permite alterar ou bloquear documento de CTe importado
type: support-article
updated_at: '2024-06-11T12:28:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422788436119-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Monitor-do-Importador-XML-N%C3%A3o-permite-alterar-ou-bloquear-documento-de-CTe-importado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23215637967255) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

No Monitor do Importador XML, ao clicar em 'Alterar' em um documento de CTe importado, ocorre uma mensagem que não permite a alteração:

**Esta ação pode ser executada apenas para documentos do tipo Normal, Devolução, Complemento ou CT-e referente a envio de mercadoria**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4422774536343)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões

**Solução**

Ao realizar uma importação de frete no Importador XML ou no Totvs Colaboração, a rotina do monitor pode ou não exibir uma mensagem de impedimento de alteração no XML de CTe, dependendo se o CTe é do tipo FOB ou CIF.

* **Frete tipo C-CIF:** Neste caso, o remetente é a própria mercadoria, permitindo a alteração do documento importado, pois pode ser necessário vincular um pedido de compra ao CTe.
* **Frete tipo F-FOB:** Neste caso, o remetente não é a mercadoria, não havendo pedido a ser vinculado, portanto, a alteração do documento importado não é permitida.

O sistema realiza a seguinte validação:

* Se o ***DS\_TIPO*** for 'T' e o ***DS\_TPFRETE*** for 'C', a variável ***lRemet*** é atribuída como verdadeira (.T.).
* Se a variável ***lRemet*** é falsa (conforme a regra acima), a mensagem de impedimento de alteração será exibida.

***Obs:***

Este é um comportamento conceitual, não havendo alternativas configuráveis que possibilitem alteração deste tipo de documento importado na rotina do Monitor. Caso, considere imprescindível à sua organização a alteração da regra padrão, recomendamos avaliar a viabilidade de implementar sua regra customizada, alterando as informações da tabela SDS / SDT, através do ponto de entrada [***MT116XMLCT***](https://tdn.totvs.com/pages/releaseview.action?pageId=243012688) ou outros que avalie adequados à necessidade ([Pontos de Entrada Importador XML](https://tdn.totvs.com/display/PROT/IX02+-+Pontos+de+Entrada)).  
  
Confira também as demais [alternativas para adaptar o Produto padrão às regras pontuais de sua Organização](https://tdn.totvs.com/x/R1gjIw)

***Saiba Mais:***

*[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Integração Importador XML x TOTVS Transmite](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7557934491159-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Integra%C3%A7%C3%A3o-Importador-XML-x-TOTVS-Transmite)*

[TC02022 - MT116XMLCT Ponto utilizado na importação do XML da NF Eletrônica](https://tdn.totvs.com/pages/releaseview.action?pageId=243012688)

[IX02 - Pontos de Entrada Importador XML](https://tdn.totvs.com/display/PROT/IX02+-+Pontos+de+Entrada)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
