---
article_id: 360050279993
category: Materiais - Compras (SIGACOM)
content_hash: b37a4aca98d9a4d8e015ef931a08bf4e895c731c24f9bff2c10baf598fcab6e8
fetched_at: '2026-06-28T22:41:24.391048+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Retorno de beneficiamento
  com vínculo  e baixa automática da OP no documento de entrada
type: support-article
updated_at: '2022-05-18T21:22:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050279993-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Retorno-de-beneficiamento-com-v%C3%ADnculo-e-baixa-autom%C3%A1tica-da-OP-no-documento-de-entrada
---

**Dúvida**

Retorno de beneficiamento com vínculo e baixa automática da OP no documento de entrada  
  
**Ambiente**

Protheus - Compras - A partir da versão 12  
  
**Solução**  
O processo tem início na remessa efetuada pelo módulo de faturamento conforme documentação a seguir :

* ### [FAT0293 Ordem de Produção x Pedido de Vendas](https://tdn.totvs.com/pages/releaseview.action?pageId=527855201)

Após o processo de remessa quando o beneficiamento retorna, a entrada deverá ser efetuada na rotina  - Documento de Entrada (**MATA103**).

Ajustar os parâmetros pelo Configurador, através do caminho a seguir :

Configurador -> Ambiente -> Cadastros -> Parâmetros, filtre :

* **MV\_PRNFBEN**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075447913/mceclip3.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074282454/mceclip2.png)

*\* Ao habilitar o parâmetro é disponibilizada a opção Retorno Ben dentro do botão Outras Ações no Documento de Entrada*

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074285094/mceclip4.png)

* **MV\_TMPAD**

*![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074286034/mceclip5.png)*

***\***Nele deve ser preenchido o código de um TM (Tipo de  Movimentação) que será utilizado para efetuar a baixa da OP automaticamente na entrada do retorno de beneficiamento. Importante : o Tipo da TM ser produção.*

Para acessar o cadastro de tipo de movimentação, siga o caminho abaixo :

Estoque/Custos -> Atualizações -> Cadastros -> Movimentações ->Internas (**MATA230***)*

*![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075451153/mceclip6.png)*

Ao acessar a rotina de documento de entrada, preencher os dados do cabeçalho normalmente.

Tipo da Nota: Normal e preencher as demais informações.

No item clicar em outras ações, na opção *Retorno ben*

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074286654/mceclip7.png)

O sistema apresentará a tela a seguir:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074286874/mceclip8.png)

Informe o número da OP e o TES (**F4\_PODER3** = D-Devolução e **F4\_ESTOQUE**=S – Sim).

Em seguida clique em OK.

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074287114/mceclip9.png)

O sistema atualizará o item com as informações referente a remessa(saída) e preencherá os campos **D1\_OP** e **D1\_ORIGEM** e a série da Origem.

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075452353/mceclip10.png)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074287214/mceclip11.png)

Caso na mesma nota de retorno haja o serviço sendo cobrado, esse item também poderá ser informado manualmente na linha abaixo:

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075452613/mceclip12.png)

O TES utilizado para a inclusão do produto serviço somente deverá gerar financeiro e não movimentar estoque. Assim o sistema gerará o título a pagar somente do valor do serviço cobrado.

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075452653/mceclip13.png)

Ao salvar a nota, o sistema efetua a baixa automática da OP vinculada.

Estoque/Custos -> Atualizações -> Cadastros -> Movimentações ->internas -> Produção -> Ordens de Produção (**MATA650**)

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074287794/mceclip14.png)

Conheça nosso PDF sobre Documento de Entrada na página Centralizadora de Compras!

Na página 22 consta a informação relacionada ao Retorno de Beneficiamento. Clique na imagem abaixo para acessar.

[![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077441073/mceclip0.png)](https://tdn.totvs.com/display/public/PROT/DOCUMENTO+DE+ENTRADA+GERAL)
