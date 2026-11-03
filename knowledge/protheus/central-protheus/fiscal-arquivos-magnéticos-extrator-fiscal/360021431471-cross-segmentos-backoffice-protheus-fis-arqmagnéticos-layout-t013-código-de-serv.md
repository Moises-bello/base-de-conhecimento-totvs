---
article_id: 360021431471
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 566442bbf9ecdb8b7dd2db4bd82269dce526739c8f938e285d4af1e3463b79fd
fetched_at: '2026-06-28T22:42:07.874383+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T013
  Código de Serviço C2F_CODSER inexistente
type: support-article
updated_at: '2022-08-18T17:39:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021431471-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T013-C%C3%B3digo-de-Servi%C3%A7o-C2F-CODSER-inexistente
---

**Ocorrência**O valor '0710' informado na coluna 14 para o campo Código do Serviço ( C2F\_CODSER ) não existe na base de dados.  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, quando o código de serviço utilizado é inválido. Sendo este validado através da tabela **C0B - Código Serviço (LCF 116/2003)**

Esta informação é validada pelo sistema, conforme [LEI COMPLEMENTAR Nº 116, DE 31 DE JULHO DE 2003](http://www.planalto.gov.br/ccivil_03/LEIS/LCP/Lcp116.htm)

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Informe um código de serviço válido no cadastro de produto  
2. Acesse o Extrator Fiscal;  
3. Responda a pergunta: **"Verifica movimento para os layouts cadastrais?"**igual a **1-Não**;  
4. Selecione o Layout **T007 - Identificação do Item**e confirme a extração;  
5. Acesse o módulo **TOTVS Automação Fiscal** -> Miscelânea -> Integração -> Processamentos para processar os dados extraídos;  
6. Confirme na tela do gerenciador de integração se houveram inconsistências na importação do Layout;  
7. Acesse o gerenciador de integração e posicione o cursor no registro que houve   
inconsistência e acione as opções: Outras Ações -> Habilitar Re-integração para que  
o registro que obteve a inconsistência seja integrado novamente ao TAF.
