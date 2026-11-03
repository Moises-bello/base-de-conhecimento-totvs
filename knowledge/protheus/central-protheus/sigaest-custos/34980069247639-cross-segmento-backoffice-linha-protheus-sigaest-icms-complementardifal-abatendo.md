---
article_id: 34980069247639
category: SIGAEST - CUSTOS
content_hash: 870cd44a39cf0dca8df415ca1b1ebecee052e74b0b2b4f14beaa5b98b182ea7e
fetched_at: '2026-06-28T22:39:01.971969+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - ICMS Complementar/Difal
  abatendo no custo do produto (D1_ICMSCOM)
type: support-article
updated_at: '2025-11-10T18:16:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34980069247639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-ICMS-Complementar-Difal-abatendo-no-custo-do-produto-D1-ICMSCOM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34980084332055) Tempo aproximado para leitura: **00:01:00 min**  
  
**Duvida**

Ao lançar uma **nota fiscal normal e de complemento** que contém **ICMS de Substituição Tributária (campo D1\_ICMSCOM e o DIFAL** foi identificado que durante o lançamento o valor desse imposto está **deduzindo do campo D1\_CUSTO** ao invés de ser somado.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

No padrão, o valor de **ICMS complementar/Difal (D1\_ICMSCOM)** não deve ser abatido do custo do produto.

O cenário relatado já foi corrigido pela TOTVS e, para regularizar o processo, é necessário aplicar o pacote de atualização disponível no link abaixo disponível na release 2410:

<https://r.totvs.io/p/1214026>

Após aplicação do patch pode efetuar um teste com um novo Documento de Entrada, **ou também**, habilitar o parametro MV\_A190REF = .T. e processar a rotina Refaz Custo de Entrada (MATA190).

**Observações Importantes:**Ao processar a rotina Refaz Custo de Entrada (MATA190) esse procedimento ajusta os Documentos que estiverem **NO PERIODO DE ESTOQUE EM ABERTO, E NÃO EM PERIODO FECHADO.**

Ou seja, de períodos que ainda não foram realizadas o processo de Virada de Saldos.

**IMPORTANTE:**

Efetuou a aplicação, processou a rotina com o parametro, mas o custo ainda esta incorreto?

**Enviar os dados seguintes ao suporte padrão, peça ao seu T.I caso necessario**

* SB1 filtrada por um produto apenas em formato .dtc/sqlite/sqlserver
* SF4 filtrada pela TES usada no documento de entrada em formato .dtc/sqlite/sqlserver
* SD1 filtrada pelo produto ou documento .dtc/sqlite/sqlserver
* [Central de diagnostico Atual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico)
* Print da aba de impostos do documento de entrada
* Se acaso usar Configurador de tributos, enviar print tambem da aba de tributos do documento de entrada, mostrando os impostos
* Informe como deveria ser o custo:

  Exemplo: O custo deveria ser (Valor - ICMS)  
  D1\_TOTAL - D1\_VALICM = D1\_CUSTO

Assim podemos tentar validar internamente uma nota com as mesmas configurações que voce, e identificar o calculo efetivado.

É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://suporte.totvs.com/portal/p/10098/download#000006/all/)), a fim de contemplar todas as melhorias e correções disponibilizadas.  
  
Efetuar o Backup antes da atualização.  
Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[SIGAEST - Como configurar o custo de entrada com impostos na TES?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19509172274455-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-configurar-o-custo-de-entrada-com-impostos-na-TES)
