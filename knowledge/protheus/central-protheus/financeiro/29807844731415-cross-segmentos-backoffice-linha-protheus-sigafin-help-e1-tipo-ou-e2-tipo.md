---
article_id: 29807844731415
category: Financeiro
content_hash: ec647e63664829c08e972e8456d989cdb56537aad69c65c18ae2f64a4d9bc66e
fetched_at: '2026-06-28T22:38:00.982841+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Help E1_TIPO OU E2_TIPO
type: support-article
updated_at: '2026-06-01T18:52:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29807844731415-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Help-E1-TIPO-OU-E2-TIPO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29807868311319) Tempo aproximado para leitura: **00:08 min**

**Ocorrência**  
No módulo Financeiro, ao pesquisar um tipo de documento que não possui cadastro ou quando migrou para release 12.1.033 e o tipo possui menos ou mais que três dígitos, é apresentado o help, conforme exemplo abaixo:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29807844699543)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro -  A partir da versão 12.1.033

**Causa**  
É apresentado este Help, pois o tipo de documento pode não ter o cadastro no sistema ou estar fora do padrão.

**Importante**

A rotina de tipos de títulos foi originalmente criada para tratamento dos tipos de títulos de Mercado Internacional (Outros países), para ajustes de eventuais diferenças de regras financeiras estrangeiras.

A utilização desta rotina ou inclusão manual diretamente na tabela SX5, em ambientes do Brasil "BRA" poderá ocasionar problemas imensuráveis em diversas rotinas do sistema, sendo expressamente não recomendada.

**Solução**

1. Acesse o **Configurador** :  
   -> **Base de dados** / **Dicionário** / **Base de dados**  
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29807844704663)
2. **Tabelas genéricas** / **Chave 05 - Tipos de títulos** / **Editar**:  
   ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29807868321047)
3. Posicione o cursor até a última linha e inclua um registro:  
   ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29807868327703)
4. Digite as informações de **chave** e **Descrição**.   
   No exemplo abaixo cadastrado **chave** = TES e a **descrição** "TESTE":   
   ![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29807844715287)

**Importante**

A criação de Tipos de Título destina-se exclusivamente ao atendimento de regras financeiras de legislações estrangeiras. Em ambientes Brasil (BRA), sua utilização, bem como inclusões manuais na tabela SX5, não é recomendada, pois pode alterar comportamentos padrão do sistema e causar impactos em diversas rotinas.

**Saiba mais**

[Utilizacao\_rotina\_tipos\_de\_titulos\_FINA015](https://tdn.totvs.com/display/public/PROT/FIN0004_Utilizacao_rotina_tipos_de_titulos_FINA015)
