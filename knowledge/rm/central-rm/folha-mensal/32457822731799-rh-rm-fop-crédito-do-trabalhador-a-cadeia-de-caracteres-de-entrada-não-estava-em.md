---
article_id: 32457822731799
category: Folha Mensal
content_hash: f3d70e61acc2d5dce5fa9f3d69bdf066be25b4fb928400b4b31c40a4946d741c
fetched_at: '2026-06-28T22:46:58.056660+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Crédito do Trabalhador - A cadeia de caracteres de entrada
  não estava em um formato correto
type: support-article
updated_at: '2025-06-11T15:26:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32457822731799-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-A-cadeia-de-caracteres-de-entrada-n%C3%A3o-estava-em-um-formato-correto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32457822716439) Tempo aproximado para leitura: **00:03:05 min****Ocorrência**Ao realizar a importação do arquivo Crédito Trabalhador, o sistema emite a seguinte mensagem de erro: **A cadeia de caracteres de entrada não estava em um formato correto**.  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

12.1.2406.277

12.1.2410.229

12.1.2502.145

12.1.2506 e superiores

**Causa**

A mensagem de erro "**A cadeia de caracteres de entrada não estava em um formato correto**" pode ser gerada por diferentes tipos de inconsistências no arquivo Crédito Trabalhador. O erro não aponta uma causa específica, podendo estar relacionado a mais de uma situação distinta no conteúdo do arquivo.

**Solução**Para solucionar o erro apresentado, verifique os seguintes pontos:

1. **CPF/CNPJ sem zeros a esquerda:**

* Devido a uma falha na plataforma do governo, os arquivos estão sendo gerados sem os zeros à esquerda nos campos de CPF e CNPJ iniciados com zero. O governo informou que realizará os ajustes necessários na plataforma nas próximas competências. Enquanto isso, as empresas deverão corrigir manualmente os dados no arquivo antes de realizar a importação. Para mais informações, verifique o link: [RH - RM - FOP - Crédito do Trabalhador : CPF/CNPJ dos trabalhadores sem os zeros à esquerda.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32044630941975-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-CPF-CNPJ-dos-trabalhadores-sem-os-zeros-%C3%A0-esquerda)

2. **Campos sem aspas duplas - Extensão JSON:**

* Caso esteja utilizando a extensão .json, valide se todos os campos estão corretamente envolvidos por aspas duplas, conforme especificado no layout. A ausência dessas aspas em determinados campos pode causar falha na leitura e gerar a mensagem de erro.

![erro parse.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32741836640919)

A imagem acima destaca os campos que devem ser analisados e ajustados para conter aspas duplas, caso estejam em desacordo com o layout.

3. **Formato incorreto dos meses em arquivos CSV editados no Excel:**

* Ao abrir ou editar o arquivo com extensão .csv diretamente no Excel, os campos '**CompetenciaInicioDesconto'** e '**CompetenciaFimDesconto'** podem ter os meses convertidos automaticamente para o formato textual (por exemplo, mai/25). No entanto, o formato correto exigido pelo layout é numérico **(05/25)**.

  Recomenda-se revisar esses campos antes de importar o arquivo, garantindo que estejam no formato adequado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32457822716951)

**Importante:**

Se você baixar o arquivo novamente e editá-lo com um editor de texto, como o Bloco de Notas ou Notepad++, esse problema não ocorrerá.

**Saiba Mais:**

[Importação Empréstimos FEBRABAN / Crédito do Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719677&draft=true)

[Layout Crédito do Trabalhador](https://hservicos.mte.gov.br/empregador/manuais/leiauteArquivoEmprestimos.html)
