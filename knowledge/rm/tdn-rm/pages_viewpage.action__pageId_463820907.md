---
content_hash: f7e860dcd90c45e9ff632ff7a3bc8d2b7af1996103ef1ebfee4a4c263a93207b
fetched_at: '2026-06-29T00:10:15.169332+00:00'
page_id: '463820907'
product: rm
source: tdn-rm
title: Eventos S-1200 e S-1210 -  Transportador autônomo - Autônomos cadastrados no
  Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463820907
version: 24
---

false

**A partir das Versões:**

* + 12.1.21.223
  + 12.1.22.203
  + 12.1.23.133
  + 12.1.24

# Objetivo:

---

       O objetivo deste documento é trazer informações de como enviar os eventos S-1200 (Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social) e S-1210 (Pagamentos de Rendimentos do Trabalho) para transportador autônomo - Autônomos cadastrados no Financeiro.

---

Conforme Manual de Orientação do eSocial (MOS) S-1.0 na página 125 e tópico 25.2, o valor do frete também deve ser enviado:

25.2) No caso de pagamento de frete a segurado transportador autônomo, o valor da base de cálculo da Contribuição Previdenciária (remuneração) é de 20% do valor do frete. O valor que deve ser informado à tributação é o da remuneração e não o valor do frete. Para evitar divergência na apuração da contribuição social previdenciária, o empregador deve calcular a base (20% do frete), truncando o valor na segunda casa decimal.

Exemplo 1: Valor do Frete: R$ 11.357,13  
Valor da remuneração (20%)= R$ 2.271,42

Exemplo 2 (combinando contribuição previdenciária com imposto de renda):  
Valor Frete (carga): 10.000,00 (conforme examinado, o empregador deve informar no eSocial rubricas com o valor da remuneração do transportador autônomo. Para a previdência social corresponde a 20% do valor do frete. Para fins de tributação do imposto de renda é de no mínimo 10% ou 60% no caso de transporte de carga ou passageiros, respectivamente). Nesse caso, a configuração da folha de pagamento do transportador será:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Rubrica | Tp Descricao | IncCP | IncIRRF | IncFGTS | Valor |
| X | Frete Remun INSS | 11 | 00 | 00 | 2.000,00 |
| XX | Frete Remun IRRF | 00 | 11 | 00 | 1.000,00 |
| XXX | Frete Remun | 00 | 09 | 00 | 7.000,00 |
| Y | Desc INSS | 31 | 09 | 00 | 220,00 |
| YY | Desc Sest | 34 | 09 | 00 | 30,00 |
| YYY | Desc Senat | 35 | 09 | 00 | 20,00 |

Passos para o envio das informações para o eSocial, exemplo 2:

* No cliente fornecedor preencher os campos:

O código de categoria pode ser o (**711** - Contribuinte individual - Transportador autônomo de passageiros) ou (**712** - Contribuinte individual - Transportador autônomo de carga).

**Observação: a partir da versão 12.1.25.00, será disponibilizado o anexo do eSocial, que irá substituir o item Integrações | eSocial**

* No lançamento financeiro, informe o valor original.

* Clique em tributos para calcular os valores de INSS e IRRF.

* Clique em "Entrar em Exibir Dados para Cálculo do INSS".

* Digitar o percentual de INSS do Empregado.

* Clique no cálculo para o sistema realizar o valor de desconto do INSS com base no percentual indicado.

* Clique em "Entrar em Exibir Dados para Cálculo do IRRF"

* Digitar o percentual de IRRF do Empregado.

* Clicar no cálculo para o sistema realizar o valor de desconto do IRRF com base no percentual indicado.

* O lançamento financeiro do cliente fornecedor deve estar baixado para que a geração do S-1210 - Pagamentos de Rendimentos do Trabalho considere o lançamento.

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

* Será gerado S-1200 - Remuneração do Trabalhador da seguinte forma:

* Será gerado S-1210 - Pagamentos de Rendimentos do Trabalho da seguinte forma:
