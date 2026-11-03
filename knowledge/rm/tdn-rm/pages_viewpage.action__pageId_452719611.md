---
content_hash: 74835a27b3ac96dd6b80a5b5dfcd39b06724e21626990ad19376a7d0273c930d
fetched_at: '2026-06-29T00:10:08.950375+00:00'
page_id: '452719611'
product: rm
source: tdn-rm
title: Parâmetros da Importação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719611
version: 14
---

**Parâmetros da Importação**

* **Controla acesso de funcionários a terminais de coleta:** Selecionando esta opção, o Sistema irá fazer o controle das batidas do funcionário de acordo com o acesso ao terminal de coleta, ou seja, se o funcionário poderá ou não efetuar uma batida em determinado terminal e se puder, qual será o tratamento desta batida.
* **Importa batidas de refeição duplicadas:** Utilizando este parâmetro o sistema irá importar todas as batidas do funcionário efetuadas no relógio de refeitório, mesmo aquelas que tenham sido coletadas no mesmo minuto. **Exemplo:** Batidas Coletadas no relógio de Refeitório: 18/11/2002 – 12:00:01 18/11/2002 – 12:00:02 18/11/2002 – 12:00:03 Batidas importadas para Pasta Batidas de Refeição no cadastro do funcionário: Data              Dia    Batida   Evento               Valor 18/11/2002   SEG  12:00    016 – Refeição    3

**Observação:** Mesmo para os relógios que não possuem campo para informação de segundos o sistema irá importar todas as batidas efetuadas no mesmo minuto. O relógio não precisa ter segundos para utilizar este parâmetro. Batidas Coletadas no relógio de Refeitório: 18/11/2002 – 12:00 18/11/2002 – 12:00 18/11/2002 – 12:00 Batidas importadas para Pasta Batidas de Refeição no cadastro do funcionário: Data              Dia   Batida  Evento               Valor 18/11/2002   SEG  12:00   016 – Refeição   3

* **Considera a alteração de natureza da batida no processo de acerto de batidas:** Utilizando este parâmetro, caso seja feito a inclusão de batidas, inclusão de batidas pela edição ou a alteração de natureza das batidas no espelho (RM.exe ou Portal), esta natureza não será alterada nos processos de importação de batidas, lançamento de horário planejado e recálculo. A alteração de natureza será somente aplicada no dia, não sendo considerada a data da jornada de referência.

**Observação:**No lançamento de Horário Planejado, se existir batida inserida para o dia com a natureza alterada, todas as batidas do horário planejado serão lançadas respeitando a batida já inserida. Na existência de batidas sem par no espelho, ao realizar o recálculo, poderá ser calculado extras ou faltas.

**Exemplo 1: Alteração de natureza da marcação**

Com o parâmetro "**Considera a alteração de natureza da batida no processo de acerto de batidas"** o produto irá se comportar da seguinte maneira:  
Foi realizada alteração de natureza da batida no espelho de ponto do funcionário do dia 01/01 às 21:41. Ao salvar e recalcular, as alterações das naturezas só serão realizadas no dia 01, **mantendo a natureza das batidas dos dias posteriores.**

| Horário executado | | | | | |
| --- | --- | --- | --- | --- | --- |
|  | Ent1 | Sai1 | Ent2 | Sai2 | Ent3 |
| 01/01 | 15:08 | 17:57 | 18:28 |  | 21:41 |
| 02/01 |  | 13:35 | 15:31 | 16:02 | 20:00 |

| Horário Alterado | | | | | |
| --- | --- | --- | --- | --- | --- |
|  | Ent1 | Sai1 | Ent2 | Sai2 | Ent3 |
| 01/01 | 15:08 | 17:57 | 18:28 | 21:41 |  |
| 02/01 |  | 13:35 | 15:31 | 16:02 | 20:00 |

A demonstração acima ficaria gravada no banco da seguinte forma: Tabela AABATFUN campo NATUREZAALTERADA

21:41 = 1

**Observação**

Os valores '0' e '1' representam as naturezas das batidas (Entrada) e (Saída).

Entrada = 0

Saída    = 1

Nesta situação, houve apenas a alteração da natureza da marcação.

**Exemplo 2: Inclusão de marcação faltante com alteração de natureza de marcação**

Com o parâmetro "**Considera a alteração de natureza da batida no processo de acerto de batidas"** o produto irá se comportar da seguinte maneira:  
Foi realizada a inclusão de uma marcação faltante e alteração de natureza da batida no espelho de ponto do funcionário do dia 01/01 às 20:41hs. Ao salvar e recalcular, as alterações das naturezas só serão realizadas no dia 01, **mantendo a natureza das batidas dos dias posteriores.**

