---
article_id: 360025043391
category: RH - 13º salário
content_hash: ecb79afe1e5a254a4cd63c710bb793316ba827ba3fc8f665d423fd8cd146c242
fetched_at: '2026-06-28T22:44:00.812859+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - ID 0670 é calculado em avos ou em dias
type: support-article
updated_at: '2025-08-13T14:42:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025043391-RH-Linha-Protheus-GPE-ID-0670-%C3%A9-calculado-em-avos-ou-em-dias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19057594042135) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**

**ID 0670,** o calculo é em avos ou em dias?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

A partir da atualização do fonte GPEXC131.PRX data de 12/02/2019 sistema passou a realizar o calculo em dias de acordo com a INSTRUÇÃO NORMATIVA RFB Nº 971, DE 13 DE NOVEMBRO DE 2009.

Por conta da obrigatoriedade do eSocial, com a criação dos proventos referentes ao 13 salário maternidade, viu-se a necessidade de adaptar os valores gerados nas verbas de 13º salário maternidade para que estas fiquem de acordo com a dedução, pois tais verbas serão utilizadas para esse fim, e não mais a verba de ID0670.

Logo, as verbas de 13 Maternidade 1ª e 2ª Parcela (bem como as médias, adicionais), seguirão a mesma regra de cálculo da dedução.

Exemplo:

Salario = 1000,00

Afastamento de 120 dias de maternidade, iniciando em 16/06/2018.

Considerando 12/12 de 13 salário.

**Cálculo antigo**:

Nesse cenário, o sistema apurará 9/12 como sendo trabalhados.

A mesma situação poderia ocorrer para afastamentos finalizados em anos posteriores ao cálculo do 13º.

2 Parcela 13 Salário: 1000,00 / 12 \* 9 = 750,00

2 Parcela 13 Salário s/ Maternidade: 1000,00 / 12 \* 3 = 250,00

Dedução: (1000,00 / 12) / 30 \* 120 = 333,33

**Cálculo Novo:**

2 Parcela 13 Salário s/ Maternidade: (1000,00 / 12) / 30 \* 120 = 333,33

2 Parcela 13 Salário: (1000,00 / 12 \* 9) - 333,33 = 416,67

Dedução: (1000,00 / 12) / 30 \* 120 = 333,33

**Importante**

1 - Devido à estrutura do layout do eSocial, entendemos que a dedução da maternidade não deve ser realizada mês a mês, mas toda na 2º parcela do 13º. Em virtude disso, o parâmetro MV\_SALMGRP deve ficar com N. Também no manual da SEFIP existe a orientação de que a verba deve ser gerada apenas na competência do 13º Salário (ou em rescisões).

2 - A princípio as referências das verbas permanecerão como estão, em avos, pois entendemos que nossos clientes estão habituados com essa forma de demonstração.

3 - A nova estrutura de cálculo também será aplicada para os adicionais (ATS, Insalubridade, Periculosidade, Confiança e Transferência), e também para as médias.

4 - Para que as verbas sejam quebradas no cálculo da 1 parcela, 2 parcela, é necessário que o campo RCM\_DECIMO esteja configurado com SIM no cadastro dos Tipos de ausência.

Documentação: <http://tdn.totvs.com/pages/releaseview.action?pageId=454846875>

**Saiba Mais**  
[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
