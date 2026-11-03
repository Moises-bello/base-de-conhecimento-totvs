---
article_id: 8118133555095
category: PCMSO / Exames
content_hash: c6d57bb9a445acf83e275efd4bc3ede364ddb3fff44e4691640cdf234deaf82f
fetched_at: '2026-06-28T22:47:42.141629+00:00'
product: rm
section_id: 1500000861462
source: central-rm
title: RH - RM - SMT - Assistente de lançamento de exames
type: support-article
updated_at: '2025-03-17T14:52:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8118133555095-RH-RM-SMT-Assistente-de-lan%C3%A7amento-de-exames
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16036747079575) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como utilizar o assistente de lançamento de exames?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Segurança e Saúde Ocupacional -  Todas as versões  
  
**Solução**Para utilizar o Assistente de lançamento de exames, segue passo a passo:

O Assistente de Lançamento de Resultados permite que os resultados dos exames sejam lançados para as pessoas cadastradas no sistema de acordo com as configurações a serem definidas nos passos do assistente. O assistente apresenta os seguintes passos:  
  
**1) Definir dados da consulta clínica para análise dos exames -** Neste passo deverão ser informados os dados da consulta como: data consulta, tipo de procedimento (Consulta Médica Ocupacional, Atendimento Ambulatorial ou Consulta para exame toxicológico), tipo de consulta, tipo de consulta E-Social, Médico, Serviço de Saúde Responsável e Selecionar situação final da consulta.

No assistente a Situação Final da consulta, será responsável por informar o resultado final da consulta, conforme opções abaixo:

1. Apto
2. Inapto
3. Apto com Restrições
4. Pendente
5. Agendada

Ao selecionar alguma das opções da Situação Final, o sistema desconsiderará o cálculo realizado para definir a situação final da consulta e será considerada, para todos os funcionários, a opção selecionada, independente dos resultados dos exames.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8117754026519)  
  
2) Seleção de Pessoas** Neste passo deverão ser selecionadas as pessoas que terão exames lançados. O usuário terá a opção de criar filtros para selecionar as pessoas desejadas.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8117755921047)

**3) Seleção de Exames -** Neste passo deverão ser selecionados os exames para o lançamento. Poderão ser selecionados por tipo de exame (admissional, demissional, mudança de função, periódico, retorno ao trabalho e exame médico de monitoração pontual), os exames pendentes, os exames agendados ou outros exames. Ao avançar para o próximo passo o sistema exibe as pessoas e os respectivos exames relacionados pelos passos anteriores.

**Observação**

 Na seleção dos exames, ao aplicar os filtros disponíveis, será considerado a opção da origem dos exames, definida no Parametrizador (Opções| Parametrizador| Exames| Origem para Exames Pendentes).  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8117808827671)

**4) Lançamento de resultados de exames -** Para inserir o resultado do exame, basta dar um duplo clique sobre o nome do exame desejado, o sistema irá abrir uma janela para que os dados do exame sejam preenchidos. Os campos tipo de exame, data do exame e entidade são de preenchimento obrigatório.

Caso algum dos exames selecionados para o lançamento não tenha os dados do resultado preenchido, o assistente não permitirá avançar para o próximo passo.

**Observação**

* O campo "Procedimento diagnóstico" se refere a tabela 27 do eSocial.
* A **Data de Emissão ASO**não poderá ser uma data posterior a data da Consulta.

**![Assistente-Lan_amento-Exames-editando-exame.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/8117909768983)  
  
5) Concluir Lançamento de Exames -** O sistema conclui o lançamento dos exames e inclui um registro com os dados da consulta e os exames realizados no Prontuário do funcionário. Caso o exame lançado seja igual a um exame que esteja pendente para o funcionário, o mesmo não será mais exibido como exames pendentes.

**Observações**

Caso a opção "Replicar informações para todos os exames?" esteja marcada, todos os exames lançados neste processo terão os mesmos dados da consulta.

Caso o exame lançado esteja agendado para o funcionário,  o sistema irá verificar se a data de realização do mesmo é sete dias anteriores ou sete dias após a data do agendamento em caso afirmativo o status do agendamento será alterado para o status "Realizado".
