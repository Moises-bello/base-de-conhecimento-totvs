---
article_id: 41358479064727
category: SIGAACD - Automação e Coleta de Dados
content_hash: cd93b4f21b18890dd6cc790eed28bea90da4e7dad129e75426c0da2a0d7a9532
fetched_at: '2026-06-28T22:39:11.427349+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Cannot find function
  :vtctrlperg on VTACHOICE(VT100.PRG) 08/05/2026 16:43:01 line : 1819'
type: support-article
updated_at: '2026-06-19T20:47:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41358479064727-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Cannot-find-function-vtctrlperg-on-VTACHOICE-VT100-PRG-08-05-2026-16-43-01-line-1819
---

O erro no relatório de código de barras e etiquetas ocorre em várias rotinas no TOTVS Backoffice (Protheus) devido à ausência da função 'VtCtrlPerg'. A solução foi restaurar essa função, usada por um componente Frame via ACD. Recomenda-se atualizar o sistema para as versões 12.1.2310, 12.1.2410 ou 12.1.2510 e realizar backup antes da atualização, sempre testando em ambiente de teste.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41358479050519) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Clica em relatórios - Código de barras - Etiqueta de produto apresenta o error.log , esse error.log apresenta também nessas outras rotinas (Etiqueta endereço) (Etiqueta de Transportadora) (Etiqueta sem titulo) ( Etiqueta usuários).

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Causa**  
Esse incidente ocorre, em outras rotinas (Etiqueta endereço) (Etiqueta de Transportadora) (Etiqueta sem titulo) (Etiqueta usuários).

**Solução**  
Alterado rotina retornando a função 'VtCtrlPerg' pois é chamada por um componente do Frame no acesso via ACD.

 12.1.2310:<https://r.totvs.io/p/1252750> ;

12.1.2410:<https://r.totvs.io/p/1252751> ;

12.1.2510:<https://r.totvs.io/p/1252749> ;

**Issue TDN:** DMANMAT01-48584  
   
É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[DMANMAT01-48584: cannot find function :vtctrlperg on VTACHOICE(VT100.PRG) 08/05/2026 16:43:01 line : 1819](https://tdn.totvs.com/pages/releaseview.action?pageId=1071993719)
