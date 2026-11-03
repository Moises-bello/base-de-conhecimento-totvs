---
article_id: 360060245733
category: 'RH - Verbas '
content_hash: 0b5796d14897c3352466d8b4dae51a81ca024e81c9db868c65c4d1037ca4ee50
fetched_at: '2026-06-28T22:43:20.107321+00:00'
product: protheus
section_id: 360010838314
source: central-protheus
title: RH - Linha Protheus - GPE - Configuração para pagamento de Adicional de Substituição
type: support-article
updated_at: '2025-02-18T14:19:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060245733-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-para-pagamento-de-Adicional-de-Substitui%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30061382131991) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Quais as configurações básicas para verba/rubrica de **Adicional de Substituição?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução**Ter a verba de **Adicional de Substituição** cadastrada, que deve conter o *Id* de cálculo **1373,** e ser do **tipo dias**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098845994)

O cálculo será efetuado pela fórmula S\_SUBSTITU, onde o sistema vai olhar o parâmetro MV\_VDFDCOM para obter o percentual do cálculo de Salário Substituição, e a tabela RI8 - Controle de Substituições.   
  
**Importante**  
**O ID 1373 é calculado somente no módulo 61 - Gestão de Folha de Pagamento Público, para servidores Públicos que cobrem ausências de outros servidores.**  
  
Para o módulo **07 - Gestão de Pessoal,** caso a empresa necessite pagar o Adicional em questão, é necessário criar uma verba de Provento, sem ID de cálculo, do tipo Valor, e efetuar o lançamento através da rotina lançamento por funcionário, lançamento por Verba ou lançamentos fixos.

**Saiba mais**

[RH - Linha Protheus - GPE - Como parametrizar o Lançamento Fixo de uma verba](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028940832-RH-Linha-Protheus-GPE-Como-parametrizar-o-Lan%C3%A7amento-Fixo-de-uma-verba?source=search)

[RH - Linha Protheus - GPE - Como realizar o cálculo do lançamento pela rotina Lançamentos por funcionários GPEA580](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061023733-RH-Linha-Protheus-GPE-Como-realizar-o-c%C3%A1lculo-do-lan%C3%A7amento-pela-rotina-Lan%C3%A7amentos-por-funcion%C3%A1rios-GPEA580?source=search)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Verbas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010838314-RH-Verbas)
