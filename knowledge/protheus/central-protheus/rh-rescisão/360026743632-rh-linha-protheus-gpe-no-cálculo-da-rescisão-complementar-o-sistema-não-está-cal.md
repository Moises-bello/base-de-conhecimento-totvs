---
article_id: 360026743632
category: RH - Rescisão
content_hash: 4f09dc010c4dc9f9220ee3586fc0af83410355b19da5f2b9a919f03a7ff925fb
fetched_at: '2026-06-28T22:43:52.236977+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - No cálculo da rescisão complementar o sistema não
  está calculando a diferença do id 0118 base FGTS depositado
type: support-article
updated_at: '2025-06-16T17:51:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026743632-RH-Linha-Protheus-GPE-No-c%C3%A1lculo-da-rescis%C3%A3o-complementar-o-sistema-n%C3%A3o-est%C3%A1-calculando-a-diferen%C3%A7a-do-id-0118-base-FGTS-depositado
---

**Dúvida**No cálculo da rescisão complementar o sistema não está calculando a diferença do id 0118, o que verificar?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**No cálculo da rescisão complementar o sistema não está calculando a diferença do id 0118.

Na versão 12 será necessário **informar apenas o valor da diferença da verba de FGTS**, tivemos uma mudança de conceito entre as versões 12 e 11.

Atenção: A diferença deverá ser informada somente se a rescisão complementar não for no mesmo da rescisão original.

Se for no mesmo mês da rescisão original necessário informar o valor "cheio" para o sistema gerar corretamente a GRRF e o id 0120, pois no mês da rescisão original o sistema levará para a RGB o calculo da segunda rescisão.

Na versão 11 os lançamentos eram realizados diretamente na tabela do cálculo SRR, já na versão 12 temos a tabela de movimento mensal RGB.   
  
Outra diferença é a implementação do conceito de períodos, a rescisão original foi calculada no período 201806, já a complementar 201807 logo não será uma alteração da verba lançada na rescisão original e sim um novo lançamento.  
  
Temos também a integridade das informações, o sistema não pode alterar o valor de verbas que foram informadas pelo usuário, com isso na rescisão complementar será utilizado o valor total informado.

 Mais detalhes sobre rescisão complementar no link <http://tdn.totvs.com/x/pEEXEQ>  
  
**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
