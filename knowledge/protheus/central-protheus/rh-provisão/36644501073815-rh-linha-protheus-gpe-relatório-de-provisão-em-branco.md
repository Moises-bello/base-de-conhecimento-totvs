---
article_id: 36644501073815
category: RH - Provisão
content_hash: 129af96a48bb2c54c11908a013ac6374bfb326d37b7b6385ee68c8bb8e8cfeac
fetched_at: '2026-06-28T22:43:56.963026+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório de Provisão em Branco
type: support-article
updated_at: '2025-11-28T19:00:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36644501073815-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Provis%C3%A3o-em-Branco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36644501060887) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**  
Ao tentar gerar o Relatório de Provisão de Férias e/ou de 13º salário, o relatório é Emitido em Branco com a mensagem "Arquivo Vazio".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36644554986391)

**Ambiente**  
TOTVS RH  TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - Todas as Versões  
  
**Causa**  
O Cálculo das Provisões de Férias e 13º Salário não foram processados antes da tentativa de geração do Relatório de provisão.  
  
**Solução**

Os Relatórios de Provisão de Férias e 13º Salário (GPER070 e GPER090) exibem dados pré-calculados.  
Para garantir a visualização correta dos valores de Provisão, é fundamental que o processo de cálculo para a competência desejada tenha sido executado e gravado na tabela SRT

Certifique-se de que o cálculo para a competência em questão tenha sido concluído com sucesso:

1. Confirme se a Base está Atualizada com o pacote RH Expedição Contínua

12.1.2310: <https://suporte.totvs.com/portal/p/10098/download?e=1170810#detail/1123885>   
**Importante: Esta atualização bloqueia ambientes SEM GARANTIA ESTENDIDA.**

12.1.2410: [https://suporte.totvs.com/portal/p/10098/download?e=1170810](https://suporte.totvs.com/portal/p/10098/download?e=1170810#detail/1170810)[#detail/1170810](https://suporte.totvs.com/portal/p/10098/download?e=1170810#detail/1170810)

12.1.2510: <https://suporte.totvs.com/portal/p/10098/download?e=1170810#detail/1221795>

2. Revise o Preenchimento das perguntas para cálculo das Provisões:

[RH - Linha Protheus - GPE - Como Calcular as Provisões de Férias e 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004784961-RH-Linha-Protheus-GPE-Como-Calcular-as-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio)

3. Caso o cálculo não esteja sendo gravado na SRT, revise as informações do artigo abaixo:

[RH - Linha Protheus - GPE - O que Analisar quando as Provisões de Férias e 13º Salário não são Calculadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23481342212631-RH-Linha-Protheus-GPE-O-que-Analisar-quando-as-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio-n%C3%A3o-s%C3%A3o-Calculadas)

Saiba Mais:

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
