---
article_id: 360052166714
category: RH - Cálculo Adiantamento
content_hash: 92a4985fc2a32902e105e3ea243e0e4373072a9f3bed13173b4f6a4a55455dea
fetched_at: '2026-06-28T22:43:14.201789+00:00'
product: protheus
section_id: 360011983213
source: central-protheus
title: RH - Linha Protheus - GPE - Adiantamento Salarial - Configurações e Conceitos
type: support-article
updated_at: '2024-06-25T19:40:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052166714-RH-Linha-Protheus-GPE-Adiantamento-Salarial-Configura%C3%A7%C3%B5es-e-Conceitos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24428360427287)**Tempo aproximado para leitura: **00:02:30 min**

**Dúvida**Orientações sobre o que é Adiantamento Salarial e como realizar o Cálculo de Adiantamento.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.25  
  
**Solução**O adiantamento salarial nada mais é que o **pagamento** de **uma parcela** do salário ao colaborador **antes** da data de recebimento usual. O valor antecipado é **descontado** na **folha** de pagamento de acordo com o **regime** de cada organização.  
  
Geralmente, o valor do adiantamento é de **40%** do salário mensal do colaborador, e é pago entre o **15º** e **20º** dia útil do mês. Como não existe uma lei específica, é importante averiguar o **sindicato** da classe trabalhista, pois muitas vezes suas **convenções** abrangem algumas regras nesse quesito, que podem diferir do habitual.  
  
Vale ressaltar que compete à **empresa** fornecer o benefício, mas os colaboradores também podem solicitar. E, quando oferecido, deve ser **documentado** e comprovado, a fim de **resguardar** os **direitos** e **deveres** tanto do colaborador, quanto da organização.  
  
**Regime Competência**O pagamento do adiantamento e folha ocorrem dentro do mesmo mês e não possuem incidência de IRRF no cálculo do adiantamento. Veja como configurar as verbas:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083940274)  
  
**Regime Caixa**  
O pagamento do adiantamento ocorre em mês diferente da folha. Geralmente adiantamento no dia 20 e folha de pagamento no 5º dia útil da competência seguinte. Veja como configurar as verbas:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085122033)  
  
Para que o sistema gere essas verbas será necessário configurar também o campo **V Mes Segui**  (**RV\_CODMSEG**) da seguinte maneira:

- Verba de identificador **0015** com o campo RV\_CODMSEG com a verba do identificador **0106**

- Verba de identificador **0066** com o campo RV\_CODMSEG com a verba do identificador **0107**

Mais orientações em relação a amarração, consulte os detalhes aqui.  
  
Qual a influência do id **0063** no adiantamento/folha?  
Em situação em que a empresa possui pagamento em regime caixa e no cálculo do adiantamento há uma redução na base de IR que ocasiona a geração da verba de Id 0063, ou seja, ocorre devolução do valor de IR que foi descontado na folha referente período anterior.  
  
**Exemplo**:

**1.** Empresa **regime caixa**

Na folha de pagamento de janeiro de 2020 data de pagamento 05/02/2020 o empregado tinha somente um dependente, houve o desconto do imposto de renda no valor de $64,79 no id 0066.  
No adiantamento salarial de fevereiro com data de pagamento 20/02/2020 a empresa cadastrou mais dependentes para o empregado em vez de um passou a ter 4.  
Este empregado iniciou férias em fevereiro e recebeu o adiantamento id 0006 (provento) proporcional aos dias trabalhados, o parâmetro **MV\_ADTOPRO** está com **S**.  
No roteiro ADI com data de pagamento 20/02/2020 recebeu 400,00.  
  
O sistema entendeu que o empregado teve um desconto de imposto de renda indevido no valor de $64,79, na verdade deveria ser de $52,08 na folha de adiantamento o sistema devolve o valor como provento 12,71 o liquido de adiantamento id 0546 é a soma da devolução do imposto de renda + o valor do adiantamento.  
  
![](https://tdn.engpro.totvs.com.br/download/attachments/555844732/image2020-7-15_10-42-35.png?version=1&modificationDate=1594823350100&api=v2)  
  
Exemplo de cadastramento da verba:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085122233)  
  
É possível trocar o regime de pagamento a qualquer momento?

A opção pelo regime de caixa **deve abranger todo o ano-calendário**, não podendo dentro do ano-calendário haver mudança do regime de competência para o de caixa e vice-versa. **Saiba mais** em [Mudança Regime Caixa X Competência](https://tdn.engpro.totvs.com.br/pages/viewpage.action?pageId=271167000)

**Tabelas** Envolvidas  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085122713)  
  
**Parâmetros**/**Mnemônicos** envolvidos  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085122753)

Caso a empresa queira incorporar os Adicionais de Periculosidade/Insalubridade/Tempo de Serviço no adiantamento, deve seguir as seguintes orientações:  
[PSIGAGPE0668 - Calculo adiantamento salarial considerando o adicional de Periculosidade- P12.](https://tdn.engpro.totvs.com.br/pages/viewpage.action?pageId=271394224)

Cálculo de Adiantamento para funcionários de licença maternidade:[PSIGAGPE0638 - GPEM020 - Pagamento do Adiantamento Salarial para funcionárias afastadas por licença maternidade, para empresas que firmaram convênio com a Previdência e optaram pelo pagamento do Salário Maternidade em Folha.](https://tdn.totvs.com/pages/viewpage.action?pageId=233760587)

Saiba mais

Para adquirir mais conhecimento acesse o *link* abaixo:

[RH - Linha Protheus - GPE - Alteração do tipo de regime caixa/competência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046198893-RH-Linha-Protheus-GPE-Altera%C3%A7%C3%A3o-do-tipo-de-regime-caixa-compet%C3%AAncia?source=search)

[RH - Linha Protheus - GPE - Configuração de verbas para Adiantamento (regime competência)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036123334-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-de-verbas-para-Adiantamento-regime-compet%C3%AAncia-?source=search)

[RH - Linha Protheus - GPE - Como efetuar a configuração de verbas de IR para o tipo de regime caixa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006990952-RH-Linha-Protheus-GPE-Como-efetuar-a-configura%C3%A7%C3%A3o-de-verbas-de-IR-para-o-tipo-de-regime-caixa?source=search)

[RH - Cálculo Adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983213-RH-C%C3%A1lculo-Adiantamento)
