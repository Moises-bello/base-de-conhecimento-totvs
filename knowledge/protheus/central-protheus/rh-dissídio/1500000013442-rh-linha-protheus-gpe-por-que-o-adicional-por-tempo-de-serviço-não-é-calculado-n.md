---
article_id: 1500000013442
category: RH - Dissídio
content_hash: 75d164c7c9f92e95e8a9f2143331fc7958143e1cc6913d790e9db8c63efa4447
fetched_at: '2026-06-28T22:43:44.304959+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Por que o Adicional por Tempo de Serviço não é
  calculado no dissidio retroativo
type: support-article
updated_at: '2025-08-20T14:31:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000013442-RH-Linha-Protheus-GPE-Por-que-o-Adicional-por-Tempo-de-Servi%C3%A7o-n%C3%A3o-%C3%A9-calculado-no-dissidio-retroativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34317243877271) Tempo aproximado para leitura: 00:00:30 min**

**Dúvida**Por que o Adicional por Tempo de Serviço não é calculado no dissidio retroativo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**1 - Verifique se o **ATS - Adicional por Tempo de Serviço** está sendo calculado sobre **valor fixo ou sobre o salário mínimo**, na aba **Adic. Tempo. Serv**. no cadastro do **Sindicato**.

Em ambos os casos, só terá cálculo no dissidio se houver alteração no cadastro do Sindicato, no caso do valor fixo, na aba **Adic. Tempo. Serv**. no campo **Vlr.Triênio**, ou no cadastro da tabela **S004 - Tabela de Salário Mínimo**, no caso do salário mínimo.  
  
2 - Caso esteja sendo calculado sobre **salário**, valide se houve alguma alteração nas tabela **SR9** (alteração no cadastro do funcionário) ou na **RG4** (alteração no cadastro do sindicato), referente ao calculo do Adicional por Tempo de Serviço, pois se tiver alguma alteração com data posterior ao cálculo do dissidio o sistema não enxergará a alteração para a composição do cálculo.  
**Ex.**  
Cálculo do dissidio retroativo 09/2020 a 11/2020.

Feita uma alteração no sindicato referente ao Adicional por tempo de serviço no mês 12/2020.

O sistema não enxergará esta alteração para o cálculo do dissidio, a alteração deveria ter sido feita com a data base do sistema no mês 09/2020, pois qualquer alteração nestes dois cadastros, o sistema salva de acordo com a data base do sistema.  
  
**Saiba Mais**  
Para adquirir mais conhecimento acesse o(s) *link*(s) abaixo:  
[MP - GPE - Não é demonstrado a verba de adicional dentro do cálculo de dissídio, deixando as demais verbas negativas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038120993-MP-GPE-N%C3%A3o-%C3%A9-demonstrado-a-verba-de-adicional-dentro-do-c%C3%A1lculo-de-diss%C3%ADdio-deixando-as-demais-verbas-negativas?source=search)

[Página Centralizadora do Dissídio (GPEM690)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
