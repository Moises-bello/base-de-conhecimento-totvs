---
article_id: 360025942811
category: Gestão de Transportes (TMS)
content_hash: 2cc86d7baeab15ba386ab645832ef08672170b63994d109d1a292d16b2503eda
fetched_at: '2026-06-28T22:45:33.281264+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição 681 RNTRC informado inexistente
type: support-article
updated_at: '2022-06-15T11:30:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025942811-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-681-RNTRC-informado-inexistente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:10 min****Ocorrência** **Rejeição 681** na transmissão do **MDFe - Manifesto Eletrônico de Documentos Fiscais.**  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**Parametrização/Cadastro inconsistente. **Solução**Esta rejeição ocorre porque o **RNTRC - Registro Nacional de Transportadores Rodoviários de Cargas** informado é inválido.  
  
Quando o veículo utilizado no **MDF-e**, for frota própria, campo **DA3\_FROVEI** igual a **1**, o parâmetro **MV\_TMSANTT** deve ser informado com o número do registro na **ANTT** **- Agência Nacional de Transportes Terrestres**, com 8 dígitos sem zeros a esquerda.  
  
Quando o veículo utilizado no **MDF-e**, for frota **Agregado/Terceiro**, deve ser informado o campo **SA2\_RNTRC** no cadastro do fornecedor, informando o **RNTRC**, do proprietário do veículo, com 8 dígitos sem zeros a esquerda.  
  
Se desejar validar o número do **RNTRC** acesse o *link*: [Consulta RNTRC.](https://consultapublica.antt.gov.br/Site/ConsultaRNTRC.aspx/ConsultaPublica/)  
  
Se mesmo assim o erro persistir, será necessário entrar em contato com **ANTT**, e também realizar uma consulta protocolada com a **SEFAZ** **- Secretaria de Estado da Fazenda**.
