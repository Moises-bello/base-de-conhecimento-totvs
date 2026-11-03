---
article_id: 17261701745431
category: RH - Dissídio
content_hash: 8afbf05df23812ffecbf457cc80d91cd2a2fc36da233cb9052c5581c59150251
fetched_at: '2026-06-28T22:43:43.458552+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Verbas que incorporam salário no cálculo de dissídio
type: support-article
updated_at: '2025-08-13T18:04:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17261701745431-RH-Linha-Protheus-GPE-Verbas-que-incorporam-sal%C3%A1rio-no-c%C3%A1lculo-de-diss%C3%ADdio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17261717189783) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Verbas que incorporam salário no cálculo de dissídio.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução**  
No cálculo de dissídio, quando uma verba esta parametrizada para incorporar ao salário (aba Incidências do cadastro da verba), indiferente de ser uma verba com ID de cálculo ou não e essa verba é calculada  em folha, o sistema carrega a verba para a rotina Histórico Salarial, sendo apresentada no reajuste aplicado: 

1) Cálculo da folha de pagamento com verba de adicional de transferência e Hora Extra 100% configuradas com o campo INCORPORA SÁLARIO = SIM  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17262543326743)

Print de tela do campo configurado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17262577400727)

2) Efetuamos o cálculo de dissídio da folha/período 01/2023, referente À folha apresentada no print 1:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17262652485783)

3) Geração do dissídio para alteração salarial e transporte de verbas para folha:![](https://centraldeatendimento.totvs.com/hc/article_attachments/17262731530263)

4) Após geração do dissídio para folha de pagamento, as verbas que incorporal salário e estão presentes na folha de pagamento são geradas no histórico salarial:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17262714131863)

**Observação:** Na consulta de cálculos anteriores que não ocorreu o passo a passo acima , as verbas podem ter sofrido alteração posteriormente ou verificar se no cálculo não existia a verba na competência de cálculo de dissídio retroativo.

**Saiba Mais:**  
[Página Centralizadora do Dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
