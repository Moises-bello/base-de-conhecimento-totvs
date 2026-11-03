---
article_id: 360017977212
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 86b114c172e07c710091ab3de4dcc633221ad6ba793b43b7155517a92e9aabb6
fetched_at: '2026-06-28T22:38:31.012524+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP - FAT - CAMPO ADA_FILENTR  NO CONTRATO DE PARCERIA '
type: support-article
updated_at: '2021-04-28T15:55:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017977212-MP-FAT-CAMPO-ADA-FILENTR-NO-CONTRATO-DE-PARCERIA
---

**Dúvida**

Uso do campo Filial Entrega **ADA\_FILENTR** no contrato de parceria.

**Ambiente**

Microsiga Protheus - a partir da versão 11.80  
  
**Solução**

O Protheus não permiti utilizar o campo Filial Entrega **ADA\_FILENTR** no Contrato de Parceria **FATA400** quando informado Filial diferente da Filial corrente.

Para uso do campo Filial Entrega **ADA\_FILENTR** com Filial diferente da Filial corrente é necessário que as tabelas abaixo estejam Compartilhadas:

* **ADA** - Contrato de Parceria;
* **SE4** - Condições de Pagamento;
* **SF4** - Tipos de Entrada / Saída;
* **DA0** - Tabelas de Preço;
* **SB1** - Descrição Generica do Produto;
* **SBM** - Grupo de Produto.

**ADB** - Itens do Contrato de Parceria  
Caso já tenha registros, deve ser avaliado para Compartilhar essa Tabela ou aumentar a numeração afim de utilizar a partir de uma numeração que não exista registros com a numeração.

**Obs**. Atentar para registros já existentes na base.  
Ressaltamos que realizar manutenção em base via **APSDU** afim de atualizar o campo da Filial, pode impactar em outras rotinas onde os registros já foram utilizados.

![contrato_de_parceria.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013465351/contrato_de_parceria.png)

Segue o link das legendas do pedido de venda para auxilio.

**Saiba mais:**

[Legendas exibidas na rotina MATA410 - Pedido de Vendas](http://tdn.totvs.com/display/public/PROT/FAT0121_Legendas_Status_do_Pedido_de_Vendas)
