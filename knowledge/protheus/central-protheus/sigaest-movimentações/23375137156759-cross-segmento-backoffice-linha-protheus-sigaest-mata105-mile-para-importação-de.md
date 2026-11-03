---
article_id: 23375137156759
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 6f04e1927c2e291bb069eb4ba6fb855b6775c5c2843fe8fbc95b0f4684de02b4
fetched_at: '2026-06-28T22:38:55.693776+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA105 - MILE para
  importação de arquivo da tabela SCP (Solicitação ao Armazém)
type: support-article
updated_at: '2024-05-21T20:52:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23375137156759-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA105-MILE-para-importa%C3%A7%C3%A3o-de-arquivo-da-tabela-SCP-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23375146075415) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como importar o arquivo do MILE na Solicitação ao Armazém(SCP)?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Segue o passo a passo para importar o arquivo do MILE na rotina Solicitação ao Armazém da tabela SCP:

**- 1 -**Criação do Layout da tabela SCP com todos os campos padrões da rotina Solicitação ao Armazém, exemplo no print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23375146079255)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23375146081943)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23375137119383)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23375137121175)

**- 2 -**Configuração do segundo Canal que seria os itens, segue exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23375146085783)

**-3 -**Configurar o arquivo TXT de importação do MILE para a tabela SCP, veja no exemplo abaixo importando canal Master cabeçalho registro para a tabela SCP, caso desejar esta anexo o arquivo TXT;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23375146087959)

**- 4 -**Configurar o arquivo TXT de importação do MILE para a tabela SCP, veja no exemplo abaixo importando canal Detalle que são os itens registro para a tabela SCP, caso desejar esta anexo o arquivo TXT;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23375137126679)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23375137128983)

**- 5 -**Na rotina Solicitação ao Armazém(MATA105) importar o arquivo criado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23375146094487)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23375137131287)![](https://centraldeatendimento.totvs.com/hc/article_attachments/23375137132183)![](https://centraldeatendimento.totvs.com/hc/article_attachments/23375137134359)

**- 6 -** Pesquisa pela Solicitação Armazém importada pelo MILE, veja o resultado do exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23375146099607)

- Conheça mais detalhes sobre o MILE no Estoque [clicando aqui](https://tdn.totvs.com/x/9bA6Kw)

**Saiba Mais:**

*[Clique aqui e veja mais artigos sobre CADASTROS E CONFIGURAÇÕES GERAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
