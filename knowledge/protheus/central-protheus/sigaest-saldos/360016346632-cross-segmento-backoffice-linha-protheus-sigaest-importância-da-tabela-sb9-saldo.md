---
article_id: 360016346632
category: SIGAEST - SALDOS
content_hash: 1d9d27b1baf20d5fbc33aaedd7e05af2f912cc7be85966c05c234603361171ba
fetched_at: '2026-06-28T22:39:14.869943+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Importância da Tabela
  SB9 (Saldos Iniciais)
type: support-article
updated_at: '2025-04-17T11:54:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016346632-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Import%C3%A2ncia-da-Tabela-SB9-Saldos-Iniciais
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31480505818647) Tempo aproximado para leitura: 00**:**01:00**min*****

**Dúvida**

Qual a importância e finalidade da tabela SB9 - Saldos Iniciais e qual a sua relação com as rotinas Saldos Iniciais (MATA220), Virada de Saldos (MATA280) e na rotina ACOMPANHA CUSTOS (MATA038)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

A tabela SB9 grava os registros de Saldos Iniciais (Físico e Custo) dos itens em um determinado período.   
  
Este saldo pode ser gerado através de:

* Inclusão de Saldos Iniciais na rotina MATA220, **sem a identificação de data**;
* Inventario Físico - MATA270, caso o saldo inventariado seja utilizado para o fechamento do período, configurando através da rotina Acerto de Inventario - MATA340, o F12 'Atualiza o Saldo do Fechamento= SIM' e processamento do fechamento;
* Processo de fechamento de estoque. Ao processar as rotinas Recálculo do Custo Médio (MATA330) ou Saldo Atual para Final (MATA350), o sistema fará checagem nos saldos gravados na tabela de saldos em estoque (SB2) referentes aos campos Quantidade Atual (B2\_QATU), Valor Atual (B2\_VATU1), Custo Médio Unitário (B2\_CM1) e "transferirá" estes dados para os campos Quantidade Final (B2\_QFIM), Valor Final (B2\_VFIM1) e  Custo Médio Final (B2\_CMFIM1). No momento da Virada de Saldos (MATA280) o sistema buscará estes valores e atualizará os dados na tabela SB9, por meio dos campos Quantidade Inicial (B9\_QINI), Valor Inicial (B9\_VINI) e Custo Médio Unitário Inicial (B9\_CM1).

* O **campo B9\_DATA** para inclusões de Saldos Iniciais deve ficar vazio, caso tenha habilitado diretamente no campo algum validador padrão, ou por execauto ou mesmo append direto no ambiente pode apresentar inconsistência nas referências de Saldos.

* O **campo B9\_DATA** recebe o conteúdo da data de Fechamento que foi definido na rotina ACOMPANHA CUSTOS (MATA038) na parametrização do Custo Médio.

**Importante**  
Esta tabela é utilizada como base para cálculo dos estoques e de custos em Relatórios e Consultas.

**Saiba mais:**

[SIGAEST - MATA220 HELP A220DTSALDO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8905341941911-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA220-HELP-A220DTSALDO)

[HELP FECHTO Não pode ser digitado movimento com data anterior a última data de fechamento (virada de saldos)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16419065822999-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-FECHTO-N%C3%A3o-pode-ser-digitado-movimento-com-data-anterior-a-%C3%BAltima-data-de-fechamento-virada-de-saldos)

[Clique aqui e veja mais artigos sobre Saldos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033462-SIGAEST-SALDOS)
