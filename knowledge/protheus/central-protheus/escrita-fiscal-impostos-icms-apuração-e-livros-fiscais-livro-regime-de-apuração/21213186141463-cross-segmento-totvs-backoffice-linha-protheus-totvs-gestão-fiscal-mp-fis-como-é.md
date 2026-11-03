---
article_id: 21213186141463
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 3969615e2bfc527038190eb3fa78119e154a19d11a98e143d4e46485da6887f7
fetched_at: '2026-06-28T22:39:22.134104+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  MP FIS Como é demonstrada  Nota fiscal de Transferencia na apuração do ICMS ?
type: support-article
updated_at: '2025-06-06T19:03:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21213186141463-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-MP-FIS-Como-%C3%A9-demonstrada-Nota-fiscal-de-Transferencia-na-apura%C3%A7%C3%A3o-do-ICMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21213188779799) Tempo aproximado para leitura: **06:00m**

**Dúvida**Como é demonstrada  Nota fiscal de Transferência na apuração do ICMS ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**.

Segue um estado de exemplo de Lançamento da NF de Transferência

MV\_ESTADO = PR  
MV\_TRSCRD = PR=4  
**MV\_CFOPTRA  = 5601**  
   
**Tipo de Nota fiscal :**Complemento de ICMS  
 

* **Configuração de TES**

Credita ICMS (F4\_CREDICM) = Não  
Calcula ICMS (F4\_ICM) = Sim  
Cod. Fiscal (F4\_CF) = Informar CFOP de transferência  
L.Fisc. ICMS (F4\_LFICM) = ICMS Zerado/Outros/Isento - A escrituração da nota fiscal deve ser analisada pelo departamento fiscal de sua empresa.  
Agrega Valor (F4\_AGREG) = Não  
Ajuste CIAP (F4\_AJUSTE)= S  
Txt Padrão (F4\_TEXTO) = Transferência  
TRF. Deb/Crd (F4\_TRFICM) = SIM - Esse campo levará o valor do ICMS transferido para linha 21 (transf. Cred) ou 22 (transf. Deb) na parte de Informações Complementares da Apuração de ICMS.

Fórmula (F4\_FORMULA) = Criar uma fórmula para ser amarrada a TES  
Menu Atualizações > Cadastros > Fórmulas:  
Informar código, descrição e no campo fórmula informar o conteúdo: “Transferência de saldo (credor/devedor) conforme art. 98 do RICMS” (utilizar aspas duplas)  
   
   
**Lançamento da Nota**  
   
Produto = Criar um produto “Transferência de Saldo de ICMS”  
Valor unitário e valor total = Valor do ICMS  
TES = Informar o TES de transferência = 5601  
   
Emissão da nota fiscal dia 04/02/2024  
   
Pedido de Vendas  
   
![](https://totvssuporte.zendesk.com/attachments/token/pcjEQLuBbV0GjOnmqiVFbx5Dv/?name=image.png)  
Apuração do mes de janeiro de 2024   
![](https://totvssuporte.zendesk.com/attachments/token/BTd8MxKfcP2iaeL6WxBHPWMVS/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/6KAia5QfG24YxtjhQYHPmEKua/?name=image.png)  
   
A nota fiscal foi considerada no mês de janeiro de 2024.

O parâmetro MV\_TRSCRD = PR=4, se a emissão da nota fiscal acontece no dia 05/02/2024 a nota fiscal será considerada no mês de fevereiro na apuração do ICMS.  
   
Emissão 05/02/2024  
    
![](https://totvssuporte.zendesk.com/attachments/token/EqNKC9P3s1wZB3MlwYi3Nhbq2/?name=image.png)  
   
Ao gerar a apuração do mês 02/2024  
   
![](https://totvssuporte.zendesk.com/attachments/token/mcidAjx1dFkI8A0LBvRPl3Lri/?name=image.png)
