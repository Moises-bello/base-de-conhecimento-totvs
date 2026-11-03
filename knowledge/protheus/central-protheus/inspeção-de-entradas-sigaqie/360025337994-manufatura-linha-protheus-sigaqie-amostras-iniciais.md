---
article_id: 360025337994
category: Inspeção de Entradas (SIGAQIE)
content_hash: 626bb5657372604fdd1a9639a1ef12ef2c661a063618f04373254e0538abe1be
fetched_at: '2026-06-28T22:42:26.867830+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAQIE - Amostras Iniciais '
type: support-article
updated_at: '2021-09-08T12:58:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025337994-Manufatura-Linha-Protheus-SIGAQIE-Amostras-Iniciais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min**  
 **Dúvida**Como é feito o controle de **Amostras Iniciais** de matérias primas?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**Na rotina de **QIEA010 -** **Especificação de Produtos**, na aba **Ensaios**, preencha o campo **Amostra/Insp - QE7\_AM\_INS**, com o valor **1 - Amostra Inicial**. Quando selecionada esta opção, os ensaios são inspecionados somente na primeira vez em que houver ocorrência de entrada a inspecionar. Caso houver mais revisões, os ensaios definidos como amostra inicial não são disponibilizados para medição na rotina de **QIEA215 -** **Resultados**.  
  
**Importante**  
Para que este conceito seja utilizado, o parâmetro **MV\_QAMOINI - Indica se os ensaios definidos como amostras iniciais serão inspecionados apenas na primeira ocorrência de Entradas com Produto X Fornecedor** deve estar preenchido como **T**. Caso o parâmetro esteja com o conteúdo **F** as entradas são inspecionadas ou certificadas de acordo com o **Skip-Lote** e **Skip-Teste**. Quando o ensaio possuir tratamento de **Skip-Teste,** o conceito de amostra inicial **não** será aplicado, prevalecendo o conceito de skip-teste.
