---
article_id: 360048496053
category: Configurações
content_hash: b5fdae28326c8a33f0a40b7284d179377962cbbea86b236930bdf8350084e5ef
fetched_at: '2026-06-28T22:46:49.616731+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Ajuste de dependente de IRRF
type: support-article
updated_at: '2021-06-18T13:23:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048496053-RH-RM-FOP-Ajuste-de-dependente-de-IRRF
---

**Ocorrência**Identificamos uma situação na liberação de competência, referente ao processo de atualização de dependente de IRRF.   
  
Patches que causam a ocorrência:   
12.1.25.269 a 12.1.25.273   
12.1.26.214 a 12.1.26.220  
12.1.27.169 a 12.1.27.175  
  
**Importante:**Clientes que estão nas releases 12.1.28 ou inferiores a 12.1.25 não precisam se atentar a essa situação.  
  
**Ambiente**RM – Totvs Folha de Pagamento – Ajuste a partir dos Patches 12.1.25.276 | 12.1.26.223 | 12.1.27.178  
  
**Causa**Causa uma inconsistência na atualização de dependente de IRRF através do processo de liberação de competência, ocorrendo somente quando o dependente tem o grau de parentesco "1-Filho Valido" ou "3-Menor Pobre". Para estes casos, o sistema desmarcou a incidência de IRRF no Cadastro do Dependente, mesmo quando a idade do dependente era inferior a 22 anos ou inferior a 25 anos e era universitário.   
  
**Solução**Para realizar os ajustes nesses dependentes, foi criado o processo de**Ajuste de Dependentes IRRF**, conforme o print abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071221633/mceclip0.png)  
  
Este processo tem como objetivo realizar a correção de forma automática no cadastro dos dependentes, portanto irá fazer a comparação entre:   
  
● o valor do campo "Nro. Dependente IRRF" da competência anterior (Funcionários | Anexo | Históricos de Dependentes)  
  
● a quantidade de dependentes que possuem o grau de parentesco igual "1-Filho Valido" e "M-Menor Pobre". (Funcionários | Anexo | Dependentes)  
  
● a quantidade de dependentes que NÃO incide IRRF, que possuem o grau de parentesco igual "1-Filho Valido" e "M-Menor Pobre" e a idade do dependente é inferior a 22 anos ou inferior a 25 anos e é universitário.  
  
Caso as três quantidades obtidas acima sejam iguais, o sistema irá realizar de **forma automática** a atualização (**marcar a incidência de IRRF** em todos os dependentes que deveriam estar incidindo).  
  
Para os casos que existirem diferenças, será exibido um grid no processo para que o usuário possa tomar a decisão de quais os dependentes devem ter ou não a incidência marcada.  
  
**Importante:**O processo irá realizar a alteração no cadastro de funcionário sendo: Dependentes (campo PFDEPEND: INCIRRF), Históricos de Dependentes (PFHSTNDP: NRODEPENDIRRF) e no campo "Nro. Dep. IRRF" (campo PFUNC: NRODEPIRRF).  
  
Esse processo ficará disponível somente nas versões 12.1.27, 12.1.26 e 12.1.25, isso porque a partir da versão 12.1.28 não há essa inconsistência.  
  
**Informações mais detalhadas,** [clique aqui](https://tdn.totvs.com/display/public/LRM/Ajuste+Dependente+IRRF#1-2).
