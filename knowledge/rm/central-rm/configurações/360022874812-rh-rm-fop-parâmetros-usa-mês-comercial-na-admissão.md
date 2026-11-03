---
article_id: 360022874812
category: Configurações
content_hash: d26f13111be490832e5ae8874d87e170f3da410c3c51c59938355de3116d09d2
fetched_at: '2026-06-28T22:46:49.628886+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: 'RH - RM - FOP - Parâmetros: Usa mês comercial na admissão'
type: support-article
updated_at: '2025-03-05T18:49:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022874812-RH-RM-FOP-Par%C3%A2metros-Usa-m%C3%AAs-comercial-na-admiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:01:00 min  
  
Dúvida**Como utilizar e qual a funcionalidade do parâmetro **Usa mês comercial na admissão**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Selecione esta opção para que o sistema considere, para o cálculo dos dias trabalhados na admissão, o número de dias de um mês comercial - 30 dias. O parâmetro apenas é válido para mensalistas. No caso de funcionário horista e tarefeiro, o sistema não verifica o parâmetro, sendo que será considerando os dias efetivos do mês calendário.  
  
Se o campo não for marcado, o sistema irá considerar para o cálculo os dias trabalhados na admissão, o número de dias efetivos do mês seja, 28, 29, 30 ou 31 dias, caso o funcionário seja admitido após o dia 01 do mês. Se o funcionário for admitido no dia 01 de algum mês que a quantidade de dias efetivos for diferente de 30 o sistema mesmo assim irá considerar 30 dias para os funcionários mensalistas.  
  
Para que o sistema considere o mês comercial, acesse: **Configurações | Parametrizador | Folha Normal** e marque o parâmetro **Usa mês comercial na admissão.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10976306779927)**No cálculo da folha, o evento de pagamento será calculado da seguinte forma:

```
Calculando evento: 0002 - DIAS TRABALHADOS  
 Código de Cálculo 2 - Prioridade 0  
   
 Funcionário admitido este mês.  
 Data de Admissão: 02/05/2018  
 Total de dias trabalhados no mês: 29  
 Salário Base: 7.500,00  
 Salário Dia: Salário(7.500,00) / 30 = 250,000000  
 Valor pago: 29 dias * 250,000000 = 7.250,000000  
 Valor do evento: 7.250,00
```

**Saiba mais**  
Veja o exemplo do funcionamento do parâmetro de acordo com meses de 31 e 28 dias, com o parâmetro marcado e desmarcado:  
  
**Mês 31 dias**

|  |  |  |
| --- | --- | --- |
| Admissão | Parâmetro Desmarcado | Parâmetro Marcado |
| Funcionário admitido em 01/12 | 30 dias | 30 dias |
| Funcionário admitido em 02/12 | 30 dias | 29 dias |
| Funcionário admitido em 11/12 | 21 dias | 20 dias |
| Funcionário admitido em 16/12 | 16 dias | 15 dias |

**Mês 28 dias**

|  |  |  |
| --- | --- | --- |
| Admissão | Parâmetro Desmarcado | Parâmetro Marcado |
| Funcionário admitido em 01/02 | 30 dias | 30 dias |
| Funcionário admitido em 02/02 | 27 dias | 29 dias |
| Funcionário admitido em 11/02 | 18 dias | 20 dias |
| Funcionário admitido em 16/02 | 13 dias | 15 dias |
