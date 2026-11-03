---
article_id: 360016249711
category: RH - 13º salário
content_hash: 7637aea16f8014334367d2d65b512da07f94e2ee731b44db042f602ae1cfc77b
fetched_at: '2026-06-28T22:44:01.641648+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não calcula verbas de médias no 13º salário
type: support-article
updated_at: '2025-08-15T19:08:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016249711-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-calcula-verbas-de-m%C3%A9dias-no-13%C2%BA-sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**No módulo Gestão de Pessoal, ao tentar realizar o Cálculo de 13º Salário  sistema não calcula verbas de Médias.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Esse incidente ocorre, pois a **parametrização das verbas** que envolvem cálculo de 13º salário não possui a configuração correta para cálculo de médias.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

Utilizaremos como exemplo uma verba de Hora Extra paga durante o Ano, porém aplica-se a **qualquer verba variável** que o funcionário receba e que entenda que deve considera-la para médias.

Para que o sistema calcule as médias, analise:

1 - A verba de Hora Extra, **deve** **constar na tabela SRD** (Acumulados), dentro do ano de pagamento do 13º;

2 - No **cadastro da verba** de H.E, na aba Médias, deve estar configurado com **S** no campo **Média 13º**;

3 - No **cadastro de Sindicato**, o campo **Meses Med 1º**, deve conter a **quantidade de meses** que o sistema irá buscar na SRD  
Exemplo: Para que sistema verifique na SRD o recebimento de Horas Extras dos últimos 6 meses, configure com 6 este campo.

4 - **Cadastro das verbas** com identificador de cálculo abaixo na SRV (Atualizações - Def. de Cálculo - Verbas)

**0123** (Médias em Valor)  
**0124** (Médias em Horas)   
**1628** (Total de Médias em Valor 1º Parc)  
**1629** (Total de Médias em Horas 1ºParc)

**Observações**  
Todas as verbas devem ser **Provento**. Sobre as incidências, caso tenha dúvida do que deve ou não incidir sobre as mesmas, orientamos a fazer uma consulta jurídica.

**Saiba Mais****[RH - Linha Protheus - GPE - Médias no cálculo do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016223611-RH-Linha-Protheus-GPE-M%C3%A9dias-no-c%C3%A1lculo-do-13%C2%BA-Sal%C3%A1rio)****[RH - Linha Protheus - GPE - Apuração das médias do 13º não batem com o cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019896372-RH-Linha-Protheus-GPE-Apura%C3%A7%C3%A3o-das-m%C3%A9dias-do-13%C2%BA-n%C3%A3o-batem-com-o-c%C3%A1lculo)  
[RH - Linha Protheus - GPE - Como analisar médias no calculo de 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015780592-RH-Linha-Protheus-GPE-Como-analisar-m%C3%A9dias-no-calculo-de-13%C2%BA-Sal%C3%A1rio)****[RH - Linha Protheus - GPE - Como gerar memória de calculo para conferência de médias da primeira parcela do 13º](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000096841-RH-Linha-Protheus-GPE-Como-gerar-mem%C3%B3ria-de-calculo-para-confer%C3%AAncia-de-m%C3%A9dias-da-primeira-parcela-do-13%C2%BA)**
