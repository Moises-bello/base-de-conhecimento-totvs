---
article_id: 6978081817751
category: GPE - eSocial - Não Periódicos
content_hash: 3688c3f576a0d023f2db452894dceafc307b793db0186263fa862c1ea411d2b8
fetched_at: '2026-06-28T22:45:04.604268+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200/S-2206 - Como enviar novos turnos
  de trabalho para o TAF
type: support-article
updated_at: '2026-06-16T11:47:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6978081817751-RH-Linha-Protheus-GPE-eSocial-S-2200-S-2206-Como-enviar-novos-turnos-de-trabalho-para-o-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25783416670359) Tempo aproximado para leitura: **00:02:00 min** **Dúvida** Como enviar novos turnos de trabalho para o TAF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução** **A** **partir do leiaute simplificado S-1.0** as informações de **turno de trabalho** passam a ser enviadas nos eventos **S-2200** (Admissão/Ingresso do Trabalhador) e **S-2206** (Alteração de Contrato de Trabalhado). Portanto, ao admitir um funcionário com o novo turno ou realizar a alteração do turno já vinculado para o novo cadastrado, os eventos S-2200 e S-2206 serão gerados com as *tag's* **horcontratual** no arquivo XML, levando informações relativas ao horário contratual do trabalhador.   
  
Abaixo segue um exemplo do formato do xml de transmissão de um evento:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6978909073943)  
  
Abaixo segue print da tabela de horário padrão e cadastro do turno de trabalho que está vinculado este funcionário de exemplo acima:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6979013713303)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6979084766487)  
Para saber mais sobre os campo **R6\_TOJOR1** e **R6\_ESNOTU** acesse:[RH - Linha Protheus - GPE - Campos R6\_TPJOR1 e R6\_ESNOTU criados para atender o leiaute simplificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6632351698711-RH-Linha-Protheus-GPE-Campos-R6-TPJOR1-e-R6-ESNOTU-criados-para-atender-o-leiaute-simplificado?source=search) **Saiba Mais**Para saber mais consulte os *links*abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocia](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)
