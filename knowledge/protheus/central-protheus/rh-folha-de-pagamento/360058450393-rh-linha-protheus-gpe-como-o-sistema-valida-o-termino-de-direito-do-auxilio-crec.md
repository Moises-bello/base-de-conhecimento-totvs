---
article_id: 360058450393
category: RH - Folha de Pagamento
content_hash: 5e35bb52e7574b09e34bbd59ca6fd8cd2a277615d7074be8c6216e1f8f3ddd59
fetched_at: '2026-06-28T22:44:13.618910+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como o sistema valida o termino de direito do auxilio
  creche
type: support-article
updated_at: '2025-08-12T13:31:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058450393-RH-Linha-Protheus-GPE-Como-o-sistema-valida-o-termino-de-direito-do-auxilio-creche
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26354257978135) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**Como sistema valida o término de direito do auxilio creche, após atingir o limite de meses?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**No cadastro do dependentes em **Atualizações > Funcionários > Dependentes (GPEA020)**, o sistema valida o campo "**Data Nasc**.", e o cadastro da tabela S015 em **Atualizações > Definições de Cálculo > Manutenção Tabelas (GPEA320).**   
  
Na tabela S015 deve determinar no cadastro o **meses a partir de** e **limite de meses**. Para cada linha cadastrada os meses informados, será considerado o direito do beneficio e calculado de cada funcionário conforme o cadastro de dependentes para receber o beneficio.  
  
Exemplo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096086174)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098381173)

**Obs.:** O cadastro da tabela S015 deve ser informado conforme a particularidade de cada empresa ou como prevê em convenção coletiva.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
