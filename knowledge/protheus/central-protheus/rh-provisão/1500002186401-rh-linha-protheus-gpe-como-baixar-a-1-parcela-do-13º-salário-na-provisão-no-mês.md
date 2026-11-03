---
article_id: 1500002186401
category: RH - Provisão
content_hash: 67d2879d2cd2071921fe3c9be4e9075836c11479958b4183b8478bbfb7a09c01
fetched_at: '2026-06-28T22:43:55.699880+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Baixar a 1 Parcela do 13º Salário na Provisão
  no mês de Desligamento
type: support-article
updated_at: '2025-10-24T11:56:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002186401-RH-Linha-Protheus-GPE-Como-Baixar-a-1-Parcela-do-13%C2%BA-Sal%C3%A1rio-na-Provis%C3%A3o-no-m%C3%AAs-de-Desligamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998824264983)** Tempo aproximado para leitura: **00:00:30 min**

**Dúvida**Como Baixar a 1 Parcela do 13º Salário na Provisão no mês de Desligamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Quando o parâmetro **MV\_PROVRES** está configurado com **N**, ao realizar os cálculos das **Provisões de 13º Salário** de um funcionário demitido, o sistema não gera a verba de Baixa da 1ª Parcela do 13º salário, apesar de exibir a baixa ao gerar o relatório da Provisão de 13º Salário.  
  
Para implementar a solução nos cálculos de Provisão, siga o passo a passo:  
  
1. Aplique o Pacote de Atualização de acordo com a Versão e Release de sua base:

[Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
  
2. Acesse: Atualizações / Definições de Cálculo / **Verbas** (GPEA040) / Clique em **Incluir**e cadastre uma nova verba com o Id de Cálculo **1854**.  
Observação: A verba deverá ser criada como **Base Provento**, e para facilitar na criação da verba, utilize como base a verba de Id de Cálculo 0334.  
  
3. Exclua os Cálculos de Provisão do funcionário desligado.  
Para mais informações sobre como Excluir os Cálculos de Provisão, [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036636774-MP-GPE-Como-Excluir-o-C%C3%A1lculo-das-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio) .  
  
4. Acesse: Miscelânea / Provisões / **Provisões de Férias/13º Salário**(GPEA070), e Processe os cálculos de Provisão somente para o funcionário desligado.

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)

<https://tdn.totvs.com/pages/releaseview.action?pageId=592553661>
