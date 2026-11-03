---
article_id: 360034004313
category: Originação de Grãos (OG)
content_hash: 4aa4bdcfee3245439ff8bb62d5cc331da995d06a665456456a833b32bb896c94
fetched_at: '2026-06-28T22:45:41.208696+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Parâmetro MV_AGRO001 Controle de status interno
  do contrato
type: support-article
updated_at: '2025-04-23T14:07:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034004313-Agro-Linha-Protheus-AGR-Par%C3%A2metro-MV-AGRO001-Controle-de-status-interno-do-contrato
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20477117128343)***Tempo aproximado para leitura: **00:00:35 min**  
**Dúvida**Para que serve o parâmetro **MV\_AGRO001 - Define o tipo de contrato a ser validado**?  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O parâmetro **MV\_AGRO001** é utilizado para não forçar o fechamento do status dos contratos, que são Assinatura, Fiscal, Financeiro e Estoque.Se ele não existir ou estiver vazio é considerada a opção 2.

* **Opção 1 ->** Quando informado um ou mais tipos de contrato, a rotina não forçará o usuário a realizar as assinaturas do contrato para os tipos informados.
* **Opção 2 ->** Realiza o processo padrão, sendo necessário efetuar as assinaturas do contrato.

![Control.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7399639547415)
