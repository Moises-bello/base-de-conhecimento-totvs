---
article_id: 360007514372
category: Funcionários
content_hash: 07b20fd26c39e25e6ea1242b1803540d444875514e1cc6c443570e0a0087888c
fetched_at: '2026-06-28T22:47:04.235798+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: 'RH - RM - FOP - Afastamento: Considera carência conforme tipo do afastamento'
type: support-article
updated_at: '2025-08-07T13:46:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007514372-RH-RM-FOP-Afastamento-Considera-car%C3%AAncia-conforme-tipo-do-afastamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:01:50 min  
  
Dúvida**Como parametrizar o Totvs Folha de Pagamento para considerar o período de carência conforme o tipo do atestado médico?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
 **Solução**Hoje o sistema realiza um tipo de cálculo para a carência que leva em consideração todos os intervalos de afastamentos de acordo com o motivo. Para que na apuração dos dias de atestado médico sejam considerados somente os afastamentos conforme o tipo do afastamento do funcionário, e assim seja aplicada a regra da carência com base nestes afastamentos, é necessário seguir os passos abaixo:

* **Parâmetro marcado**

1. Acesse: **Configurações | Parametrizador** **| Folha Normal | Afastamento 1\2** e marque o parâmetro **Atestado Médico considera somente afastamentos da última sequência do período de carência.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419712399511/mceclip0.png)**Realizando esta parametrização o sistema irá considerar como base o primeiro dia do atestado médico da competência atual e irá validar todos os afastamentos até os dias definidos de acordo com o tempo de carência parametrizado em **Configurações | Parametrizador | Folha Normal | Afastamento 1\2**. Caso encontre atestados em interseção dentro dos dias de atestado, ele irá validar quantos dias já foram pagos e irá lançar somente o residual até que se completem os 15 dias relativos à empresa.  
  
Veja o exemplo abaixo para facilitar ao entendimento:  
  
Atestado Medico (Previdência) - Código de calculo 145  
Dias de carência para afastamento com o mesmo motivo: 60  
Folha competência junho/2018  
  
Histórico de afastamento do funcionário:  
  
1. 01/06/2018 à 01/06/2018 = 01 dias  
2. 01/04/2018 à 05/04/2018 = 05 dias  
3. 01/03/2018 à 10/03/2018 = 10 dias  
  
No cálculo da folha do mês junho/2018 o sistema tomará por base o inicio do afastamento 1 e irá aplicar a regra dos 60 dias para validar outros afastamentos com o mesmo motivo. O afastamento 2 será considerado no cálculo, uma vez que o final deste afastamento é o dia 05/04 e com isso ele está dentro do período dos dias da carência - regressivo de 01/06 até 02/04. O afastamento 3 não irá entrar para o cálculo, porque é anterior ao período final da carência, dia 02/04.

* **Parâmetro desmarcado**

Quando o parâmetro **Atestado Médico considera somente afastamentos da última sequência do período de carência**estiver desmarcado os dias de carência serão considerados apenas nos intervalos entre atestados lançados. Ou seja, o sistema irá contar os dias de carência e, encontrando um afastamento com o mesmo motivo, irá considerá-lo para o cálculo. Isso é feito recorrentemente até que não sejam encontrados mais afastamentos com o mesmo motivo.   
  
Veja o exemplo abaixo para facilitar ao entendimento:  
  
Atestado Medico (Previdência) - Código de calculo 145  
Dias de carência para afastamento com o mesmo motivo: 60  
Folha competência junho/2018  
  
Histórico de afastamento do funcionário:  
  
1. Atestado médico: 01/06/2018 à 01/06/2018 = 01 dias  
2. Atestado médico: 01/04/2018 à 05/04/2018 = 05 dias  
3. Atestado médico: 01/03/2018 à 10/03/2018 = 10 dias  
  
Afastamento 02  
O tempo total do afastamento 01 até o afastamento 02 totalizam 57 dias. Como no nosso exemplo a carência são 60 dias, este afastamento será contado no cálculo, relativo a 05 dias de afastamento.  
  
Afastamento 03  
O tempo total do afastamento 02 até o afastamento 03 totalizam 22 dias. Como no nosso exemplo a carência são 60 dias e com o parâmetro desmarcado o sistema valida somente o intervalo entre os afastamentos, este afastamento também será contado no cálculo, relativo a 10 dias de afastamento.  
  
Os 10 dias pagos no afastamento 03 com os 05 dias pagos no afastamento 02 totalizam 15 dias. Por isso, o afastamento 01, relativo a um dia, será pago pela previdência, pois a soma dos três afastamentos totalizam 16 dias.
