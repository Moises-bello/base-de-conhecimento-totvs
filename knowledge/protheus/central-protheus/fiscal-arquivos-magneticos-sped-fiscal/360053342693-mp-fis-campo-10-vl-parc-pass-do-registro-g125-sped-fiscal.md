---
article_id: 360053342693
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 8887db0f830e929c0f17a7dd45128efae03e91bbe43b0f53389bd9c9bd08ee12
fetched_at: '2026-06-28T22:42:03.764979+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'MP - FIS - CAMPO 10-VL_PARC_PASS do REGISTRO G125 - SPED FISCAL '
type: support-article
updated_at: '2021-04-28T14:24:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053342693-MP-FIS-CAMPO-10-VL-PARC-PASS-do-REGISTRO-G125-SPED-FISCAL
---

**Dúvida**Composição do campo 10-VL\_PARC\_PASS do registro G125 do SPED FISCAL  
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**A Gravação do campo 10-VL\_PARC\_PASS do registro G125 é composta através da soma dos campos abaixo e dividido pelo numero de parcelas:  
  
5-VL\_IMOB\_ICMS\_OP,  
6-VL\_IMOB\_ICMS\_ST,  
7-VL\_IMOB\_ICMS\_FRT  
8-VL\_IMOB\_ICMS\_DIF  
  
Abaixo um exemplo de calculo utilizando 48 parcelas:   
  
|G125|002631|01032020|SI|1207,14|0|0|657,11|3|38,84|  
  
(1207,14+0+0+657,11)/48 = 38,84  
  
O campo 10-VL\_PARC\_PASS é calculado no momento da geração do arquivo, portanto o valor gravado no campo 10 não vai bater com os valores gravados na tabela SFA (Estorno Mensal CIAP).  
  
Na tabela SFA é feita a apropriação e multiplicação pelo fator de apropriação "(Total das Saídas e Prestações Tributadas/Total de todas as Saídas e Prestações)".  
  
O validador do SPED FISCAL não prevê esse fator no G125, então é gravado somente o valor do ICMS gravado no campos mencionados acima e dividido pelo número de parcelas.  
  
Em situações que o valor gravado no campo 10--VL\_PARC\_PASS, for diferente entre um período e outro, será necessário verificar os valores gravados referente o ICMS nos campos 5, 6, 7 e 8 do registro G125.

Utilizando o exemplo de um arquivo gerado, temos o seguinte calculo:   
  
Período de Fevereiro:   
|G125|002631|01022020|SI|1314,22|0|0|657,11|2|41,07|  
  
(1314,22+657,11)/48 = 41,07  
  
Período de Março:   
|G125|002631|01032020|SI|1207,14|0|0|657,11|3|38,84|  
  
(1207,14+657,11)/48 = 38,84  
  
No exemplo citado acima, a diferença apresentada referente os valores gravados no campo 10, ocorre por motivo do valor do ICMS no campo 5-VL\_IMOB\_ICMS\_OP estar diferente entre os períodos de Fevereiro e Março, por conta disso, é apresentado a diferença na gravação do campo 10-VL\_PARC\_PASS.  
  
Para checagem dos valores do ICMS, será necessário avaliar as informações gravadas na SD1 - (Documento de Entrada) com os valores de ICMS gravados na tabela SF9 - Manutenção CIAP.
