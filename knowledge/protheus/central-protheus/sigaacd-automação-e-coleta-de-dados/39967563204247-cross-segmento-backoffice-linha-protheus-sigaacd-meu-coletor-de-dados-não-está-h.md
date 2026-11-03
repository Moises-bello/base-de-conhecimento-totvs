---
article_id: 39967563204247
category: SIGAACD - Automação e Coleta de Dados
content_hash: 4b34314bbe4150e14264f4d4b8557285816105f5286482d864aa600d3e63de49
fetched_at: '2026-06-28T22:39:12.786385+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Meu Coletor de Dados
  - Não está habilitando o endereçamento na rotina de transferência.
type: support-article
updated_at: '2026-04-23T19:36:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39967563204247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Meu-Coletor-de-Dados-N%C3%A3o-est%C3%A1-habilitando-o-endere%C3%A7amento-na-rotina-de-transfer%C3%AAncia
---

Na rotina de Transferência do aplicativo Meu Coletor de Dados, o campo "Endereço" não habilita para digitação se o parâmetro MV\_ARQPROD = SBZ estiver ativo e o produto não estiver cadastrado na tabela SBZ. Deve-se verificar se o produto utiliza localização na SB1. Recomenda-se manter o produto sempre atualizado na última versão disponível e realizar backups antes da atualização.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39967606946839) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Na rotina de Transferência, o campo de "Endereço" não é habilitado para digitação no aplicativo Meu Coletor de Dados.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**  
Na rotina de Transferência, quando a empresa trabalha com o parâmetro MV\_ARQPROD = SBZ, porém o produto não está cadastrado nessa tabela, deverá verificar se o produto trabalha com localização na SB1.

**12.1.2310**: <https://r.totvs.io/p/1247606>

**12.1.2410**: <https://r.totvs.io/p/1247607>

**12.1.2510**: <https://r.totvs.io/p/1247608>

**Issue TDN:** DENTRINO-6509  
   
É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://totvs.fluigidentity.com/cloudpass/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/xlglk8zqmzw44blf1442945918727)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização. Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[DENTRINO-6509 DT Meu Coletor de Dados - Não está habilitando o endereçamento na rotina de transferência.](https://tdn.totvs.com/pages/releaseview.action?pageId=1060239200)
