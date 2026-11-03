---
article_id: 360059317953
category: RH - Folha de Pagamento
content_hash: 009a25e93d21ac819bc7beb49aeb06e7ef7ccc22f0b9c5d1599970e2db29bc31
fetched_at: '2026-06-28T22:44:13.315745+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o parâmetro MV_DIASPER para definir
  regra de calculo
type: support-article
updated_at: '2024-09-10T11:59:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059317953-RH-Linha-Protheus-GPE-Como-configurar-o-par%C3%A2metro-MV-DIASPER-para-definir-regra-de-calculo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26264880241815)** Tempo aproximado para leitura**: 00:02:00 min**

**Dúvida**Como configurar o calculo de dias da folha ou definir como será a regra de calculo, se será considerado o divisor por 30 dias ou a quantidade dias do mês? Como realizar a configuração do parâmetro MV\_DIASPER?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.25  
  
**Solução**O parâmetro MV\_DIASPER define como será a regra de calculo em relação aos dias do mês, se será considerado o divisor por 30 dias ou a quantidade dias do mês.

Para verificar a configuração do parâmetro , acesse o módulo configurador em **Base de Dados -> Dicionário -> Base de Dados**, selecione a opção **Parâmetro** e procure por **MV\_DIASPER:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8101105470487)

**Parâmetro com 1** - Divisor será a quantidade de dias do mês: O sistema irá considerar para a regra de calculo a divisão sobre os dias do mês. Será validado no cadastro de períodos a quantidade de dias do período que consta no campo **Dias Cálculo/Dias Mês** na aba **Cadastro de Calendário**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8101031008023)

**Parâmetro com 2** - Divisor será sempre 30: O divisor para calculo será considerado sempre 30 dias, independente da quantidade de dias mês do período:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8101034507799)

**Saber Mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - O sistema está considerando 30 dias de referência no calculo da folha, para funcionário afastado em meses de 31 dias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015451892-RH-Linha-Protheus-GPE-O-sistema-est%C3%A1-considerando-30-dias-de-refer%C3%AAncia-no-calculo-da-folha-para-funcion%C3%A1rio-afastado-em-meses-de-31-dias-?source=search)

[RH - Linha Protheus - GPE - Como sistema calcula folha de pagamento para funcionário afastado, com MV\_DIASPER igual a 2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015099431-RH-Linha-Protheus-GPE-Como-sistema-calcula-folha-de-pagamento-para-funcion%C3%A1rio-afastado-com-MV-DIASPER-igual-a-2?source=search)

[RH - Linha Protheus - GPE - Como fazer para que o sistema considere o dia 31 no mês de retorno do afastamento para montagem do saldo de salário proporcional do empregado, mesmo que mensalista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000010482-RH-Linha-Protheus-GPE-Como-fazer-para-que-o-sistema-considere-o-dia-31-no-m%C3%AAs-de-retorno-do-afastamento-para-montagem-do-saldo-de-sal%C3%A1rio-proporcional-do-empregado-mesmo-que-mensalista?source=search)

[RH - Linha Protheus - GPE - Como efetuar o cadastro de período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052262653-RH-Linha-Protheus-GPE-Como-efetuar-o-cadastro-de-per%C3%ADodo?source=search)

[RH - Linha Protheus - GPE - Férias Proporcionais dividindo por 31 dias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003366622-RH-Linha-Protheus-GPE-F%C3%A9rias-Proporcionais-dividindo-por-31-dias-?source=search)
