---
content_hash: 5610ef610b501d9b04063dcd16b1f5482eeeeb034df168d754299593e31851df
fetched_at: '2026-06-29T00:05:48.033789+00:00'
page_id: '1021212238'
product: rm
source: tdn-rm
title: Como calcular a Isenção do Imposto de Renda para quem ganha até 5.000,00 e
  redução gradual até 7.350,00 - LEI 15.270/2025
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1021212238
version: 46
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **How To**
5. **Tabelas utilizadas**

## **01.****VERSÕES**

* Veja em [DT - Isenção do Imposto de Renda para quem ganha até 5.000,00 e redução gradual até 7.350,00 - LEI 15.270/2025](https://tdn.totvs.com/pages/viewpage.action?pageId=1022391668)
* Veja em [DT - Calculo Pensão Nova Tabela IRRF Redução](https://tdn.totvs.com/pages/viewpage.action?pageId=1031534137)
* Veja em [DT - Função de Fórmula TR2](https://tdn.totvs.com/pages/releaseview.action?pageId=1039515779)

## **02.** **VISÃO GERAL**

 Implementação para o cálculo da folha para atender a [Lei nº 15.270, de 26 de novembro de 2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm), que altera o cálculo do IRRF sobre salários.

|  |  |
| --- | --- |
| **LIMITE RENDIMENTO** | **REGRA** |
| Até R$5000,00 mensais | IRRF zerado |
| Entre R$5000,01 e R$7350,00 mensais | Aplicar redutor (conforme fórmula legal) no valor do IRRF. A redução será decrescente e linear até zerar para quem atinge R$ 7.350,00 |
| Acima de R$7350,00 mensais | IRRF normal (sem redutor) |

A redução não pode exceder o valor do imposto calculado pela tabela progressiva mensal.  
A fórmula da redução será aplicada automaticamente pelo sistema na **base de tributação de IRRF sem as deduções** legais: **978,62 - (0,133145 x rendimentos tributáveis)**

Dessa forma, o procedimento será o seguinte:

* Inicialmente, realiza-se o **cálculo do IRRF pela regra padrão** (*tabela de cálculo de finalidade "2-IRRF"*), obtendo-se o valor do imposto devido.
* Em seguida, aplica-se a **fórmula de redução** (*tabela de cálculo de finalidade "6-IRRF\_REDUÇÃO"*) prevista na legislação:   
  **Redução = R$ 978,62 - (0,133145 × rendimentos tributáveis sujeitos à incidência mensal)**

IMPORTANTE:

* **A tabela original de IRRF de finalidade 2 - IRRF continua existindo, ou seja, seus valores não serão alterados. Para 2026, pode-se atualizar a vigência da tabela atual.**
* Deve-se criar uma **nova Tabela de Cálculo** de **finalidade 6 - IRRF\_REDUÇÃO** onde deverão ser informados os **valores para o cálculo da redução**. Ver detalhes abaixo.
* A parametrização da tabela é feita pelo usuário. Veja como é a parametrização seguida pela empresa principalmente sobre arredondamentos para **marcar ou não** o parâmetro "**Arredondar valores**".

Para o **correto funcionamento** do cálculo do IRRF, é imprescindível:

* Fazer o **recálculo de ao menos 1 funcionário** e, após
* Realizar o **cadastro da tabela de cálculo** com a **finalidade 6 - IRRF\_REDUÇÃO**
* Cadastrar nova tabela com a finalidade **6 - IRRF\_REDUÇÃO** em **Administração de Pessoal | Cálculos | Tabelas de Cálculo**:

* Faixa 1 - Limite Superior = 5000,00 - Percentual = 0 - Valor a Deduzir = 0
* Faixa 2 - Limite Superior = 7350,00 - Percentual = 13,3145 - Valor a Deduzir = 978,62
* Vigência **01/01/2026 a 31/12/2026**

Será apresentada a mensagem abaixo caso o pagamento seja no caixa 2026 e a tabela de **finalidade 6 - IRRF\_REDUÇÃO** **não exista** na base:

Atenção:

* A base utilizada para o cálculo da redução será a **base tributável bruta, antes da aplicação de quaisquer deduções**.   
  **Para conferir veja o valor localizado no log de cálculo como Rendimentos Tributáveis que equivale a proventos menos descontos, sendo os valores de descontos considerando eventos que estornam IRRF.**
* Base para cálculo da Redução: Entra os valores que estornam IRRF.
* Para o cálculo do IRRF incidente sobre a **PLR**, **não haverá redução**, uma vez que a tabela aplicada é distinta.
* Quanto ao **RRA**, seus efeitos ocorrerão **apenas a partir de 2027**, não havendo, portanto, qualquer alteração no momento.
Dica:

Veja também - [Orientações Consultoria de Segmentos - Novo Cálculo do IRRF](https://tdn.totvs.com/pages/releaseview.action?pageId=1019343450)

## **03.****EXEMPLO DE UTILIZAÇÃO**

Veja abaixo os exemplos de cálculo do IRRF conforme nova Lei 15.270:

Folha mensal

*Dados fictícios*

Cálculo considerando o pagamento da folha em 30/12/2025 - ainda sem o desconto do valor redutor

Cálculo considerando o pagamento da folha em 05/01/2026 - com o desconto do valor redutor

Abaixo alguns cálculos com os limites de aplicação do redutor

Férias

*Dados fictícios*

Cálculo considerando o pagamento das férias em 30/12/2025 - ainda sem o desconto do valor redutor

Cálculo considerando o pagamento das férias em 01/2026 - com o desconto do valor redutor

13º salário

*Dados fictícios*

Cálculo considerando o pagamento do 13º salário em 12/2025 - ainda sem o desconto do valor redutor

Cálculo considerando o pagamento do 13º salário em 12/2026 - com o desconto do valor redutor

Rescisão

*Dados fictícios*

Cálculo considerando o pagamento de Rescisão em 30/12/2025 - ainda sem o desconto do valor redutor

Cálculo considerando o pagamento de Rescisão em 05/01/2026 - com o desconto do valor redutor

Observação:

No exemplo acima, o valor dos rendimentos tributáveis ficou maior que o valor limite para dedução e por isso não houve cálculo do redutor.

Quando o valor está abaixo do limite do redutor, é feito o cálculo considerando o redutor normalmente.

Múltiplos vínculos

*Dados fictícios*

Cálculo considerando o pagamento de múltiplos vínculos em 01/2026 - com o desconto do valor redutor

**VÍNCULO 01** - Chapa 00014 - Valor dentro da isenção

**VÍNCULO 02** - Chapa 99914 - Valor dentro da isenção

**VÍNCULO 01** - Chapa 00014 - Lançamento de valor em outro período para alcançar rendimento para aplicação do redutor

Adiantamento

Exemplo envelope com adiantamento:

1º Envelope lançamos o evento de CC 34, é um provento do Tipo Valor

2º Envelope lançamos o evento de CC 19, que é um Desconto do Tipo Valor  

**Observação:**

Vale lembrar que o CC19 foi ativado a flag **Estorna IRRF** em **Inc. Descontos**, essa flag é de extrema importância para o cálculo do IRRF. Caso a flag esteja inativa e a flag **Dedutível IRRF** esteja ativa em seu lugar, o cálculo do IRRF sofrerá impacto para a tabela de redução, tendo em vista que a dedução de IRRF não impacta diretamente no Rendimento tributável e sim na Base de IRRF.

Log de cálculo do IRRF ( CC 4 )

Pensão

*Dados fictícios*

Para os casos onde o **Valor aplicado na tabela de Redução de IRRF**for menor que o Limite superior da primeira faixa ( R$ 5.000,00 ), será exibido o detalhamento no log do cálculo dos eventos de pensão alimentícia  
  
  
Caso o funcionário atinja a segunda faixa da nova tabela de IRRF  ( R$ 5.000,01 a  R$ 7.350,00 ), será exibido no log o detalhamento da Redução 

Dica:

Veja também - [Função de Fórmula: TR2](https://tdn.totvs.com.br/pages/releaseview.action?pageId=1039514917)

## **04.** **HOW TO**

## **05.** **TABELAS UTILIZADAS**

* PFFINANC
