---
article_id: 35519961717911
category: Financeiro - Conciliador Backoffice
content_hash: 216854b5c0281c557e80c8e47386dc46b0817f918a6cf89859dce559940e8eb4
fetched_at: '2026-06-28T22:37:47.277718+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Campo Beneficiário
type: support-article
updated_at: '2025-10-09T19:06:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35519961717911-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Campo-Benefici%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35519961669655) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Na versão antiga do conciliador, existia um campo de beneficiário, no novo conciliador (CTBA940) não é exibido este campo.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release da 12.1.2310  
  
**Solução**

O **novo conciliador** utiliza **tabelas diferentes** da estrutura adotada no programa anterior, devido à **reestruturação das tabelas financeiras**.

* [Reestruturação da tabela SE5 na família de tabelas FKx](https://tdn.totvs.com/pages/releaseview.action?pageId=183730415)

A rotina **CTBA940** passou a usar a **nova tabela principal de movimentação bancária (FK5)**.  
O uso nas releases **2310** e **2410**, o **campo de beneficiário** ainda **não havia sido incluído** na tabela de consulta do novo conciliador, o que impedia sua exibição.

Essa limitação foi **encerrada a partir de março de 2025**, quando o campo **FK5\_BENEF** foi **adicionado como melhoria** e incluído no **dicionário de dados** por meio de um **SDF disponibilizado após essa data para todas as releases.**

Dessa forma, para que o sistema reconheça o campo de beneficiário no conciliador, é necessário que o **dicionário esteja atualizado**.

Caso o campo ainda **não exista na base**, siga os passos abaixo:

**Baixe o pacote de atualização atual e SDF -**[**Pacotes de Atualização - Financeiro**](https://tdn.totvs.com/pages/releaseview.action?pageId=531017758)

1. Recolha o arquivo de SDF do idioma utilizado,   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35519961673495)
2. Insira os arquivos na pasta **\systemload**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35519961678231)
3. **Execute o UPDDISTR em modo exclusivo**, garantindo que o sistema crie corretamente os novos campos.

Após essa atualização, o sistema passará a validar e exibir o **campo de beneficiário (FK5\_BENEF)** conforme a estrutura atualizada do dicionário.

**Importante** ⚠️: Para implantações posteriores a data mencionada, o sistema passará a obrigar o campo FK5\_BENEF para criação do processo de conciliação bancária manual (0024).

**Saiba Mais**:

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Os menus do Conciliador Backoffice não estão sendo exibidos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35032695025815-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Os-menus-do-Conciliador-Backoffice-n%C3%A3o-est%C3%A3o-sendo-exibidos)
