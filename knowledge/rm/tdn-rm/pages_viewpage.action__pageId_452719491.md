---
content_hash: 7e21b05ddb43572139b14675c2a62ff02034978fcf9fc10f7ac7f89e17802f1e
fetched_at: '2026-06-29T00:10:07.984127+00:00'
page_id: '452719491'
product: rm
source: tdn-rm
title: Ocorrências Coletadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719491
version: 80
---

Neste módulo, serão mostradas as ocorrências dos funcionários. As suas ocorrências irão decorrer dos cálculos efetuados a partir de batidas coletadas no relógio. O usuário terá apenas a opção de alterar a atitude da ocorrência, ou seja, enviar as horas para o banco ou para o movimento. O sistema não permitirá fazer alteração de atitude para funcionários que não possuírem banco de horas diário por ocorrência.

**Observações:**

* As ocorrências dos períodos anteriores ficarão disponíveis somente para consultas.

* O processo de Alteração de Atitude das Ocorrências não deverá ser realizado durante o período de apuração de ponto quando o parâmetro "Simula o Fim do Período com a Data Atual" estiver marcado.

* Funcionários com cálculo por jornada não será possível compensar parte das horas extras e mandar pagar a outra parte.

**Identificação** **Data:** Clique no ícone para ativar o calendário e selecionar a data.

Selecione o tipo da atitude desejada. Este parâmetro deve ser selecionado apenas quando for trocar a atitude (pagar/descontar ou compensar) de todo o período das horas extras, atrasos ou faltas.

**Exemplo:** No dia 05/01 o funcionário de chapa XXXXX efetuou 05:00 horas extras e a atitude default selecionada no parâmetro Sindicato RM Chronus do funcionário é compensar, mas o funcionário irá receber todas as 05:00, ou seja as 05:00 horas serão pagas no movimento do funcionário.  
Para alterar a atitude dessa ocorrência basta marcar o campo Pagar/Descontar que o sistema irá pagar todas as 05:00 horas extras efetuadas pelo funcionário.

**Observação** Caso este mesmo funcionário fosse receber apenas 02:00 horas e as outras 03:00 horas forem para o banco de horas, não podemos alterar a atitude dessa ocorrência, pois se marcarmos este campo o sistema irá mudar a atitude de toda hora efetuada pelo funcionário e não apenas parte dela. basta informar 02:00 no campo abaixo Pagar/Descontar.

**Pagar/Descontar:** Quando a atitude da ocorrência for compensada, temos como pagar ou descontar um número de horas dentro do período informado para serem pagas ou descontadas no movimento do período atual. Para isto basta informar estas horas neste campo.

**Exemplo:** Em um dia de descanso o funcionário fez 06:00 horas extras (08:00 as 14:00), e a atitude selecionada no parâmetro Sindicato RM Chronus do funcionário é compensar. Para pagar 03:00 horas e compensar 03:00 horas, basta informar 03:00 no campo Pagar/Descontar.

**Observação** Sempre que ocorrer o preenchimento de número de horas no campo Pagar/Descontar que seja menor que o total das ocorrências o produto irá recriar as ocorrências após o recalculo considerando que o inicio do intervalo será o número de horas a compensar, o intervalo restante o número de horas a pagar/descontar.   
No exemplo anterior será criado o intervalo 08:00 as 11:00 como compensar e o intervalo 11:00 as 14:00 como a pagar/descontar.

**Horas:** Este campo será utilizado para mostrar o número de horas da ocorrência para funcionários que utilizam horário flexível com compensação diária e banco de horas diário por ocorrências. Neste caso, o início e fim deverão ser desconsiderados, uma vez que será considerado apenas o total (extras ou atrasos/faltas) após a compensação diária.

**Total Horas** Este campo demonstra o total de horas da ocorrência. Os funcionários com horário do tipo flexível devem verificar o cálculo do campo Horas e não este campo.

|  |  |
| --- | --- |
|  | Como Fazer |

---

Ocorrências Coletadas
