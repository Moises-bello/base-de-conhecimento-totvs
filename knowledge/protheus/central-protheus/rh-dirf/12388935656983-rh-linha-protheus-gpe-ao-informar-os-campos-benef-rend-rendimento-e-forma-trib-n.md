---
article_id: 12388935656983
category: RH – DIRF
content_hash: 1625804dafb979296efc4aa375f5db20647a2e0959f1b58f7a460e36aeee1bf8
fetched_at: '2026-06-28T22:44:06.787193+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Ao informar os campos Benef Rend, Rendimento e
  Forma Trib na Manutenção Arquivo, é gerada mensagem de Tabela não encontrada
type: support-article
updated_at: '2025-08-15T13:46:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12388935656983-RH-Linha-Protheus-GPE-Ao-informar-os-campos-Benef-Rend-Rendimento-e-Forma-Trib-na-Manuten%C3%A7%C3%A3o-Arquivo-%C3%A9-gerada-mensagem-de-Tabela-n%C3%A3o-encontrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34206326239383) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao informar os campos Benef Rend, Rendimento e Forma Trib na Manutenção Arquivo, é gerada mensagem de Tabela não encontrada:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12388469228567)  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12  
  
**Causa**Tabelas S021, S022 e S023 não existem na rotina Manutenção tabelas.  
  
**Solução**1. Entre na rotina **Definição tabelas** para carregar a mesma, pelo caminho **>Atualizações >Definição cálculos >Definição tabelas**, verifique se existem as tabelas **S021, S022 e S023:**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12388672932887)

2. Entre na rotina Manutenção tabelas para também carregar as tabelas, pelo caminho **>Atualizações >Definição cálculos >Manutenção tabelas**, verifique se existem as tabelas **S021, S022 e S023:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12388730710551)  
  
Visualização das tabelas na rotina Manutenção tabelas  
  
S021  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12388772603671)  
  
  
S022  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12388828120855)  
  
  
S033  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12388837805207)**  
Após isso, o o sistema localizará as tabelas para o cadastro na rotina Manutenção Arquivo.

**Saiba Mais**  
[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
