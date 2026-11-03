---
article_id: 39457376965911
category: SIAGEST - CUSTOS
content_hash: a6c762232d13781008b14b3cce9c84a28c2bce008145e189799450ab80c8128f
fetched_at: '2026-06-28T22:42:14.215269+00:00'
product: protheus
section_id: 5367943695255
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - D1_CUSTO incorreto
  quando F4_AGREG = 'A' e utilizando Configurador de tributos com CBS e IBS
type: support-article
updated_at: '2026-04-02T12:28:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39457376965911-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-D1-CUSTO-incorreto-quando-F4-AGREG-A-e-utilizando-Configurador-de-tributos-com-CBS-e-IBS
---

A correção no TOTVS Protheus ajusta o cálculo do custo para incluir o valor do ICMS quando o campo Agrega Valor da TES está configurado como 'A' e há cálculo de IBS/CBS pelo configurador de tributos. Recomenda-se manter o sistema atualizado e realizar backup antes da atualização.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39457376957591) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Não considera o valor do ICMS no custo quando a configuração da TES considera quando o campo Agrega Valor da TES esta com o conteúdo igual a 'A'  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -Estoque/Custos - Todas as versões.  
  
**Solução**  
Corrigido o calculo do custo para considerar o valor do ICMS quando houver calculo de IBS/CBS pelo configurador de tributos.

12.1.2310:<https://r.totvs.io/p/1240635>

12.1.2410:<https://r.totvs.io/p/1240636>

12.1.2510:<https://r.totvs.io/p/1240634>

**Issue TDN:** DMANMAT01-47714

É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[26324246 DMANMAT01-47714 DT D1\_CUSTO incorreto quando F4\_AGREG = 'A' e utilizando Configurador de tributos com CBS e IBS](https://tdn.totvs.com/display/public/PROT/26324246+DMANMAT01-47714+DT+D1_CUSTO+incorreto+quando+F4_AGREG+%3D+%27A%27+e+utilizando+Configurador+de+tributos+com+CBS+e+IBS)
