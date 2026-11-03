---
article_id: 8866127138967
category: RH - Provisão
content_hash: a435728c2d40923a336c2f0533b8e9c790981aeacbb0ebbf6e4032417472e219
fetched_at: '2026-06-28T22:43:55.863126+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Conceito de configuração dos adicionais de horas
  extras com "S" para médias e "SIM" para incorpora salário
type: support-article
updated_at: '2025-10-24T13:13:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8866127138967-RH-Linha-Protheus-GPE-Conceito-de-configura%C3%A7%C3%A3o-dos-adicionais-de-horas-extras-com-S-para-m%C3%A9dias-e-SIM-para-incorpora-sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32904202891799) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Conceito de configuração dos adicionais de horas extras com "S" para médias e "SIM" para incorpora salário.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -Gestão de Pessoal – A partir da versão 12.

**Solução**  
1) Vamos avaliar a verba 170 (hora extra 100%) calculada na folha de pagamento:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8892299980695)

2) Configuração das verbas com INCORPORA SALÁRIO= SIM e Médias = S  
MV\_MEDDIRE = N  
Cadastro de sindicatos = 0 

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8892661163287)

3) Relatório de provisão apresentando adicionais no valor de R$ 65,16:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8892729705623)

4) De acordo com o cálculo da folha e a configuração da verba 170, vamos apresentar como o sistema   se comporta para composição do adicional:   
  
Considerando que agora temos adicional de periculosidade e 1 verbas (170) configuradas como sim    para médias e sim para incorpora salário no cadastro de verbas:   
  
Adicional de periculosidade: R$ 600,00 / 12 avos = R$ 50,00  
Médias (verbas 170) = R$ 90,91/12 = R$ 7,58  
Incorpora salário (verba 170) = R$ 90,91/12 = R$ 7,58  
Adicionais do relatório : R$ 50,00 + R$ 15,16 = R$ 65,16  
  
**Observação:** De acordo com esta configuração na verba, veja que a hora extra é considerada 2 vezes no cálculo dos adicionais, seguindo a lógica de ser média e fazer parte de salário (salário incorporado).  
  
**Importante:**

O relatório de Médias apresentará apenas o valor referente à configuração das médias (Média Férias = S), uma vez que as outras configurações de adicionais são tratadas automaticamente pelo ID de cálculo da periculosidade (verba 060 do print) e pelo campo Incorpora salário (da verba 170) como parte do salário.   
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8894605125911)

**Saiba Mais:**[RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o) [Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
