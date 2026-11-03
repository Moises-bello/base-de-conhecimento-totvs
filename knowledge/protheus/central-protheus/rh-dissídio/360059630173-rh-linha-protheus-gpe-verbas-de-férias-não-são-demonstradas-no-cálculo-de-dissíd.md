---
article_id: 360059630173
category: RH - Dissídio
content_hash: 95034da35268c5473cf14734c06c6f92e5eb30530800153fbe8fcf7542b8119f
fetched_at: '2026-06-28T22:43:44.327532+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Verbas de férias não são demonstradas no cálculo
  de dissídio retroativo
type: support-article
updated_at: '2025-08-20T14:33:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059630173-RH-Linha-Protheus-GPE-Verbas-de-f%C3%A9rias-n%C3%A3o-s%C3%A3o-demonstradas-no-c%C3%A1lculo-de-diss%C3%ADdio-retroativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34317300514199) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Ao executar o cálculo de dissídio retroativo, as verbas de férias não são demonstradas na competência de gozo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Verifique as seguintes configurações:

1. Verifique se as verbas de férias estão vinculadas a uma verba de pagamento do dissídio retroativo. Siga as instruções da documentação abaixo - passo 04:  
[MP - GPE - Qual a configuração que antecede o cálculo do dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054351414-MP-GPE-Qual-a-configura%C3%A7%C3%A3o-que-antecede-o-c%C3%A1lculo-do-diss%C3%ADdio-retroativo?source=search)  
  
2. Verifique se a data de pagamento das férias é a mesma entre o cabeçalho de férias - tabela SRH, cálculo de férias - tabela SRR e o acumulado do funcionário - tabela SRD:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100229213)  
  
**Observação**: Mesmo que esse cálculo férias esteja enquadrado na MP 927, onde o pagamento foi realizado no 5º dia útil do mês subsequente, a data de pagamento nos campos sinalizados devem ser as mesmas.  
Exemplo: [MP - GPE - MP 927 - Como efetuar o calculo das ferias com pagamento no 5º dia útil dos mês subsequente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045055114-MP-GPE-MP-927-Como-efetuar-o-calculo-das-ferias-com-pagamento-no-5%C2%BA-dia-%C3%BAtil-dos-m%C3%AAs-subsequente?source=search)  
  
3. Verifique se a data de atualização do fonte GPEXCAL3 em seu ambiente está compatível com a última atualização liberada no pacote de expedição quinzenalmente:  
<https://suporte.totvs.com/portal/p/10098/download#000006/all/>  
  
Caso não esteja compatível, faça um backup do seu atual RPO, aplique o a atualização. Em seguida exclua o dissídio já calculado e calcule novamente.  
  
**Saiba mais:**<https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio>
