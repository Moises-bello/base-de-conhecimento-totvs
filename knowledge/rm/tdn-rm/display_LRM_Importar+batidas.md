---
content_hash: 4264995c649a00a64b186dede19fe9622a5d01ba4738c766f2ab1a10ded8911b
fetched_at: '2026-06-29T00:10:02.608470+00:00'
page_id: '452718977'
product: rm
source: tdn-rm
title: Importar batidas
type: documentation
url: https://tdn.totvs.com/display/LRM/Importar+batidas
version: 3
---

**Importação de Batidas**   
**Considerar jornadas sem trabalho contínuas como única jornada para cálculo da natureza:** Marcando este parâmetro, as jornadas sem trabalho contínuas serão concatenadas, para que a natureza das batidas nesses dias obedeça à paridade *Entrada/Saída***.**  
   
**Tempo de Acrésc. p/ limite da jornada de trabalho anterior/posterior à jornada sem trabalho, para cálculo da natureza:** Este parâmetro trata os seguintes casos:

* *Funcionário irá trabalhar até mais tarde, e a próxima jornada é um compensado ou descanso:* Nesse caso, é importado a batida de saída como uma entrada, pois a batida está mais próxima da jornada sem trabalho.
* *Funcionário inicia a jornada mais cedo para fazer extras, e a jornada anterior também é uma jornada sem trabalho:* Nesse caso normalmente é importado a batida de entrada como uma saída, pois a batida está mais próxima da jornada sem trabalho.
* Casos onde há esquecimento de efetuar batidas.

O parâmetro não irá ser considerado para casos de jornadas de trabalho contínuas, ou seja, duas jornadas seguidas. Portanto o acréscimo só ocorrerá caso a jornada anterior ou posterior corresponder a uma jornada sem trabalho (descanso, compensado, extra nula, etc).

Obs: esse paramêtro influência no .
