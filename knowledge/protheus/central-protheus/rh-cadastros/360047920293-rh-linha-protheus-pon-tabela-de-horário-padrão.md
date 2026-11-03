---
article_id: 360047920293
category: RH - Cadastros
content_hash: 7333a4335798d1a5d80e32dfd073128024a364d81b95e71395768f5a3b4b307e
fetched_at: '2026-06-28T22:44:53.125896+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Tabela de Horário Padrão
type: support-article
updated_at: '2025-12-16T13:06:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31988006574743) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Como realizar o cadastro da Tabela de Horário Padrão para um Turno de Trabalho?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
A parametrização da Tabela de Horário Padrão só é possível após a inclusão de um Turno de Trabalho.   
Neste cadastro, determinamos quais serão os dias Trabalhados/Não Trabalhados, os horários que deverão ser cumpridos em cada dia, o Tipo de Hora Extra apontado em cada dia, a Faixa de Refeição (caso a empresa tenha Refeitório e faça este controle), etc.

Para realizar o cadastro da Tabela de Horário Padrão, acesse **Atualizações > Cadastro do Ponto > Tabela de Horário Padrão**, posicione-se sobre o turno em que será realizado o cadastro e clique em **Incluir**.  
Primeiramente, determine os Tipos dos Dias, ou seja, quais serão os dias **Trabalhados**, **Não Trabalhados**, **Compensado** e **DSR**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31988022828311)  
  
  
Determine os **valores** de **Limite Inferior e Superior** para todos os dias. Por padrão, orientamos que seja configurado como 5,00 em cada, mas se houver necessidade de aumentar, para auxilio [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002754861-RH-Linha-Protheus-PON-Funcionalidades-dos-campos-de-Limite-inferior-e-Limite-superior-na-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o?source=search)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31988006577175)

Informe quais serão os horários de **Entrada/Saída e Intervalo**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31988006578967)

Se a empresa tiver **Refeitório** e fizer o controle de Refeições, é possível fazer o vínculo na Tabela de Horário Padrão, para mais informações [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018129092-RH-Linha-Protheus-PON-Como-efetuar-os-cadastros-das-refei%C3%A7%C3%B5es-para-Leitura-no-Ponto-Eletr%C3%B4nico?source=search)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31988006582167)

Determine quais serão os **Tipos de Horas Extras** apontados em cada dia.   
Este campo é ajustado conforme a opção selecionada na coluna **Tipo Dia**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31988022831639)

**Obs.:** Caso o Turno tenha apenas 04 batidas ao dia, o que resulta em um único Intervalo, é **obrigatório** deixar o campo **1ª S. Interv. como SIM**. Caso o turno tenha mais intervalos no dia, é importante que os demais colunas também fiquem como **SIM**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31988006583703)

Nas ultimas colunas é possível ver a quantidade de horas de Intervalo, de cada jornada de Trabalho e total das horas previstas para cada um dos dias:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31988006584855)

**Importante**: É possível **cadastrar até 99 sequências** na **Tabela de Horário Padrão,** e uma vez que este Turno é vinculado a um funcionário, toda Segunda-Feira é feita será realizado a alteração de forma automática da Sequência, conforme exemplo abaixo:  
- Período de **01.04.2025** à **30.04.2025**, Turno com **05 sequências** na Tabela de Horário Padrão  
- Início do período em **01.04.2025** na **Sequência 01**.   
- No dia **07.04** o sistema fará a alteração para a **Sequência 02**.  
- No dia **14.04** o sistema fará a alteração para a **Sequência 03** e **assim sucessivamente**.  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
