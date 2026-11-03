---
content_hash: fda8f035ea5926106ca721a8b331be67f177b413a053793612649e0ea8c2f852
fetched_at: '2026-06-29T00:10:11.268198+00:00'
page_id: '452720020'
product: rm
source: tdn-rm
title: Tabela de Atrasos
type: documentation
url: https://tdn.totvs.com/display/LRM/Tabela+de+Atrasos
version: 3
---

**Tabela de Atrasos**

Cadastro de intervalos diários que definem o tempo a ser considerado de atrasos no dia.  
**Atenção:** Para que este cálculo seja considerado, é necessário que a tabela de atrasos esteja  
definida como **Diário** na etapa de **Atrasos e Faltas** no **Parametrizador do Sindicato**.

Exemplo:

Jornada do funcionário: 08:00 12:00 13:00 17:00  
Horário executado: 08:10 12:00 13:00 16:50

Intervalos cadastrado na tabela de atrasos:

1. Início: 00:00 Fim: 00:10 Desconsiderar: 00:00
2. Início: 00:10 Fim: 00:20 Desconsiderar: 00:10

Cálculo das ocorrências:

08:00 - 08:10 = Atraso  
08:10 - 12:00 = Trabalho  
13:00 - 16:50 = Trabalho  
16:50 - 17:00 = Saída antecipada

No exemplo de jornada acima, o funcionário teve um total de 20 min de atrasos no dia, sendo 10 min ao início  
da jornada e 10 min ao fim da jornada.

Com os intervalos que foram cadastrados na tabela de atrasos, o sistema irá calcular o total de atrasos do dia e irá  
verificar qual intervalo cadastrado se encaixa na quantidade de horas.

Para o exemplo acima, o intervalo escolhido será o 2, pois este considera valores entre 10 e 20 min, como no dia temos   
20 min, está dentro da faixa considerada. Não será considerado o intervalo 1, pois este considera apenas valores até 10 min.

Desta forma, o cálculo das ocorrências será o seguinte:

08:00 - 08:10 = Atraso  
08:10 - 12:00 = Trabalho  
13:00 - 16:50 = Trabalho  
16:50 - 17:00 = Saída antecipada desconsiderada

**Considerações importantes (Versões à partir da 12.1.31)**

1. A tabela de atrasos não é considerada na compensação do horário flexível/semi-flexível;
2. Os parâmetros **Realiza a compensação de cálculo antes da autorização das extras** e **Realiza a compensação de****cálculo antes de abonar** não surtem efeito para este cálculo;
3. Os cálculos da tabela de atrasos ocorrerão após o cálculo dos abonos
