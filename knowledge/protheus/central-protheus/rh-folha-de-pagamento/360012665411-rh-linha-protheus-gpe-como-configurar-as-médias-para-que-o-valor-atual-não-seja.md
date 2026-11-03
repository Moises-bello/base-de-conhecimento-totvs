---
article_id: 360012665411
category: RH - Folha de Pagamento
content_hash: dd333cb88243d80e646e2f68338579796b221106217e58273f85066a7644289e
fetched_at: '2026-06-28T22:44:13.284883+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como Configurar as Médias para que o valor Atual
  não seja menor do que o Valor Original
type: support-article
updated_at: '2025-06-13T20:29:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012665411-RH-Linha-Protheus-GPE-Como-Configurar-as-M%C3%A9dias-para-que-o-valor-Atual-n%C3%A3o-seja-menor-do-que-o-Valor-Original
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18675758562967) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como configurar o Protheus para que o Valor Atual das Médias não seja Menor do que o Valor Original?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução**Na apuração da média, o sistema irá manter o valor original caso o valor atual seja menor que o valor original através do Mnemônico P\_MEDORIG ou parâmetro MV\_MEDORIG.  
  
Com a conversão dos parâmetros (SX6) referentes a médias em mnemônicos (carregará o conteúdo padrão dos mnemônico com uma fórmula para validar conteúdo do parâmetro).  
Caso seja necessária alteração, poderá modificar diretamente o mnemônico e o parâmetro será inutilizado.  
  
Exemplo:  
Caso o funcionário que recebia algum valor que incorporava ao salário, que fez com que o valor de uma hora extra fosse calculada considerando o salário incorporado, e no momento atual da apuração da média o funcionário não recebe mais esse valor.  
O Protheus diminuiu o valor da média dessa verba pois não considera mais o valor que foi incorporado, uma vez que o sistema utiliza o salário atual do funcionário.

Se o mnemônico ou parâmetro estiver configurado com **.T.**, o Valor Atual da Média não será menor do que o Valor Original.  
Caso o Valor Atual seja maior do que o valor original, será mantido o valor atual.

Se configurado com **.F.**, as médias serão apuradas utilizando a remuneração atual do funcionário, podendo apresentar na coluna Valor Atual um valor menor do que o Valor Original.

**Importante:** na inexistência do parâmetro, o sistema irá apurar a média como se o parâmetro estivesse configurado com o **.T.** (verdadeiro).

Para alterar o Mnemônico Acesse: Gestão de Pessoal (**SIGAGPE**) / Atualizações / Definições de Cálculo / Mnemônicos (GPEA300) / Localize o mnemônico **P\_MEDORIG** através do Filtro da rotina:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18675758572055)

Caso opte por alterar o Parâmetro, deixe o mnemônico P\_MEDORIG com o conteúdo SUPERGETMV("MV\_MEDORIG",, .T.) como no exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18675778565527)  
  
  
Para alterar o Parâmetro Acesse: Configurador (**SIGACFG**) / Ambiente / Cadastros / Parâmetros (CFGX017) / Localize o parâmetro **MV\_MEDORIG** através do Filtro da rotina, clique em Alterar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18675778574359)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)  
[RH - Linha Protheus - GPE - Cálculo de médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050726154-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-m%C3%A9dias)
