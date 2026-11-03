---
article_id: 360026656153
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 1e1ee768764541cdc8403c2acee0b6594b1c26a16088e2061e0fc94a716538bf
fetched_at: '2026-06-28T22:38:40.008182+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Qual o tratamento para os
  Campos C5_FRETE e C5_TPFRETE no Pedido de Venda e no Documento de Saída?
type: support-article
updated_at: '2025-02-18T14:16:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026656153-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Qual-o-tratamento-para-os-Campos-C5-FRETE-e-C5-TPFRETE-no-Pedido-de-Venda-e-no-Documento-de-Sa%C3%ADda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30061284428055)** Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**

Qual o tratamento para os Campos **C5\_FRETE** e **C5\_TPFRETE** no Pedido de Venda e no Documento de Saída?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Se for registrado conteúdo nos campos, como o de Frete **C5\_FRETE** no Pedido de Vendas - o qual representa valor - esse valor será somado e destacado na Nota, além de, acrescido no Título a pagar (desde que o TES esteja configurado para gerar duplicata).

Esse comportamento é independe se o Tipo de frete **C5\_TPFRETE** está como CIF ou FOB ou qualquer outra opção.

As opções atualmente disponíveis atendem ao manual da NF-e 4.0 o qual indica que devem ser identificadas no campo Modalidade de Frete (**modFrete do xml**):

**"C"** - (0) - Contratação do Frete por conta do Remetente (CIF);  
**"F"** - (1) - Contratação do Frete por conta do Destinatário (FOB);  
**"T"** - (2) - Contratação do Frete por conta de Terceiros;  
**"R"** - (3) - Transporte Próprio por conta do Remetente;  
**"D"** - (4) - Transporte Próprio por conta do Destinatário;  
**"S"** - (9) - Sem Ocorrência de Transporte (sem cobrança de frete).

**Importante**: O módulo de faturamento não trata cotação de compras, logo para tratativas específicas de frete na rotina de Cotação de Compras, contate a equipe de Protheus Compras para melhor orientação.

Com relação a cotação de vendas, esta opção não é tratada em Faturamento, o frete deverá ser tratado ou via cadastro do cliente para preencher automático o pedido de vendas ou incluído manualmente no pedido de vendas. Caso queira fixar a opção de frete no pedido, basta colocar no inicializador padrão do campo c5\_tpfrete a informação entres aspas, exemplo frete tipo FOB---> "F" e ao abrir o pedido, o sistema já deixará marcado como F.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407919892247)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407919896215)

**Observações:**

- Quando houver mais de um **Pedido de Venda** para o mesmo cliente e for realizada a aglutinação, caso todos os pedidos possuam um valor de frete, o sistema somará os valores do campo **C5\_FRETE** de todos os pedidos, transferindo o total para o campo **F2\_FRETE**.

- Caso o campo **Tipo de Frete (C5\_TPFRETE)** seja preenchido, não será possível deixá-lo em branco posteriormente. Para indicar que não haverá cobrança de frete, é necessário atribuir o valor **"S" - (9) - Sem Ocorrência de Transporte**.

- Para que as **Despesas Acessórias** (frete, seguro e outras despesas) sejam exibidas apenas de forma informativa no DANFE, é necessário registrá-las no campo **C5\_MENNOTA**.

**Saiba mais:**

**[FAT0071\_Informação\_Complementar\_Para\_Nota\_C5\_MENNOTA\_F2\_MENNOTA](http://tdn.totvs.com/pages/viewpage.action?pageId=238028227))**

**[FAT0118\_Frete\_no\_Pedido\_de\_Venda\_C5\_FRETE\_e\_C5\_TPFRETE](http://tdn.totvs.com/display/public/PROT/FAT0118_Frete_no_Pedido_de_Venda_C5_FRETE_e_C5_TPFRETE)**

**Sobre frete:**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Dividir/acumular os valores de FRETE/DESPESAS/SEGURO entre as parcelas do pedido de vendas Artigo da Central de Ajuda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040965714-MP-FAT-Dividir-acumular-os-valores-de-FRETE-DESPESAS-SEGURO-entre-as-parcelas-do-pedido-de-vendas)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como fica o saldo das despesas acessórias (Frete/Seguro/Despesa) na planilha financeira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021542151-MP-FAT-Como-fica-o-saldo-das-despesas-acess%C3%B3rias-Frete-Seguro-Despesa-na-planilha-financeira)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como o sistema realiza o rateio das Despesas Acessórias (Frete/Seguro/Despesa) no Documento de Saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037627993-MP-FAT-Como-o-sistema-realiza-o-rateio-das-Despesas-Acess%C3%B3rias-Frete-Seguro-Despesa-no-Documento-de-Sa%C3%ADda)**

**Sobre cotações de compras:**

**[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Existe como Incluir novos Itens / Produtos em uma Cotação de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009374021-MP-SIGACOM-Existe-como-Incluir-novos-Itens-Produtos-em-uma-Cota%C3%A7%C3%A3o-de-Compras-)**

**[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como informar um Tipo de Frete em uma Cotação de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408064931991)**
