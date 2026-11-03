---
article_id: 36639345952023
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: b7c2a1fd8aa936d3e2b9a515777b44b806b75b1d7b45bfe12598e96287f10712
fetched_at: '2026-06-28T22:37:22.735213+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Erro ao Incluir Tipo
  de Planilha - CNTA230 - SetOrder - Index not found. on CN230ALCMD(CNTA230.PRW)
type: support-article
updated_at: '2025-11-28T15:06:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36639345952023-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Erro-ao-Incluir-Tipo-de-Planilha-CNTA230-SetOrder-Index-not-found-on-CN230ALCMD-CNTA230-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36639345944855) Tempo aproximado para leitura: **05:00:00 min**  
  
**Dúvida**

Ao realizar a inclusão de um Tipo de Planilhas (CNTA230) ocorre o error.log:

THREAD ERROR

SetOrder - Index not found. on CN230ALCMD(CNTA230.PRW)

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Referente ao erro, as ocorrências mapeadas e com retornos positivos de solução dos mesmos, estão relacionados a um ou mais dos pontos abaixo:  
   
1. A não existência no ambiente em questão, de todos os índices padrões da tabela CNA,   
   
2. A ordem dos campos da tabela CNL não estar conforme o padrão  
   
3. Campo CNL\_ALCMED não estar com as configurações e ordem corretas na tabela CNL:  
   
   
   
Dessa forma orientamos a realização da checagem dos 3 pontos, (**principalmente a existência dos índices conforme o padrão da tabela CNA**) conforme as imagens padrões abaixo:  
 

1. Realizar a verificação nos índices da tabela CNA, se no ambiente em questão existem os índices e se eles estão conforme o padrão da imagem abaixo, e se não existe nenhum índice diferente, onde caso haja divergência orientamos realizar um backup em ambiente de homologação e ajuste para deixar conforme padrão da imagem abaixo:

   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36639345945623)  
   
   
   
2. Caso ainda assim persista, verificar o campo CNL\_ALCMED que é um campo de ordem fixa obrigatória. Verificar se está conforme padrão, se não realize um ajuste em ambiente de teste com backup para validação.  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36639360011671)  
   
   
   
3. Se ainda persistir, verificar se o campo CNL\_ALCMED está conforme ambiente padrão segue telas abaixo:  
   
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36639360011927)  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36639360012567)  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36639360012695)  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36639345947415)  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36639360013079)  
 

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Documentação Gestão de Contratos do TDN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441027145623)

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[FAQs - Gestão de Contratos](https://tdn.totvs.com/x/O_tgDQ)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
