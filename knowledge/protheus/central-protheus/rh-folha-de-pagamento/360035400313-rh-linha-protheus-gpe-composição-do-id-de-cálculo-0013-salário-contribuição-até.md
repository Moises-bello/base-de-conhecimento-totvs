---
article_id: 360035400313
category: RH - Folha de Pagamento
content_hash: a0d8b56d32403a257ab915cef4cda4a5e9fbeb85a02cfef0077303f9a134b56b
fetched_at: '2026-06-28T22:44:14.836158+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Composição do ID de Cálculo 0013 - Salário Contribuição
  Até Limite e 0014 - Salário Contribuição Acima do Limite
type: support-article
updated_at: '2025-09-12T14:42:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035400313-RH-Linha-Protheus-GPE-Composi%C3%A7%C3%A3o-do-ID-de-C%C3%A1lculo-0013-Sal%C3%A1rio-Contribui%C3%A7%C3%A3o-At%C3%A9-Limite-e-0014-Sal%C3%A1rio-Contribui%C3%A7%C3%A3o-Acima-do-Limite
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26247467450519) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Composição do ID de Cálculo 0013 - Salário Contribuição Até Limite e 0014 - Salário Contribuição Acima do Limite  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas - Todas as versões  
  
**Solução**A composição do ID 0013, são as verbas calculadas na folha, que estão com SIM para INSS, observando o teto máximo da Base de INSS, definido na tabela S001 em manutenção de tabelas (Versão 12) ou no Parâmetro 08 (Versão 12), e o ID 0014, são as verbas calculadas na folha, que estão com SIM para INSS, porém que ultrapassam o teto máximo definido na tabela S001 (Versão 12) ou Parâmetro 08 (Versão 11).  
 **Exemplo:**

Acesse **Gestão de Pessoal > Atualizações > Definições de Cálculo > Parâmetro 08 (Versão 11) ou Atualizações > Definições de Cálculo > Manutenção de Tabelas > Tabela S001 (Versão 12)  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10844087923607)**

Acesse **Gestão de Pessoal > Atualizações > Lançamentos > Lançamentos Mensal (Versão 11) ou Consultas - Cálculos - Por Funcionário (Versão 12)  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10844408033303)****ID 0013** (Salário contribuição até limite base), destacado em amarelo na imagem acima, sempre que o sistema ultrapassar o limite de base de cálculo do **INSS**, o sistema automaticamente buscará do **parâmetro 08 (Versão 11) ou S001 (Versão 12)** o teto para cálculo, que neste exemplo está com R$ 7.087,22,ou seja, basicamente o sistema levará para essa verba o **Teto Máximo** definido na tabela S001 caso o total de verbas com Sim para INSS ultrapasse o limite, ou então o total caso a soma seja inferior ao limite.

**ID0014** (Salário Contribuição Acima Limite Base), destacado em vermelho na imagem acima, calculará verbas que estão com **Sim** para**INSS** abatendo o que já foi gerado no ID 0013, exemplo: **somando as verbas com sim para INSS que são 001/006/017 e 142= R$ 12.570,60 – 7.087,22  da Verba com ID 0013= 5.483,38** que é o valor que ultrapassou o teto sem gerar desconto de **INSS**.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
