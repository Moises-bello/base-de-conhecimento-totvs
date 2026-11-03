---
article_id: 360059260673
category: RH - Provisão
content_hash: 907d83fdcf7a83d0bcc35f90e8f06e414e0aba024d9fda79bfc7f8a091ce2aa0
fetched_at: '2026-06-28T22:43:55.638860+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Baixas de 13º Salário na Provisão
type: support-article
updated_at: '2025-06-17T20:27:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059260673-RH-Linha-Protheus-GPE-Baixas-de-13%C2%BA-Sal%C3%A1rio-na-Provis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17717244978967) T**empo aproximado para leitura: **00:02:00 min**

**Dúvida**Como funciona a Baixa de 13º na Provisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Solução**As baixas de 13º Salário na Provisão ocorrem quando há a quitação do 13º salário em Dezembro, ou no desligamento do funcionário.  
  
1. Para que as baixas de 13º salário sejam geradas corretamente em Dezembro, é necessário que as verbas com identificadores de cálculo abaixo estejam cadastradas.   
Acesse: Atualizações / Definições de Cálculo / Verbas (GPEA040) e verifique se as verbas estão cadastradas.  
Os identificadores de cálculo são:

**0332 –** Baixa Provisão de 13º salário;  
**0333** – Baixa Adicional de Provisão de 13º salário;  
**0334** – Baixa Antecipação da 1ª parcela do 13º salário;  
**0335** – Baixa INSS Provisão do 13º salário;  
**0336** – Baixa FGTS Provisão do 13º salário;  
Observação: As verbas devem ser incluídas como Base Provento e sem incidências.  
  
2. Para que a Baixa ocorra em Dezembro, é necessário que o cálculo do roteiro 132 (2º Parcela do 13º Salário) já tenha sido processada, assim como a folha de pagamento de Dezembro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17716197127703)

3. Acesse: Miscelânea / Provisões / Provisões de Férias e 13º Salário (GPEA070) e processe os cálculos das provisões.  
Veja que serão geradas as verbas de Baixas de 13º Salário com os valores pagos de 2ª Parcela do 13º Salário e o saldo atual e os avos de direiro serão zerados.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17716804147735)

4. Acesse: Miscelânea / Provisões / Provisões de Férias e 13º Salário / Outras Ações / Imprimir 13º (GPER090) e preencha as perguntas para emissão do relatório de Provisão de 13º Salário.  
No relatório será apresentada a linha **Valor Baixa 13º Salário**, onde constarão os valores pagos ao funcionário.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17717092673943)

Para mais informações sobre as baixas de 13º salário no mês de desligamento do funcionário [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007260472-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Provis%C3%A3o-no-m%C3%AAs-de-Desligamento) 

**Saiba mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
