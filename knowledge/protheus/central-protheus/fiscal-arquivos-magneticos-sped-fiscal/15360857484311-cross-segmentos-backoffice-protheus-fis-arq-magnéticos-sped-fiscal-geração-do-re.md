---
article_id: 15360857484311
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: af0de8763ac309079314684ef688a29e181e851abc83a27dd583e40223319b45
fetched_at: '2026-06-28T22:42:02.616299+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos -SPED FISCAL-
  Geração do registro 1601, de forma automática '
type: support-article
updated_at: '2023-06-16T15:19:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15360857484311-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Gera%C3%A7%C3%A3o-do-registro-1601-de-forma-autom%C3%A1tica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15360902500119) Tempo aproximado para leitura: **00:05:00min****Ocorrência**

Como gerar o registro 1601 de forma automática ?  
**Ambiente**

Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Foi incluído rotina **FISA312** para cadastro de operações, com instrumentos de pagamentos eletrônicos para o **registro 1601 - SPED FISCAL**.  
  
Esta rotina tem o objetivo de compor os valores com incidência de **ICMS**, **ISS** e outros, por participante, para a geração do registro **1601** do arquivo do **SPED FISCAL**.  
  
A rotina permite a inclusão de valores manuais e também, a importação de valores da movimentação financeira de baixa, baseada no relatório Relações de Baixas (**FINR190**), através de um facilitador encontrado em ações relacionadas.  
  
Com os valores importados ou incluídos, serão gravados em tabela, ficando assim disponíveis para a geração do **SPED Fiscal no registro 1601.**Boletim Técnico da rotina:  
  
<https://tdn.totvs.com/pages/viewpage.action?pageId=754623335>

<https://tdn.totvs.com/pages/releaseview.action?pageId=770942059>

<https://tdn.totvs.com/pages/releaseview.action?pageId=770963231>  
  
*Download* disponível no endereço abaixo:  
  
12.1.2210: <https://suporte.totvs.com/portal/p/10098/download?e=1109538> ;

12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1109539> ;   
12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1109540> ;  
  
Pra criação dos novos campos, execute o *UPDDISTR* com o dicionário de dados que estão no *link* abaixo:  
  
12.1.33: <https://suporte.totvs.com/portal/p/10098/download#detail/1039088>

12.1.2210: <https://suporte.totvs.com/portal/p/10098/download#detail/1080345>
