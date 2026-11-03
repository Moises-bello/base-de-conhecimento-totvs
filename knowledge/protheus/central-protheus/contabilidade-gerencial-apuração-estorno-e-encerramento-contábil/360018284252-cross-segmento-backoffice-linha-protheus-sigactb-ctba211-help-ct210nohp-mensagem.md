---
article_id: 360018284252
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 92b0d042dcc618fd83df0266b8d981b25c810d2cc39554a01d71a5678340d915
fetched_at: '2026-06-28T22:41:05.043241+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA211 -  HELP: CT210NOHP
  - Mensagem apresentada na execução da apuração'
type: support-article
updated_at: '2025-01-22T21:53:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018284252-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA211-HELP-CT210NOHP-Mensagem-apresentada-na-execu%C3%A7%C3%A3o-da-apura%C3%A7%C3%A3o
---

**Ocorrência**

Ao realizar a apuração de resultado o sistema gerar mensagem:

**Help: CT210NOHP**

**Problema: Filial 0102**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013905991)

**Ambiente**    
Protheus – Contabilidade Gerencial – A partir da versão 11.80   
  
**Causa**

**O código do Histórico Padrão informado não está cadastrado em todas as filiais.**

Com o fonte **CTBA211** superior a **12/03/2018**, o sistema apresenta a seguinte mensagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013906151)  
  
**Solução**

Acesse a rotina **"CTBA070 - Históricos Inteligentes"** e cadastre o histórico com o mesmo código nas filiais que serão apuradas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013890052)
