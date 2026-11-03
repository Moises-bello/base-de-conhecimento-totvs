---
article_id: 15663065954583
category: Metrologia (SIGAQMT)
content_hash: 3f006526e1f546d1d309ffde08e6d2e6300b0e631e9957b27f5daac788026cf3
fetched_at: '2026-06-28T22:42:24.851092+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - QMTA140 - Não atualiza legenda do padrão
type: support-article
updated_at: '2023-06-29T14:36:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15663065954583-Manufatura-Linha-Protheus-SIGAQMT-QMTA140-N%C3%A3o-atualiza-legenda-do-padr%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15663071664023) Tempo aproximado para leitura: **00:01:41 min****Ocorrência**No módulo **SIGAQMT - Metrologia**, ao realizar a calibração do instrumento, as medições são informadas dentro do intervalo especificado, porém a cor da bolinha do padrão não é atualizada. Com isso, ao concluir a calibração, a mesma fica como reprovada.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Qualidade - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**A legenda do padrão não é atualizada, ficando na cor vermelha devido uma parametrização utilizada para esta faixa do instrumento.  
No cadastro da faixa na rotina **QMTA040 - Faixas**, ao informar no campo **Laudo** a opção **2 - Incerteza/Sem Conf Metrológica,** o Sistema validará a incerteza informada no cadastro do instrumento , na rotina **QMTA010 - Instrumentos**, no campo **Inc.Permitid** da aba **Faixas**.  
Quando a **Inc.Permitid** está em branco, o Sistema não consegue identificar qual o valor permitido e por este motivo que o padrão é reprovado.  
  
**Solução**Para evitar que este tipo de situação ocorra durante a calibração do instrumento, deve-se ajustar o cadastro do instrumento, informando uma incidência para a faixa no campo **Inc.Permitid** na rotina **QMTA010**.  
Caso não deseje utilizar uma incerteza no instrumento, é necessário utilizar outro tipo de **Laudo** na faixa deste instrumento.  
  
**Saiba Mais**  
Para mais detalhes sobre o tipos de laudos verifique a documentação [Tipos de Laudos](https://tdn.totvs.com/pages/viewpage.action?pageId=306856133#samples-4).
