---
article_id: 360025453271
category: Gestão de Transportes (TMS)
content_hash: 2066ac933573097527887e15930d37f509126dc883389b796018b76ef2590414
fetched_at: '2026-06-28T22:45:32.521245+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Região de Origem do MDF-e
type: support-article
updated_at: '2025-04-09T12:04:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025453271-Log%C3%ADstica-Linha-Protheus-TMS-Regi%C3%A3o-de-Origem-do-MDF-e
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura:**00:01:18 min****Dúvida**Como informar uma **cidade de início** diferente da **cidade da transportadora** na emissão do **MDF-e - Manifesto Eletrônico de Documentos Fiscais?**  
  
**Ambiente**

TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Para operações de transporte onde se faz necessária a emissão do **MDF-e,** ao qual o município de início da prestação seja diferente do município da transportadora, deverá possuir um **Cadastro de Rota - OMSA100** específico para esta situação, onde o campo **Cd.Ori.MDF-e - DA8\_CDOMDF**deve ser preenchido com a cidade de início da prestação de serviço de transporte:

![rota_1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360038096374/rota_1.PNG)

A região preenchida no campo **Cd.Ori.MDF-e - DA8\_CDOMDF**deverá possuir os campos **Cd.Municipio** e **Estado**preenchidos no cadastro de regiões. Caso contrário, ao transmitir o **MDF-e,** haverá falha de **schema** informando que não foi possível localizar dados para criar dentro das *tags* o conteúdo necessário.

![grupo_de_regiao_1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360038096354/grupo_de_regiao_1.PNG)

Após esta configuração, basta realizar os processos de viagem e emissão do **MDF-e** já tradicionais no módulo **SIGATMS - Gestão de Transportes** **Protheus**. Ao emitir o **MDF-e**, as *tags* pertinentes à inicio da prestação de serviço serão alteradas para a região computada no cadastro da nova rota. São as *tags*:

* **UFIni *-***Sigla da **UF - Unidade de Federação** do Carregamento
* **cMunCarrega *-***Código do Município de Carregamento
* **xMunCarrega *-***Nome do Município de Carregamento

**Importante**Caso mesmo com esta orientação não consiga gerar o **MDF-e** com a origem da rota, peço que abra um *ticket* para o Atendimento da **TOTVS** informando a data do fonte **TMSAF16 - Percursos da Viagem**, pois este efetua a geração do percurso da viagem e possui atualização referente a geração da origem do **MDF-e.**
