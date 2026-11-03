---
article_id: 360000368067
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 7c6957474b6e1622db2a3d5ccddc3e775a5f5150609be8849526a0fb48dda993
fetched_at: '2026-06-28T22:41:48.454662+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF- Ativo cadastrado com
  CIAP por engano via Documento de Entrada
type: support-article
updated_at: '2023-11-30T17:11:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000368067-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Ativo-cadastrado-com-CIAP-por-engano-via-Documento-de-Entrada
---

**Ocorrência**Procedimento para ajuste de bens que foram incluídos através da integração com o módulo Compras, a partir da nota de entrada utilizando TES que gera CIAP, por engano.   
   
 **Ambiente**Protheus – Ativo Fixo – A partir da versão 11.80  
   
 **Causa**Esse incidente ocorre pois foi utilizada uma TES que gera CIAP de maneira indevida.  
   
 **Solução**Não será permitida a alteração do campo referente ao CIAP no cadastro do ativo, assim como também não será possível excluir o vínculo do CIAP no módulo Fiscal.  
  
Através da rotina "Manutenção CIAP - MATA905" existe a opção de excluir o CIAP, porém não será permitido uma vez que o CIAP foi gerado a partir da criação do ativo.  
  
![](https://totvssuporte.zendesk.com/attachments/token/zGSHqmaWgIX14Ebx7pFr3khYh/?name=inline-65699132.png)​  
  
Mesmo que o sistema exiba a mensagem solicitando a exclusão da NF, não será possível caso os ativos já tenham sido classificados.  
  
  
Existem 2 procedimentos possíveis neste caso:  
  
1.Exclusão do ativo fixo (somente caso o ativo não tenha sofrido nenhuma movimentação, como transferência e/ou depreciação);  
![](https://totvssuporte.zendesk.com/attachments/token/Nffz6b1XY15pY3HsOe3us6DMj/?name=inline1788951149.png)​  
  
Mesmo que a mensagem seja exibida, é possível confirmar a exclusão do bem, caso ele não tenha sido movimentado em nenhum momento.  
  
2.Baixa do ativo fixo (este se aplica caso o bem tenha sofrido movimentações, como transferência e/ou depreciação):  
![](https://totvssuporte.zendesk.com/attachments/token/fAVwNXKzAtvik2hhrJClAO78E/?name=inline-1196209434.png)​  
O motivo de baixa pode ser o que mais se adequa a situação da empresa.
