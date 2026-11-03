---
article_id: 9799496074391
category: Materiais - Compras (SIGACOM)
content_hash: ed98fbfcb2aecff3df4e6c72ec8b2b77adc4fb10afd2a22f177c7512ed249db6
fetched_at: '2026-06-28T22:41:11.732678+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Qual a funcionalidade
  da opção 'Proposta' na rotina Atualizar Cotações (MATA150) ?
type: support-article
updated_at: '2022-10-26T11:18:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9799496074391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Qual-a-funcionalidade-da-op%C3%A7%C3%A3o-Proposta-na-rotina-Atualizar-Cota%C3%A7%C3%B5es-MATA150
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual a funcionalidade da opção 'Proposta' na rotina Atualizar Cotações (MATA150) ?

![imagem2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9799271255063)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**

Permite incluir novas propostas dos fornecedores participantes da cotação, sem alterar as condições colocadas no primeiro contato (primeira proposta). O objetivo é registrar todas as propostas negociadas entre a empresa e os fornecedores até o fechamento da Cotação.

O registro de todas as propostas é fundamental para avaliar o desempenho do comprador durante a negociação com os fornecedores.

**Procedimentos**

Para registrar uma proposta nova de um fornecedor:

1. Na janela de manutenção da rotina **Atualiza Cotação**, posicione sobre a cotação e o fornecedor que deseja cadastrar uma nova proposta e clique em **Proposta**.

O sistema apresenta a janela **Atualização de Preços da Cotação/Total do Pedido**, destacando os produtos, as quantidades, valor das mercadorias por item e data de validade da cotação.

2. Confirme a tela com o total do pedido para dar continuidade.

Será apresentada a janela **Atualização de Preços da Cotação - Proposta**, dividida em áreas:

* **Cabeçalho**

Nesta área, são informadas: A Condição de pagamento, Contato, Moeda da cotação, etc.

* **Itens**

Nesta área, são informados: Preço unitário, Tabela de preço, Total do item, Taxa de financiamento, Prazo de entrega, Filial de entrega, Alíquota de IPI, TES (tipo de entrada), Alíquota de ICMS, Valor do frete, Valor da embalagem, Data de validade, Valor do desconto, Valor do seguro, Valor da Despesa, Valor IPI, Valor ICMS, Base de IPI, Base de ICMS, Percentual de desconto, Quantidade de orçamentos, etc.

* **Rodapé**

Esta área é subdividida em pastas:

* Totais (valores totais da cotação atualizada, tais como: valor das mercadorias, valor do IPI, descontos, valor do ICMS, frete + despesas, valor do ICMS retido, total do pedido, etc.)
* Informações do Fornecedor (dados cadastrais dos fornecedor que participa da cotação, tais como: nome, telefone, endereço, estado, primeira compra, última compra, CNPJ/CPF, etc.)
* Frete/Despesas (dados relacionados ao frete e outras despesas, tais como: tipo de frete, valor do frete, despesas, seguro, total (frete + despesas), etc.)
* Descontos (descontos comerciais concedidos pelos fornecedores que podem ser em percentual ou em valor).
* Impostos (informações relacionadas aos tributos que incidem sobre a cotação).
* Mensagem/Reajuste (fórmulas para mensagens padrões ou para reajustes da cotação a serem aplicados na entrada da nota fiscal, se necessário).

3. Na área **Cabeçalho**, preencha os dados conforme orientação do help de campo.

4. Posicione na área **Itens**, informe os preços e as condições da nova proposta do fornecedor.

5. Preencha os dados conforme orientação do help de campo.

6. Observe, porém, os campos:

* **Proposta**- Verifique o número da nova proposta gravada para o fornecedor.
* **Taxa de Financiamento**- Neste campo informe a taxa de financiamento praticada pelo fornecedor quando a condição de pagamento for a prazo.

Se esta não for informada é considerado a taxa configurada no parâmetro MV\_JUROS (Taxa informada para calcular o valor presente das cotações de compra). A taxa de financiamento é utilizada para calcular o valor presente das cotações de compra.

7. Na área **Rodapé**, verifique os totais da cotação e os dados cadastrais do fornecedor. E se necessário informe: Valor do frete e Outras despesas, Descontos comerciais, Incidência de outros tributos, Mensagens padrões para os documentos de entrada ou Fórmulas para reajuste da Cotação.

8. Confirme a inclusão da nova proposta do fornecedor.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
