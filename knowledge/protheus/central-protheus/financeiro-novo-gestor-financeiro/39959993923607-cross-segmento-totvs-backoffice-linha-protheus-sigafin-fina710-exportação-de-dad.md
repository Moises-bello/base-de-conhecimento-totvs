---
article_id: 39959993923607
category: Financeiro - Novo Gestor Financeiro
content_hash: c1db16f5231995afa99713618e176a23c65f7872214ae90931dafda8e4a06352
fetched_at: '2026-06-28T22:37:41.424210+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - FINA710 - Exportação
  de dados para Excel
type: support-article
updated_at: '2026-04-23T16:48:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39959993923607-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Exporta%C3%A7%C3%A3o-de-dados-para-Excel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39960009920663) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como funciona o recurso de exportação de dados para Excel no módulo Financeiro e qual a diferença entre as opções "Somente Dados Apresentados" e "Dados Completos"?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - A partir da release 12.1.33  
  
**Solução**  
Ao selecionar a opção Exportar, o sistema oferece flexibilidade na extração dos dados conforme a necessidade do usuário. O comportamento das opções é o seguinte:

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39960009921943)

1. Somente Dados Apresentados: Esta opção exporta exclusivamente os registros que estão visíveis na tela no momento da ação. É recomendada para gerar planilhas rápidas de um subconjunto de dados após a aplicação de filtros manuais ou navegação por páginas.
2. Dados Completos: Esta opção exporta todos os registros que atendem aos parâmetros e filtros da consulta, independentemente de estarem carregados na visão atual da tela. É ideal para extrações integrais de relatórios ou consultas extensas.

É importante destacar que essa seleção impacta apenas a quantidade de linhas (registros). As colunas do arquivo gerado permanecem inalteradas, seguindo o padrão nativo do sistema em termos de ordem e quantidade, não sendo afetadas por personalizações de interface feitas pelo usuário (como ocultar campos ou reordenar colunas).

**Passos**

1. Acesse a rotina desejada no módulo SIGAFIN.
2. Aplique os filtros necessários para localizar os registros.
3. Clique na opção Exportar.
4. No questionamento apresentado pelo sistema, escolha entre Somente Dados Apresentados ou Dados Completos.
5. O sistema processará o arquivo e iniciará o download/abertura da planilha.

**Saiba Mais:** [**Exportação de dados para Excel - FINA710**](https://tdn.totvs.com.br/pages/releaseview.action?pageId=1005421949)
