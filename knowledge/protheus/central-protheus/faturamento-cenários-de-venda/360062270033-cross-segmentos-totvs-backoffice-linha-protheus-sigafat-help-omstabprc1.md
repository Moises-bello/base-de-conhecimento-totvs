---
article_id: 360062270033
category: Faturamento - Cenários de Venda
content_hash: da422a63ab9dc2019040e88231e5ff0f2166612da0eedeb175a792f857bde4cc
fetched_at: '2026-06-28T22:38:34.065750+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help OMSTABPRC1
type: support-article
updated_at: '2023-01-02T19:35:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062270033-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-OMSTABPRC1
---

**Ocorrência**Ao incluir o pedido de vendas gera o help **OMSTABPRC1**, como solucionar?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento - A partir da versão 11.80  
  
**Causa**Esta mensagem indica que foi informada uma **tabela de preço** no **Pedido de Vendas (MATA410) seja inclusão direta ou efetivação de um orçamento** e a vigência da tabela utilizada esta fora de um prazo válido, sendo necessário ajustar para incluir/alterar o pedido.  
  
**Solução**

Avalie se a **DATABASE** (data informada no sistema, canto superior direito) está entre o intervalo da Tabela de Preços (**OMSA010**), mencionado nos campos Data Inicial "Data Inicial [**DA0\_DATDE]**" e "Data Final [**DA0\_DATATE]**", ambos campos no cabeçalho da rotina.

1 - Para não perda do histórico, é necessário criar uma nova tabela de preços com os campos **DA0\_DATDE** e **DA0\_DATATE** válidos para o dia do ambiente (dia atual).

2 - Caso o histórico da tabela de preços não seja importante, basta mudar os campos **DA0\_DATDE** e **DA0\_DATATE** para uma nova data válida que esteja suportando o dia atual do sistema.

3 - Alterar a data do sistema (DATABASE) para uma data válida entre a data dos campos **DA0\_DATDE** e **DA0\_DATATE.**

**Saiba Mais:**  
Caso apresente o help **OMSTABPRC2** realize o procedimento da documentação:  
[Help OMSTABPRC2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001965222)
