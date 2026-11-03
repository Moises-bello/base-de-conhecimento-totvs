---
content_hash: cd529c70b548ec2ac7aa61f48152e8027a320d5b68d7672785ef8ee00969cc3b
fetched_at: '2026-06-29T00:09:47.741680+00:00'
page_id: '435105058'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Aluguel - Contrato de Locação - Comissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105058
version: 9
---

Esta parte do sistema trata as comissões a serem geridas para os contratos de aluguéis. O tratamento das comissões para aluguéis é bem similar com as comissões para vendas, pois ocorre a geração de um movimento de comissão para TOTVS Gestão de Estoque, Compras e Faturamento ou para o Protheus. Abaixo temos os detalhes da tela.

**Aba Identificação**

* **Contrato locação:** Campo usado para selecionar o Contrato de Locação em questão.
* **Situação comissão:** Este campo mostra a situação da comissão.
* **Código corretor:** Este campo é usado para selecionar o corretor que está anexado ao contrato de locação que foi selecionado. Um contrato de aluguel pode ter vários corretores.
* **Fórmula:** Fórmula que irá calcular o valor da comissão.
* **Valor total da comissão:** Campo que mostra o valor total da comissão.
* **Memória de cálculo:** Memória de cálculo mostra como se chegou no valor encontrado.

**Aba Integração**  
Esta aba precisa ser preenchida com informações cadastradas no sistema TOTVS Gestão de Estoque.

* **Movimento:** Campo usado para exibir o número do movimento gerado.
* **Tipo de Movimento:** Campo usado para selecionar o Tipo de Movimento criado no **TOTVS Gestão de Estoque, Compras e Faturamento** ou no **Protheus**, um tipo de movimento que seja apropriado para os casos de comissão do **TOTVS Incorporação**. Este tipo de movimento pode ser cadastrado como Outras Movimentações.
* **Produto:** Produto ou serviço a ser usado para a comissão de Aluguéis do **TOTVS Incorporação**. É indicado criar no **TOTVS Gestão de Estoque, Compras e Faturamento** um Serviço apropriado para os casos de comissão do **TOTVS Incorporação**.
* **Filial:** Filial da comissão, que será preenchida no Movimento criado.
* **Centro de Custo:** Centro de custo da comissão, que será preenchido no Movimento criado.
* **Histórico do Movimento:** Histórico do movimento gerado.

Atenção

O sistema somente permite salvar o registro quando o contrato de locação, o tipo do movimento e o produto/serviço estiverem configurados na mesma coligada.

Exemplo Básico de Fórmula de Comissão do Aluguelvb

**Aba Campos Complementares**

Esta aba é utilizada por campos complementares. Estes campos complementares são inseridos acessando Aluguel > Campos Complementares > Comissão.

Como Fazer

---
