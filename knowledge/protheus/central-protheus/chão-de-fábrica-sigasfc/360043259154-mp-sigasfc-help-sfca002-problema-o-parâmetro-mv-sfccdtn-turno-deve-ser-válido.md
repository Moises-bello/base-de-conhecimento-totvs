---
article_id: 360043259154
category: Chão de Fábrica (SIGASFC)
content_hash: 5b5f2d5a2ad03b73835c7e5b9c8f0f10e52d6e961f91bd4e24216ab4451a8513
fetched_at: '2026-06-28T22:42:49.906742+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: 'MP - SIGASFC - Help: SFCA002 Problema: O parâmetro MV_SFCCDTN (Turno) deve
  ser válido'
type: support-article
updated_at: '2020-03-17T18:51:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043259154-MP-SIGASFC-Help-SFCA002-Problema-O-par%C3%A2metro-MV-SFCCDTN-Turno-deve-ser-v%C3%A1lido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:00:30 min**  
**Ocorrência**  
Ao tentar cadastrar uma máquina no módulo **Chão de Fábrica** é apresentada a mensagem: **Help: SFCA002 Problema: O parâmetro MV\_SFCCDTN (Turno) deve ser válido**.

![blobid0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059409773/blobid0.png)

**Ambiente**Microsiga Protheus – Chão de Fábrica - Versão 12  
   
 **Causa**Essa mensagem ocorre quando o parâmetro **MV\_SFCCDTN - Modelo Turno** está preenchido com um valor inválido.  
  
 **Solução**Cadastrar um turno no **SFCA011 - Turno** e informá-lo no parâmetro **MV\_SFCCDTN**.  
  
**Importante**  
Esse parâmetro é válido tanto para o **Chão de Fábrica - SIGASFC** quanto para o **Desenvolvedor de produtos - SIGADPR**.
