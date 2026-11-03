---
article_id: 360058710734
category: RH - 13º salário
content_hash: 999c5dd65fe68e6364784695c85f6c11fbfb755659de058cd21ec2e432098947
fetched_at: '2026-06-28T22:44:00.864606+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - O que conferir quando não gera valores de Médias
  no 13º Salário 2ª Parcela
type: support-article
updated_at: '2025-01-17T18:07:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058710734-RH-Linha-Protheus-GPE-O-que-conferir-quando-n%C3%A3o-gera-valores-de-M%C3%A9dias-no-13%C2%BA-Sal%C3%A1rio-2%C2%AA-Parcela
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18913972099735) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**O que conferir quando não gera valores de Médias no 13º Salário 2ª Parcela?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**1. Acesse: Atualizações / Definições de Cálculo / Verbas (GPEA040) e Verifique no cadastro de verbas se os identificadores de cálculo referente as médias de 13º 2ª parcela, **0123** - Médias 13º Salário Valor e **0124** - Média 13º Salário Horas, foram criadas com tipo **Base**.   
Em caso positivo, retire o identificador de cálculo das verbas em questão, crie duas novas verbas, do tipo **Provento,** e amarre os id's 0123 e 0124.   
  
2. Acesse> Miscelanea / Cálculos / Por roteiro (GPEM020) e ao processar o cálculo do Roteiro 132, verifique se a pergunta "**Referência para Média?**" está preenchida com o último dia do Ano Corrente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18913939291031)

**Saiba Mais:**  
[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
