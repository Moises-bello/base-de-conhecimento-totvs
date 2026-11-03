---
article_id: 360021877271
category: Ativo Fixo - Solicitação Baixa ou Transferência
content_hash: d6cc49dc6245105eee009cb96c1730340d150ef0491b44004dba9fa874ba0ad6
fetched_at: '2026-06-28T22:41:49.112900+00:00'
product: protheus
section_id: 1500001547622
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA125 PERMISSÃO PARA
  ACESSO Á ROTINA SOL. BAIXA/TRANSF '
type: support-article
updated_at: '2021-12-09T17:37:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021877271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA125-PERMISS%C3%83O-PARA-ACESSO-%C3%81-ROTINA-SOL-BAIXA-TRANSF
---

**Dúvida**

Permissão para acesso a rotina  Solicitação de baixa ou transferência (ATFA125).

**Ambiente**

Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – A partir da versão 11.80  
  
**Solução**

O acesso à rotina "**Sol. Baixa/Transf." (ATFA125)"** tem como regra algumas configurações no módulo Contabilidade Gerencial (SIGACTB):

Parâmetro **MV\_ALTLCTO** deve estar diferente de **S**.

* Parâmetro **MV\_PRELAN** deve estar diferente de**N**.
* Parâmetro **MV\_CT105MS** deve estar diferente de **S**.

Esta medida é realizada em diversas rotinas do Protheus, especificadamente naquelas que trabalham com muitos registros ao mesmo tempo e processamento, como por exemplo: Baixa Automática de Títulos ou Ativo, onde é possível baixar uma quantidade N de registros de uma só vez.

Ainda sobre estas rotinas que validam tal configuração, todas elas são trabalhadas em "transação", ou seja, a rotina trava, no banco de dados, o acesso a todos os registros utilizados pela rotina para protegê-los de alterações simultâneas ou de quedas no sistema.

Portanto, a fim de proteger a integridade de dados de possíveis impactos negativos de uso da empresa, o sistema não permite tal uso da rotina ATFA125 enquanto a configuração de parâmetros não for acertada, pois a contabilização do processo poderá travar diversos registros enquanto a tela estiver aberta para contabilização.
