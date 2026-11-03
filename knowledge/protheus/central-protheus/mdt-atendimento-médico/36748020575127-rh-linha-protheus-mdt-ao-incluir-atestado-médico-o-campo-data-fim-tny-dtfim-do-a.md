---
article_id: 36748020575127
category: MDT - Atendimento Médico
content_hash: b475477a21b8426d623748ffa646280e88194e0cab89221883a474ef405e32e4
fetched_at: '2026-06-28T22:44:20.461814+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: 'RH - Linha Protheus - MDT -  Ao incluir atestado médico: O campo data fim
  (TNY_DTFIM) do atestado foi preenchido, por tanto o campo data alta (TYZ_DTALTA)
  na grid afastamentos deve ser preenchido!'
type: support-article
updated_at: '2025-12-05T13:36:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36748020575127-RH-Linha-Protheus-MDT-Ao-incluir-atestado-m%C3%A9dico-O-campo-data-fim-TNY-DTFIM-do-atestado-foi-preenchido-por-tanto-o-campo-data-alta-TYZ-DTALTA-na-grid-afastamentos-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36748020564631) Tempo aproximado para leitura: **0002:00 min**  
  
**Ocorrência**  
Ao incluir um atestado médico no módulo de Medicina e Segurança do Trabalho, o sistema está apresentando a mensagem "O campo data fim (TNY\_DTFIM) do atestado foi preenchido, por tanto o campo data alta (TYZ\_DTALTA) na grid afastamentos deve ser preenchido!"

**Ambiente**  
RH - Linha Protheus - MDT - Todas as versões  
  
**Causa**  
Quando a data de inicio e fim do atestado estão preenchidas, o sistema exige que a data alta na aba de afastamento também seja informada.

**Solução**  
Para correção será necessário a aplicação do pacote:

12.1.2210:<https://r.totvs.io/p/1226428> ; 12.1.2310:<https://r.totvs.io/p/1226426> ; 12.1.2410:<https://r.totvs.io/p/1226427> ; 12.1.2510:<https://r.totvs.io/p/1226429> ;
