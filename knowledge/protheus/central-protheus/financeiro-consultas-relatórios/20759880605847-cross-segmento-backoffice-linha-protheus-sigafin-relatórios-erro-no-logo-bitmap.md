---
article_id: 20759880605847
category: Financeiro - Consultas / Relatórios
content_hash: 0d2c8b117ecfd875e8caca029418723b2dc967efb85ad42024ad83b96fd9a1a8
fetched_at: '2026-06-28T22:37:58.434698+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Relatórios - Erro no
  logo - Bitmap logo with size error
type: support-article
updated_at: '2024-01-24T12:30:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20759880605847-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Relat%C3%B3rios-Erro-no-logo-Bitmap-logo-with-size-error
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20759910106135) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Error log ao gerar os relatórios do módulo Financeiro **(Bitmap logo with size error)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20759880589975)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre quando o arquivo de imagem (logo), dos relatórios, está nas dimensões ou formato incorreto na pasta **System** dentro da pasta Protheus data  
  
**Solução**

1 - A imagem contendo o logo da empresa deve ter **100 pixels de largura por 20 pixels de altura**;

2 - A imagem deve ser salva no formato **BMP** e usando a **paleta de 256 cores**;

3 - O nome do arquivo deve iniciar com **lgrl**, seguido do código da empresa e do código da filial.  
  
**Exemplos:**   
Empresa 01 e filial 02 o nome do arquivo deve ser **lgrl0102.bmp**.  
Para que a mesma imagem seja usada para todas as filiais, basta omitir o código da filial.  
Todas as filiais da empresa 01 o nome do arquivo deve ser **lgrl01.bmp**.   
  
**Importante:**

Se o arquivo de logo incorreto for deletado da pasta ***system***, o sistema automaticamente cria um novo, de nome lgrl99, com as dimensões padrões conforme a imagem abaixo e gera o relatório normalmente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20759910109847)  
  
**Saiba Mais**

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Aumentar tamanho e tipo da fonte em relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410790668951-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Aumentar-tamanho-e-tipo-da-fonte-em-relat%C3%B3rios)
