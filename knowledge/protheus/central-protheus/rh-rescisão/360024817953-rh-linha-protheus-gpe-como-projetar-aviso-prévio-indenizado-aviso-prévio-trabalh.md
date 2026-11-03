---
article_id: 360024817953
category: RH - Rescisão
content_hash: edffe061b4952648374aa3241cc98e6112cb496134ff143d43812be8807d89ad
fetched_at: '2026-06-28T22:43:49.569435+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como projetar aviso prévio indenizado,  aviso prévio
  trabalhado e aviso prévio na rescisão por acordo
type: support-article
updated_at: '2025-07-14T19:07:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024817953-RH-Linha-Protheus-GPE-Como-projetar-aviso-pr%C3%A9vio-indenizado-aviso-pr%C3%A9vio-trabalhado-e-aviso-pr%C3%A9vio-na-rescis%C3%A3o-por-acordo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33462470469271) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como parametrizar o sistema para projetar os dias de aviso prévio indenizado e aviso prévio trabalhado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) – Gestão de Pessoal – A partir da Versão 12  
  
**Solução**Para **projetar o Aviso Prévio**, seja ele indenizado, trabalhado ou por acordo, a principal configuração é na tabela **S043** da rotina Manutenção Tabelas (Atualizações >Definição de Cálculo >Manutenção Tabelas), onde a coluna Projeta Aviso deve ficar com **S**, e além dessa configuração, quando o Aviso é Trabalhado, no cadastro do Sindicato relacionado a matricula, na aba Rescisão o campo Proj. Av. Trab. deve ficar com SIM, abaixo configurações:

**Aviso Indenizado**:  
Na Tabela S043, para o Tipo de **Aviso Indenizado**, a **coluna Aviso Prévio** deve ficar com **I** e a **coluna Projeta Aviso** deve ficar com **S**:![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038883713)

**Aviso Trabalhado:**  
Na Tabela S043, para o Tipo de **Aviso Trabalhado**, a **coluna Aviso Prévio** deve ficar com **T** e a **coluna Projeta Aviso** deve ficar com **S**:![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038039074)  
  
Além disso, no **cadastro do Sindicato**, na aba **Dados Rescisão** o campo **Proj. Av. Trab** deve ficar com **SIM**:![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038884093)

**Aviso Indenizado por Acordo**:  
Na Tabela S043, para o Tipo de **Aviso Indenizado por Acordo**, a **coluna Aviso Prévio** deve ficar com **A** e a **coluna Projeta Aviso** deve ficar com **S**:![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038884193)

**Aviso Trabalhado por Acordo**:  
Na Tabela S043, para o Tipo de **Aviso Trabalhado por Acordo**, a **coluna Aviso Prévio** deve ficar com **B** e a **coluna Projeta Aviso** deve ficar com **S**:![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038884293)  
  
Além disso, no **cadastro do Sindicato**, na aba **Dados Rescisão** o campo **Proj. Av. Trab** deve ficar com **SIM**:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038884093)

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
