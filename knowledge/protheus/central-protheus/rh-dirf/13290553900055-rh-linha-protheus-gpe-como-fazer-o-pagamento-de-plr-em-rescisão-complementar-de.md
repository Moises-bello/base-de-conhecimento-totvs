---
article_id: 13290553900055
category: RH – DIRF
content_hash: 7399c2c2d54752a1f420ce2c21eecff9ee114cf79d9ad089bb3a2cba0a074e74
fetched_at: '2026-06-28T22:44:06.876165+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como fazer o pagamento de PLR em rescisão complementar
  de forma que carregue a informação para a DIRF como residente no exterior
type: support-article
updated_at: '2025-08-15T11:50:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13290553900055-RH-Linha-Protheus-GPE-Como-fazer-o-pagamento-de-PLR-em-rescis%C3%A3o-complementar-de-forma-que-carregue-a-informa%C3%A7%C3%A3o-para-a-DIRF-como-residente-no-exterior
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34203849273751) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como fazer o pagamento de PLR em rescisão complementar para ex funcionário que reside no exterior de forma que carregue a informação para a DIRF como residente no exterior?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para que valores a PLR pago em rescisão complementar para residente no exterior seja enviada no bloco de expatriados na DIRF, siga os passos abaixo:

1. Crie uma verba sem ID para o lançamento na rescisão complementar conforme orientação [RH - Linha Protheus - GPE - Como cadastrar verbas no Protheus,](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411677253783) informe incidência A para a DIRF;

2. No cadastro do **Funcionário**, pelo caminho **>Atualizações >Funcionários >Funcionários**, na aba Endereço, informe que o funcionário é residente no exterior:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13289973309719)  
  
3. Lance o valor a ser pago na rescisão complementar na verba sem ID criada, para o passo a passo de cálculo de rescisão complementar, [CLIQUE AQUI;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021889631)

4. Em **Histórico Contratos**, pelo caminho **>Atualizações >Funcionários >Histórico Contrato,** informe os dados de residente exterior conforme seu cenário:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13290295217559)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13290365790999)

5. Execute a rotina Gerar Arquivo conforme [passo a passo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437012);

6. Os dados serão gerados em Manutenção Arquivo conforme código de retenção e dados informado em Histórico Contratos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13290392758295)

7. Gere o arquivo magnético da DIRF conforme [passo a passo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022076092);

8. No arquivo magnético, o registro será gerado no bloco RPDE conforme abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13290509571223)

**Saiba mais**  
[RH - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)   
[Consultoria de segmentos - Expatriados - Apuração do Imposto de Renda Brasileiros que vão trabalhar no Exterior](https://tdn.totvs.com/pages/releaseview.action?pageId=266971250)
