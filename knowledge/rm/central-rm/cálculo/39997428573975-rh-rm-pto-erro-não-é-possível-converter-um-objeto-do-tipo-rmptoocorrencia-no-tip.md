---
article_id: 39997428573975
category: Cálculo
content_hash: 14982edae6831321f04744bd65acd9c92afb2f82a454d3bc809ea97462743a85
fetched_at: '2026-06-28T22:46:29.155602+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: 'RH - RM - PTO - Erro: Não é possível converter um objeto do tipo ''RM.Pto.Ocorrencia''
  no tipo ''RM.Pto.AbonoFuncionario'''
type: support-article
updated_at: '2026-04-24T20:04:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39997428573975-RH-RM-PTO-Erro-N%C3%A3o-%C3%A9-poss%C3%ADvel-converter-um-objeto-do-tipo-RM-Pto-Ocorrencia-no-tipo-RM-Pto-AbonoFuncionario
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39997428550551) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
No módulo Automação de Ponto ao recalcular o espelho de ponto do funcionário o sistema emite uma mensagem de erro: \*\* Erro ao calcular o funcionário 19999 da coligada 1 \*\* Mensagem Interna de Erro: Não é possível converter um objeto do tipo 'RM.Pto.Ocorrencia.PtoOcorrenciaModificacaoOcorrencia' no tipo 'RM.Pto.AbonoFuncionario.PtoOcorrenciaAbono'.

Erro completo na imagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39997369304343)

**Ambiente**  
RH - RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Causa**  
Esse erro ocorre, quando existe modificação de ocorrência para a ocorrência de Abono (ABO).  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse no espelho de ponto do funcionário, o ícone de Anexos por Período | Modificação de Ocorrências e verifique se há registro de modificação de ocorrência para Abono;

2. E então exclua a modificação de ocorrência;

3. Após execute o recálculo selecionando parâmetros.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39997428552855)

Após o recálculo, poderá inserir um abono.

**Saiba mais**  
[RH - RM - PTO - Como Inserir abono no espelho do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018486631-RH-RM-PTO-Como-Inserir-abono-no-espelho-do-funcion%C3%A1rio)
