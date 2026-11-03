---
article_id: 360063112573
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 9fd7735bd4b3485c5773a9a6b169ee6c7eafb4a4d7c32f42dfbd3e3d42202c80
fetched_at: '2026-06-28T22:39:58.544903+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Transmissão
  de Cancelamento (Nota não é apresentada no Grid)
type: support-article
updated_at: '2025-06-10T18:30:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063112573-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Transmiss%C3%A3o-de-Cancelamento-Nota-n%C3%A3o-%C3%A9-apresentada-no-Grid
---

**Ocorrência**Ao tentar realizar a transmissão de [cancelamento de um RPS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004979372-MP-NFSE-Como-cancelar-uma-nota-fiscal-de-servi%C3%A7o-), a nota não é apresentada no GRID para que seja selecionada:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103683133/mceclip0.png)  
  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Esse problema geralmente ocorre por alguns motivos principais:  
  
1. A nota não foi devidamente monitorada após autorização, logo, os campos na tabela SF3 não foram atualizados e no filtro realizado pela rotina acaba falhando;

2. Há duplicidade de registros na SF3 para o mesmo RPS x SÉRIE x ESPÉCIE;

3. O documento de saída não foi excluído;

4. Está tentando ser realizado o cancelamento de uma nota que não foi previamente autorizada.  
  
**Solução**Ainda em relação aos itens citados acima, segue orientações:  
 **1.** Acessar a rotina e realizar o monitoramento (Outras Ações -> Monitor), mesmo que a nota não seja mais exibida na tela do grid (comportamento comum pelo fato dela ter tido o documento excluído).

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002683181/mceclip2.png)

Após monitorar, os campos da SF3 serão populados da seguinte maneira e a nota será apresentada corretamente no filtro após clicar em 'Trans. Canc', desde que a data informada no range contemple a data de exclusão do documento (campo F3\_DTCANC):  
  
F3\_CODRSEF = S  
F3\_CODRET = 111  
F3\_OBSERV = 'NF CANCELADA'  
F3\_DTCANC = 'AAAAMMDD'  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002644642/mceclip3.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101528114/mceclip1.png)  
  
**2.** Deverá conter apenas um registro ativo por nota na SF3, e caso haja duplicidade, deverá verificar junto a equipe Fiscal para a correta configuração. (*Exemplo: TES estar calculando ICMS para Nota de Serviço é uma das possibilidades).***3.** O procedimento deve ser executado conforme o material [cancelamento de um RPS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004979372-MP-NFSE-Como-cancelar-uma-nota-fiscal-de-servi%C3%A7o-), isso inclui a exclusão do documento de saída.  
 **4.** Nesse caso não será possível de fato realizar a transmissão de cancelamento pois a nota não foi enviada para a prefeitura, basta apenas realizar a correção do documento, corrigir e prepara-lo para transmitir novamente.
