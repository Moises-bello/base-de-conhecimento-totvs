---
article_id: 36250817320343
category: RH - Rescisão
content_hash: b24619c1b6f675dddfe0011b8ad181baa72e13a0ff3fc19b6c5cfa145032ff23
fetched_at: '2026-06-28T22:43:48.529032+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de rescisão apresenta saldo negativo e
  insuficiência de saldo quando há desconto do eConsignado
type: support-article
updated_at: '2025-11-11T17:45:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36250817320343-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-rescis%C3%A3o-apresenta-saldo-negativo-e-insufici%C3%AAncia-de-saldo-quando-h%C3%A1-desconto-do-eConsignado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36250832907799) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
No módulo GPE, ao realizar o processo de **rescisão** contratual de um funcionário, verifica-se que o desconto do empréstimo **eConsignado** está gerando um **saldo negativo**, levando a um valor a pagar pela empresa.

**Ambiente**  
TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12

**Causa**  
Esse incidente ocorre, pois o sistema está aplicando descontos do empréstimo eConsignado na base de cálculo da rescisão, mesmo quando o valor a receber do funcionário é **insuficiente** para cobrir os descontos.  
  
Conforme analise junto a Consultoria de Segmentos, previsto no **artigo 7º da Portaria 435/2025**, o cálculo do percentual de **35%** deve ser aplicado sobre a **remuneração disponível do trabalhador**.   
  
Para a apuração dessa base, devem ser consideradas as **verbas com incidência de INSS**, deduzindo-se os descontos compulsórios.   
  
Se a rescisão **possui** base **INSS**, o calculo **irá ocorrer** mesmo sem liquido a receber.

**Solução**  
Sugestão para solucionar essa ocorrência:

1. Acesse o módulo de GPE e **atualizações > definições de cálculo > mnemônicos** e ajuste o **P\_DEDCONS**, informando uma **verba de desconto** (aviso prévio por exemplo), utilizando o formato "756".
2. Após ajustes, **recalcule** a **rescisão** do funcionário

**Importante**  
As ações sugeridas acima são de acordo com o entendimento do cliente, o que pode ou não estar de acordo com a legislação vigente.

**Saiba Mais**

[Orientações Consultoria de Segmentos - Crédito do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=939253541#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosCr%C3%A9ditodoTrabalhador-2.NormasApresentadaspeloCliente)
