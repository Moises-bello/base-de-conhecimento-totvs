---
content_hash: 11256ac3e2c0a4eb696d8f02a238a599d9fa9ea801745d267b2cbd31d81e6cf5
fetched_at: '2026-06-29T00:05:48.228868+00:00'
page_id: '1024335823'
product: rm
source: tdn-rm
title: Nota Orientativa nº 11/2025 - Leiaute S-1.3 - FGTS DIGITAL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1024335823
version: 63
---

Objetivo:

Em 09/12/2025, foi disponibilizada a [Nota Orientativa FGTS Digital nº 11/2025](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/nota-orientativa-fd-11-2025-13-e-rescisao.pdf), que traz orientações sobre os procedimentos que devem ser adotados pelos empregadores para o **tratamento correto do cálculo e do recolhimento do FGTS incidente sobre o 13º salário**.

Na referida Nota, são apresentados **três SUGESTÕES de cenários.**

A Nota Orientativa foi publicada sem tempo hábil para que as empresas de software de folha de pagamento pudessem implementar as tratativas sugeridas.

Diante desse cenário, os usuários devem continuar adotando o procedimento de FGTS do 13º salário que sempre foi utilizado até o momento: sempre que houver demissão, o FGTS deve ser recolhido de forma antecipada, respeitando o prazo legal de até 10 dias para pagamento das verbas rescisórias, ou se, necessário realizar a alteração manual da folha de pagamento.

Lembrando que, caso seja necessário realizar ajustes manuais, é importante reforçar que essas alterações devem ser feitas diretamente na folha de pagamento, garantindo que os valores reflitam corretamente nos encargos, nos relatórios e no envio ao eSocial, evitando divergências entre a folha e o eSocial.

Abaixo descrevemos as **três SUGESTÕES de cenários,** apresentadas pela Nota Orientativa:

1true1CENÁRIO 1CENÁRIO 1

**ANTECIPAÇÃO DO VENCIMENTO DO FGTS SOBRE O 13º SALÁRIO EM RESCISÕES OCORRIDAS EM DEZEMBRO**

Quando o empregado é desligado em dezembro, o FGTS incidente sobre o 13º salário deixa de observar apenas os prazos ordinários da folha anual, com vencimento até 20 de janeiro do ano seguinte, e passa a acompanhar o prazo de vencimento das verbas rescisórias.

**AJUSTES NA FOLHA ANUAL NO ESOCIAL (13º SALÁRIO)**

**1️⃣ Rubrica de vencimento do 13º salário**

* + Tipo de rubrica: Tipo 1 – Vencimento
  + Incidência de FGTS: 12 – Base de cálculo do FGTS 13º salário
  + Exemplo de valor: 13º salário: R$ 3.000,00

**2️⃣ Rubrica de desconto do adiantamento do 13º salário (se houver)**

* + Tipo de rubrica: Tipo 2 – Desconto
  + Incidência de FGTS: 12 – Base de cálculo do FGTS 13º salário
  + Exemplo de valor: Adiantamento do 13º: R$ 1.500,00

**3️⃣** **Rubrica informativa dedutora - NOVA VERBA**

* + Tipo de rubrica: Tipo 4 – Informativa Dedutora
  + Incidência de FGTS: 12 – Base de cálculo do FGTS 13º salário
  + Valor informado: R$ 3.000,00 (mesmo valor do vencimento do 13º)

**Resultado**Com a inclusão da rubrica informativa dedutora, a base de cálculo do FGTS do 13º salário na folha anual fica zerada, impedindo a geração de débito de FGTS na competência anual.

**AJUSTES NO EVENTO S-2299 (DESLIGAMENTO) OU S-2399 (TÉRMINO - TSVE) – 13º SALÁRIO RESCISÓRIO**

1️⃣ **Rubrica de 13º salário proporcional (saldo devido na rescisão)**

* + Tipo: 1 – Vencimento
  + codIncFGTS: 12 – Base de cálculo do FGTS 13º salário
  + Valor: R$ 3.000,00

2️⃣ **Rubrica de Desconto de adiantamento do 13º salário (1ª e 2ª parcelas)**

* + Tipo: 2 – Desconto
  + codIncFGTS: 12 – Base de cálculo do FGTS 13º salário
  + Valor: R$ 3.000,00

3️⃣ **Rubrica Informativa Base de FGTS do 13º salário rescisório - NOVA VERBA**

* + Tipo: 3 – Informativa
  + codIncFGTS: 12 – Base de cálculo do FGTS 13º salário
  + Valor: R$ 3.000,00

**Com esses lançamentos:**

