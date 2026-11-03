---
article_id: 26740861368087
category: Originação de Grãos (OG)
content_hash: f41ba583fe93f6151eb940ea1ae72d121b4276f63b20ab4cccda1c2634767a97
fetched_at: '2026-06-28T22:45:45.192998+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Transferência entre Filiais Comercialização
type: support-article
updated_at: '2024-12-10T20:53:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26740861368087-Agro-Linha-Protheus-AGR-Transfer%C3%AAncia-entre-Filiais-Comercializa%C3%A7%C3%A3o
---

Para esta operação será gerada uma nota fiscal de saída/transferência na filial de origem, e ao chegar na filial de destino será recebida esta nota fiscal.  
  
**Há duas formas de proceder com esta operação no módulo SIGAAGR:**

1. Através do **Romaneio com Pesagem OGA250**
2. Através do **Romaneio sem Pesagem OGA251**  
     
   **Para utilizar através das funções OGA250/OGA251** **é necessário:**

* Registrar um **Contrato de Vendas**, através da função **OGA290** na filial de origem, sendo que a entidade cliente do contrato será a entidade correspondente a filial de destino.
* No **contrato de Vendas**, informar **TES** de saída transferência entre filiais, e demais  configurações fiscais necessárias para a operação.
* Registrar um **Contrato de Compras**, através da função **OGA280** na filial de destino, sendo que a entidade fornecedor do contrato será a entidade correspondente a filial de origem.
* No **contrato de Compra**s, informar **TES** de entrada transferência entre filiais, e demais  configurações fiscais necessárias para a operação.
* Para a saída, na filial de origem criar romaneio **OGA250/OGA251**, informando o tipo **4,** **S - Saída por Venda**, informar contrato de vendas, pesagem e classificação. Atualizar e confirmar para gerar a nota fiscal da transferência.
* Para a entrada, na filial de destino criar romaneio **OGA250/OGA251**, informando o tipo **5, E** - **Entrada por Compra**, informar contrato de compras, pesagem e classificação, bem como as informações da **nota fiscal** recebida. Atualizar e confirmar para efetuar o recebimento da **nota fiscal** no destino.

**NOTA**: Os tipos de romaneio **B, S** Saída por Transferência e **A** **E** Entrada por Transferência ainda não estão liberados para serem utilizados através das funções **OGA250/OGA251**. Foi iniciado um estudo, pela área de produto, para permitir uma nova forma de executar a transferência, sem a utilização de contratos, através da criação de tipos de operação **AGRA510**, onde estes tipos de romaneios **A** e **B** serão utilizados. Foi iniciado um protótipo, ainda não homologado, para transferir através do **Romaneio Unificado AGRA500**, porém o desenvolvimento não foi concluído e direcionamos o estudo para o **OGA250/OGA251**. Quando esta implementação estiver disponível esta **FAQ** será atualizada, bem como o documento técnico do desenvolvimento está disponível na expedição da **release/patch** no **tdn**.
