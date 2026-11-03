---
article_id: 33172768314775
category: Materiais - Compras (SIGACOM)
content_hash: 7b489708c0bc73cbdc82920fcaf25d9fefe17ca7ccd8faa8977b9169b26bae39
fetched_at: '2026-06-28T22:41:08.976952+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Integração do PCO com
  o Novo Fluxo de Compras (PGCA010)
type: support-article
updated_at: '2025-10-23T19:20:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33172768314775-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Integra%C3%A7%C3%A3o-do-PCO-com-o-Novo-Fluxo-de-Compras-PGCA010
---

**Dúvida:**  
Como realizar a integração do PCO com o Novo Fluxo de Compras (PGCA010)?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2210.  
  
**Solução:**  
Para que a integração do Novo Fluxo de Compras com o PCO funcione **é fundamental** que aplique o pacote de **Expedição Contínua do Backoffice**. Pois apenas a versão mais atualizada está preparada para realizar a integração.

Por gentileza realize teste em ambiente de Homologação com as atualizações a seguir:  
- [Acumulado Compras conforme sua versão](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)  
Obs: Recomendamos backup e validação primeiramente em ambiente teste.

Para que a integração com o **PCO** funcione corretamente, é **necessário configurar o campo "Valor Lancto"** das rotinas **PCOA030 e PCOA035**com um dos campos abaixo, porém pode-se utilizar outros campos ou regras conforme a necessidade:

* + **SC8->C8\_TOTPCO:** Para **lançamento ou bloqueio** com base no **valor total da cotação;**
  + **SC8->C8\_ITEMPCO:**Para **lançamento ou bloqueio** com base no **valor total de cada item da cotação;**

Essa configuração é essencial para o funcionamento do **bloqueio de contingência** (Exemplo: PCOA035, **lançamento 000052**, **item 2**) e será responsável por **enviar o valor da solicitação** ao pressionar o botão **Salvar**.

**Exemplo de configuração na rotina PCOA030, campo SC8->C8\_TOTPCO:**

![](https://tdn.totvs.com.br/download/attachments/680260500/image-2025-9-15_18-37-29.png?version=1&modificationDate=1757972250060&api=v2)

**Exemplo de configuração na rotina PCOA030, campo SC8->C8\_ITEMPCO:**

![](https://tdn.totvs.com.br/download/attachments/680260500/image-2025-9-15_18-40-10.png?version=1&modificationDate=1757972410927&api=v2)

**Exemplo de configuração na rotina PCOA035, campo SC8->C8\_TOTPCO:**

![](https://tdn.totvs.com.br/download/attachments/680260500/image-2025-9-15_18-45-5.png?version=1&modificationDate=1757972705897&api=v2)

**Exemplo de configuração na rotina PCOA035, campo SC8->C8\_ITEMPCO:**

![](https://tdn.totvs.com.br/download/attachments/680260500/image-2025-9-15_18-48-47.png?version=1&modificationDate=1757972927747&api=v2)

**Importante:**

* + **O bloqueio sempre será realizado no passo final da geração do pedido de compra.**
  + **Para realizar bloqueio por item, realize o cadastro do campo C8\_ITEMPCO no Configurador (SIGACFG) conforme as orientações abaixo:**
* + - **Aba Campo:**
      * **Campo:** C8\_ITEMPCO
      * **Tipo:** 2 - Numérico
      * **Tamanho:**14
      * **Decimal:** 2
      * **Contexto:** 1 - Real
      * **Propriedade:** 2 - Visualizar
    - **Aba Informações:**
      * **Tít. Português:**Vl Item PCO
      * **Tít. Espanhol:** Vl Item PCO
      * **Tít. Inglês:**PCO Item Vl
      * **Desc. Português:**Vl Contingencia PCO
      * **Tít. Espanhol:**Vl Contingencia PCO
      * **Desc. Inglês:**PCO Contingency Vl
      * **Help:**Valor de contingência do item para  
        integração com o PCO.
    - **Aba Uso:**
      * **Usado:**Ativado

**Observação**

Para o processo de PCO com a cotação temos os lançamentos e bloqueios abaixo:

Processo 000051 item 03 - SOLICITACAO DE COMPRAS - RATEIO POR CC NA COTAÇÃO

Processo 000052 item 02 - PEDIDO DE COMPRAS - INCLUSAO DE PEDIDO DE COMPRAS POR COTAÇÃO

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
