---
content_hash: b0b431e0c5e899f4d0111e6518799e2069071fd799d0b6a4d34b51b02ca5d7d5
fetched_at: '2026-06-29T00:09:59.964488+00:00'
page_id: '452718467'
product: rm
source: tdn-rm
title: ESTABILIDADEPROVISORIA
type: documentation
url: https://tdn.totvs.com/display/LRM/ESTABILIDADEPROVISORIA
version: 2
---

**ESTABILIDADEPROVISORIA**   
    
A função ESTABILIDADEPROVISORIA irá retornar se o funcionário possui estabilidade provisória.

**Parâmetros:**

* Código da Coligada (CODCOLIGADA) do Funcionário;
* Chapa do Funcionário (CHAPA);
* Ano da Competência para consulta;
* Mês da Competência para consulta (1 a 12);

Será consultado se o funcionário possui estabilidade provisória (CIPA, afastamentos, leis sindicais ou fórmulas).

**Exemplo:**ESTABILIDADEPROVISORIA(1,'00002',2007,4)

Neste exemplo iremos verificar se o funcionário da coligada: "1" de chapa: "00002" possui estabilidade provisória no mês: "4" do ano de "2007".
