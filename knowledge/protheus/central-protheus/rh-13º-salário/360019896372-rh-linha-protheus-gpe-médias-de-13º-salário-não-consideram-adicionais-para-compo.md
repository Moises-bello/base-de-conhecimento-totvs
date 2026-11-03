---
article_id: 360019896372
category: RH - 13º salário
content_hash: f946f27d4f2a2b4b4e95c5ce2f4c54b2c068523383e7a9ec7c8da5ac87382e43
fetched_at: '2026-06-28T22:44:00.844857+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Médias de 13º Salário não consideram adicionais
  para compor o salário incorporado
type: support-article
updated_at: '2025-08-13T14:48:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019896372-RH-Linha-Protheus-GPE-M%C3%A9dias-de-13%C2%BA-Sal%C3%A1rio-n%C3%A3o-consideram-adicionais-para-compor-o-sal%C3%A1rio-incorporado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19058368216855) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**Ao conferir o Relatório de Médias de 13º Salário, os adicionais por tempo de serviço, periculosidade, insalubridade, cargo de confiança e adicional de transferência não estão sendo considerados no salário incorporado.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Este incidente ocorre porque a configuração das verbas de adicionais estão incorretas.  
Veja no exemplo abaixo que o sistema demonstra no cabeçalho do relatório de médias GPER080 o valor do adicional de insalubridade, porém o adicional não está sendo considerado no salário incorporado.  
Com isto, as médias não são calculadas considerando a remuneração atual do funcionário, apenas com o salário:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10436522386327)  
  
  
**Solução**Se o Funcionário possui algum adicional como o ATS, periculosidade, insalubridade, cargo de confiança ou adicional de transferência que incorpore o salário na folha de pagamento, é necessário que as verbas de adicionais de 13º salário também incorporem o salário do funcionário, para que o cálculo das médias seja realizado considerando a remuneração do funcionário.  
  
No Exemplo abaixo, temos um funcionário com cálculo de insalubridade que incorpora na folha, portanto, a verba com Id 1634 - Insalubridade 13º Salário 1ª Parcela também deverá incorporar.

Para solucionar este incidente, realize os passos abaixo:  
  
1. Acesse no Módulo Gestão de Pessoal **Atualizações / Definições de Cálculo / Verbas**, localize a verba de adicional da folha (neste exemplo, a verba de Insalubridade Máxima) e clique em Visualizar, e verifique se na aba Incidências, o campo **Incorp. Sal** (RV\_INCORP) está Preenchido com Sim:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10436839725719)

2. Localize a verba do Adicional de 13º Salário, e clique em Alterar. Altere o conteúdo do campo **Incorp. Sal** (RV\_INCORP) para Sim, para que a mesma configuração da verba de folha seja refletida no 13º Salário e salve. No caso da Insalubridade, a verba de 13º salário tem o Id de Cálculo 1634:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10436904316311)

3. Em seguida, reprocesse os Cálculos de 13º Salário, emita o Relatório de Médias e confirme se o salário incorporado e as médias de pagamento sofreram alteração:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10436971840151)

**Dica:** Para facilitar a conferência dos valores de adicionais, emita o relatório de médias pela rotina de Consulta de Cálculo.

![GIF_13.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/10437390076951)

**Saiba Mais:**

Para Saber quais são as verbas de Adicionais de 13º Salário 1ª Parcela [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016051891-RH-Linha-Protheus-GPE-Separa%C3%A7%C3%A3o-dos-Adicionais-e-M%C3%A9dias-da-1%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio-Cria%C3%A7%C3%A3o-IDs-de-c%C3%A1lculo-1628-ao-1637-).

Para saber quais são as verbas de Adicionais de 13º Salário 2ª Parcela [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10479927089175).

Para saber quais são as verbas de Adicionais de 13º Salário Maternidade 1ª Parcela [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454112-RH-Linha-Protheus-GPE-Separa%C3%A7%C3%A3o-Adicionais-e-M%C3%A9dias-1%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio-Maternidade-Cria%C3%A7%C3%A3o-IDs-de-c%C3%A1lculo-1639-ao-1648-e-IDs-1653-a-1654-).

Para saber quais são as verbas de Adicionais de 13º Salário Maternidade 2ª Parcela [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10008359545879-RH-Linha-Protheus-GPE-Separa%C3%A7%C3%A3o-Adicionais-e-M%C3%A9dias-2%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio-Maternidade-Cria%C3%A7%C3%A3o-IDs-de-c%C3%A1lculo-1434-ao-1447-e-IDs-1651-a-1652-).  
[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
