---
article_id: 360057165713
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 99a294132b29d50e0a137881a64a67e3bf5573cddf5756d178348ea218b737f8
fetched_at: '2026-06-28T22:42:10.733352+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DIEF PA - Anexo
  II Substituição Tributária - Errado - Este Código de Município não Consta em Nossa
  Base de Dados
type: support-article
updated_at: '2022-08-17T20:18:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057165713-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DIEF-PA-Anexo-II-Substitui%C3%A7%C3%A3o-Tribut%C3%A1ria-Errado-Este-C%C3%B3digo-de-Munic%C3%ADpio-n%C3%A3o-Consta-em-Nossa-Base-de-Dados
---

**Dúvida**  
Ao importar o arquivo da DIEF PA é apresentando o erro abaixo:  
  
Descrição: Anexo II Substituição Tributária - Errado  
Detalhe: Este código de município não consta em nossa base de dados.  
  
![](https://totvssuporte.zendesk.com/attachments/token/RXiZk6XHWGtLT2qTPFNFCA8tK/?name=inline-1575986516.png)  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
 **Solução**O código de Município da DIEF é obtido através do campo Cód. DIEF (A1\_DIEF - Cadastro de Clientes) e Cód. DIEF (A2\_DIEF -Cadastro de Fornecedor) campos estes configurados nos parâmetros MV\_A1DIEF e MV\_A2DIEF.

**Informação sobre os campos:**  
  
**Cód. DIEF - A1\_DIEF:**  
Código do município do cliente conforme a tabela SEFA-PA, utilizado para a geração da DIEF

**Cód. DIEF - A2\_DIEF:**   
Código do município do fornecedor conforme a tabela SEFA-PA, utilizado para a geração da DIEF.  
  
**Informação sobre os parâmetros:**  
  
**MV\_A1DIEF**   
Informa campo da tabela SA1 que contém o código do município do cliente, conforme a tabela da SEFA-PA.  
  
**MV\_A2DIEF**  
Informa campo da tabela SA2 que contém o código do município do fornecedor, conforme a tabela da SEFA-PA.  
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=233765585>
