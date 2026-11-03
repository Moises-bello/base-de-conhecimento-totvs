---
article_id: 4414523041943
category: RH - 13º salário
content_hash: 6d1a006a4760a033bc7af757cc43e58cee0574db91e7c4662efdc5563cc31671
fetched_at: '2026-06-28T22:44:00.870935+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Pensão de 13 salário negativa no complemento do
  13º Salário, criação id 1679
type: support-article
updated_at: '2025-01-20T12:20:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414523041943-RH-Linha-Protheus-GPE-Pens%C3%A3o-de-13-sal%C3%A1rio-negativa-no-complemento-do-13%C2%BA-Sal%C3%A1rio-cria%C3%A7%C3%A3o-id-1679
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26169090721687) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Pensão de 13 salário negativa no complemento do 13º Salário, criação do identificador de cálculo 1679.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Ao calcular complemento 13º, pode ocorrer casos em que a pensão sobre o 13 salário dê valor negativo.  
Isso devida a mudança de percentual de desconto de beneficiário, ou mudança de configuração de verbas durante o cálculo do 13 salário e o cálculo do complemento, na folha de dezembro.  
  
Pensando nessa situação, foi realizada manutenção para que o sistema acate o valor negativo.  
Ocorre que para o eSocial, por exemplo, verbas com valores negativos sequer são transmitidas, ocasionando então divergência com o líquido da folha.  
  
No caso específico da pensão, como o valor já foi creditado na conta do beneficiário, na folha, ao gerar o desconto de pensão negativo, o valor é compensado ao funcionário mas como não há estorno do que já foi pago ao beneficiário, fica o ônus com a empresa.  
  
Nesse sentido, planejamos uma implementação para gerar a diferença de pensão como base (somente para quando houvesse esse tipo de "ressarcimento"), para então ficar a cargo da empresa decidir o destino desse valor.  
  
Para que a verba seja gerada, é necessário realizar a seguinte configuração.  
  
Cadastrar uma verba de BASE (PROVENTO) com o ID abaixo:

|  |  |  |
| --- | --- | --- |
| ID | Descrição | Tipo |
| 1679 | Base Pensão 13 Salário Devolução | Base (Provento) |

**Exemplo de cálculo:**Supondo que o funcionário X possua um beneficiário Y com desconto de pensão sobre o líquido, com percentual de 30%.  
  
No cálculo da 2 parcela do 13 salário, os proventos foram.  
2 Parcela = 2248,40  
Média Horas = 86,87  
Médias Valor = 14,79  
  
Nesse momento, a configuração da verba de INSS 13 Salário estava com NÃO para pensão.  
Logo, o valor da pensão ficou.  
       (2248,40 + 14,79 + 86,87) \* 30% = 705,01.  
  
Ao realizar o cálculo da folha de dezembro, foram lançadas algumas verbas de horas extras, gerando uma diferença de 13º.  
  
Durante também o cálculo da folha, o usuário identificou que a verba de INSS 13 Salário estava com a configuração incorreta e alterou o seu registro, colocando SIM para Pensão.  
  
Nesse momento, supondo que o sistema gerou na folha os seguintes valores de diferença de 13 salário.

       Diferença 13º - R$1,19  
       Inss 13º - R$0,11  
  
Dessa forma, o sistema apurará o seguinte valor de pensão.

       (2248,40 + 14,79 + 86,87 + 1,19 – 211,50 – 0,11) \* 30% = 641,89  
       641,89 - 705,01 = - R$63,12.  
  
Logo, o sistema gerará a verba de ID1679 com valor positivo de R$63,12, onde a empresa ficará responsável de como destinar tal valor.

**Saber Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Desconto de pensão alimentícia na 2º Parcela do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016145152-RH-Linha-Protheus-GPE-Desconto-de-pens%C3%A3o-aliment%C3%ADcia-na-2%C2%BA-Parcela-do-13%C2%BA-Sal%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Desconto de pensão alimentícia na 2º Parcela, quando já ocorreu desconto na 1° Parcela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10784734204951-RH-Linha-Protheus-GPE-Desconto-de-pens%C3%A3o-aliment%C3%ADcia-na-2%C2%BA-Parcela-quando-j%C3%A1-ocorreu-desconto-na-1-Parcela?source=search)

[RH - Linha Protheus - GPE - Desconto de pensão alimentícia na 1º Parcela do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10771368342551-RH-Linha-Protheus-GPE-Desconto-de-pens%C3%A3o-aliment%C3%ADcia-na-1%C2%BA-Parcela-do-13%C2%BA-Sal%C3%A1rio?source=search)  
[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
