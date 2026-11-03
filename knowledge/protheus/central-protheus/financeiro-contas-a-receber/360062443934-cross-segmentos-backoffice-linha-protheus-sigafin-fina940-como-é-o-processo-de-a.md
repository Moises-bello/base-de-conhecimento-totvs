---
article_id: 360062443934
category: Financeiro - Contas a Receber
content_hash: 9f6c4d92db3b0184b3aa07d0354cd5ee8dc68fabc3d0552b256a28f23295e5a8
fetched_at: '2026-06-28T22:38:14.104686+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA940 - Como é o
  processo de Ajuste Valor Presente no contas a receber '
type: support-article
updated_at: '2023-01-25T23:39:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062443934-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA940-Como-%C3%A9-o-processo-de-Ajuste-Valor-Presente-no-contas-a-receber
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Como é o processo de Ajuste Valor Presente no contas a receber?  
  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - TFINA940 - Todas as versões  
  
**Solução**Premissas de Teste:

**Cadastro de Naturezas**;  
**Cadastro de Clientes**;  
**Cadastro de Títulos a Receber**;  
Se for utilizar Índices Financeiros. Acesse o módulo **Financeiro** e selecione as opções:  
**Atualizações/Cadastros/Índices Financeiros** (FINA017);  
**Atualizações/Cadastros/Atualização do Índice** (FINA018).

Efetuar a simulação, conforme os parâmetros demostrado na documentação do Saiba mais abaixo.  
Efetiva a simulação realizada, gravando na tabela de valor presente do título, permitindo a contabilização da operação.

Na rotina **“Cálc. AVP CR**” posicione o cursor num processo simulado e selecione a opção **Efetivar**. São apresentados os títulos que devem ser ajustados. Confira os registros e confirme. Os registros serão gravados no sistema.  
Além da constituição dos títulos que não estão em processo de ajuste, permite o ajuste dos valores de valor presente dos títulos já constituídos.

Na rotina **Cálc. AVP CR**, selecione no **sub-menu** Ações **Relacionadas\Processar**.

A opção **Processar** deve permitir realizar o ajuste de títulos já em processo de **AVP** mesmo que não sejam selecionados novos títulos e que ainda não tenham nenhum tipo de processo **AVP** (simulação/efetivação).

**Importante**  
O cadastro de fórmulas poderá ser utilizado para calcular um índice que poderá ser aplicado no processo de **AVP**.

**Saiba mais:**[FIN0026\_CREC\_AVP\_ajuste\_valor\_presente\_contas\_receber](https://tdn.totvs.com/x/VdmRDg)
