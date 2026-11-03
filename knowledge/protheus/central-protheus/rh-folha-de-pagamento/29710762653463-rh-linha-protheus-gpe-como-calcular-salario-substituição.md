---
article_id: 29710762653463
category: RH - Folha de Pagamento
content_hash: afa06947f5d65cb38ad32d56d978a219cbc157aefcbae709428eb02014b5f4f2
fetched_at: '2026-06-28T22:44:13.212005+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular Salario Substituição
type: support-article
updated_at: '2025-03-18T11:48:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29710762653463-RH-Linha-Protheus-GPE-Como-calcular-Salario-Substitui%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29710822471959) Tempo aproximado para leitura: **00:03:00min** **Dúvida**Como realizar o calculo do Salario Substituição?  
De acordo com o Artigo 450 da CLT, o salário substituição, deve ser pago ao funcionário que, independente do motivo, passa a exercer a função de outro funcionário por tempo variável.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões   
  
**Solução**

Visando atender as necessidades de nossos clientes no tocante ao cálculo do salário substituição, foi disponibilizada a nova rotina "**Períodos de Substituição**" (GPEA946), que deverá ser incluída no menu [Framework - Linha Protheus - Como incluir e utilizar menus customizados com o dicionário no banco de dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035446693-Framework-Linha-Protheus-Como-incluir-e-utilizar-menus-customizados-com-o-dicion%C3%A1rio-no-banco-de-dados), e que possibilitará o cadastro de períodos em que determinado funcionário irá substituir outro.

A nova tela contará com os seguintes campos:  
**RUE\_FILSUB**- Filial do Substituído - Onde deve ser informado a filial do funcionário que será substituído.  
**RUE\_MATSUB**- Matrícula do Substituído - Onde deve ser informado a matrícula do funcionário que será substituído.

Esses dois primeiros campos não são obrigatórios, porém, é a partir deles que será calculado o valor da diferença de salário que será pago ao "funcionário substituto".

**RUE\_SALARI** - Salário Substituto: Este campo é habilitado e torna-se obrigatório apenas se os dois primeiros não forem preenchidos. Via de regra deve ser utilizado quando o funcionário irá substituir provisoriamente outro funcionário que tenha sido demitido.  
**RUE\_VERBA** - Verba Pagamento na Folha: Neste campo deve ser informado a verba onde será realizado o pagamento da diferença de salário entre os funcionários. O campo é obrigatório e a verba deve ser um provento.  
**RUE\_PDADI** - Verba Pagamento no Adiantamento: Neste campo deve ser informado a verba onde será realizado o pagamento da diferença de salário entre os funcionários no roteiro de adiantamento. Caso não seja informada, o salário substituição não será calculado no roteiro de adiantamento, apenas na folha. A verba obrigatoriamente deve ser um provento.  
A verba deve ter configuração para adiantamento (RV\_ADIANTA = 'S') para que o abatimento do adicional seja feito na folha/rescisão.  
**RUE\_PDRES** - Verba Pagamento na Rescisão: Neste campo deve ser informado a verba onde será realizado o pagamento da diferença de salário entre os funcionários no roteiro de rescisão. Caso não seja informada, o salário substituição não será calculado no roteiro de rescisão, apenas na folha. A verba obrigatoriamente deve ser um provento.  
**RUE\_DATDE**- Data Inicial: Campo para informar a data de início da substituição. Somente a partir desta data o sistema irá calcular a diferença de salário. O sistema não permitirá que seja incluída uma data anterior ao período atual do cálculo da folha.  
**RUE\_DATATE**- Data Final: Campo para informar a data final da substituição. Caso fique em branco, o cálculo continuará sendo feito até que uma data seja incluída. O sistema não permitirá que seja incluída uma data anterior ao período atual do cálculo da folha. Caso a substituição seja finalizada no último dia do mês, certifique-se de atualizar o cadastro antes do fechamento do período.  
**RUE\_EVEFAL** - Evento de Falta: Informe os eventos de falta do ponto eletrônico para que o sistema verifique se houve faltas durante o período de substituição e desconte da verba gerada. Para que não seja apurado desconto referentes a faltas o campo deve ser deixado vazio.  
**RUE\_MOTIVO** - Motivo de Substituição: Campo informativo utilizado para descrever a razão da substituição.  
  
Ao informar os campos **RUE\_FILSUB**e **RUE\_MATSUB**, o sistema pegará o salário diário do funcionário substituído, subtrairá o salário do funcionário substituto, e irá gerar esse valor multiplicado pela quantidade de dias no período que devam ser pagos na verba cadastrada de acordo com o roteiro.  
Essa verba será paga no cálculo do adiantamento, folha e rescisão de acordo com o cadastro. Para que seja paga no 13º e Férias, as verbas devem ser cadastradas com incidência para médias, dessa forma tanto o cálculo de férias e 13º quanto a provisão, irão considerar os valores.  
Da mesma forma, para que eventuais horas extras considerem o valor da substituição, o cadastro de verbas deverá ser ajustado. Por exemplo, configurando a verba de Hora Extra para ser calculada sobre salário incorporado, e cadastrando a verba de substituição para incorporar o salário.

**Exemplo de calculo:  
Rotina GPEA946**Informar Funcionário Substituto / período de substituição/ verba de calculo na folha

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30649054488215)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30649054494359)

Salário diário Empregado substituto: R$ 2.900,00 / 31 = **R$93,54**Salário diário Empregado substituído: R$ 2.500,00 / 31 = **R$ 80,64**Diferença entre salário diário do substituto e substituído: R$ 93,54 – R$ 80,64 = **R$12,90**Valor a pagar para o substituto: R$ 12,90 \* 5 = **R$ 64,50**

Observações.:  
- Não será permitido o cadastro de mais de uma substituição para o mesmo período e o cálculo será feito SOMENTE se o salário de substituição for maior que o salário do funcionário substituto.  
- A divisão do salário para apuração do salário dia, será sempre com base nos dias do período, ou seja, não será utilizado o parâmetro MV\_DIASPER para divisão com base em 30 ou quantidade de dias do mês.  
  
Documentação técnica - <https://tdn.totvs.com/pages/releaseview.action?pageId=842273181#exemplos-exemplo1>

**Saiba mais  
[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)**
