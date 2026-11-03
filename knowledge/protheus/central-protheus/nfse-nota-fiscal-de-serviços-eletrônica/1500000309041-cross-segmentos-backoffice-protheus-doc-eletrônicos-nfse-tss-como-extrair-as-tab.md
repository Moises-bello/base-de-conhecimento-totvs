---
article_id: 1500000309041
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: b309508e634780b02a3bd6384e889a80d7c9c01627f824b3730051de8e0dc1ed
fetched_at: '2026-06-28T22:39:58.561649+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TSS: COMO
  EXTRAIR AS TABELAS SPED051, SPED053 E SPED055'
type: support-article
updated_at: '2025-12-13T11:34:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000309041-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TSS-COMO-EXTRAIR-AS-TABELAS-SPED051-SPED053-E-SPED055
---

**Dúvida**  
Como extrair as tabelas SPED051, SPED053 E SPED055?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.

**Solução**  
As tabelas **SPED051, SPED053 e SPED055** são do TSS e exclusivas para armazenar dados da Nota fiscal de Serviço, modelo 56.  
  
Para extração dessas tabelas primeiramente deverá abrir o SmartClient do TSS, localizado na pasta BIN nos diretórios de instalação:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36994856735511)  
  
Acesse o **banco de dados do TSS** via APSDU.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101439173)  
  
 Faça a busca pelo nome da tabela:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000331742)  
  
Faça o filtro(Ctrl+F ) necessário.  
No exemplo abaixo, filtramos a SPED051 pela entidade que representa a filial e pelo número da nota:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000343861)  
  
Resultado do filtro:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000331902)  
  
Para exportar essa tabela, use o atalho Ctrl+Y ou clique em **Útil->Copiar para:**  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000343961)

Selecione o caminho para salvar o arquivo em formato SBD\* (SQLite (Local) ) e clique em OK:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36994856736535)

O arquivo será salvo com extensão .SBD:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36994856738071)  
  
O processo para extração das tabelas SPED053 e SPED055 é o mesmo, porém a SPED053 deve ser filtrada pelo número do lote, que pode ser obtido no campo NFSE\_LOTE da tabela SPED051.
