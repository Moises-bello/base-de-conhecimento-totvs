---
article_id: 19120465589783
category: Escrita Fiscal - Configurador de Tributos
content_hash: 68fa8a67a56602872117abdef2a5764f8bba3c036a39d923f3db0c85ba86b55b
fetched_at: '2026-06-28T22:39:17.310954+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como calcular
  ICMS diferido 100% com CST 53?
type: support-article
updated_at: '2024-12-09T13:53:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19120465589783-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-ICMS-diferido-100-com-CST-53
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19120441048343) Tempo aproximado para leitura: 05:00 **Dúvida**Como calcular ICMS diferido 100% com CST 53?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Parâmetro

MV\_ESTADO = PB

Cadastro do cliente 

Cliente = PB  
   
Cadastro de produtos

Álcool  
   
TES

Código Fiscal = 5652  
   
Rotina FISA170  
   
![](https://totvssuporte.zendesk.com/attachments/token/UkwJE2PknDzNbIE3idu0mdc9Z/?name=image.png)  
   
   
Perfil cadastro de produto  
![](https://totvssuporte.zendesk.com/attachments/token/KNdBb412dKmN3H1sa9XBJnEFW/?name=image.png)  
O NCM cadastrado no produtos deve estar cadastrado na tabela SYD ( NCM )

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19120465534487)

Perfil de operação

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19120410937879)

Perfil Participante

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19120441054871)Perfil origem / destino

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19120465538839)Regra de Base de calculo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19120449721751)

Regra de Aliquota

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19120425815959)

Regra de Escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19120465549463)

Regra de calculo Documentos Fiscais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19120449727127)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19120425823895)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19120465558039)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19120449738903)

Dados do teste

Quantidade = 10  
Valor unitário = 2,78  
Valor total = 27,80  
   
Base de calculo do ICMS = 10  
alíquota = 1,22  
ICMS = 0,12  
   
TES  
Calcula ICMS = não  
L fiscal ICMS = outros  
CFOP = 5652  
CST = 53  
   
O sistema usa o TES para compor o CFOP   
   
Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19120425838743)

![cst 53.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19124964826263)

Boletim

<https://tdn.totvs.com/pages/releaseview.action?pageId=765332384>
