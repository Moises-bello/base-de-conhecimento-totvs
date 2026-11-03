---
article_id: 360053622674
category: MDT - Atendimento Médico
content_hash: fcbee977771b1cdd7ddbc2464f04c6ae417d65be86231bd2f5d8eebd5e858300
fetched_at: '2026-06-28T22:44:20.703821+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Erro "O valor atribuído difere do tamanho do campo
  (Tipo Afasta.)" quando informado o código de ausência na rotina atestado medico
type: support-article
updated_at: '2025-08-14T19:16:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053622674-RH-Linha-Protheus-MDT-Erro-O-valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-Tipo-Afasta-quando-informado-o-c%C3%B3digo-de-aus%C3%AAncia-na-rotina-atestado-medico
---

**Ocorrência**Erro "O valor atribuído difere do tamanho do campo (Tipo Afasta.)" quando informado o código de ausência na rotina atestado medico.  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Esse erro ocorre quando a consulta padrão (SBX) tem um registro incorreto ou falta de registro referente aos campos Cod. Ausência (TNY\_CODAFA**)** ou Tipo afasta. (TNY\_TIPAFA). Isso pode acontecer por motivo de manipulação de tabelas, ou algum problema na migração de dados / release.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089616614)  
  
**Solução**A correção de validações de campos só ocorre por meio da atualização de dicionário. Nesse caso para correção execute em ambiente de homologação a atualização do ultimo dicionário diferencial (UPDDISTR) do modulo medicina e segurança do trabalho disponível na central de downloads.  
  
Link: [MP - MDT - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo medicina e segurança do trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773-MP-MDT-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-medicina-e-seguran%C3%A7a-do-trabalho?source=search)  
  
**Saiba Mais**[Central de Artigos de Medicina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT)  
[Na rotina de Atestado Médico o campo Tipo Afas. (TNY\_TIPAFA)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045649953-RH-Linha-Protheus-MDT-Na-rotina-de-Atestado-M%C3%A9dico-o-campo-Tipo-Afas-TNY-TIPAFA-n%C3%A3o-habilita)
