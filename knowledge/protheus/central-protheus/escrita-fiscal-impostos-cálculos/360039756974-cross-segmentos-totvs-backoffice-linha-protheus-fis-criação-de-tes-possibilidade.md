---
article_id: 360039756974
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 59a4960e6a76860c2fa59eb2260d48f0e1f119fa08c8d95e139c2eb40b9d26bb
fetched_at: '2026-06-28T22:39:30.564487+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Criação de TES -
  Possibilidades e quantidades
type: support-article
updated_at: '2022-07-06T18:40:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039756974-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Cria%C3%A7%C3%A3o-de-TES-Possibilidades-e-quantidades
---

**Dúvida**

Como fazer criação e diferenciação de cadastro de TES

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

**Tipos de TES**  
Para definição do TES deve-se observar :

|  |  |
| --- | --- |
| ***Códigos*** | ***O que representam*** |
| 000 a 500 | Entradas |
| 501 a 999 | Saídas |

\* Observando que o campo **F4\_CODIGO** é alfanumérico, o primeiro digito deve ser numérico pois é pelo primeiro digito que o sistema valida se o TES é para **entrada** ou **saída**, então poderá incluir todas letras intercaladas por números, gerando uma grande variedade de combinações.  
  
Exemplos para TES de entradas, considerar mesma lógica para saídas;

N = Numero

L= Letras

 N/L/L= 2.500 (TES)  
 0/A/A ATÉ 9/Z/Z

N/N/N= 499 (TES)

0/0/1 ATÉ 4/9/9

  N/N/L=900 (TES)

  0/0/Z ATÉ 4/9/Z

  N/L/N=900 (TES)

  0/A/0 ATÉ 4/Z/9
