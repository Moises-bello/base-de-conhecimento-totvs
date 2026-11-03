---
article_id: 360013969291
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 14a99a05e5c65de7d449888ff4b75bc0953ab41e74ebae39967aec1409191314
fetched_at: '2026-06-28T22:40:32.422938+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como alterar o histórico
  de estorno de Lançamento Contábil
type: support-article
updated_at: '2024-04-05T14:57:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013969291-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-alterar-o-hist%C3%B3rico-de-estorno-de-Lan%C3%A7amento-Cont%C3%A1bil
---

**Dúvida**Como alterar o histórico de estorno de Lançamento Contábil?  
  
**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus  – Contabilidade Gerencial – A partir da versão 11.80 **Solução**

No processo padrão da rotina (CTBA102) Lançamentos Contábeis Automáticos, no Botão Outras opções, em estorno de lançamento contábil, a informação gravada no Histórico deste lançamento de estorno é: "a palavra "ESTORNO" + Dados do lançamento estornado (DATA+LOTE+SUB-LOTE+DOCUMENTO+LINHA)

No padrão, para alterar o histórico de um lançamento de estorno, precisa liberar a alteração de lançamentos desse tipo, pois nativamente o sistema vem como bloqueado a alteração de lançamentos de estorno. Para habilitar a edição de lançamentos de estorno deverá deixar o parâmetro **MV\_CTBDEST** igual a 1:

![](https://totvssuporte.zendesk.com/attachments/token/Ot5wsRBBgCXHWg8SSGoB5KeCH/?name=image.png)

Lembrando que ao habilitar o parâmetro o usuário poderá alterar os dados do estorno inclusive o histórico, porém precisa de uma ação do usuário.

Caso o cliente deseje que o processo seja sem interação do usuário não será possível no padrão, somente utilizando ponto de entrada. Abaixo temos uma sugestão de Ponto de Entrada que pode ser utilizado no processo:

<http://tdn.totvs.com/pages/releaseview.action?pageId=6068588>

[DT PE Ct102Carr Manipulação de leitura do TMP CTBA102](https://tdn.totvs.com/pages/releaseview.action?pageId=776111317)
