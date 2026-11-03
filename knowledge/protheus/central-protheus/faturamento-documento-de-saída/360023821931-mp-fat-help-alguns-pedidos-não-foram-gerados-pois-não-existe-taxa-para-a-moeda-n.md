---
article_id: 360023821931
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 1bb539e252243949a29f6fe0921617dbd9feb2b456c42f45b817018bf83c5926
fetched_at: '2026-06-28T22:38:45.176103+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP - FAT - Help Alguns pedidos não foram gerados pois não existe taxa para
  a moeda na data
type: support-article
updated_at: '2021-04-28T15:13:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023821931-MP-FAT-Help-Alguns-pedidos-n%C3%A3o-foram-gerados-pois-n%C3%A3o-existe-taxa-para-a-moeda-na-data
---

**Dúvida**

Help Alguns pedidos não foram gerados pois não existe taxa para a moeda na data.  
  
**Ambiente**

Microsiga Protheus –  A partir da versão 11.80.  
  
**Solução**

O sistema apresenta esta mensagem, devido a algumas configurações não realizadas:

1° Esse incidente pode ocorrer quando o campo **C9\_PRCVEN** consta em **Branco,**devido às casas decimais dos campos **C6\_PRCVEN, D2\_PRCVEN, D1\_VUNIT**estarem divergentes.

2° Quando o cadastro de Moeda (MATA090) não estiver preenchido para a data de Faturamento na nota;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003807481/mceclip0.png)

3°Quando ao faturar, para utilizar a taxa de moeda de outro dia, diferente do dia da Preparação do documento (DATABASE),  não há registro da data na pergunta "Dt. Ref. Conversão?" Contida na janela de parâmetros disponibilizada ao acionar a Preparação do Documento de saída ou não foi configurado a moeda para conversão na data descrita. *Se não preencher o campo, será considerada a DATABASE.*  
OBS: Conforme help do parâmetro, essa opção é válida somente caso utilize moeda diferente de 1 (Moeda Forte) no Pedido.

Se utilizar Moeda 1, será levado para a Nota o valor gravado no Pedido de Vendas.

OBS: Avaliar no cadastro de Moeda (**MATA090**), se a data definida no "Dt. Ref. Conversão?" esta com a conversar cadastrada e correta.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003757562/mceclip1.png)

Ajuste os campos, com o número de casas decimais que o cliente utiliza. Para auxilio na alteração da casa decimal verificar link abaixo.

**Saiba mais com as documentações relacionadas ao uso de moeda no faturamento e aumento de casas decimais :**  
**[Aumento de Casa Decimal](http://tdn.totvs.com/display/public/PROT/FAT0068_Aumento_de_Casas_Decimais_no_ambiente_Faturamento_SIGAFAT)**

**[MP-FAT-Uso Moeda Modulo Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000731448-MP-FAT-Uso-Moeda-Modulo-Faturamento)**
