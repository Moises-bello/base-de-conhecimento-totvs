---
content_hash: b3835f0cc04510943d16b39ca9e7d216e6fac7be082c1b886e97397987d9cbda
fetched_at: '2026-06-29T00:09:12.806218+00:00'
page_id: '417700535'
product: rm
source: tdn-rm
title: Taxa Global
type: documentation
url: https://tdn.totvs.com/display/LRM/Taxa+Global
version: 1
---

**Taxa Global**   
O cubo taxa global faz parte das estatísticas do menu Relatórios. Expressa a taxa global do hospital a partir dos relatórios por Unidade/Especialidade e por Sítio Primário/Secundário.   
   
Por Unidade/Especialidade  
Quando selecionar filtro sítio primário "todos os sítios" o relatório apresentará um resultado trazendo todas as infecções por todos os sítios.  
Quando selecionar um filtro por um determinado sítio primário você poderá também selecionar todos os sítios secundários ou algum especifico.  
Dimensões: Especialidade, Unidade Clínica (taxa geral/unidade clínica).  
Fatos de análise: Internações, Infecção, Tx. de infecção (%), Pac/dia, (Infec/Pac. dia) x 1000, Infectados, Tx. Infectados (%).  
   
Por Sítio Primário/Secundário  
Filtro: Unidade Clínica. Permite você filtrar todas as unidades clínicas ou uma isoladamente.  
Campos Internações e Paciente/dia apresentando os valores destes correspondentes ao período da análise.  
Dimensões: Sítio Primário e Sítio Secundário que podem ser analisadas juntas ou em separado.  
Fatos de análise: Infecção, Tx. de infecção (%), (Infec/Pac. dia) x 1000, Infectados, Tx. Infectados (%).  
   
**Observações:**  
Você poderá comparar os dois relatórios se estiverem analisando o mesmo período o número de internações e de paciente/dia deverão apresentar o mesmo valor.   
 A Unidade Clínica Berçário, categoria C, o denominador é informado pelo usuário e pode ser de forma mensal ou diária a critério de cada usuário. Vale ressaltar um ponto importante: quando a opção for mensal ocorre que este valor permanecerá fixo. Se você gerar um relatório de taxa global referente a um determinado mês o valor deste aparecerá fixo mensal, entretanto, se o período do relatório for inferior a um mês, o valor será o mesmo e integral, pois, é um valor fixo referente ao mês. Caso  envolva partes de meses diferentes o valor do denominador será a soma dos meses envolvidos.  Para obter um valor mais próximo do real em caso de quebras é necessário que o cadastro do denominador em população | admissões seja diário. Assim, ao solicitar qualquer período gerará o relatório criando o denominador pela soma dos dias que foram cadastrados.   
   
Para entendimento do conceito desta taxa é necessário saber o conceito dos fatos de análise.  
Internações: quantidade de internações ocorridas no período. Conta apenas internações distintas.   
Infecções: quantidade de infecções ocorridas no período. Conta apenas infecções distintas.  
Tx. Infecção (%): quantidade de infecções / quantidade de internações   
Pac. dia: quantidade de pacientes/dia.  
(Infec/Pac. dia) x 1000: (quantidade de infecções / quantidade de pacientes/dia) x 1000  
Infectados: quantidade de pacientes que tiveram infecções, independentes de quantas infecções cada um teve.  
Tx. Infectados (%): quantidade de infectados / quantidade de internações.  
   
-Não se soma a linha do Grand total das colunas Tx.Infec.%, (Infec/Pac.Dia)\*1000, Tx Infectados%. Realiza-se os cálculos:  
Tx.Infec.% = (total Infecções/Total Internações)\*100  
(Infec/Pac.Dia)\*1000 = (Total Infecções/Total Pac/Dia)\*1000  
Tx Infectados% = (Total Infectados/Total Internações)\*100
