---
article_id: 360058234133
category: 'RH - Verbas '
content_hash: b6727adcc301066f91e279f7841ba7e5410a76fe13d1ad0b59bd0968ac5fd991
fetched_at: '2026-06-28T22:43:20.142273+00:00'
product: protheus
section_id: 360010838314
source: central-protheus
title: RH - Linha Protheus - GPE - Qual a finalidade do campo Fech Compete no cadastro
  de verbas
type: support-article
updated_at: '2025-02-18T11:49:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058234133-RH-Linha-Protheus-GPE-Qual-a-finalidade-do-campo-Fech-Compete-no-cadastro-de-verbas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19663413695255)** Tempo aproximado para leitura: **00:01:30 min**

**Ocorrência**Qual a finalidade do campo "Fech Compete" no cadastro de verbas?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal - A partir da versão 12.  
  
**Solução**

Dentro do cadastro de verbas, existe o campo **"Fech Compete"** (RV\_FECCOMP).  
  
Esse campo é utilizado durante a execução do fechamento do período, objetivamente define se a verba será fechada por período ou por competência.

A diferença é que se a verba estiver configurada com SIM, ela será paginada na próxima COMPETÊNCIA do cálculo e se a verba estiver configurada com NÃO, ela será paginada no próximo PERÍODO do cálculo.

Abaixo um exemplo do funcionamento do campo:  
  
- Funcionário gozou férias de 14/02/2019 a 15/03/2019.

No cálculo das férias, serão geradas as verbas de Férias Mês e Férias Mês Seguinte.

Supondo que a empresa precisou cadastrar uma folha complementar para pagamento de verbas que não foram pagas na folha original.  
  
Então no cadastro de períodos, teremos:

Período 201902 - Pagamento 01 → Folha Original.

Período 201902 - Pagamento 02 → Folha Complementar.

Período 201903 - Pagamento 01 → Folha Original.

Se as verbas de férias de férias mês seguinte estiverem configuradas com o FECH COMPETE igual a NÃO, ao realizar o fechamento da folha, tais verbas serão paginadas no período 201902 pagamento 02.

Contudo, se as verbas estiverem configuradas com SIM, ao realizar o fechamento da folha, tais verbas serão paginadas no período 201903 pagamento 01

**Campo Fech Compete.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19663429872279)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19663413698967)**

**Saiba mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como efetuar o cálculo de folha complementar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018943752-RH-Linha-Protheus-GPE-Como-efetuar-o-c%C3%A1lculo-de-folha-complementar)

[RH - Linha Protheus - GPE - Configuração de verbas mês seguinte quando existe folha complementar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033431594-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-de-verbas-m%C3%AAs-seguinte-quando-existe-folha-complementar)

[RH - Linha Protheus - GPE - Qual a finalidade do campo Fech Compete no cadastro de verbas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058234133-RH-Linha-Protheus-GPE-Qual-a-finalidade-do-campo-Fech-Compete-no-cadastro-de-verbas)
