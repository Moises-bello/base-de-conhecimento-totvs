---
article_id: 32803208415639
category: RH - Provisão
content_hash: 5e590032c7273977e3d2905c90d7ae165578b256ae07367ae696e7baa5498388
fetched_at: '2026-06-28T22:43:55.787250+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Conferir os Relatórios de Provisão com Transferência
  de Item Contábil
type: support-article
updated_at: '2025-06-13T19:59:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32803208415639-RH-Linha-Protheus-GPE-Como-Conferir-os-Relat%C3%B3rios-de-Provis%C3%A3o-com-Transfer%C3%AAncia-de-Item-Cont%C3%A1bil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32803208382999) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como Conferir os Relatórios de Provisão com Transferência de Item Contábil?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

O parâmetro **MV\_TRFAMES** indica o Ano/Mês (deve ser preenchido no formato AAAAMM) inicial de utilização, na demonstração das transferências na **Provisão**.

**Exemplo:** Funcionário sem informações do Item Contábil preenchido no cadastro do funcionário. Foi habilitado o parâmetro **[MV\_ITMCLVL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020271991-RH-Linha-Protheus-GPE-Par%C3%A2metro-MV-ITMCLVL-para-configura%C3%A7%C3%A3o-de-Item-e-Classe-de-Valor),** para utilização do campo, e efetuada a transferência para o Item Contábil em 01/05/2025.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32803208384535)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32803208385943)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32803148162327)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32803148165783)

Independente do preenchimento do parâmetro MV\_TRFAMES, ao consultar o Acumulado de Provisões (GPEA070), no mês da transferência serão apresentadas duas linhas com o cálculo de provisão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32803148166423)

O movimento 5, refere-se à Baixas de Transferências, e será calculada para o Item Contábil Origem.  
O movimento 6, refere-se à Entrada do saldo de Transferência, e será calcula para o Item Contábil Destino.

Relatório de Provisão com o Parâmetro Preenchido:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32803148156439)

No Relatório de Provisão do Centro de Custo, Empresa ou Filial de Origem, os valores provisionados até o mês anterior são baixados na linha **"Val. Baixa Saída"**, zerando o Saldo Atual para este Centro de Custo, Empresa ou Filial.  
No Centro de Custo, Empresa ou Filial de Destino, os os valores de Provisão serão apresentados na linha **"Val. Baixa Entr."** para que o Saldo baixado na movimentação seja provisionado no novo Item Contábil, Centro de Custo, Empresa ou Filial do funcionário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32803569868055)

Relatório de Provisão com o Parâmetro Em Branco:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32803593341079)

No Relatório de Provisão do Centro de Custo, Empresa ou Filial de Origem, os valores provisionados até o mês anterior são apresentados como Baixa de Transferência, zerando o Saldo Atual para este Centro de Custo, Empresa ou Filial .  
No Item Contábil, Centro de Custo, Empresa ou Filial de Destino, o Protheus provisiona todos os avos de direito do funcionário. Todo o direito que o funcionário tem será provisionado de uma só vez, na linha **"No Mês"** e a partir do mês seguinte passará a calcular com informações na linha **"Anterior"**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32803569870487)

**OBS:**O mesmo ocorre quando já existe Item Contábil preenchido no cadastro do funcionário e é realizada a transferência.

**Saiba Mais:**

[Provisão com Transferência](https://tdn.totvs.com/pages/releaseview.action?pageId=233744464)   
[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
