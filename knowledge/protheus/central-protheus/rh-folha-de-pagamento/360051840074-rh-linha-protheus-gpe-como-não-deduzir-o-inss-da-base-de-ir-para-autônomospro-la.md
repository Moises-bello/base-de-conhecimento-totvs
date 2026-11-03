---
article_id: 360051840074
category: RH - Folha de Pagamento
content_hash: 1c0387a558ecf2a86d95b81402f2957b5d58941960f7f28f42b0c590e9d7dc93
fetched_at: '2026-06-28T22:44:13.566676+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como não deduzir o INSS da base de IR para autônomos/pro-labores
  residentes no exterior
type: support-article
updated_at: '2024-09-09T20:19:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051840074-RH-Linha-Protheus-GPE-Como-n%C3%A3o-deduzir-o-INSS-da-base-de-IR-para-aut%C3%B4nomos-pro-labores-residentes-no-exterior
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26252791447831) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como parametrizar o sistema para que não seja abatido o valor do INSS da base de IR para autônomos/pro-labores residentes no exterior?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**1. No cadastro do Funcionário, na aba Endereço, o campo Res. Exterior, cadastre com SIM:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082677534)  
  
2. Com o campo Res. Exterior com SIM no cadastro do Funcionário, na rotina Histórico de Contrato (caminho >Atualizações >Funcionários >Histórico de Contrato) o sistema habilita a aba Residente Exterior, então no campo Deduz INSS deixe com Não. Assim, o sistema não deduzirá o INSS da base de IR:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082677634)  
  
**OBS.:** O sistema somente habilita a aba **Residente Exterior** na rotina Histórico de Contrato se no cadastro do Funcionário estiver preenchido que reside no Exterior.

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
