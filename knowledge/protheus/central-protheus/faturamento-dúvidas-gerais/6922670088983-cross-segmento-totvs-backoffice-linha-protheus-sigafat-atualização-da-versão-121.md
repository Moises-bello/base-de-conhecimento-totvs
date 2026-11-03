---
article_id: 6922670088983
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 90788aa201ef82f215a067c19773829e2f33478b8f7a53494ac2cedf7be3d3b7
fetched_at: '2026-06-28T22:38:28.697926+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat- Atualização da
  versão 12.1.33
type: support-article
updated_at: '2022-06-29T20:10:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6922670088983-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Atualiza%C3%A7%C3%A3o-da-vers%C3%A3o-12-1-33
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Atualizar versão/release para 12.1.33.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat- Todas as versões  
  
**Solução**

Informações adicionais sobre Upgrades para Releases a partir da 12.1.33

* É necessário utilizar o License Server Virtual, versão **igual ou superior a 3.2.0**
* É obrigatória a atualização para a **última versão** dos artefatos abaixo:  
  - Application Server (Binário Harpia)  
  - SmartClient (Binário Harpia)  
  - DBAccess  
  - WebApp  
  - RPO específico para binário Harpia  
  \* Informações de como atualizar os artefatos [neste link](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410703652375-MP-FRAME-Atualiza%C3%A7%C3%A3o-de-Artefatos-para-Bin%C3%A1rio-Harpia-Release-33-)
* Na chave **DBDATABASE** (da seção do Ambiente), para ambientes com Banco de Dados SQL Server, utilizar o valor **MSSQL** e não MSSQL7  
  Ex.: [P12.1.33]  
  SourcePath=  
  ...  
  DBALIAS=P12133  
  DBSERVER=192.168.1.1  
  **DBDATABASE=MSSQL**  
  DBPORT=7890
* **Importante**: o binário Harpia possui uma arquitetura exclusiva. Portanto, não sobrescreva os arquivos do Harpia na pasta do antigo Lobo Guará. Faça uma pasta nova de binário (renomeie as antigas appserver e smartclient e crie novas), descompacte o novo binário nelas, e copie da original apenas os arquivos appserver.ini e smartclient.ini.

Maiores detalhes acesse: <https://tdn.totvs.com/x/-FIMEQ>

Dúvidas sobre atualização de release, contate a equipe de framework.
