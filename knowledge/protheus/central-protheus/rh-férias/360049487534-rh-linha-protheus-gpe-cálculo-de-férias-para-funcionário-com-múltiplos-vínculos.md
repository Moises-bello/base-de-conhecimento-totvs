---
article_id: 360049487534
category: RH - Férias
content_hash: 2d99ac0705d3164756aab78298c034802fff90a9e8e760aeca9d5eee5645de56
fetched_at: '2026-06-28T22:43:59.276636+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de férias para Funcionário com múltiplos
  vínculos em empresas diferentes
type: support-article
updated_at: '2021-11-09T18:26:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049487534-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-f%C3%A9rias-para-Funcion%C3%A1rio-com-m%C3%BAltiplos-v%C3%ADnculos-em-empresas-diferentes
---

**Dúvida**Como calcular férias para Funcionário com múltiplos vínculos, quando são de empresas diferentes?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para funcionários com mais de um **vínculo empregatício** em empresas diferentes, deve lançar manualmente os valores de Base INSS outras empresas e o valor descontado de INSS outras empresas no ato do cálculo das Férias:  
  
Identificadores de cálculo:  
**0396** - Base Inss Ferias Outros Períodos (Verba Tipo Base)  
**0397** - Inss Ferias Outros Períodos (Verba Tipo Base)  
  
Exemplo:  
  
No cálculo de férias, selecione Lançamentos:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074243114/mceclip1.png)  
  
Nesse caso o funcionário teve em outra empresa o limite do desconto de INSS  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074243194/mceclip2.png)  
  
O sistema demonstrará a mensagem abaixo:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075403513/mceclip3.png)  
  
Preencha os campos solicitados:  
Documentação: <https://tdn.totvs.com/pages/releaseview.action?pageId=543084285>

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074243374/mceclip4.png)  
  
Confirme a inclusão dos dados, calcule as férias e confira os valores. Nesse exemplo, não houve desconto de Inss Férias visto que na outra empresa já foi recolhido o teto.  
  
**Tp. Recolhimento:** Informe o tipo de recolhimento do funcionário. Uso eSocial. Opções disponíveis:

**1 -** Contribuição Descontada pelo empregador declarante;

**2 -** Contribuição descontada por outra empresa ou recolhida pelo próprio trabalhador sobre valor inferior ao limite máximo do salário de contribuição;

**3 -** Contribuição sobre o limite máximo de salário de contribuição já descontada/recolhida em outras empresas.

**Tp. Inscrição:** Informe o tipo de inscrição da empresa referente ao Múltiplo Vínculo. Uso eSocial.

Tipos de inscrições permitidas: **1 - CNPJ 2 - CPF  
Nr. Inscrição:** Informe o número da inscrição da outra empresa sendo, caso seja CNPJ a raiz do mesmo não deve ser igual ao CNPJ do empregador, caso seja CPF deve ser igual ao CPF do funcionário. Uso eSocial.

**Valor Remuneração:** Informe o valor da remuneração recebida pelo trabalhador na outra empresa/atividade, sobre a qual houve desconto/recolhimento da contribuição do segurado.   
**Regra eSocial:** Só será permito valor igual a ZERO, somente quando Tipo de Recolhimento igual a 3.  
**Cat. eSocial:**Informe neste campo, a categoria eSocial do funcionário na outra empresa que o funcionário trabalha.

Em casos de férias partida, o sistema verifica o parâmetro MV\_DINSSFM.  
  
Se estiver preenchido com R ou S, onde o sistema fará o rateio do INSS mês e INSS mês seguinte, o sistema não irá calcular o INSS férias mês caso o valor da outra empresa tenha atingido o limite, porém fará o cálculo do INSS mês seguinte. Lembrando que o INSS é competência, portanto quando há o rateio do INSS o valor do mês seguinte, **é devido no calculo de férias**.   
  
Quando o parâmetro estiver com **N**, o sistema **não gera o INSS mês seguinte** (ID 0232).  
  
Caso o lançamento não atinja o limite do INSS, o sistema refaz a base e no identificador 0065 lança a diferença do INSS.  
  
Exemplo:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075408073/mceclip6.png)  
  
Cálculo de férias:  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074247454/mceclip7.png)  
  
Verifique que a soma do INSS gerado nas férias com o valor lançado, não ultrapassa o limite.
