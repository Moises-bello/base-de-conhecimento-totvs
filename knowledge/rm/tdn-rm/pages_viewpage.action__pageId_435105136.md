---
content_hash: 9481f62fd2fca4eec8df83043ed7484cac54a90cbfc02ab0ae4548430e883945
fetched_at: '2026-06-29T00:09:48.371274+00:00'
page_id: '435105136'
product: rm
source: tdn-rm
title: Definir Aluguel Complementar - Funções de Fórmula para o Aluguel Complementar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105136
version: 5
---

Abaixo estão descritas as funções de fórmulas que podem ser utilizadas no processo de Geração do Aluguel Complementar.

**COMPETENCIAALGCOMPLEMENTAR**

* **Contexto** (Contrato de Locação) | Retorna a competência que está sendo processada na geração de aluguel complementar. Se for processado fora do contexto, irá retornar a data atual.
* **Sintaxe** COMPETENCIAALGCOMPLEMENTAR

**VALORBASEALUGUEL**

* **Contexto:**(Contrato de Locação) | Retorna o valor base do aluguel para uma determinada Competência. O valor base considera os valores de Escalonamento ou Aluguel em Dobro, caso os mesmos estejam aplicados na competência informada;
* **Sintaxe:**VALORBASEALUGUEL(VALOR);
* **Parâmetros da função:**VALOR (Data da competência);
  + **Observação:** No parâmetro da função VALORBASEALUGUEL deve ser inserido uma data que representa a Data de Competência do Aluguel complementar que vai ser processado. Como forma de facilitar o uso da função de fórmula, pode ser utilizado a função de fórmula COMPETENCIAALGCOMPLEMENTAR, no qual retorna competência que está sendo processada pela geração de aluguel complementar.

**FATURAMENTOALGCOMPLEMENTARVALOR**

* **Contexto:** (Contrato de Locação) | Retorna o valor do faturamento da competência.
* **Sintaxe:** FATURAMENTOALGCOMPLEMENTARVALOR(VALOR)
* **Parâmetros da função:**VALOR (Data da competência)

**PERCENTUALFATURAMENTOALGCOMPLEMENTAR**

* **Contexto:**(Contrato de Locação) | Retorna o percentual (Conforme faturamento) da Competência.
* **Sintaxe:**PERCENTUALFATURAMENTOALGCOMPLEMENTAR(VALOR)
* **Parâmetros da função**:VALOR (Data da competência)

Além das funções de fórmulas criadas  foram incluídas algumas informações no contexto do processo, que podem ser usadas para cálculo:

* DATACOMPETENCIA
* VALORBASEALUGUEL
* PERCENTUALALUGUELDOBRO
* VALORALUGUELCOMPLEMENTAR
* VALORFATURAMENTO
* PERCENTUALFATURAMENTO

Veja Também

---
