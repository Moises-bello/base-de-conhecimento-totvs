---
article_id: 360027855571
category: RH - Provisão
content_hash: 801f8b87f676055c0d4d6c69f65409c8a157ecef32b0333b29c092b3a4e43f5f
fetched_at: '2026-06-28T22:43:55.846968+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Provisionar Férias e 13º Salário Sobre o Aviso
  Prévio no mês da Demissão
type: support-article
updated_at: '2025-06-17T19:55:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027855571-RH-Linha-Protheus-GPE-Como-Provisionar-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio-Sobre-o-Aviso-Pr%C3%A9vio-no-m%C3%AAs-da-Demiss%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16477510393239)**Tempo aproximado para leitura: **00:01:30 min****Dúvida**Como Provisionar Férias e 13º Salário Sobre o Aviso Prévio no mês da demissão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões.  
  
**Solução**O Mnemônico**P\_PROVAVP**possibilita a opção entre provisionar ou não Férias e Décimo Terceiro Salário Sobre o Aviso Prévio Indenizado no mês de demissão do empregado.

1. Em Gestão de Pessoas acesse: Atualizações/ Definições de cálculo/ Mnemônicos e altere o Mnemônico **P\_PROVAVP** para **"S".  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16476641762583)**2. Após a alteração, realize o cálculo das Provisões novamente.

3. Rescisão do Funcionário:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18330970188055)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18330997512215)

4. Emita o Relatório de Provisão acessando Relatórios / Provisões / Provisão de Férias (GPER070) ou Provisão  de 13º Salário (GPER090):

Provisao de Férias:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18330921832727)

**Memória de Cálculo:**  
  
**Valor:** Férias Prop. Indenizadas + Férias Aviso.

Verba 042 - Férias Proporcionais - 1.494,70  
Verba 076 - Férias Aviso Indenizado - 166,08  
1.494,70 + 166,70 = **1.660,78**

**1/3 Constit.:** 1/3 Férias Prop. Indenizadas + 1/3 Férias Aviso.

Verba 088 - 1/3 Férias Proporcionais - 498,23  
Verba 077 - 1/3 Férias Aviso Indenizado - 55,36  
498,23 + 55,36 = **553,59  
  
Observação:** Como as Indenizações de Férias em Rescisão não tem indidência sobre o INSS e o FGTS, não serão geradas Baixas sobre os encargos, e os valores provisionado até o mês anterior serão apresentados em negativo na linha "No Mês".

Provisão de 13º Salário:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18330954796951)

**Memória de Cálculo:**  
  
**Valor:** 13º Salário Proporcional + 13º Aviso.

Verba 058 - 13 º Salário Proporcional - 830,39  
Verba 059 - 13º Salário Ind. Aviso - 332,16  
830,39 + 332,16 = **1.162,55**

**Observação:** Como ha tributação de 13º salário indenizado em rescisão, serão geradas Baixas sobre os encargos de INSS e FGTS, de acordo com os valores calculados em Rescisão.

**Importante**: Para Provisionar Férias e 13º Salário Sobre o Aviso Prévio no mês da demissão, além do mnemônico, é necessário que o parâmetro **MV\_PROVRES** esteja configurado com S.

**Saiba Mais**[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
