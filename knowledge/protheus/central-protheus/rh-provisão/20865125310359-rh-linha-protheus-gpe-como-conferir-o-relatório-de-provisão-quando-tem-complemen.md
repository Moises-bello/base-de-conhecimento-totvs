---
article_id: 20865125310359
category: RH - Provisão
content_hash: 3b9546de4f52a66f25d38e5616f59d145e95fdddc7708a11fff692e7176a53c2
fetched_at: '2026-06-28T22:43:55.769477+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Conferir o Relatório de Provisão quando tem
  Complemento de 13º Salário
type: support-article
updated_at: '2025-06-17T19:44:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20865125310359-RH-Linha-Protheus-GPE-Como-Conferir-o-Relat%C3%B3rio-de-Provis%C3%A3o-quando-tem-Complemento-de-13%C2%BA-Sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20865153906327) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como Conferir o Relatório de Provisão de Dezembro, quando na Folha de Pagamento o funcionário teve Complemento de 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Quando na competência de Dezembro o funcionário tem o lançamento de verbas variáveis com Sim para médias de 13º salário, ou alteração salarial, é devido complemento de 13º salário.  
Este complemento também será considerado para Baixas de 13º Salário nas Provisões.  
  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Emita o Recibo de Pagamento do 13º Salário acessando: Atualizações / Funcionários / Gestão de Funcionários (GPEA011) Selecione o funcionário e clique em Outras Ações / Lançamentos / Recibo de Pagamento e Visualiza. Informe o período 202312 e o roteiro 132.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20865153908503)  
  
2. Emita o Recibo de Pagamento da Folha de Pagamento na mesma rotina, informando o período 202312 e o roteiro FOL :  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20865125263895)  
  
3. Após o Cálculo das provisões de Dezembro, emita o Relatório de Provisão de 13º Salário acessando: Relatórios / Provisões / Provisão 13º Salário (GPER090), e preencha os parâmetros para o relatório do mês de Dezembro:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20865125268759)  
Some o Valor da verba de 13º Salário com o valor do Complemento de 13º Salário, para compor a Baixa de 13º na provisão.  
Verba 010 do roteiro 132 + verba 012 do roteiro FOL = 3.000 + 500 = **3.500,00****Importante:** Neste exemplo, o funcionário teve uma alteração salarial, mas o mesmo pode ocorrer para funcionários que tem verbas de Horas Extras, Adicional Noturno, Comissões ou Bonificações em Dezembro.Vale ressaltar, que mesmo que o complemento de 13º salário refira-se à valores de Adicionais e/ou médias, na Baixa de 13º da Provisão o valor do complemento sempre será baixado na coluna "Valor".

**Saiba Mais:**[RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o) **[-](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)** [Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
