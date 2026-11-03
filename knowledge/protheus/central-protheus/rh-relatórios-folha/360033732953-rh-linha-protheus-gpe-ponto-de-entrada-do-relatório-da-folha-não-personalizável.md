---
article_id: 360033732953
category: RH - Relatórios Folha
content_hash: 9ad3743dcb1603bddd240606c4e10a85740f50ba9c145379b7b8e51f609c3867
fetched_at: '2026-06-28T22:43:17.552572+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de entrada do relatório da folha não personalizável
  (GPER040), GP040Det
type: support-article
updated_at: '2025-08-04T12:09:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033732953-RH-Linha-Protheus-GPE-Ponto-de-entrada-do-relat%C3%B3rio-da-folha-n%C3%A3o-personaliz%C3%A1vel-GPER040-GP040Det
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23698321352599) Tempo aproximado para leitura: **01:30:00 min****Dúvida**Ponto de entrada no Relatório da Folha, formato não personalizável (GPER040), GP040Det   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Ponto-de-Entrada: **GP040Det - Emissão Cabeçalho Folha Pagamento**

**Descrição:**

Ponto de entrada para emissão do cabeçalho da folha de pagamento

**Eventos**  
O ponto de entrada está localizado após a formação de cada uma das linhas do cabeçalho do funcionário.  
Será executado a cada funcionário.

**Programa Fonte**  
GPER040.PRW

**Sintaxe**  
GP040Det - Emissão Cabeçalho Folha Pagamento ( ) --> cDetAux

**Retorno**

**cDetAux**(caracter)  
Uma string completa com todas as informações de cada uma das linhas a serem impressas

**Observações:**  
Será enviado um array contendo:

paramixb[1] :  
'1' - Indica que o ponto de entrada está sendo executado após a primeira linha do cabeçalho;  
2' - Indica que o ponto de entrada está sendo executado após a segunda linha do cabeçalho.

paramixb[2] - Contém a string completa da linha a ser impressa.  
O conteúdo do segundo parâmetro deve ser alterado e ser devolvido no retorno da função.  
  
**Saiba Mais**

[RH - Relatório Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
