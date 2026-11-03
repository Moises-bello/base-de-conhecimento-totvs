---
article_id: 22998462547095
category: Originação de Grãos (OG)
content_hash: 23821e1134e7203215ff01282755d4599ffa5ac599e1f3b9279379f5462554d5
fetched_at: '2026-06-28T22:45:39.367759+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Emblocamento Automático seguindo Regras de Emblocamento
type: support-article
updated_at: '2025-04-07T20:34:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22998462547095-Agro-Linha-Protheus-AGR-Emblocamento-Autom%C3%A1tico-seguindo-Regras-de-Emblocamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22998462526487) Tempo aproximado para leitura: **00:00:50 min** **Dúvida**Emblocamento Automático seguindo Regras de Emblocamento. Como proceder em**Venda a Ordem**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
**Emblocamento Automático seguindo Regras de Emblocamento:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Função:** | UBAA060 - Regra Emblocamento  UBAA070 - Emblocamento Automático |
| **Situação/Requisito:** | Há a necessidade de realizar automaticamente o emblocamento de fardos de algodão seguindo regras predeterminadas. |
| **Solução/Implementação:** | Para atender à essa necessidade foram desenvolvidas duas novas rotinas:  UBAA060 - Está localizada na pasta Cadastros do macroprocesso de UBA e é responsável por predeterminar as regras para o Emblocamento Automático. Essas regras possuem critérios como Grau de Relevância, % de Formação, Não Incidência de Contaminantes e Tipo Comercial.  UBAA070 - Localiza-se na pasta Blocagem do macroprocesso de UBA e possui o objetivo de gerar automaticamente o emblocamento, de acordo com as regras impostas na rotina UBAA-060. |
| **Requisito:** | DAGROUBA-196 |
