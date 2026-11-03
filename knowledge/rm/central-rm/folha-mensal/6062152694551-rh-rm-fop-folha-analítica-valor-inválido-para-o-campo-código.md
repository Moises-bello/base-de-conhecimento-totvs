---
article_id: 6062152694551
category: Folha Mensal
content_hash: defac29cdf627f302035943a1205c4461b1c80423edead2854c6808037829c76
fetched_at: '2026-06-28T22:46:59.186609+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Analítica: Valor inválido para o campo código'
type: support-article
updated_at: '2025-01-22T19:00:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6062152694551-RH-RM-FOP-Folha-Anal%C3%ADtica-Valor-inv%C3%A1lido-para-o-campo-c%C3%B3digo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29426077525015) Tempo aproximado para leitura: **00:01:21 min** **Dúvida**Ao realizar a geração da Folha Analítica é apresentada a seguinte mensagem de erro: **Valor inválido para o campo código**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar esse erro, será necessário importar o relatório **FOPRELL0009 - Folha Analítica**, para isso, realize os seguintes passos:

1. Acesse: **Gestão | RM Reports** | **Processos | Importar Estrutura de Relatório.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29426077529111)

2. Logo, a tela abaixo será aberta para a localização do relatório. Clique no campo **Adicionar Objetos** para importar o relatório de folha analítica. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29426141264407)

3- Após isso, localize e execute o relatório **FOPRELL0009**. Para localiza-lo, siga o caminho abaixo: **C:\TOTVS\CorporeRM\ObjetosGerenciais\Relatórios.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29426077532695)

4- Feito isso, vá em **Folha Mensal | Folha Analítica** e  informe o relatório executado no campo **Código do Relatório (PDF)**, como mostra a imagem a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29426077535639)

5- Para finalizar, avance as telas para prosseguir com a geração da folha analítica e a mensagem de erro não será mais apresentada.

**Saiba Mais**[RH - RM - FOP - RM Reports: Importação de Relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007544951-RH-RM-FOP-RM-Reports-Importa%C3%A7%C3%A3o-de-Relat%C3%B3rios?source=search)
