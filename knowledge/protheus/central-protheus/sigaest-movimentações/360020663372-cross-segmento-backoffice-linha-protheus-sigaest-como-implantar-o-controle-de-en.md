---
article_id: 360020663372
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 1e9861c4503f5bafd464c4ceb0719033f662374f7f9ea012c57b90f00f8b9cba
fetched_at: '2026-06-28T22:38:53.940991+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como implantar o controle
  de endereço para produtos que já tem saldo?
type: support-article
updated_at: '2025-03-12T12:26:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020663372-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-implantar-o-controle-de-endere%C3%A7o-para-produtos-que-j%C3%A1-tem-saldo
---

**Dúvida**Como alterar o controle de endereço para produtos que já possuem saldo no ambiente?  
  
**Ambiente**Protheus – Estoque – A partir da versão 11.80  
  
**Solução**

Para solucionar essa dúvida, realize os seguintes passos, também abaixo vídeo com teste do processo simulado como exemplo:

**⇛** Alterar o parâmetro **MV\_LOCALIZ** para S no módulo Configurador

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000344801/mceclip0.png)

**⇛** Revisar o saldo do produto para que possa fazer a inclusão de todo o Saldo para o Endereçamento;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12926384782615)

**⇛** No cadastro do produto alterar o campo **"Contr. Endere"** **(B1\_LOCALIZ)** para Sim;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12926436530071)

**⇛** Criar o(s) endereço(s) na rotina **Endereço Físico** (MATA015) para que possa receber o saldo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12927191923351)

**⇛** Acessar a rotina **Criar Saldo no Endereço** **(MATA805)** incluir um número de documento e informar o saldo no endereço desejado. ***Obs.:*** Recomendamos que inicialmente crie o saldo em apenas um endereço, e caso desejar, pode transferir o saldo pela rotina TRANSFERÊNCIA MÚLTIPLA (MATA261);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12926542204951)

**⇛** Com isso, o saldo do produto na SBF é atualizado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12926805864343)

***Obs 1:*** Após efetuado o processo acima, o produto passa a controlar, além do saldo físico e financeiro, o saldo por endereço. Com isso todo saldo que for movimentado ou requisitado deve ser diretamente do endereço, e atualiza as tabelas referenciadas, abaixo segue o fluxo de movimentação dos saldos.

|  |  |  |
| --- | --- | --- |
|  | ***Saldo físico e Financeiro*** | ***Saldo por******Endereço*** |
| ***Saldo Inicial*** | **SB9** | **SBK** |
| ***Movimentos*** | **SD1, SD2, SD3** | **SDB** |
| ***Saldo Atual*** | **SB2** | **SBF** |
| ***Empenhos e Bloqueio******s*** | **SD4** | **SDC, BF\_EMPENHO**  (Saldo a endereçar) |
|  |  | **SDA**  (Cadastro de endereço) |

***Obs 2***: Para endereçar um produto após dar entrada nele, basta acessar à rotina "Endereçamento" (**MATA265**), disponível no menu **Atualizações -> Movimentações -> Internas -> Endereçamento -> Endereçar.**

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*

[*SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)