* + O eSocial consolida corretamente as verbas rescisórias no S-2299.
  + O FGTS Digital recebe o totalizador correto do FGTS do 13º salário.
  + O débito é gerado como FGTS rescisório, com vencimento antecipado, conforme a legislação vigente.

2CENÁRIO 2CENÁRIO 2

**ADIANTAMENTO DE 13º SALÁRIO MAIOR QUE O 13º PROPORCIONAL DEVIDO NA RESCISÃO**

Em determinadas situações, o trabalhador recebe, um adiantamento de 13º salário (por exemplo, 6/12 avos em fevereiro), mas é desligado alguns meses depois (por exemplo, em abril), de modo que o valor antecipado pode ser superior ao 13º proporcional devido. Nessa hipótese, o excedente pode ser compensado com outras verbas rescisórias, desde que respeitados os limites legais, exigindo ajuste no eSocial, em especial, quanto ao código de incidência de FGTS (codIncFGTS) do valor excedente.

**EXEMPLO PRÁTICO:**

**Adiantamento do 13º salário**

* + Envelope de Férias – 1ª parcela (fevereiro): **R$ 600,00**

**Situação Atual - Cálculo da rescisão (demissão em 30/04)**

* + **R$ 400,00** – Provento de 13º salário proporcional *(codIncFGTS = 12)*
  + **R$ 600,00** – Desconto da 1ª parcela do 13º *(codIncFGTS = 12)*
  + **R$ 300,00** – Provento de saldo de salário *(codIncFGTS = 11)*

**Situação após o tratativa da Nota Técnica (envelope final)**

* + **R$ 400,00** – Provento de 13º salário *(codIncFGTS = 12)*
  + **R$ 600,00** – Desconto da 1ª parcela do 13º *(codIncFGTS = 12)*
  + **R$ 300,00** – Provento de saldo de salário *(codIncFGTS = 11)*
  + **R$ 200,00** – Base de Cálculo de FGTS *(codIncFGTS = 11 | Tipo 4 – Dedutora) -* **NOVA VERBA**

Ressaltamos que o valor lançado na nova verba de Base de Cálculo de FGTS não pode ultrapassar o limite legal permitido.

3CENÁRIO 3CENÁRIO 3

**REMUNERAÇÕES LANÇADAS ANTECIPADAMENTE NO S-1200 (EX.: PAGAMENTO VIA SIAPE) E DESLIGAMENTO NA MESMA COMPETÊNCIA**

Em determinadas situações, o empregador declara no eSocial remunerações pagas antecipadamente em folha mensal (S-1200). Isso ocorre, por exemplo, em sistemas de pagamento centralizados, como o SIAPE, quando a remuneração é declarada na mesma competência em que ocorre a rescisão.

Entendemos que esse cenário não é tratado de forma nativa no produto TOTVS Folha de Pagamento RM, por ser um cenário específico de órgãos públicos. Dessa forma, ele não será contemplado.

4EXEMPLOSEXEMPLOS

Para facilitar o cadastramento manual dos cenários sugeridos pela Nota Técnica, disponibilizamos abaixo alguns exemplos para melhor entendimento:

1true1Exemplo CENÁRIO 1Exemplo CENÁRIO 1

**ANTECIPAÇÃO DO VENCIMENTO DO FGTS SOBRE O 13º SALÁRIO EM RESCISÕES OCORRIDAS EM DEZEMBRO** 

Segue exemplo para esse cenário:

## **CENÁRIO SEM A MUDANÇA DA NOTA ORIENTATIVA**

1) Demonstrativo do cálculo da 2a. Parcela de 13º Salário.

A Base de FGTS 13o. Salário no valor de **R$3.393,75.**

2) Demonstrativo do cálculo do 13º Salário na Rescisão.

A Base de FGTS 13o. Salário no valor de **R$565,63**. No Envelope de Pagamento, constam os valores do 13o salário e adiantamento.

## **CENÁRIO COM A MUDANÇA DA NOTA ORIENTATIVA**

1) Acesse o menu Administração de Pessoal | Eventos e crie as verbas abaixo:

1.1) A verba deverá ser do tipo **“Base de Cálculo”** e possuir incidência em **“Estorna FGTS 13º”**, para que seja enviada ao eSocial no evento **S-1010**, conforme as definições abaixo:

* + Tipo de rubrica: Tipo 4 – Informativa Dedutora
  + Incidência de FGTS: 12 – Base de cálculo do FGTS 13º Salário

Nesse exemplo criamos a verba **9003**:

1.2)  A verba deverá ser do tipo **“Base de Cálculo”** e possuir incidência em **“FGTS 13º salário”**, para que seja enviada ao eSocial no evento **S-1010**, conforme as definições abaixo:

* + Tipo: 3 – Informativa
  + codIncFGTS: 12 – Base de cálculo do FGTS 13º salário

