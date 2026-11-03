---
article_id: 1500011935502
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 72dce3e9791fc146c9ec53d61c15167c1cd919629265357317207722a70421e3
fetched_at: '2026-06-28T22:38:54.065371+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA261 - Transferência
  Múltipla de Produtos
type: support-article
updated_at: '2026-02-20T16:41:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011935502-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA261-Transfer%C3%AAncia-M%C3%BAltipla-de-Produtos
---

A rotina Transferência Múltipla (MATA261) do TOTVS Protheus permite transferir saldos entre armazéns, códigos de produtos diferentes, lotes e endereços, desde que o produto controle localização. É possível transferir múltiplos produtos simultaneamente, mas não por armazém inteiro. Customizações podem bloquear transferências entre produtos distintos via ponto de entrada A261TOK.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28944980319639)** Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Qual a função da rotina de Transferencias Múltiplas (MATA261)? Como efetuar o processo de Transferencias?É possível realizar a transferencia de Saldos entre produtos com códigos diferentes?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

A rotina **Transferência Múltipla (MATA261)** permite ao usuário transferir Saldo dos Produtos com as seguintes opções padrões: 

 - Transferência de Saldos **entre Armazéns;**

 - Transferência de Saldos de **um Código de Produto para outro Código Produto;**

**-** Transferência de Saldos de um **Lote para outro Lote de determinado Código de produto ou mesmo para Códigos de Produtos diferentes;**

**-** Transferência de Saldos entre **Endereços quando Produto controla Localização (B1\_LOCALIZ=S)**

**Exemplo prático abaixo efetuando a Transferência entre Armazéns**

**- Vídeo com exemplo na prática:** [**How To | SIGAEST – Transferências entre Armazéns (MATA261)**](https://www.youtube.com/watch?v=-C05diWV9D4)

Exemplo passo a passo teremos o seguinte cenário:

|  |  |  |
| --- | --- | --- |
| **Produto** | **Armazém** | **Quantidade** |
| PA99 | 01 | 250 |
| PA99 | 02 | 0 |
| PA100 | 01 | 0 |
| PA101 | 01 | 0 |

**Transferindo saldo do produto entre Armazéns**

Vamos transferir 50 itens do PA99 do armazém 01 ao armazém 02.

![Transferencia_entre_armazens.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019200902)

**Com isso, veja como nosso saldo do PA99 passou a ser 200 itens no Armazém 01 e 50 itens no Armazém 02:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019443501)

**Transferindo saldo do PA99 para os produtos PA100 e PA101**

Nesta rotina podemos fazer uma ou mais transferências. Neste caso vamos fazer, de uma só vez, a transferência de:

- 10 itens do PA99 para o PA100;

- 20 itens do PA99 para o PA101.

![transferencia_entre_produtos_diferentes.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019201062)

**Com isso, teremos: Saldo de 10 itens no PA100:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019201122)

**Saldo de 20 itens no PA101:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019443901)

**Saldo de 170 no PA99 (e armazém 01):**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019443961)

**Lembrando que na rotina pode ser transferido saldo com critérios de Lote e Endereço também (caso tenha produtos com estes controles), bastando, no momento da transferência, delegar qual o Lote/Endereço Origem e Lote/Endereço destino.**

## **Eu consigo transferir os saldos por "armazem" ao invés de "produto a produto"?**

Atualmente no padrão, essa funcionalidade não existe, a transferencia multipla, funciona apenas de produto para produto.

## 

## **Como bloquear a transferencia multipla entre produtos distintos**

No padrão para essa rotina não tem essa funcionalidade, mas é possível customizar com o Ponto de Entrada A261TOK conforme sua necesidade, verificar com seu Analista Desenvolvedor e implementar conforme sua necessidade específica. Segue abaixo link do PE.  
   
**PONTO DE ENTRADA A261TOK - Valida movimento de transferência**  
[***https://tdn.totvs.com/x/iUh7K***](https://tdn.totvs.com/x/iUh7K)

**Possa interessar:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA261 - Pontos de Entrada da rotina Transferência Múltipla](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004779102-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA261-Pontos-de-Entrada-da-rotina-Transfer%C3%AAncia-M%C3%BAltipla)

**Saiba mais:**

[SIGAEST - É possível criar saldo do produto no armazém de destino na Transferência de Produtos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020863311-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-criar-saldo-do-produto-no-armaz%C3%A9m-de-destino-na-Transfer%C3%AAncia-de-Produtos)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
