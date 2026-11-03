---
article_id: 360027693112
category: RH - Folha de Pagamento
content_hash: e4d79a86b7890e16fddc04e121472b5e466514fa5ea4cd87ec4ffb896adcc9ea
fetched_at: '2026-06-28T22:44:11.816728+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE -  Como configurar o cálculo de múltiplos vínculos
  na versão 12
type: support-article
updated_at: '2026-06-24T20:01:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027693112-RH-Linha-Protheus-GPE-Como-configurar-o-c%C3%A1lculo-de-m%C3%BAltiplos-v%C3%ADnculos-na-vers%C3%A3o-12
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22248139782167) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como configurar o cálculo de múltiplos vínculos na versão 12?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**1 - SIGACFG - CFGX031- Base de dados / Dicionários / Base de dados. Localize a tabela SRA (cadastro de funcionários) e verifique se existe o índice: CPF + Filial + Matrícula.

Caso não exista, crie um novo índice no cadastro de Funcionários (SRA), com a seguinte chave: RA\_CIC+RA\_FILIAL+RA\_MAT.  
  
![](http://tdn.totvs.com/download/attachments/270911833/image2017-1-6%2017%3A6%3A55.png?version=1&modificationDate=1483731061000&api=v2)  
  
![](http://tdn.totvs.com/download/attachments/270911833/image2017-1-6%2017%3A6%3A42.png?version=1&modificationDate=1483731061000&api=v2)  
  
2 - GPEA160 - Atualizações/ Definições de Cálculo/ Roteiros de Cálculo: Habilitar o roteiro  padrão **S\_MULTV:  
![](http://tdn.totvs.com/download/attachments/270911833/image2017-1-6%2017%3A10%3A34.png?version=1&modificationDate=1483731061000&api=v2)**3 -Ter na base de dados os eventos a seguir:  
     3.1 - Folha de pagamento:  
![](http://tdn.totvs.com/download/attachments/240294624/image2016-6-20%2011%3A8%3A36.png?version=1&modificationDate=1466428138000&api=v2)  
       
3.2 - Férias:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027798271)  
  
3.3 - Adiantamento:  
![](http://tdn.totvs.com/download/attachments/240294624/image2016-6-20%2011%3A9%3A12.png?version=1&modificationDate=1466428173000&api=v2)  
       
3.4 - 13º Salário – 2ª Parcela:  
![](http://tdn.totvs.com/download/attachments/240294624/image2016-6-20%2011%3A10%3A7.png?version=1&modificationDate=1466428229000&api=v2)  
       
3.5 - Rescisão:  
![](http://tdn.totvs.com/download/attachments/240294624/image2016-6-20%2011%3A11%3A22.png?version=1&modificationDate=1466428304000&api=v2)  
  
4 - Ter 2 ou mais matrículas com o mesmo CPF para caracterizar o múltiplo vínculo:  
![](http://tdn.totvs.com/download/attachments/270911833/image2017-1-6%2017%3A15%3A27.png?version=1&modificationDate=1483731061000&api=v2)  
  
5 - Conferência:

Exemplo: Cálculo de IRRF: Depois dessa configuração acima, basta calcular a folha das duas matrículas e verificar que já está considerando o múltiplo vínculo para o cálculo.  
  
Exemplo verbas:  
![](http://tdn.totvs.com/download/attachments/270911833/image2017-1-6%2017%3A20%3A23.png?version=1&modificationDate=1483731061000&api=v2)  
  
![](http://tdn.totvs.com/download/attachments/270911833/image2017-1-6%2017%3A23%3A5.png?version=1&modificationDate=1483731061000&api=v2)  
  
![](http://tdn.totvs.com/download/attachments/270911833/image2017-1-6%2017%3A23%3A53.png?version=1&modificationDate=1483731061000&api=v2)  
  
![](http://tdn.totvs.com/download/attachments/270911833/image2017-1-6%2017%3A24%3A32.png?version=1&modificationDate=1483731061000&api=v2)  
  
Exemplo **Cálculo IRRF**:  
![](http://tdn.totvs.com/download/attachments/270911833/image2017-1-6%2017%3A27%3A7.png?version=1&modificationDate=1483731061000&api=v2)  
  
![](http://tdn.totvs.com/download/attachments/270911833/image2017-1-6%2017%3A28%3A53.png?version=1&modificationDate=1483731061000&api=v2)  
  
**Observação:** Esta configuração de múltiplos vínculos somente será calculada automaticamente pelo sistema, quando o funcionário está cadastrado em filiais distintas, porém no mesmo grupo de empresas. Pois no Protheus existem basicamente 2 formas de cadastros de grupo de empresa/filiais:  
  
**1 - Existe apenas um grupo de empresa e todas as filiais pertencem a este grupo:**  
Quando o cliente trabalha neste conceito, o cálculo do múltiplo vínculo funciona automaticamente, pois todas as filiais pertencem ao mesmo grupo de empresa, possui o mesmo RH etc, e isso permite que o roteiro MULTIV reprocesse o cálculo da folha nas duas filiais em que o funcionário está cadastrado atualizando os valores de INSS e IR por exemplo e considerando as bases das duas empresas em tempo real, sem a intervenção do usuário.  
  
**2 - Existe vários grupos de empresas e filiais.**  
Quando o cliente trabalha neste conceito, o cálculo do múltiplo vínculo não funciona automaticamente, pois cada filial pertence a grupos de empresas diferentes e que não se relacionam entre si, não tem relação alguma uma com a outra, é como se fosse bases e empresas totalmente distintas. E que geralmente o RH de cada grupo de empresas são também distintos impedindo que o roteiro **MULTIV** reprocesse o cálculo da folha nos dois grupos de empresas que não se relacionam.   
Neste caso, sugerimos que calcule a folha e após lance manualmente o valor do múltiplo vínculo da outra empresa ID 0289.

**Saber Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)

RH - Linha Protheus - GPE - Tratamento INSS de múltiplos vínculos: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052624413?source=search>  
RH - Linha Protheus - GPE - Novo cálculo múltiplos vínculos de empresas diferentes: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058056993?source=search>
