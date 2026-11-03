---
article_id: 4414532770711
category: RH - Fechamento Período
content_hash: b12fef4655eccd3307f0698641cbd4ad5976aef9850e8932d4eba4a8c283eaf1
fetched_at: '2026-06-28T22:43:24.380782+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: RH - Linha Protheus - GPE - Após fechamento do período, Sistema não atualiza
  status para Fechado no cadastro de períodos
type: support-article
updated_at: '2025-04-16T12:38:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414532770711-RH-Linha-Protheus-GPE-Ap%C3%B3s-fechamento-do-per%C3%ADodo-Sistema-n%C3%A3o-atualiza-status-para-Fechado-no-cadastro-de-per%C3%ADodos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22095849162647) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No Módulo 7, Gestão de Pessoal, após fechamento do período, sistema não atualiza status para fechado no cadastro de períodos (FQ\_STATUS).  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Causa**Funcionários cadastrados em filiais inexistentes

**Solução**O processo de fechamento de períodos da Folha de Pagamento envolve diversas tabelas do Sistema.

Neste caso o que pode ocasionar erro na atualização do status do período (campo **FQ\_STATUS**) é existir funcionários cadastrados em **filiais inexistentes**.

Em casos de alteração de codificação de empresas/ filiais ou até mesmo inativação, é necessário que sejam feitos ajustes para estes funcionários, ou até mesmo transferi-los.

Este cenário é identificado através da análise dos dados gravados nas tabelas relacionadas (**SRA** - Cadastro de Funcionários e **SYS\_COMPANY -**Cadastro de Empresas), 

**Saiba Mais:**

[RH - Linha Protheus - GPE - Melhoria de performance no fechamento mensal com MV\_CALCTHD ativo:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050884333?source=search)

[RH - Linha Protheus - GPE - Implementação de GRID no Fechamento de Período:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19124711142679?source=search)

[RH - Linha Protheus - GPE - Implementação do Multi Thread no fechamento da folha:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034908554?source=search)

[RH - Fechamento Período](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909793-RH-Fechamento-Per%C3%ADodo)
