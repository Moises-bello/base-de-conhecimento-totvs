---
article_id: 360007061372
category: RH - Lançamentos
content_hash: 8171fd9c235a71298e346503ebf2182c338d5d6cbfdf17d92aad0c27dc330243
fetched_at: '2026-06-28T22:44:46.809889+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON - Como efetuar desconto de DSR no próximo período
type: support-article
updated_at: '2025-06-12T20:43:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007061372-RH-Linha-Protheus-PON-Como-efetuar-desconto-de-DSR-no-pr%C3%B3ximo-per%C3%ADodo
---

**Dúvida**Como efetuar **desconto de DSR no próximo período?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O Protheus permite **nos casos onde ocorre qualquer ocorrência de desconto na última semana do período**, como faltas, atrasos ou saídas antecipadas, que o **desconto de DSR referente a esta ocorrência, fique pendente e seja processado apenas no período seguinte.** Para isso, siga as configurações abaixo:

1. Ative o parâmetro **MV\_DSRPPER**![](https://tdn.totvs.com/download/attachments/273303121/image2021-5-20_10-52-5.png?version=1&modificationDate=1621518725684&api=v2)

2. **Período de apontamento** que será utilizado no **exemplo**![](https://tdn.totvs.com/download/attachments/273303121/image2021-5-20_10-58-15.png?version=1&modificationDate=1621519095732&api=v2)

3. Cadastre o **evento com ID 022A** e configure-o com **Sim** no campo **Desc. DSR**![](https://tdn.totvs.com/download/attachments/273303121/image2021-5-20_10-59-14.png?version=1&modificationDate=1621519155070&api=v2)

**Importante:** O Identificador de Ponto 022A é **apenas referência** para que ocorra o Desconto do DSR no próximo período. Ele **NÃO** é o próprio desconto de DSR, apenas será considerado neste evento a totalização de atrasos/faltas do período anterior que ocorreram na última semana, para que sobre ele, seja feito o desconto do DSR.

4. Funcionário com **2 faltas na última semana** do período de apontamento, nos dias **19/05 e 20/05**![](https://tdn.totvs.com/download/attachments/273303121/image2021-5-20_11-0-29.png?version=1&modificationDate=1621519230745&api=v2)

5. Apontamentos gerados com as **duas faltas nos dias 19/05 e 20/05**![](https://tdn.totvs.com/download/attachments/273303121/image2021-5-20_11-2-55.png?version=1&modificationDate=1621519375304&api=v2)

6. Cálculo mensal do ponto para o período  
![](https://tdn.totvs.com/download/attachments/273303121/image2021-5-20_11-4-39.png?version=1&modificationDate=1621519479143&api=v2)

7. Resultados **após calculo mensal**. **Desconta as faltas** porém o **DSR ficará para o próximo período**, por isso, não foi descontado  
![](https://tdn.totvs.com/download/attachments/273303121/image2021-5-20_11-5-16.png?version=1&modificationDate=1621519516688&api=v2)

8. Observe que no **primeiro dia do próximo período (no exemplo, 21/05)** foi gerado o evento correspondente ao **ID 022A em apontamentos**![](https://tdn.totvs.com/download/attachments/273303121/image2021-5-20_11-6-4.png?version=1&modificationDate=1621519564686&api=v2)

9. Marcações do funcionário no **período seguinte, de 21/05 à 20/06**![](https://tdn.totvs.com/download/attachments/273303121/image2021-5-20_11-7-1.png?version=1&modificationDate=1621519621816&api=v2)

10. Apontamentos gerados, **veja que consta o evento referente ao ID 022A**![](https://tdn.totvs.com/download/attachments/273303121/image2021-5-20_11-6-8.png?version=1&modificationDate=1621519568713&api=v2)

11. Cálculo mensal do ponto para o novo período

![](https://tdn.totvs.com/download/attachments/273303121/image2021-5-20_11-7-52.png?version=1&modificationDate=1621519673043&api=v2)

12. Resultados após o cálculo, veja que **gerou o desconto do DSR sobre o ID 022A, que é referente as faltas da última semana do período anterior**![](https://tdn.totvs.com/download/attachments/273303121/image2021-5-20_11-8-46.png?version=1&modificationDate=1621519726858&api=v2)

**Observação:** Se por alguma necessidade for preciso descontar **apenas** DSR utilizando um abono, é necessário **amarrar a própria verba de Desconto de DSR no cadastro de Motivo de Abono**, exemplo:  
A configuração da regra de apontamento está para **não descontar DSR** em caso de faltas, porém gostaria de abrir uma exceção e descontar apenas um DSR de um funcionário que faltou. Para isso Crie um **Motivo de Abono** e no campo **Cód. Verba** amarre o **próprio evento de Desconto de DSR**, após isso, informe nos apontamentos esse Abono para o dia que foi gerada falta.  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
