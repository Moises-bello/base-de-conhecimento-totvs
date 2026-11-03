---
article_id: 15741756726423
category: Escrita Fiscal - Configurador de Tributos
content_hash: cea06e4b65c810664b8adb70c4e7da7cedd24f0065ed698e2bd47c13933f6a30
fetched_at: '2026-06-28T22:39:17.466734+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como gerar
  o STMONO 61?
type: support-article
updated_at: '2025-11-04T22:07:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15741756726423-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-gerar-o-STMONO-61
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22658942011799) Tempo aproximado para leitura: **00:05:00min** **Dúvida**Como gerar o ICMS STMONO 61?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - à partir da release 12.1.27.  
  
**Solução**  
Rotina: FISA170   
ID - STMONO  
   
![](https://totvssuporte.zendesk.com/attachments/token/qZiQqIAFtyazi6juExfGXpnXK/?name=image.png)  
   
PERFIS  
   
PERFIL DO PRODUTO  
   
![](https://totvssuporte.zendesk.com/attachments/token/OWCUj564CXIglkppm6nt4J8Pt/?name=image.png)  
   
PERFIL DA OPERAÇÃO  
   
![](https://totvssuporte.zendesk.com/attachments/token/0U00RNj2SS4aVZed36ZBCfGaT/?name=image.png)  
   
PERFIL DE PARTICIPANTE  
   
![](https://totvssuporte.zendesk.com/attachments/token/R6WxdlaQWyDAo88f7ucUKU8rs/?name=image.png)  
   
PERFIL DE ORIGEM / DESTINO  
   
![](https://totvssuporte.zendesk.com/attachments/token/nYEi546KktKdr1yMXTvLGrC8m/?name=image.png)  
   
REGRAS DE CALCULO DOCUMENTO FISCAL  
   
REGRA DE BASE DE CALCULO  
   
![](https://totvssuporte.zendesk.com/attachments/token/9Jn3sTu7r6azn4nHJlez1mjC0/?name=image.png)  
   
PERFIL DE ALIQUOTA  
   
![](https://totvssuporte.zendesk.com/attachments/token/61bn1V9Y4fJy6ggphSS0xgXR2/?name=image.png)  
   
REGRA DE ESCRITURAÇÃO  
![](https://totvssuporte.zendesk.com/attachments/token/23zpaOLW0PLGqwZW8wUQxvVdI/?name=image.png)  
   
REGRA DE CALCULO DOCUMENTOS FISCAIS  
   
![](https://totvssuporte.zendesk.com/attachments/token/FDWlFy2Q3ulXZRgnNgpVq7p4s/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/OUnzHYtHCOTp2xmJkWinKE5VG/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/SCoiTowIppAeDmZNOiuIyCBrI/?name=image.png)  
   
MV\_ESTADO = MG  
   
Cliente = MG  
   
  
Valores da nota fiscal  
quantidade = 50  
Valor unitário = 4,43  
Valor da mercadoria = 221,50  
   
   
Base de calculo do ICMS  
50 x 0,95 = 47,28  
   
TES  
Calcula ICMS= não  
L fiscal ICMS= não  
CST = 61  
CFOP = no meu exemplo 5949

Cadastrar de acordo com perfil tributário de operação  
   
   
Pedido de Vendas  
   
![](https://totvssuporte.zendesk.com/attachments/token/waYfA8ZjUuOLX78u6kZ2e3wb5/?name=image.png)  
 

#### **Escrituração do Livro ICMS**

O ICMS Monofásico (STMONO) não é o ICMS próprio, por isso, a escrituração parametrizada para ele não tem efeito e não cria o livro de ICMS de forma automática. Portando mesmo o ICMS não sendo destacado na operação, é necessário criar um tributo específico para poder realizar a escrituração.

Abaixo será demonstrado como fazer a escrituração e para isto utilizei os mesmos perfis descritos acima.

Criar um tributo e amarrar no ID000021

![](https://totvssuporte.zendesk.com/attachments/token/aO1BqrxKXEiirz3Qf38ayAD0N/?name=image.png)

Regra de Base de Calculo - valor da mercadoria

![](https://totvssuporte.zendesk.com/attachments/token/QL1x8033vqzM4HLAU1c6b2OPR/?name=image.png)

Regra de alíquota - zero

![](https://totvssuporte.zendesk.com/attachments/token/sS3Vaoo8CbDSKgtg1HYtMp7hr/?name=image.png)

Regra de Escrituração

![](https://totvssuporte.zendesk.com/attachments/token/z70ZBojNOdDrif5SWN296DiHI/?name=image.png)

Regra de Cálculos - Documentos Fiscais

![](https://totvssuporte.zendesk.com/attachments/token/unTIIuH4PgU925eBL1KO8Yq8L/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/2SARntlM39hwgvkswl6YoshIN/?name=image.png)

Igual aos perfis do STMONO

![](https://totvssuporte.zendesk.com/attachments/token/SCoiTowIppAeDmZNOiuIyCBrI/?name=image.png)

Após gerar a nota fiscal será criado a CD2 com as informações do livro do ICMS e STMONO

Conforme boletim

#### [CFGTRIB - Cálculo de ICMS Monofásico Lei Complementar 192/2022](https://tdn.totvs.com.br/pages/viewpage.action?pageId=765332384)

* [Memória de cálculo - CST 61](https://tdn.totvs.com.br/pages/releaseview.action?pageId=765332384#CFGTRIBC%C3%A1lculodeICMSMonof%C3%A1sicoLeiComplementar192/2022-Mem%C3%B3riadec%C3%A1lculo-CST61)
  + [Escrituração do Livro ICMS](https://tdn.totvs.com.br/pages/releaseview.action?pageId=765332384#CFGTRIBC%C3%A1lculodeICMSMonof%C3%A1sicoLeiComplementar192/2022-Escritura%C3%A7%C3%A3odoLivroICMS)
