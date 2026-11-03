---
article_id: 23642634053271
category: SIGAEST - MOVIMENTAÇÕES
content_hash: a810cf9dc75dd6ccbf7c4e22060dbd2e60cdb4beda57b6760c6e694e63076701
fetched_at: '2026-06-28T22:38:57.098439+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310 - Saldo em
  branco (sem Armazém) nas Filiais Destino
type: support-article
updated_at: '2025-03-12T12:23:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23642634053271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-Saldo-em-branco-sem-Armaz%C3%A9m-nas-Filiais-Destino
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23642610153623) Tempo aproximado para leitura: **00:03:25 min**

**Dúvida**

Na rotina **Transferência entre Filiais (MATA310)** é possível transferir Saldo entre as Filiais sem que tenha incluido um Saldo Inicial (MATA220) na Filial Destino, da mesma forma que o [parâmetro MV\_VLDALMO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020863311-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-criar-saldo-do-produto-no-armaz%C3%A9m-de-destino-na-Transfer%C3%AAncia-de-Produtos) igual a N para as transferências entre Armazéns. Ao tentar efetuar o processo na rotina MATA310 apresenta os dados em branco na Filial Destino como no exemplo do print abaixo.

**![MATA310 PRINT 01.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23642634027543)**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Sim, é possível habilitando o **parâmetro MV\_SB2AUTO para T**. Como esse parâmetro habilitado ao incluir a Transferência entre Filiais com os produtos listados na parametrização inicial é criado o Saldo automaticamente no Armazém Padrão (B1\_LOCPAD) do cadastro do Produto.

![MATA310 PRINT 02 PARAME.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23643092103319)

![MATA310 PRINT 03.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23643544691223)

|  |
| --- |
| **Observações importantes: Avaliar a regra de negócio em cada empresa se tem necessidade de utilizar os produtos em todas as Filiais. Com esse parâmetro habilitado passa a enxergar os produtos em todas as Filiais no momento da Transferência.** |

***Saiba Mais:***

*[MATA310 / MATA311 - Como configurar a Transferência entre Filiais (MATA310 / MATA311) no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-a-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus)*

*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
