---
article_id: 360037132274
category: Faturamento - Cenários de Venda
content_hash: 066d0dfcc48ed0597155e8504f4e3fdc154416c20f58ff4a2a3d244d250ba532
fetched_at: '2026-06-28T22:38:33.877723+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus)  - FAT - Descrição dos Produtos
  não é preenchida na tabela de Preços
type: support-article
updated_at: '2023-01-30T21:15:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037132274-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FAT-Descri%C3%A7%C3%A3o-dos-Produtos-n%C3%A3o-%C3%A9-preenchida-na-tabela-de-Pre%C3%A7os
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:04:00 min**

**Ocorrência**Descrição do produto não é apresentada ao incluir um Produto em uma Tabela de Preço, porém ao visualizar ou alterar a tabela após sua inclusão a descrição é apresentada.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT - A partir da versão 12.  
  
**Causa**Esta inconsistência ocorre quando o **tamanho** dos campos **DA1\_DESCRI** e **B1\_DESC** esta **diferente**.

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Acessar o ambiente Configurador (**SIGACFG**);  
2. Selecionar a opção Base de dados/ Dicionario/ **Base de dados**;  
3. Localizar a tabela **SB1** e verificar o tamanho do campo **B1\_DESC**;  
4. Localizar a tabela **DA1** e verificar o tamanho do campo **DA1\_DESCRI**;  
5. Deixar os dois campos com o **mesmo tamanho**, não ultrapassando 250 caracteres;  
6. Salvar as novas configurações;  
7. Acessar a rotina **Tabela de Preços** (**OMSA010**), selecionar o produto e validar que a **Descrição** será apresentada.

**Saiba mais**:   
**[FAT0088\_Integridade\_dos\_campos\_Descrição\_Produto\_Tabela\_de\_Preço\_(Não\_carrega\_descrição\_na\_tabela)](https://tdn.totvs.com/pages/viewpage.action?pageId=240302745)**
