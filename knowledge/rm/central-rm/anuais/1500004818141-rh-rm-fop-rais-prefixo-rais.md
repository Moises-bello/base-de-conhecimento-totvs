---
article_id: 1500004818141
category: Anuais
content_hash: 54bf577ef4f4d11de26ba6fd38dabc60437238eae5be5de6a629efcbefb7b19b
fetched_at: '2026-06-28T22:46:51.144945+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - RAIS: Prefixo RAIS'
type: support-article
updated_at: '2025-03-05T18:43:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004818141-RH-RM-FOP-RAIS-Prefixo-RAIS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:50 min****Dúvida**Como deve ser parametrizado o campo **Prefixo RAIS** no cadastro de seção?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O Prefixo RAIS é utilizado quando a empresa é uma construtora, possui CEI e CNPJ cadastrado. Para realizar a parametrização, acesse: **Administração de Pessoal | Seções | Selecione a seção | aba RAIS/ CAGED/ ESOCIAL**:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10988723162391)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10988763092759)

Para cada CEI dentro de um CNPJ será informado um prefixo separado. Então, por exemplo:  
Consideremos uma empresa com as seguintes seções cadastradas:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Código** | **Descrição** | **CNPJ** | **CEI** | **Prefixo** |
| 01 | Construtora M&M | CNPJ1 | SEM CEI | 00 |
| 010 | Matriz | CNPJ1 | SEM CEI | 00 |
| 010.1 | Depto. Pessoal | CNPJ1 | SEM CEI | 00 |
| 02 | Construção M&M | CNPJ2 | SEM CEI | 00 |
| 020 | Filial | CNPJ2 | SEM CEI | 00 |
| 020.1 | Depto. Pessoal | CNPJ2 | SEM CEI | 00 |
| 021 | Obra Edifício SS | CNPJ2 | CEI 1 | 01 |
| 021.1.1 | Parte Elétrica | CNPJ2 | CEI 1 | 01 |
| 022 | Obra Edifício PP | CNPJ2 | CEI 2 | 02 |
| 022.1.1 | Parte Elétrica | CNPJ2 | CEI 2 | 02 |

Observe:

* As seções de códigos 01 a 020.1 não tem CEI;
* As seções de códigos 021 a 021.1.1 pertencem ao CEI 1;
* As seções de códigos 022 a 022.1.1 pertencem ao CEI 2;

É necessário, portanto, utilizar prefixos diferentes, ou seja, não poderá repetir prefixos em CEI diferentes que são estabelecidos em um mesmo CNPJ.   
  
**Importante**O prefixo não poderá ser informado como letra, pois o validador não aceita.

***Informações gerais sobre a RAIS 2022****Foi publicado no* [*Portal da RAIS*](https://www.rais.gov.br/sitio/index.jsf) *no dia 15/03/2022 o Manual e o Leiaute relativos ao Ano Base 2021. A adequação é apenas no campo de identificação do trabalhador* ***PIS/PASEP/NIT****, passando a ser facultativo, de acordo com o Manual de Orientação da RAIS ano-base 2021. O Programa Validador da RAIS –* ***GDRAIS2022****, está disponível no portal para download, então já é possível preparar-se para a transmissão da RAIS, uma vez que* ***para a linha RM, não será necessária adequação do produto****. As versões que atenderão a rotina serão as mesmas que atenderam a DIRF 2022:*

* *12.1.32.241 ou superiores;*
* *12.1.33.178 ou superiores;*
* *12.1.34.100 ou superiores.*

*Ressaltamos que, a entrega da RAIS para os Grupos 1 e 2 já foram substituídas pelo envio mensal dos eventos de remuneração no eSocial desde 2019, e para estes grupos está bloqueado o envio através do GDRAIS.*
