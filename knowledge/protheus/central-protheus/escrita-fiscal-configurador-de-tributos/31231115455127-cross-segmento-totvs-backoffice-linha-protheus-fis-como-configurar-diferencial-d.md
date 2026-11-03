---
article_id: 31231115455127
category: Escrita Fiscal - Configurador de Tributos
content_hash: 73df417d0a6f463bd510f79379252a6a074fc81fccf7ab0b8d127cb085facc22
fetched_at: '2026-06-28T22:39:17.193837+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  Diferencial de alíquotas base dupla sem deduzir o ICMS próprio no FISA170?
type: support-article
updated_at: '2025-11-04T21:08:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31231115455127-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-Diferencial-de-al%C3%ADquotas-base-dupla-sem-deduzir-o-ICMS-pr%C3%B3prio-no-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31231077152535) Tempo aproximado para leitura: **00:08:00 min** **Dúvida** Como configurar Diferencial de alíquotas base dupla sem deduzir o ICMS próprio no fisa170?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

**Exemplo  de Configuração de produto importado**

**MV\_Estado = AL  
   
Fornecedor - PB  
   
Cadastro de produtos  
NCM = 82032010  
aliq ipi = 5,2%  
origem = 1  
   
Valor da mercadoria = 133,08  
Base de calculo do icms = 164,41 x 4% = 6,58  
Base de calculo do IPI = 156,28 x 5,2% = 8,13  
frete = 23,20  
Total da NF = 164,41  
   
Calculo do Difal = 164,41/0,80 = 205,51  
205,51 \*20% = 41,10  
41,10-6,58 = 34,52  
Calculo do FECP sobre difal = 205,51 \*1% = 2,06  
   
   
TES  
Gera duplicata = sim  
Calcula icms = não  
L fiscal icms = não  
CFOP = 2556  
mat consumo = sim**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231115404439)**

**Configurações dentro do Fisa170  
   
ID - tributo   ICMS / IPI / CMP / FCPCMP  
   
Regras de NCM     
ICMS - aliquota - 4%  
IPI - aliquota - 5,2%**

**CMP - aliquota - 19%**

**FCPCMP - aliquota - 1%**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231115406615)**

**Perfil de cadastro de Produtos**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231077155607)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231115408023)**

**Perfil de Operação - criei um perfil 000056 - com os CFOPS de consumo 2556/2551**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231115408919)**

**Perfil de Participante - fornecedor de PB**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231115409431)**

**Perfil de origem /destino - todas as UFS 000002**

**1a ) REGRA DE BASE DE CALCULO DO IPI  
Valor da mercadoria  + frete  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231077157655)  
Regra de Aliquota usada para todos os impostos desse calculo**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231077159063)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231077160087)**

**Regra de Escrituração do IPI  
Livro = outros  
Soma total da nota fiscal e duplicata  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231115417111)**

**Regra de Calculo Documentos Fiscais - IPI  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231115417751)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231077162007)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231115420183)

**Obs: O perfil será o mesmo para todos os impostos desse calculo  
   
2a) REGRA DE BASE DE CALCULO DO ICMS  
valor da mercadoria + frete + IPI**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231115420695)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231115421975)**

**Regra de Aliquota a mesma  
   
Regra de Escrituração do ICMS   
Incidencia = outros  
CST = 90**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231115422871)  
   
Regra de Calculo Documentos Fiscais - ICMS  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231077165207)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231077165847)**

**3a) Base de calculo do Diferencial de aliquotas - base dupla  
( O:VAL\_MERCADORIA + O:FRETE + IPI  ) / ( 1 - A:000002 / 100 )**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231077167383)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231077168023)  
   
Regra de aliquota 20%**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231077169943)**

**Regra de escrituração a mesma do ICMS**

**Regra de Calculo Documentos Fiscais - Diferencial de aliquotas**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231077171095)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231077171863)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231077172503)

**4a) FECP icms complementar  
   
Base de calculo do icms complementar a mesma do Diferencial de aliquotas  
   
Regra de aliquota = a mesma   
   
Regra de escrituração = a mesma do ICMS  
   
Regra de Calculo documentos Fiscais  
tributo = FCPCMP**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231115435671)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231115437207)**

**Após criar a regra do FECP do icms complementar alterar a regra de calculo do Diferencial de aliquotas para majorar**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231115437975)**

**( B:000013 \* ( A:000014 + ALQ:000029 ) )**

**Lançamento da nota fiscal de entradas**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31231077177879)**

**Boletim**

**<https://tdn.totvs.com/pages/releaseview.action?pageId=717702574>**

[CFGTRIB - Perguntas e Respostas](https://tdn.totvs.com/x/qVWhMQ)

[CFGTRIB - Boas Práticas - Guia de Utilização do Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=825324804)

**[CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/PROT/CFGTRIB+-+Configurador+de+Tributos)**
