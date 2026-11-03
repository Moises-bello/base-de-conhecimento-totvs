---
article_id: 360018844351
category: SIGAEST - FECHAMENTO DE ESTOQUE (VIRADA DOS SALDOS)
content_hash: 65803c068e56eb7eaf6c6fb160c3b94624f06cb3ae21e9ec8a11ee85d9ac8fef
fetched_at: '2026-06-28T22:38:52.700008+00:00'
product: protheus
section_id: 1500001538921
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como realizar o bloqueio
  de Movimentações no Estoque durante o Fechamento de Estoque?
type: support-article
updated_at: '2025-09-05T14:56:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018844351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-realizar-o-bloqueio-de-Movimenta%C3%A7%C3%B5es-no-Estoque-durante-o-Fechamento-de-Estoque
---

**Dúvida**

Como realizar o bloqueio de Movimentações no Estoque durante o processo de Fechamento de Estoque

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O método para bloquear movimentações no estoque se dá através do parâmetro **MV\_DBLQMOV**. Quando nele é selecionada uma data, não será permitido efetuar quaisquer movimentações caso o sistema esteja com a **data igual** **ou anterior** à que estiver delegada no parâmetro.

Normalmente este bloqueio é feito durante o Fechamento de Estoque (Virada de Saldos), para que outros usuários não façam movimentos simultaneamente ao processo, desta forma evita que hajam problemas na Virada de Saldos.

Para ajustar este parâmetro, realize os seguintes passos:  
  
**- 1 -** Acesse o módulo Configurador (SIGACFG);

**- 2 -** Acesse o caminho Base de Dados - Dicionário - Base de Dados;

**- 3 -** Selecione a opção Parâmetros;

**- 4 -** Localize o parâmetro MV\_DBLQMOV;

**- 5 -** Informe a data desejada para o bloqueio com a configuração "**AAAAMMDD**". Por exemplo: **20240630**. 

![mv_dblqmov.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/27149109761175)

***Observação importante******:*** Também é possível utilizar o parâmetro MV\_CMDBLQV para que ao processar o CUSTO MÉDIO (MATA330) ou a rotina ACOMPANHA CUSTOS (MATA038) o parâmetro **MV\_DBLQMOV seja populado automaticamente** com a data de processamento para o período de Fechamento. [Veja a FAQ com instruções](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012892521-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MV-CMDBLQV-Controle-autom%C3%A1tico-de-bloqueio-de-movimenta%C3%A7%C3%A3o-durante-o-Custo-M%C3%A9dio-e-Fechamento-de-Estoque).

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Fechamento de Período no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012208793-SIGAEST-FECHAMENTO-DE-ESTOQUE-VIRADA-DOS-SALDOS-)

[SIGAEST - MV\_CMDBLQV - Controle automático de bloqueio de movimentação durante o Custo Médio e Fechamento de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012892521-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MV-CMDBLQV-Controle-autom%C3%A1tico-de-bloqueio-de-movimenta%C3%A7%C3%A3o-durante-o-Custo-M%C3%A9dio-e-Fechamento-de-Estoque)
