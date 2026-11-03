---
article_id: 1500003366622
category: RH - Férias
content_hash: ebe12345dedb46170e6bd09ee12eaae8f85f09c56dcd3b962ad67e56d5df17e9
fetched_at: '2026-06-28T22:43:58.276773+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Férias Proporcionais dividindo por 31 dias
type: support-article
updated_at: '2025-08-28T18:24:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003366622-RH-Linha-Protheus-GPE-F%C3%A9rias-Proporcionais-dividindo-por-31-dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31880962127767) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Ao calcular Férias, seu valor proporcional está sendo dividido por **31** dias e não por **30.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Parâmetro **MV\_DIASPER** está = **1 -** Divisor será a **quantidade de dias do mês**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10656841064343)  
  
**Solução**Caso o parâmetro **MV\_DIASPER** esteja = **1,** é necessário alterar o conteúdo para 2 - Divisor **sempre igual a 30**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10656881732503)  
  
Caso possua períodos já **criados e abertos** **antes dessa alteração**, deve ajustar manualmente o número de dias para cálculo. Para isso, acesse **Atualizações/** **Definições de Cálculo/ Períodos**, altere o período desejado e na aba **Cadastro de Calendário**, altere o campo **Dias Calculo para 30.**

 

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10656945525911)

**Saiba Mais**[RH - Linha Protheus - GPE - Recalculo de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420404618903-RH-Linha-Protheus-GPE-Recalculo-de-F%C3%A9rias-?source=search)  
[RH - Linha Protheus - GPE - Como configurar o parâmetro MV\_DIASPER para definir regra de](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059317953-RH-Linha-Protheus-GPE-Como-configurar-o-par%C3%A2metro-MV-DIASPER-para-definir-regra-de-calculo)  
[RH - Linha Protheus - GPE - Impressão Relatório de Férias Calculadas - GPER550](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035142854-RH-Linha-Protheus-GPE-Impress%C3%A3o-Relat%C3%B3rio-de-F%C3%A9rias-Calculadas-GPER550)
