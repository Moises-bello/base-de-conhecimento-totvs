---
article_id: 41178115254807
category: SIGAACD - Automação e Coleta de Dados
content_hash: be0897484122411bc2cb73a9acda19fa219dacf9d1b8b9c31ad8852831c6e90f
fetched_at: '2026-06-28T22:39:12.807018+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Meu Coletor de Dados
  não finaliza a Ordem de Separação por Nota de Saída ao ter carácter especial
type: support-article
updated_at: '2026-06-12T18:04:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41178115254807-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Meu-Coletor-de-Dados-n%C3%A3o-finaliza-a-Ordem-de-Separa%C3%A7%C3%A3o-por-Nota-de-Sa%C3%ADda-ao-ter-car%C3%A1cter-especial
---

O problema do Coletor de Dados que não finaliza a ordem de separação por nota de saída ao conter caracteres especiais foi corrigido com atualização na rotina de tratamento desses caracteres.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41178115242519) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Meu Coletor de Dados não finaliza a ordem de separação por nota de saída ao ter carácter especial  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Causa**  
Esse incidente ocorre no momento que foi tentar finalizar a ordem de separação no aplicativo meu coletor de dado.

**Solução**  
Alterado a rotina para tratamento de conversão de caracteres especiais na finalização da separação.

12.1.2310:<https://r.totvs.io/p/1253705>

12.1.2410:<https://r.totvs.io/p/1253706>

 12.1.2510:<https://r.totvs.io/p/1253704>

**Issue TDN:** DENTRINO-6555  
   
É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[DENTRINO-6555 DT Meu Coletor de Dados não finaliza a Ordem de Separação por Nota de Saída ao ter carácter especial](https://tdn.totvs.com/pages/releaseview.action?pageId=1071998762)
