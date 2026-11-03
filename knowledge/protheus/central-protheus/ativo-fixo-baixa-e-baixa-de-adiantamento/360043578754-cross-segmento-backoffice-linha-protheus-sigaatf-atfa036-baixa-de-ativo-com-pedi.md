---
article_id: 360043578754
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: de2d194e6e4ba9448b22681d92e873bff520cd5ddd8122befbe243efc43c7692
fetched_at: '2026-06-28T22:41:55.509759+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA036 - Baixa de Ativo
  com Pedido de Venda
type: support-article
updated_at: '2023-11-20T16:16:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043578754-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-Baixa-de-Ativo-com-Pedido-de-Venda
---

**Dúvida**Como realizar uma Baixa de Ativo que gere um Pedido de Venda?  
  
**Ambiente**Protheus - Ativo Fixo - A partir da release 12.1.23  
  
**Solução**A partir da data **04/02/2020** a rotina de **Baixa de Ativo(ATFA036)** passou por uma melhoria referente ao processo de Venda, agora a rotina gerará além do Documento de Saída, também o Pedido de Venda, a ideia é que a partir do momento de Baixa, seja validado as mesmas questões de um Pedido de Venda, exemplo, o Saldo do Produto em Estoque, Limite de Crédito do Cliente.

Para usar a funcionalidade siga os passos abaixo:

1- Primeiramente, será necessário configurar os parâmetros conforme abaixo:

**-****MV\_ATFGRPV**(Este parâmetro tem como objetivo habilitar a funcionalidade) **= .T.**

**OBS:**Para as releases anteriores a **12.1.27** será necessário a criação do parâmetro via configurador, conforme a documentação: [Processo de baixa com geração de NF](https://tdn.totvs.com/pages/releaseview.action?pageId=533736504)

Além disso, com a geração do pedido de vendas, o sistema passa a obedecer também a regra do parâmetro **MV\_1DUPNAT**. Segue a documentação sobre o parâmetro: [Clique Aqui para a documentação do MV\_1DUPNAT](https://tdn.totvs.com/display/PROT/FAT0038_A410NATVZO_A410NATUSO_A410NATCLI_A410NATPED_Cadastro_Natureza_MV_1DUPNAT)

Se estiver parametrizado para utilizar a natureza do pedido de vendas, o sistema respeitará o conteúdo informada no campo "Natureza (**FN6\_NATURE**)" da rotina de baixas. Exemplo:

**-MV\_1DUPNAT = SC5->C5\_NATUREZ**

2- Após a configuração dos parâmetros, verifique se o cliente a ser informado na baixa possui crédito de compra através dos campos **A1\_RISCO** e **A1\_LC,**pode ser visto através da rotina **MATA030.** Documentação:[Configuração de Bloqueio e Limite de Crédito](https://tdn.totvs.com/pages/viewpage.action?pageId=225950030)

3- Além do cliente, também será verificado o Saldo em Estoque do Produto que está vinculado ao bem, a validação do sistema será feita nas tabelas **SB2, SBF e SB8**(essas ultimas duas se o produto controlar lote e localização), portanto veja se há quantidade e saldo disponível para venda através do módulo de Estoque. Documentação: [Liberação Pedido de Venda](https://tdn.totvs.com/pages/viewpage.action?pageId=330839110)

4- Na rotina de Baixa o processo é o mesmo, neste caso, posicione no bem e baixe-o de uma forma que gere a Nota de Saída, segue exemplo:

Aba Dados da Baixa:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059617993)

Aba Dados da NF:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059618073)
