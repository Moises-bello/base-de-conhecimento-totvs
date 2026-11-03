---
article_id: 360018249431
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 94f7450de227571091d3c45b9379e08e5c370c9972a1b5875946e844a0bf3a07
fetched_at: '2026-06-28T22:42:07.843631+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T007
  Código de Serviço C1L_CODSER inexistente
type: support-article
updated_at: '2022-08-18T17:35:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018249431-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T007-C%C3%B3digo-de-Servi%C3%A7o-C1L-CODSER-inexistente
---

**Ocorrência**O valor '2879' informado na coluna 10 para o campo Cod. Id. Serviço (**C1L\_CODSER**) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, quando o código de serviço utilizado é inválido. Sendo este validado através da tabela **C0B - Código Serviço (LCF 116/2003)**

Esta informação é validada pelo sistema, conforme [LEI COMPLEMENTAR Nº 116, DE 31 DE JULHO DE 2003](http://www.planalto.gov.br/ccivil_03/LEIS/LCP/Lcp116.htm)  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Informe um código de serviço válido no cadastro de produto  
2. Acesse o Extrator Fiscal;  
3. Responda a pergunta: **"Deseja Integrar:"**igual a **1-Somente Cadastros**;  
4. Selecione o Layout **T007 - Identificação do Item** e confirme a extração;  
5. Acesse o módulo **TOTVS Automação Fiscal -> Miscelânea -> Integração -> Processamentos** para processar os dados extraídos;  
6. Confirme na tela do gerenciador de integração se houveram inconsistências na importação do Layout.
