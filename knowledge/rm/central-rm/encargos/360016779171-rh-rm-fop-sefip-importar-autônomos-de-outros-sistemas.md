---
article_id: 360016779171
category: Encargos
content_hash: dbfd3f192eea066025bb2369f5a890dbcc41aa1866e9d0e1af6ed42f8f0ab1f6
fetched_at: '2026-06-28T22:46:52.145076+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - SEFIP: Importar autônomos de outros sistemas'
type: support-article
updated_at: '2025-01-21T19:41:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016779171-RH-RM-FOP-SEFIP-Importar-aut%C3%B4nomos-de-outros-sistemas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:05:31 min  
  
Dúvida**No módulo Folha de Pagamento, como importar autônomos de outros sistema para gerar a rotinas da SEFIP?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para importar autônomos de outro Sistema na geração da SEFIP, deverá seguir os passos abaixo:    
  
1. Acesse: **Encargos | SEFIP | Geração SEFIP**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12906530473751)

2. Feito isso, selecione a coligada desejada e acesse:**Parâmetros específicos da coligada | Integrações** e marque o parâmetro**Importar autônomos de outro sistema**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12906597848215)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12906646196887)

Este parâmetro serve para incluir no arquivo do SEFIP.RE uma relação de autônomos para que sejam feitos os devidos cálculos. Ao clicar neste parâmetro será apresentado um campo para preencher com a localização e nome do arquivo de autônomos a ser importado.

**Layout do arquivo de importação**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **DESCRIÇÃO** | **INICIO** | **FIM** | **TAM** | **TIPO** | **MÁSCARA** |
| Inscrição da Empresa | 001 | 014 | 14 | Numérico | 99999999999999 |
| Inscrição do Tomador de Serviço | 015 | 028 | 14 | Numérico | 99999999999999 |
| CI do Autônomo | 029 | 039 | 11 | Numérico | 99999999999 |
| Categoria do Trabalhador | 040 | 041 | 02 | Numérico | 99 |
| Nome do Trabalhador | 042 | 111 | 70 | Alfa Numérico |  |
| CBO | 112 | 116 | 05 | Alfa Numérico |  |
| Remuneração | 117 | 131 | 15 | Numérico | 00999999999999 |
| Ocorrência | 132 | 133 | 02 | Numérico | 99 |
| Valor descontado do Segurado | 134 | 148 | 15 | Numérico | 000999999999999 |
| Data de Início Atividade | 149 | 158 | 10 | Alfa Numérico | DDMMAAAA |

**Importante**

* Conforme recomendações do validador do SEFIP os campos **Remuneração** e **Valor descontado do Segurado** devem seguir da seguinte forma: **Remuneração e Valor descontado do Segurando:** Se informado deve ter 2 casas decimais válidas. **Remuneração:** Preencher o campo com zeros a esquerda e no máximo 13 dígitos de valor. **Valor descontado do Segurando:** Preencher o campo com zeros à esquerda e no máximo com 12 dígitos de valor.
* As casas decimais do item acima serão consideradas como os dois últimos dígitos informados no arquivo e NÃO devem conter ponto ou vírgula.
* O campo Data de Inicio Atividade NÃO deve ser informado caso a categoria seja diferente de 01,03,04,05,06,07,11,12,19,20,21 e 26.
* O campo Data de Inicio Atividade deve conter as barras " / " dentro do arquivo para importação.
* O campo Valor descontado do Segurado somente será importado caso a ocorrência seja de múltiplos vínculos.
* O campo Inscrição do Tomador de Serviços poderá ser preenchido com espaços em branco ou zeros (0).
* Para importar o arquivo que contém CEI que tem 12 dígitos, os dois dígitos faltantes devem ser completados com espaço (tanto faz no início ou no fim do número). O mesmo deve ocorrer com CPF que tem 11 dígitos.
