---
article_id: 360060132053
category: RH - 13º salário
content_hash: 9e324c9cc08f5b17f7df4aba4da9996579c7b9da40f4cc1a04fc2dd4f7197c19
fetched_at: '2026-06-28T22:44:00.600308+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como considerar médias de 13º para calcular ATS
  de 13º sobre verbas
type: support-article
updated_at: '2025-08-20T14:11:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060132053-RH-Linha-Protheus-GPE-Como-considerar-m%C3%A9dias-de-13%C2%BA-para-calcular-ATS-de-13%C2%BA-sobre-verbas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26914880809751) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Como considerar médias de 13º para calcular ATS de 13º sobre verbas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Sistema não considera valor de médias que incidem para Adicional de Tempo de Serviço no valor de Adicional Por Tempo de Serviço 13º salário na 1ª Parcela do 13º Salário.  
  
**Solução**

Realizado ajuste para que o valor de ATS 13º Salário Sobre Verbas considere o valor das médias em sua base de cálculo.  
  
Os IDs abaixo devem ser configurados com "Sim" para Ref. 13º Salário (RV\_REF13) e ATS (RV\_ADICTS):

* Médias Valor 1ª Parc (id 1628)
* Médias Horas 1ª Parc (id 1629)
* ATS 13ºS+V 1ª Parc (id 1631)

Quando no cadastro do sindicato a parametrização para calculo dos adicionais for de Salario + Verbas, o sistema irá considerar para base de cálculo do adicional as verbas que estiverem com SIM para o adicional em questão. No exemplo, as verbas que devem compor a base do ATS sobre verbas devem ficar como SIM no campo ATS.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10400994121879)

**Saber Mais:**

[RH - Linha Protheus - GPE - Como parametrizar o Sistema para que não considere médias na 1ª parcela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016402511-RH-Linha-Protheus-GPE-Como-parametrizar-o-Sistema-para-que-n%C3%A3o-considere-m%C3%A9dias-na-1%C2%AA-parcela?source=search)

[RH - Linha Protheus - GPE - Sistema não calcula verbas de médias no 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016249711-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-calcula-verbas-de-m%C3%A9dias-no-13%C2%BA-sal%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Apuração das médias do 13º não batem com o cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019896372-RH-Linha-Protheus-GPE-Apura%C3%A7%C3%A3o-das-m%C3%A9dias-do-13%C2%BA-n%C3%A3o-batem-com-o-c%C3%A1lculo?source=search)

[RH - Linha Protheus - GPE - Separação Adicionais e Médias 1ª Parcela do 13º Salário Maternidade (Criação IDs de cálculo 1639 ao 1648 e IDs 1653 a 1654)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454112-RH-Linha-Protheus-GPE-Separa%C3%A7%C3%A3o-Adicionais-e-M%C3%A9dias-1%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio-Maternidade-Cria%C3%A7%C3%A3o-IDs-de-c%C3%A1lculo-1639-ao-1648-e-IDs-1653-a-1654-?source=search)

[RH - Linha Protheus - GPE - Separação dos Adicionais e Médias da 1ª Parcela do 13º Salário (Criação IDs de cálculo 1628 ao 1637)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016051891-RH-Linha-Protheus-GPE-Separa%C3%A7%C3%A3o-dos-Adicionais-e-M%C3%A9dias-da-1%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio-Cria%C3%A7%C3%A3o-IDs-de-c%C3%A1lculo-1628-ao-1637-?source=search)  
[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
