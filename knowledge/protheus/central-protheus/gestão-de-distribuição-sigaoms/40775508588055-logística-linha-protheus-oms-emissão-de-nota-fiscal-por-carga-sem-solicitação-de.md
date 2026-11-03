---
article_id: 40775508588055
category: Gestão de Distribuição (SIGAOMS)
content_hash: d135bfc9f4f95cc17d23e473fb41bcdc6f81d7ab128f1836a7b21c75d1870d68
fetched_at: '2026-06-28T22:45:49.794949+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Emissão de Nota Fiscal por Carga sem Solicitação
  de Número e Série
type: support-article
updated_at: '2026-05-29T20:29:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40775508588055-Log%C3%ADstica-Linha-Protheus-OMS-Emiss%C3%A3o-de-Nota-Fiscal-por-Carga-sem-Solicita%C3%A7%C3%A3o-de-N%C3%BAmero-e-S%C3%A9rie
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40775504111383) Tempo aproximado para leitura: **00:02:48 min**  
  
**Dúvida**  
Como desabilitar solicitação de Número e Série na Nota Fiscal por Carga?  
  
**Ambiente**  
TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões.  
  
**Solução**  
No **módulo OMS**, disponibilizamos o conceito de **Operador Logístico** que, quando ativado, permite que a rotina **Montagem de Carga - OMSA200** trabalhe com pedidos de múltiplas filiais em uma mesma carga.  
  
Nesse cenário, ao realizar o faturamento da carga pela rotina **MATA460B - Documento de Saída por Carga**, o Sistema apresenta a **tela padrão para seleção da Série e Número da Nota Fiscal**. Como a carga pode conter pedidos de diferentes filiais, o comportamento padrão do Sistema **é solicitar a seleção da Série e Número da NF individualmente para cada filial envolvida no processo**.  
  
Dessa forma, após a geração das Notas Fiscais da primeira filial, o Sistema exibirá novamente a tela de seleção para a próxima filial e assim sucessivamente, até concluir o faturamento de todas as notas relacionadas à carga. Em razão desse comportamento padrão, é necessário que o **usuário realize manualmente a seleção da Série e Número da Nota Fiscal durante o processamento.**

![tela serie 1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/40778044931223)

Para cenários em que seja necessário automatizar esse processo, seja utilizando uma série fixa, uma definição customizada ou eliminando a necessidade de interação manual durante o faturamento de cargas, o **OMS** disponibiliza o **Ponto de Entrada OS460SNF**.  
  
Quando esse Ponto de Entrada estiver implementado, a **tela padrão de seleção da Série da Nota Fiscal não será apresentada durante o faturamento por carga, permitindo que a definição da série ocorra de forma automática e transparente ao usuário.**  
  
Importante destacar que esse comportamento se aplica exclusivamente ao faturamento realizado por carga, através da rotina **MATA460B**. Portanto, caso o faturamento seja efetuado por pedido, utilizando a rotina **MATA460A**, a tela padrão para seleção da Série da Nota Fiscal continuará sendo exibida normalmente.  
  
**Saiba mais**  
Para mais informações e exemplos de implementação, consulte a documentação técnica abaixo:  
[PE OS460SNF - Determina a série utilizada nos documentos de saída por carga](https://tdn.totvs.com/pages/releaseview.action?pageId=612260239)  
[Logística - Linha Protheus - OMS - Montagem de carga compartilhada com pedidos de múltiplas filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027375872-Log%C3%ADstica-Linha-Protheus-OMS-Montagem-de-carga-compartilhada-com-pedidos-de-m%C3%BAltiplas-filiais)  
[Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis Faturamento por Carga - MATA460B - OMSA460B](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012675322-Log%C3%ADstica-Linha-Protheus-OMS-Pontos-de-Entrada-dispon%C3%ADveis-Faturamento-por-Carga-MATA460B-OMSA460B)  
[Logística - Linha Protheus - OMS - Faturamento por carga no TOTVS OMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027664131-Log%C3%ADstica-Linha-Protheus-OMS-Faturamento-por-carga-no-TOTVS-OMS)
