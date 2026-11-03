---
article_id: 4403795836823
category: SIGAEST - CUSTOS
content_hash: 74ff7626729ca85c50ef366e02f83b6ecd0ebeadc73fdba012800839d750c0c4
fetched_at: '2026-06-28T22:39:02.141051+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Concorrência
  na execução do Recálculo do Custo Médio
type: support-article
updated_at: '2022-12-01T18:38:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403795836823-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Concorr%C3%AAncia-na-execu%C3%A7%C3%A3o-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio
---

**Dúvida**Ao executar o Recálculo do Custo Médio, está apresentando a mensagem: "*Concorrência - As seguintes filiais da empresa corrente já estão sendo utilizadas no processo de recálculo ou contabilização do custo médio - Filiais: 01(Código da Filial)".*O que fazer para conseguir concluir com o Recálculo do Custo Médio?

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403788935703/mceclip0.png)**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
**Solução**

Esta mensagem pode ocorrer dentro de alguns cenários comuns, tais como:

- Processo preso em algum ponto por conta de ter abortado o processamento do Custo Médio;

- Alguma tabela de estoque aberta na APSDU;

- Rotina em aberto que faz uso de tabelas de saldos e movimentos do Estoque;

- Algum usuário efetuando movimentação no mesmo momento da execução do Custo Médio;

Verificar também como esta definido o parâmetro **MV\_CUSTEXC**, pois este parâmetro define se o custo médio deverá ser executado de forma exclusiva ou não.   
  
É sempre aconselhável que seja gerado em modo exclusivo para que não haja divergências entre movimentações.   
  
Detalhes do parâmetro MV\_CUSTEXC: **[Clique aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=6085215)**  
  
Existe também parâmetro MV\_DBLQMOV, que bloqueia o usuário de fazer qualquer movimentação ao se executar o Custo Médio. **[Clique aqui para mais detalhes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018844351-MP-SIGAEST-Como-realizar-o-bloqueio-de-Movimenta%C3%A7%C3%B5es-no-Estoque-?source=search)**  
  
É importante sempre manter o ambiente atualizado, mantendo-o com os artefatos (Libs, Binários e Acumulados) na última versão disponível a fim de contemplar todas as melhorias e correções disponibilizadas. **[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=550332596)** para obter acesso à Central de Downloads TOTVS  
  
OBS: Sempre que aplicar pacotes, recomendamos que efetue um backup prévio do ambiente e aplique pacotes sempre primeiramente em ambiente de homologação.

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como é feita a ordenação dos movimentos no Recálculo do Custo Médio?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005800542-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-%C3%A9-feita-a-ordena%C3%A7%C3%A3o-dos-movimentos-no-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Perguntas do Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Perguntas-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
