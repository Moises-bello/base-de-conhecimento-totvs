---
article_id: 360022090112
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 255cb37804410195503d8779a40afa3d34ab06a0873e8f0bbcbdc46b29ff0b71
fetched_at: '2026-06-28T22:41:48.281232+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF  - ATFA012  - Erro ao
  incluir cadastro do ativo campo N1_CODCIAP não encontrado
type: support-article
updated_at: '2023-11-30T15:03:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022090112-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Erro-ao-incluir-cadastro-do-ativo-campo-N1-CODCIAP-n%C3%A3o-encontrado
---

**Dúvida**Error log apresentado ao incluir cadastro do ativo  
THREAD ERROR ([7852], adm,usuario) 13/12/2018 09:32:14  
erro no parâmetroFWFormViewStruct: O erro no método SETPROPERTY: Campo N1\_CODCIAP não encontrado. on FWFORMVIEWSTRUCT:SETPROPERTY(FWFORMVIEWSTRUCT.PRW) 23/10/2018 18:06:50 line : 467

**Ambiente**  
Microsiga Protheus – Ativo fixo  – A partir da versão 12  
  
  
**Solução**

Para que o erro não seja apresentado será necessário atualizar o dicionário e executar UPDDISTR

[**MP -SIGACTB - Como realizar a atualização do ambiente no Microsiga Protheus 12?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006655452-MP-SIGACTB-Como-realizar-a-atualiza%C3%A7%C3%A3o-do-ambiente-no-Microsiga-Protheus-12-?source=search)

Pode observar a estrutura da tabela na base , após executar o **UPDDISTR**

No padrão o campo **N1\_CODCIAP**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019148111)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019285792)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019148131)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019148151)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019148171)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019148191)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019148211)
