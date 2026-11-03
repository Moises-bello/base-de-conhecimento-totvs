---
article_id: 33874389401623
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: 598b56a44416bb9de09521281afc5dbbcdb4c16dae642bb74d7ceff92e5c12d9
fetched_at: '2026-06-28T22:38:48.067575+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ao instalar a procedure
  da Virada de Saldos 17 é gerado o erro: Invalid column name B1_SEGUM.'
type: support-article
updated_at: '2025-08-04T16:42:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33874389401623-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-instalar-a-procedure-da-Virada-de-Saldos-17-%C3%A9-gerado-o-erro-Invalid-column-name-B1-SEGUM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33874373403671) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao realizar a instalação da Procedure 17, relacionada à rotina de **Virada de Saldos**, é apresentado o seguinte erro:

**"Invalid column name B1\_SEGUM":**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33874389381399)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33874389384087)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
Esse erro ocorre porque a procedure está tentando acessar a coluna `B1_SEGUM`. Isso geralmente acontece quando a base não está atualizada com os **fontes mais recentes** da rotina de Virada de Saldos.

**Solução**

Para resolver este problema, siga os passos abaixo de acordo com a versão do seu Protheus:  
1. **Aplique os fontes atualizados da rotina de Virada de Saldos** conforme a sua versão:

12.1.2310:<https://r.totvs.io/p/1207442> ;   
12.1.2410:<https://r.totvs.io/p/1207440>

**2. Após aplicar os fontes**, realize a reinstalação da **Procedure 17** no ambiente, conforme boletim:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel)

> ⚠️ **Importante:** Certifique-se de compilar corretamente os fontes aplicados e reiniciar os serviços do Protheus, caso necessário, para garantir que as atualizações sejam carregadas corretamente.

#### 

#### **Resultado Esperado**

Após seguir os passos acima, a instalação da Procedure 17 será realizada com sucesso, sem apresentar o erro relacionado à coluna `B1_SEGUM`.

É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://suporte.totvs.com/portal/p/10098/download#000006/all/)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização.  
Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba mais:**  
[*Clique aqui e saiba mais sobre Fechamento de Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012208793-SIGAEST-FECHAMENTO-DE-ESTOQUE-VIRADA-DOS-SALDOS-)
