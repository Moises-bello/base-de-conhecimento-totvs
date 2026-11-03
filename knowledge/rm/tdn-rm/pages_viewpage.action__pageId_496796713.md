---
content_hash: 03668edf55c3a8e03cefe09b7b99b70766890c61ee5b67ef5f935358f8c927c7
fetched_at: '2026-06-29T00:10:22.481679+00:00'
page_id: '496796713'
product: rm
source: tdn-rm
title: Eventos S-1200 e S-1210 -  Transportador autônomo - Autônomos Externo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496796713
version: 13
---

false

**A partir das Versões:**

* 12.1.22.264
* 12.1.23.191
* 12.1.24.127

# Objetivo:

---

       O objetivo deste documento é trazer informações de como enviar os eventos S-1200 (Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social) e S-1210 (Pagamentos de Rendimentos do Trabalho) para transportador autônomo -Autônomos Externo.

---

O manual de orientação do e-Social cita:

Conforme MOS 2.5 na página 118 e tópico 41, o valor do frete também deve ser enviado:

41) No caso de pagamento de frete a segurado transportador autônomo, o valor da base de cálculo da Contribuição Previdenciária (remuneração) é de 20% do valor do frete. O valor que deve ser informado à tributação é o da remuneração e não o valor do frete. Para evitar divergência na apuração da contribuição social previdenciária, o empregador deve calcular a base (20% do frete), truncando o valor na segunda casa decimal.

Exemplo 1.: Valor do Frete: R$ 11.357,13  
Valor da remuneração (20%)= R$ 2.271,42

Exemplo 2 (combinando contribuição previdenciária com imposto de renda):  
Valor Frete (carga): 10.000,00 (conforme examinado, o empregador deve informar no eSocial rubricas com o valor da remuneração do transportador autônomo. Para a previdência social corresponde a 20% do valor do frete. Para fins de tributação do imposto de renda é de no mínimo 10% ou 60% no caso de transporte de carga ou passageiros, respectivamente). Nesse caso, a configuração da folha de pagamento do transportador será:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Rubrica | Tp Descricao | IncCP | IncIRRF | IncFGTS | Valor |
| X | Frete Remun INSS | 11 | 701 | 00 | 2.000,00 |
| XX | Frete Remun IRRF | 00 | 11 | 00 | 1.000,00 |
| XXX | Frete Remun | 00 | 701 | 00 | 7.000,00 |
| Y | Desc INSS | 31 | 41 | 00 | 220,00 |
| YY | Desc Sest | 34 | 09 | 00 | 30,00 |
| YYY | Desc Senat | 35 | 09 | 00 | 20,00 |

Passos para o envio das informações para o eSocial, exemplo 2:

**Passo 1**

Para a liberação dos novos campos (VALORREMUNERACAOFRETE, VALORREMUNFRETEINCIDEIRRF, VALORREMUNFRETEINCIDEINSS) será necessário executar o script ('ESOCIALFOP01-10709.SQL' para base SQL ou 'ESOCIALFOP01-10709.ORA' para base ORACLE) através do aplicação RM.Script.Executor.exe.

**Passo 2**

* Preencha sua tabela PPAGTOAUTONOMOEXT conforme sua integração (exemplo: Webservice, conceito, etc...)

Para essa geração dos valores dos transportadores autônomos serão considerados os campos :

* CATEGORIAESOCIAL :códigos de categoria  (**711** - Contribuinte individual - Transportador autônomo de passageiros) ou (**712** - Contribuinte individual - Transportador autônomo de carga) campo 'CATEGORIAESOCIAL'.

* VALORREMUNFRETEINCIDEINSS: Informe o valor total da remuneração do transportador Exemplo : R$ 2.000,00

* VALORREMUNFRETEINCIDEIRRF: Informe o valor total da remuneração do transportador. Exemplo : R$ 1.000,00

* VALORREMUNERACAOFRETE: Informe o valor total da remuneração do transportador. Exemplo : R$ 10.000,00

* VALORINSS: Informe o valor total da remuneração do transportador. Exemplo : R$ 220,00

* VALORSEST: Informe o valor total da remuneração do transportador. Exemplo : R$ 30,00

* VALORSENAT: Informe o valor total da remuneração do transportador. Exemplo : R$ 20,00

**Passo 3**

* No parametrizador deve existir eventos previamente cadastrados para serem informados no eSocial.

* Crie os novos eventos para essa tela abaixo com os seguintes códigos de calculo:

1
incomplete
[Código de Cálculo 399 - REMUNERAÇÃO FRETE AUTÔNOMO](http://tdn.totvs.com.br/pages/viewpage.action?pageId=461921339)

2
incomplete
[Código de Cálculo 400 - REMUNERAÇÃO FRETE AUTÔNOMO COM INCIDÊNCIA EM IRRF](http://tdn.totvs.com.br/pages/viewpage.action?pageId=461921371)

3
incomplete
[Código de Cálculo 401 - REMUNERAÇÃO FRETE AUTÔNOMO COM INCIDÊNCIA EM INSS](http://tdn.totvs.com.br/pages/viewpage.action?pageId=461921386)

**Passo 4 -** Gerar os XML dos eventos periódicos S-1200 e S-1210 do período.

* Será gerado S-1200 - Remuneração do Trabalhador da seguinte forma:

* Será gerado S-1210 - Pagamentos de Rendimentos do Trabalho da seguinte forma:
