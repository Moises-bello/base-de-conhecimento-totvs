---
article_id: 5839601668375
category: Inspeção de Entradas (SIGAQIE)
content_hash: 9d9b4013824fe748eac5b92aef4717b7c4baf9dc9d25dcbebaf04c4ee6f102a2
fetched_at: '2026-06-28T22:42:27.054900+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Informação obrigatória de Instrumento
type: support-article
updated_at: '2022-05-03T14:59:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5839601668375-Manufatura-Linha-Protheus-SIGAQIE-Informa%C3%A7%C3%A3o-obrigat%C3%B3ria-de-Instrumento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min****Ocorrência**Na rotina **QIEA215 - Resultados** ocorre a mensagem **Instrumento obrigatório para a Medição XX referente ao Ensaio XX**. Como desabilitar a obrigatoriedade do registro de um instrumento?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**A mensagem **Instrumento obrigatório para a Medição XX referente ao Ensaio XX** ocorre quando o conteúdo do parâmetro **MV\_QEINSOB - Define se é obrigatória a especificação do Instrumento para a gravação dos resultados (SIGAQIE)** está como **S - Sim** e não foi informado o instrumento durante a inspeção.  
  
**Solução**Para desabilitar a obrigatoriedade de informar um instrumento na rotina **QIEA215** altere o  conteúdo do parâmetro **MV\_QEINSOB** para **N - Não**.
