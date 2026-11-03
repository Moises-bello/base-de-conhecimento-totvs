---
article_id: 360028877851
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 3f8575b9c6b2a432fba2eabb642274d75294ee911acf42031a0ee2247e15de22
fetched_at: '2026-06-28T22:37:22.837849+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Formas de geração da
  Multa ou Bonificação em pedidos de compra ou venda gerado por medição - Parâmetro
  MV_MULTMED
type: support-article
updated_at: '2025-12-22T12:38:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028877851-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Formas-de-gera%C3%A7%C3%A3o-da-Multa-ou-Bonifica%C3%A7%C3%A3o-em-pedidos-de-compra-ou-venda-gerado-por-medi%C3%A7%C3%A3o-Par%C3%A2metro-MV-MULTMED
---

**Dúvida**  
Formas de geração de multa ou bonificação em pedidos de compra ou venda gerado na medição. Parâmetro MV\_MULTMED   
  
**Ambiente**  
  
Microsiga Protheus – Gestão de Contratos – A partir da versão 12  
  
**Solução**  
  
Para se entender onde o sistema esta gravando os valores referente às multas/bonificações de medições, na versão 12, estas tem seus valores armazenados nos campos de desconto/despesas (**C7\_VLDESC/C7\_DESPESA** para medições de Compra e **C5\_DESPESA/C5\_DESCONT** para de venda) no momento da geração dos pedidos. Na versão 11 o sistema distribuía o valor da multa dentre os itens da planilha da medição.

Dessa forma, foi criado o parâmetro **MV\_MULTMED**(tipo caractere) que possibilita a configuração do sistema para que funcione também como antes na versão 11.

O parâmetro pode receber no conteúdo dois valores:

* **1, para que distribua entre os valores unitários**
* **ou 2, para que utilize os campos de despesas do pedido**. O valor padrão do parâmetro é 2.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029602152)

**Sobre criação do parâmetro**

O parâmetro **MV\_MULTMED**só será expedido no dicionário da 12.1.25, para sua utilização é necessário sua criação de forma manual via Configurador.

**Obs:**

Ao proceder com alteração do parâmetro **MV\_MULTMED, é necessário sair do sistema e logar novamente para que o conteúdo do parâmetro seja considerado.**

**Obs2:**

No uso do parâmetro **MV\_MULTMED = 2** o valor de Multa ou Bonificação, quando configurado para refletir no pedido, são refletidos nos seguintes campos:

* **Contrato de Compra (Pedido de Compras):**

  + Multa (valor descontado): C7\_VLDESC
  + Bonificação (valor acrescido): C7\_DESPESA
* **Contrato de Venda (Pedido de Vendas):**

  + Multa (valor acrescido): C5\_DESPESA
  + Bonificação (valor descontado): C5\_DESCONT

***Saiba Mais:***

[GCT0140\_Parâmetro MV\_MULTMED](https://tdn.totvs.com/pages/releaseview.action?pageId=544703177)

[GCT0150\_Processo de Multa / Bonificação que interfira nos Pedidos na nova rotina de medição (CNTA121)](https://tdn.totvs.com/x/ElGHK)

[MP - SIGAGCT - Multa e Bonificação no Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000583548)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