| Horário executado | | | | |
| --- | --- | --- | --- | --- |
|  | Ent1 | Sai1 | Ent2 | Sai2 |
| 01/01 | 15:08 | 17:57 | 21:41 |  |
| 02/01 |  | 13:35 | 15:31 | 16:02 |

| Horário Alterado | | | | | |
| --- | --- | --- | --- | --- | --- |
|  | Ent1 | Sai1 | Ent2 | Sai2 | Ent3 |
| 01/01 | 15:08 | 17:57 | 20:41 | 21:41 |  |
| 02/01 |  | 13:35 | 15:31 | 16:02 | 20:00 |

A demonstração acima ficaria gravada no banco da seguinte forma: Tabela AABATFUN campo NATUREZAALTERADA

20:41 = 0

Nesta situação, houve a inclusão de marcação faltante e alteração da natureza da marcação posterior.

**Comportamento na importação de batidas**

Sempre que a importação de batidas é realizada, todas as batidas do período tem o seu cálculo de natureza atualizado, mesmo que o parâmetro **Considera a última linha importada** esteja marcado.

Desta forma, é necessário que algumas situações sejam consideradas para a importação de batidas. Veja os exemplos abaixo:

Exemplo 1 - Horário planejado diferente do horário executado

O cálculo das naturezas das batidas, é realizado considerando um limite para cada jornada, o que ajuda ao sistema compreender se determinada batida encontra-se na jornada atual ou em jornadas anteriores/posteriores.

Em casos onde temos batidas fora do horário, estas podem se encontrar fora do limite para cálculo da natureza, e neste caso, no momento da importação de batidas, podem se deslocar no espelho do funcionário. Veja abaixo:

| Horário planejado | | | | |
| --- | --- | --- | --- | --- |
|  | Ent1 | Sai1 | Ent2 | Sai2 |
| 01/01 | 06:00 | 09:00 | 09:30 | 12:30 |
| 02/01 | 06:00 | 09:00 | 09:30 | 12:30 |

Veja que as batidas serão deslocadas, isso porque de acordo com o comportamento padrão do sistema, temos um limite até às 21:15 para a execução da jornada no dia 01/01.  
Assim sendo, a batida de 21:41 do dia 01/01 será alocada como Entrada, pois está mais próxima da jornada de Entrada do dia 02/01.

| Horário executado | | | | | |
| --- | --- | --- | --- | --- | --- |
|  | Ent1 | Sai1 | Ent2 | Sai2 | Ent3 |
| 01/01 | 15:08 | 17:57 | 18:28 |  | 21:41 |
| 02/01 |  | 13:35 | 15:31 | 16:02 | 20:00 |

Com o parâmetro "**Considera a alteração de natureza da batida no processo de acerto de batidas"** marcado, podemos corrigir manualmente a natureza das batidas deslocadas, alterando a batida de 21:41 do dia 01/01 e a batida de 13:35 do dia 02/01.

| Horário Alterado | | | | | |
| --- | --- | --- | --- | --- | --- |
|  | Ent1 | Sai1 | Ent2 | Sai2 | Ent3 |
| 01/01 | 15:08 | 17:57 | 18:28 | 21:41 |  |
| 02/01 | 13:35 | 15:31 | 16:02 | 20:00 |  |

Em uma segunda importação, estas batidas não irão se deslocar novamente, pois o sistema irá considerar a natureza da batida alterada para **leitura** da natureza da próxima batida, considerando a natureza oposta para a batida posterior.

Assim sendo, se no dia 02/01 a batida de 13:35 foi considerada para cálculo de natureza (houve alteração manual na natureza), sendo assim, o sistema irá compreender a partir das demais importações que a alteração manual da natureza deve ser considerada no processo. Desta forma, a batida de 15:31 terá a natureza oposta a da batida de 13:35, neste caso, a batida de 15:31 será uma saída.

**Atenção!!!**

*O sistema não conseguirá garantir o mesmo para dias que houverem horários executados diferentes do horário planejado e houver batidas ímpares no dia, estando em desconformidade com a Portaria 1510/2009 e 671/2021.*

* **Bloquear edição de data e hora e exclusão de batidas coletadas:**Com este parâmetro marcado não é possível editar/excluir batidas coletadas no espelho do funcionário, sendo possível editar apenas a natureza da batida.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Assistente de Implantação de Processos
