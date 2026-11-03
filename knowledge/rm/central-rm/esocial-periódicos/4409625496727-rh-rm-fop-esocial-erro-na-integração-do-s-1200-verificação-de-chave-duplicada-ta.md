---
article_id: 4409625496727
category: esocial - Periódicos
content_hash: 7df0b97d6bfd180aab03e25e150f6789b1a38dfe0e50e12f37dff87d0837e04e
fetched_at: '2026-06-28T22:47:09.362487+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na integração do S-1200: Verificação de chave
  duplicada. Tabela C9M - Grupo itensRemun'
type: support-article
updated_at: '2024-06-28T19:50:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409625496727-RH-RM-FOP-eSocial-Erro-na-integra%C3%A7%C3%A3o-do-S-1200-Verifica%C3%A7%C3%A3o-de-chave-duplicada-Tabela-C9M-Grupo-itensRemun
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24453911176727) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao realizar a integração dos eventos periódicos com o TAF, após executar o processamento de *Jobs*, o sistema apresenta no **Gerenciador de Integração** o erro:**Verificação de chave duplicada, Erro de chave duplicada, favor verificar as informações que estão sendo integradas. Tabela: C9M - Grupo da Tag: itensRemun.**

![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409603766167)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro geralmente ocorre para o evento quando o XML possui a *tag* **codRubr** duplicada no mesmo grupo de remuneração. A *tag* **codRubr**deverá conter um identificador único não podendo se repetir dentro do grupo de remuneração ao qual pertence (**remunPerApur** ou **remunPerAnt**).

Abaixo, exemplo de **codRubr** duplicado:

![codrubr_duplicado.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409695080471)

**Solução**Para correção da ocorrência favor realizar as validações abaixo:

• **D****istribuição do SEFIP**

Para empresas que utilizam tomadores de serviço, o sistema irá buscar as verbas para montagem do XML na distribuição do SEFIP realizada. Desta forma, verifique em **Encargos | SEFIP | Distribuir SEFIP** a distribuição realizada para o mês/ano correspondente ao período de apuração.

• **De/Para eventos férias eSocial (S-1200)**

No parametrizador do eSocial foi criado um **De/Para** para incluir novos eventos a serem gerados no XML do S-1200. As verbas informadas nesses campos devem ser diferentes dos eventos originalmente informados no envelope do funcionário, e não podem possuir código de cálculo ou incidência.  Para verificar acesse **Configurações |** **Parametrizador | eSocial | Configurações Gerais 6/7.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24511236708503)

**Saiba mais**  
Para mais informações acesse:   
     - [Configurações Gerais 6/7](https://tdn.totvs.com/pages/releaseview.action?pageId=540899121)  
     - [Rateio por Tomador de Serviço](https://tdn.totvs.com/pages/releaseview.action?pageId=453280016#deck02-6)
