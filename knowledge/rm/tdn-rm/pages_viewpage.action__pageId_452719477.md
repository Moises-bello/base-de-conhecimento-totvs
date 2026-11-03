---
content_hash: a24411a69cab1ff888299a1d7e50713d10ab27b321c1dcffd4e9c0af42fa9af4
fetched_at: '2026-06-29T00:10:07.936676+00:00'
page_id: '452719477'
product: rm
source: tdn-rm
title: Opções de Compensação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719477
version: 6
---

**Opções de Compensação**

---

Ao definir somente a compensação, o crédito ou débito não será lançado para movimentação do funcionário.  
   
Cada extra a compensar poderá ser definida previamente com um valor de percentual, ou seja, conforme legislação, a hora extra deve valer 50% a mais que a hora normal do funcionário. Ou mesmo, decidir que a extra realizada em dias de descanso tenha um valor percentual de 100% para compensação. E para considerar esse percentual, o parâmetro **'Considera percentual de incidência para a compensação das horas'** deverá ser utilizado.  
**Exemplo:**   
Banco de horas – 01:00 Hora extra normal 50%  
                             01:00 Atraso  
A compensação será da seguinte forma:  
01:00 extra + 50% = 01:30 de extra à Aplica percentual  
01:30 extra – 01:00 Atraso = 00:30 de extra à Compensa  
00:30 extra – 50% = 00:20 de extra à Retira percentual  
Nesse caso, após a compensação, o banco de horas terá 00:20 de extra para ser lançada ou não para movimentação.

**Observação**  
1 - Este percentual de incidência será buscado no respectivo campo cadastrado para o evento na tabela de eventos do Sistema TOTVS Folha de pagamento, que estiver associado ao evento correspondente do Sistema TOTVS Automação de Ponto pela tabela de relacionamento de eventos, segundo o parâmetro Sindicato RM Chronus informado para o funcionário.  
2 – Para utilizar o percentual na compensação o parâmetro 'Considera percentual na compensação de horas' da tabela de eventos associados no sindicado do funcionário deverá estar marcado.  
   
Há casos em que o funcionário tem um saldo inicial no banco de horas de períodos anteriores, ou por algum motivo possui horas de extra, atraso ou falta iniciais. Lembrando que estas horas iniciais não estão no banco de horas e devem ser informadas nos parâmetros do funcionário, pois as mesmas poderão ser utilizadas para futuras compensações. Haverá também a possibilidade de compensar primeiramente essas horas iniciais antes de realizar a compensação do banco utilizando o parâmetro '**Compensa saldo inicial antes de compensar as horas do banco'**.  
   
O parâmetro **'Considera convenção coletiva para compensação'** será visível somente quando o tipo do banco de horas for diário e quando a forma de compensação for somente Compensação. Ao marcar esse parâmetro será considerada a convenção coletiva de compensação, mantendo compatibilidade com a compensação antiga, se sobrarem extras após a compensação no mês de início do período de compensação, automaticamente serão lançados as horas para o movimento. Caso não marcado, somente irá efetuar a compensação mantendo as horas restantes no banco de horas.

**Exemplo**  
Período atual e ativo: 01/05 a 31/05/2011  
Ocorrências no banco: 10/05 -> 01:00 Hora Extra  
                                     11/05 -> 00:30 Atraso  
                                     15/04 -> 02:00 Horas Extras  
                                     16/04 -> 00:30 Atraso  
Período para compensação: 01/04 a 31/05/2011  
Após a compensação a movimentação e o banco ficarão da seguinte forma:  
Movimento: 01:00 Hora Extra  
Banco de horas: 01:00 Hora Extra

Importante

No cálculo da compensação ao validar o parâmetro “**Considera convenção coletiva**” a data que é considerada será a definida considerando o parâmetro **“Considera limite de dias conforme parametrização”**,se ele estiver marcado ou a data de início do período.

**Ordenação**  
Para a compensação, poderá ser definida uma prioridade de ordenação por data ou por tipo. O entendimento é simples, caso a prioridade seja data, o sistema ordenará as ocorrências por data mais antiga ou mais atual e posteriormente ordenar as ocorrências por tipo para realizar a compensação.  
A ordenação por tipo é referente às ocorrências de crédito, ou seja, as extras, onde poderão ser organizadas pelo tipo (Normal, Compensado, Descanso e Feriado) ou mesmo organizadas pelo código de cálculo ou faixas por tipo(1ª Faixa Extra Normal, 2ª Faixa Extra Normal.....1ª Faixa Extra Descanso, 2ª Faixa Extra Descanso).  
Considerando então as prioridades por data ou por tipo a ordenação fica da seguinte forma:

* Compensação por data:  
  Data mais antiga;  
  Data mais atual.
* Compensação por tipo:  
  Tipo de ocorrência (extra normal, descanso, compensado e feriado);  
  Código de cálculo (tipo de faixa).

 Além disso, os códigos de cálculo a considerar na compensação poderão ser selecionados conforme necessidade.  
   
Para retornar ao menu 'Compensação/Lançamento do Banco de Horas' Clique aqui