Nesse exemplo criamos a verba **9005**:

A Nota Orientativa não especifica a natureza da rubrica. No exemplo acima, foi utilizada a natureza 9989. Entretanto, cabe a empresa analisar e definir a natureza adequada em que o novo evento se enquadra. O evento 9003 se trata de um exemplo. Você poderá utilizar qualquer outro código que esteja disponível. O novo evento cadastrado deve ser transmitido ao governo através do S-1010.IMPORTANTE!

2) Geração do XML do evento S-1010 para as novas verbas criadas.

3) Demonstrativo do cálculo da 2a. Parcela de 13º Salário.

Deverá ser lançada averba com incidência **"Estorna FGTS 13º" (9003)** com o valor correspondente à base de FGTS de 13º**.** Neste cenário o valor é de **R$ 3.933,76.**

Isso se faz necessário para que oenvelope da 2ª parcela do 13º salário fique com a base de FGTS do 13º zerada, garantindo que o recolhimento do valor ocorra corretamente na rescisão.

4) Demonstrativo do cálculo do 13º Salário na Rescisão:

Deverá ser lançada averba com incidência **"FGTS 13º" (9005)** com o valor correspondente à base de FGTS de 13º**.** Neste cenário o valor é de **R$ 3.933,76.**

Isso se faz necessário para que o **FGTS do 13º**, referente ao **envelope da 2ª parcela**, seja **recolhido na rescisão**, garantindo que o **recolhimento ocorra na data correta de pagamento**.

5) Geração do XML do evento S-1200 anual.

6) Geração do XML do evento S-2299.

2Exemplo CENÁRIO 2Exemplo CENÁRIO 2

**ADIANTAMENTO DE 13º SALÁRIO MAIOR QUE O 13º PROPORCIONAL DEVIDO NA RESCISÃO**

Segue exemplo para esse cenário:

## **CENÁRIO SEM A MUDANÇA DA NOTA ORIENTATIVA**

1) Demonstrativo do Adiantamento de 13º Salário:

* + Envelope de Férias – Recebimento da 1ª Parcela 13º Salário(fevereiro): **R$1.596,40**

2) Demonstrativo do cálculo na Rescisão com data de demissão **30/04**:

* **R$ 1.064,27** – Provento de 13º Salário Proporcional *(codIncFGTS = 12)*
* **R$ 1.596,40** – Desconto da 1ª parcela do 13º *(codIncFGTS = 12)*
* **R$ 3.192,80** – Provento de saldo de salário *(codIncFGTS = 11)*

Nesse cenário, as bases serão:

• **Base de FGTS de 13º Salário:** R$ 0,00 *(R$ 1.064,27 − R$ 1.596,40)*  
• **Base de FGTS:** R$ 3.192,80

## **CENÁRIO COM A MUDANÇA DA NOTA ORIENTATIVA**

1) Acesse o menu Administração de Pessoal | Eventos e crie as verbas abaixo:

Verba do tipo base de cálculo para que seja enviado ao eSocial no evento S-1010, com as incidências abaixo:

* + Tipo de rubrica: Tipo 4 – Informativa Dedutora
  + Incidência de FGTS: 11 – Base de Cálculo do FGTS

Nesse exemplo criamos a verba **9006**:

2) Geração do XML do evento S-1010 para as novas verbas criadas.

3) Demonstrativo do cálculo na Rescisão com data de demissão **30/04**:

* + **R$ 1.064,27** – Provento de 13º salário proporcional *(codIncFGTS = 12)*
  + **R$ 1.596,40** – Desconto da 1ª parcela do 13º *(codIncFGTS = 12)*
  + **R$ 3.192,80** – Provento de saldo de salário *(codIncFGTS = 11)*
  + **R$ 532,13** – Base de Cálculo de FGTS *(codIncFGTS = 11 | Tipo 4 – Dedutora) -***NOVA VERBA **COM CC 492****

    Dica:

    O valor será calculado automaticamente e será deduzido do código de cálculo 26 - FGTS QUITAÇÃO conforme descrito no TDN:

    - [Código De Cálculo 492 - Base Excedente FGTS 13º a Compensar no FGTS Folha](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1043712337)

Nesse cenário, as bases serão:

• **Base de FGTS de 13º Salário:** R$ 0,00 *(R$ 1.064,27 − R$ 1.596,40)*  
• **Base de FGTS:** R$ 2.660,67 *(R$3.192,80 - R$532,13)*

4) Geração do XML do evento S-2299:

## **DEMAIS INFORMAÇÕES**

* [NOTA ORIENTATIVA FGTS DIGITAL Nº 11/2025](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/nota-orientativa-fd-11-2025-13-e-rescisao.pdf)
