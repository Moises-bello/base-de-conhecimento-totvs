---
article_id: 14300625093143
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 91977af1e9c71df4cfc015e890afc6b051d14492d52aca53caa3c95d21040261
fetched_at: '2026-06-28T22:42:02.316280+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED Fiscal
  - D190 - Para documento fiscal de serviço o primeiro caractere do código do CST
  deverá ser igual a zero
type: support-article
updated_at: '2023-05-03T12:28:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14300625093143-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-Fiscal-D190-Para-documento-fiscal-de-servi%C3%A7o-o-primeiro-caractere-do-c%C3%B3digo-do-CST-dever%C3%A1-ser-igual-a-zero
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02:00 min****Ocorrência**Ao validar o arquivo txt do Sped Fiscal gerado pelo Protheus, ocorre o seguinte erro de validação: Para documento fiscal de serviço o primeiro caractere do código do CST deverá ser igual a 0 (zero)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Causa**  
Esse incidente ocorre, pois a parametrização do sistema está incorreta quanto a definição do campo **Cód.Situação Tributária** das notas de conhecimento de frete.  
  
**Solução**É possível configurar o parâmetro MV\_STFRETE. O parâmetro em questão é utilizado  para definir se o campo **Cód.Situação Tributária** das notas de conhecimento de frete é considerado do **Cadastro de Produtos**, campo **Origem (B1\_ORIGEM)**, ou se iniciará em **0** (zero) mesmo sendo uma importação.

Para que gere iniciado em 0 é preciso configurar o parâmetro como .T.  
 

|  |  |
| --- | --- |
| **Itens/Pastas** | **Descrição** |
| **Nome da Variável** | MV\_STFRETE |
| **Tipo** | Lógico |
| **Conteúdo** | .T. |
| **Descrição** | Para notas fiscais de serviço o primeiro caractere do código do **Cód da Sit Trib**(CST\_ICMS) deverá ser igual a 0 (zero). |
