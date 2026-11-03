---
article_id: 360058604693
category: Financeiro - Contas a Pagar
content_hash: 8559e41c4fa49dede0ebdc6bf3d0db5feb9595855a648c512024e274ee451860
fetched_at: '2026-06-28T22:38:08.462995+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  FINA290 - Help: INDVAZIO'
type: support-article
updated_at: '2024-05-31T19:00:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058604693-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA290-Help-INDVAZIO
---

**Ocorrência**Ao realizar um cancelamento de fatura pela FINA290 apresenta o **Help**: **INDVAZIO**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23869507154199)  
**Ambiente**Microsiga Protheus – Financeiro – FINA290 - Todas as versão.  
  
**Causa**Os registros não estão sendo selecionados para o cancelamento, devido ao tipo de compartilhamento da tabela FI8.  
  
**Solução**

1 - Caso o campo **E2\_ORIGEM** do título que está tentando cancelando esteja com outra rotina e não "**FINA290**", irá ocorrer o HELP, sendo necessário cancelar pela rotina do campo.

2 - Verifique o compartilhamento entre as tabelas **FI8** e **SE2**, no qual as mesmas devem possuir o mesmo nível de compartilhamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23869641635735)

Além do compartilhamento, validar campos da FI8 e SE2

**Saiba mais**[Compartilhamento de tabela para rastreamento financeiro](https://tdn.totvs.com/display/public/PROT/FIN0064_Compartilhamento_de_tabela_para_rastreamento+financeiro)

[Compartilhamento de tabelas do módulo Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=307830478)  
  
****Importante****A manipulação da base de dados não é contemplada em nosso escopo de atendimento de Suporte Técnico, esse tipo de procedimento é efetuado apenas por analista in loco. Confira nosso Escopo  

[Guia de Relacionamentos - Específico SUPORTE PROTHEUS](%C2%A0https://tdn.totvs.com/pages/releaseview.action?pageId=547876496)
