---
content_hash: 91ee5d929962a96a03c1d9638bc079ef8731aa0d9d50be01778b9ab954dfaa8c
fetched_at: '2026-06-29T00:10:03.153710+00:00'
page_id: '452719030'
product: rm
source: tdn-rm
title: Adicional Noturno - Parametrizador
type: documentation
url: https://tdn.totvs.com/display/LRM/Adicional+Noturno+-+Parametrizador
version: 3
---

**Adicional Noturno**   
**Pagar adicional noturno:** Determina se será lançado o evento de adicional noturno para o funcionário que trabalhar neste período, segundo os horários informados nos campos início e fim, do cadastro de parâmetros do sindicato.   
Deixando o espaço em branco, o sistema irá ignorar o adicional noturno.

Importante

* O  cálculo de adicional noturno pode variar em feriados, tudo irá depender da solução de conflito utilizada e tipo de horário.
* Sendo um horário com limite, com solução de conflito **"Considera Apenas o Feriado"** que tenha interseção entre o dia do feriado e o dia que se encerra a jornada, é feita uma quebra a 00:00, que mesmo que o funcionário tenha feito batidas para refeição dentro do limite e sendo antes da 00:00, esse intervalo não é considerado como ausência de refeição e consequentemente se o intervalo feito ultrapassar as 22:00 (considerando o início do adicional noturno), não é entendido como adicional noturno, fica-se entendido que o funcionário ficou ausente neste tempo e não contabiliza este adicional.
* Uma solução de contorno para este cenário, seria diminuir o limite para que não haja tal interseção. Desta forma é considerada as batidas realizadas dentro deste limite cadastrado, que mediante a parametrização pode ser considerada também como adicional noturno.

   
**Pagar nona hora:** Determina se será lançado o evento nona hora para o funcionário que trabalhar no período de adicional noturno, determinado na tabela de parâmetros do sindicato.  
Deixando o espaço em branco, o sistema não lançará este evento.   
   
**Observação:** Se o funcionário efetuar horas extras no período noturno e as extras não forem autorizadas o sistema não irá calcular nona hora se o parâmetro Acrescenta a nona hora às horas extras estiver marcado.  
Caso o parâmetro não esteja marcado o sistema vai calcular nona hora mesmo se a extra não for autorizada.  
   
**Exemplo:** Se um funcionário trabalhou de 22:00h às 24:00h, ele terá 00:07:30 min multiplicado por 2 (são duas horas de adicional) totalizando 00:15:00 min de nona hora.
