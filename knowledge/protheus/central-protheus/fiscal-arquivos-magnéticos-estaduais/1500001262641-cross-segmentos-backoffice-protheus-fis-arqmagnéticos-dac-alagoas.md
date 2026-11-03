---
article_id: 1500001262641
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 578c6fd6074f6c98fc8548ad267938d4d7c26b4caeca42169d3dc7930c8eba58
fetched_at: '2026-06-28T22:42:10.654080+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DAC ALAGOAS
type: support-article
updated_at: '2022-08-18T14:16:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001262641-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DAC-ALAGOAS
---

**Dúvida**Como realizar a configuração dos campos e parâmetros da **DAC - Declaração das Atividades do Contribuinte -Alagoas**?  
  
  
**Ambiente**Microsiga Protheus – Fiscal – A partir da versão 11.80  
  
**Solução**

1- No Configurador (SIGACFG), acesse Base de Dados/ Dicionário/Base de Dados . Altere o tamanho do campo Cód. Receita do Cadastro da GNRE – Guia Nacional de Recolhimento, conforme segue: Tabela SF6 - Guia Nacional de Recolhimento, conforme segue:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100163754/mceclip0.png)

2- No Configurador (SIGACFG), acesse Ambiente/Cadastros/Parâmetros, observe/crie os parâmetros a seguir:

**MV\_DAC01**

Tipo = Caracter

Conteúdo <definido pelo cliente>

Descrição= Campo do SA2 que contém o Código do Município, conforme Tabela da DAC.

Obs: No conteúdo, informe o campo da tabela de **Fornecedores (SA2**), que contém o Código do Município,  conforme a tabela de Códigos de Produtos da DAC. Sugestão de conteúdo: **A2\_COD\_MUN**

O parâmetro **MV\_DAC01** é utilizado para gerar o Registro Tipo 61.

**MV\_DAC02**

Tipo = Caracter

Conteúdo <definido pelo cliente>

Descrição= Campo do SB5 que contém o código do produto, conforme Tabela da DAC.

OBs: No conteúdo, Informe o código do produto conforme a Tabela de Códigos de

Produtos da DAC. Sugestão para o nome do campo: **B5\_CODIGO**

**MV\_DAC04**

Tipo = Caracter

Conteúdo <definido pelo cliente>

Descrição= CFOPs de Entrada ST Petróleo e Energia para geração da DAC-AL.

Obs: No conteúdo, informe os **CFOPs** referentes ao ICMS pago por Substituição Tributária nas entradas de energia e/ou produtos derivados de petróleo (combustíveis e lubrificantes). Informe os **CFOPs** sem  aspas (“”) e separados por barras (/). Exemplo de conteúdo: XXXX/YYYY;

O parâmetro **MV\_DAC04** é utilizado para gerar o Registro Tipo 63.

3. Caso os campos indicados nos parâmetros não existam, crie - os no Configurador (SIGACFG). Acesse Base de Dados/Dicionário/Base de Dados, conforme estrutura a seguir: Tabela **SA2** – Cadastro de  fornecedores

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001259122/mceclip3.png)

Sugestão para o nome do campo: **A2\_COD\_MUN**;

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102343613/mceclip4.png)

Sugestão para o nome do campo: **B5\_CODIGO**

**Para os procedimentos de configuração e utilização, acesse o link abaixo no qual será direcionado para o boletim técnico.**

**<http://tdn.totvs.com/pages/viewpage.action?pageId=37748882>**
