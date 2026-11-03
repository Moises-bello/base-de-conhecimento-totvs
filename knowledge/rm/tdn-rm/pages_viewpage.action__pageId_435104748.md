---
content_hash: b2c3276e256af4981cfb465abc56133f973c6146908560725cded174b472c1c5
fetched_at: '2026-06-29T00:09:46.018892+00:00'
page_id: '435104748'
product: rm
source: tdn-rm
title: Medidor - Anexo - Medições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104748
version: 4
---

Para acessar o cadastro de Medições, basta acessar **Condomínio / Medidores / Anexo Medições**. Nesta tela serão registradas todas as medições de um determinado medidor.  
As informações preenchidas nas Medições serão usadas para Calcular o Fechamento.

**Campos da tela**

* **Código:** Código identificador da Medição vinculada ao Medidor.
* **Situação:** Situação da medição que pode assumir os seguintes valores de acordo com a situação do fechamento
  + **Em preparação:** Fechamento foi criado, porém ainda não foi calculado.
  + **Calculado:** Apuração do fechamento foi realizada porém os lançamentos financeiros ainda não foram gerados.
  + **Integrado:** Apuração do fechamento foi realizada e os lançamentos financeiros gerados para o TOTVS Gestão Financeira.
    - **Observação:** O único status que permite alterações nas medições é o Status de **Em Preparação**.
* **Medidor:** Medidor ao qual a medição está sendo vinculada.
* **Medição:** Receberá o valor da medição atual
* **Medição Anterior:** Valor da medição cadastrada anteriormente e que será usada para cálculo do consumo da medição atual
* **Consumo:** Calculado pela diferença entre **medição** e **medição anterior**
* **Constante:** Multiplicador cadastrado no medidor para que seja aplicado sobre o consumo
* **Consumo x Constante:** Resultado da multiplicação do **consumo** pela **constante**. Este valor é que será usado no cálculo da apuração do fechamento. Caso o campo constante tenha valor 0 ele será ignorado e o valor do **consumo x constante** será o mesmo do **consumo**.
* **Data da medição:** Data em que a medição foi realizada. Ex.: Data em que o funcionário da Copasa/Cemig registrou a leitura do relógio.
* **Fechamento do Condomínio:** Esse campo exibe o Fechamento no qual a mediação está associada. Esse campo somente é preenchido quando o Fechamento é Calculado envolvendo a medição.
* **Competência:** Data da competência em que o cálculo será realizado. Esta é a data a ser usada para calcular o Fechamento.

**Edição de Medições – Medidores Individuais e Gerais**  
**1. Medidores Individuais**

**Edição de Medições:**  
A medição de um medidor individual só pode ser alterada caso não exista apuração no fechamento para a subunidade correspondente. Ou seja, após a apuração do fechamento, as medições ficam bloqueadas para edição.

**2. Medidores Gerais**

**Edição de Medições:**  
Da mesma forma que nos medidores individuais, as medições de medidores gerais só podem ser editadas enquanto não houver nenhuma apuração no fechamento, visto que a medição é para todas.

**3. Status da Medição em Medidores Gerais no Condomínio Individualizado**

Quando o medidor está configurado como Geral, o status "Calculado" da medição não será levado em conta, pois **não** há controle individualizado de status para cada subunidade dentro do sistema.
