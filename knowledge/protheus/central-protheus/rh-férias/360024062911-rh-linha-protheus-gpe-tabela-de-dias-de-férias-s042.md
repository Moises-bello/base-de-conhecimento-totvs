---
article_id: 360024062911
category: RH - Férias
content_hash: 8d4972f3183e65007a4ac3e0611e2ef48e4206efdc94cd43ef6c00c650605089
fetched_at: '2026-06-28T22:43:59.242417+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Tabela de Dias de Férias - S042
type: support-article
updated_at: '2025-09-02T18:03:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024062911-RH-Linha-Protheus-GPE-Tabela-de-Dias-de-F%C3%A9rias-S042
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26439786737303) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como realizar no módulo **Gestão de Pessoal** a configuração para calcular **férias** diferente de 30 dias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Quando existe pagamento diferenciado para dias de **férias** de acordo regras específicas de sindicatos ou mesmo por ações coletivas e entendimento da empresa, o sistema permite a configuração através do preenchimento da tabela **S042 - Dias de Férias**.

Para configurar a tabela S042 - Dias de Férias acesse **Atualizações/ Definições de Cálculos/  Manutenção Tabelas (GPEA320)/ selecione a tabela S042/ Clique em Incluir.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26439786744599)**

Na tabela **S042** são definidos os parâmetros para cálculo de quantidade de dias de direito de férias do funcionário.

**Filial:** para a qual será utilizada a tabela (se vazio, será utilizado para todas)  
**Sindicato:** para o qual será utilizado a tabela  
**Nr. Meses do Período:** Número de meses de cada período aquisitivo (normalmente 12)  
**Número de Períodos:** Será sempre "0" (Zero).  
**Dias Trabalhados no Mês:** Número de dias que o funcionário deverá trabalhar no mês para adquirir direito a 1/12 avos de férias. Normalmente 15, pois o colaborador precisa ter no mínimo 15 dias trabalhados, terá direito a 1/12 (conteúdo do campo "Fator de Férias")  
**Fator de Férias:**Número de Dias correspondente a 1/12 avos do período (Normalmente 2.5). Se 2.5, indica que no final do período (12 meses) o funcionário terá direito a 30 dias de férias (2.5 x 12). Se os dias do período corresponderem a 45 dias, deverá ser informado 3.75 dias ( 3.75 x 12 = 45).

**Exemplo:**

Para Radiologista o preenchimento ficaria :

**Nr. Meses do Período:** 6  
**Número de Períodos:** 0  
**Dias Trabalhados no Mês:** 15  
**Fator de Férias:**3.3334  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26439772760471)  
  
**Saiba Mais**[RH - Férias](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597291-RH-F%C3%A9rias)

[Manual de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=941247504)
