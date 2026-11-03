---
article_id: 360045247114
category: RH - Definições de Cálculo
content_hash: 1e162a8db2ef56a8f1007b0cd2bc10e82f5ebf76cad91322a251b2e87f95290e
fetched_at: '2026-06-28T22:43:22.369576+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Como criar processo e período de cálculo diferente
  do padrão já existente no sistema
type: support-article
updated_at: '2025-09-30T16:53:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045247114-RH-Linha-Protheus-GPE-Como-criar-processo-e-per%C3%ADodo-de-c%C3%A1lculo-diferente-do-padr%C3%A3o-j%C3%A1-existente-no-sistema
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como criar processo e cadastrar período de cálculo diferente do padrão já existente no sistema?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**No sistema existe 4 processos pré-definidos **0001** (Celetista/Estagiário Mensal), **0002** (Celetista/Estagiário Semanal), **0003** (Contribuinte Individual Mensal), e **0004** (Contribuinte Individual Semanal). Porém é possível cadastrar um novo processo para vincular períodos e roteiros para calculo.  
  
Para criar um novo processo acesse o caminho atualizações > definições de cálculo > processos, clique em incluir e crie o processo. O novo processo terá a legenda verde que identifica que não é um processo padrão do sistema.  
  
Exemplo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063799853/mceclip0.png)  
  
Após a inclusão do processo acesse o caminho Atualizações > Definições de Cálculo > Períodos, posicione no novo processo e inclua os períodos e roteiros referente a esse processo.![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062899034/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062899294/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063800433/mceclip3.png)  
  
Após procedimentos de processo e período os novos trabalhadores podem ser incluídos no novo processo informado no campo **Cod. Processo** (RA\_PROCES), ou pode ser realizada a transferência de processos.

Para saber como realizar a transferência de processo consulte: [MP - GPE - Como transferir o trabalhador de processo de folha no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045780433)  
  
**Observações**A chave para qualquer cálculo e lançamento, na versão 12, é: Processo + Período + Número de Pagamento + Roteiro.

O processo serve como agrupador de funcionários no momento dos cálculos. Os funcionários são agrupados de acordo com o tipo de cálculo que possuem, por exemplo, celetistas mensalistas são agrupados em processo diferente dos celetistas semanalistas.

Os períodos são o espaço de tempo que o cálculo deve abranger para o processamento. Seu código é constituído por ano e mês.

[Por exemplo, para realizar o cálculo de funcionários mensalistas no mês de janeiro/2015 é necessário cadastrar um período iniciado em 01/01/2015 a 31/01/2015. O código do período será 201501]

O número de pagamento viabiliza a divisão do período em diversos intervalos de pagamento. Utilizado, por exemplo, para pagamento de semanalistas (4 pagamentos em um mesmo mês).

O roteiro indica qual cálculo será realizado.  
  
**Saiba Mais**  
[RH - Linha Protheus - GPE - Como gerar turnos automaticamente para a rotina Períodos (Cadastro de Calendário)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044827634-RH-Linha-Protheus-GPE-Como-gerar-turnos-automaticamente-para-a-rotina-Per%C3%ADodos-Cadastro-de-Calend%C3%A1rio-?source=search)

[RH - Linha Protheus - GPE - Como Criar Períodos Automaticamente pela Rotina Geração Período Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010729592-RH-Linha-Protheus-GPE-Como-Criar-Per%C3%ADodos-Automaticamente-pela-Rotina-Gera%C3%A7%C3%A3o-Per%C3%ADodo-Padr%C3%A3o?source=search)

[RH - Linha Protheus - GPE - Como configurar bloqueio de período na rotina GPEA400 - Cadastro de Períodos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053486853-RH-Linha-Protheus-GPE-Como-configurar-bloqueio-de-per%C3%ADodo-na-rotina-GPEA400-Cadastro-de-Per%C3%ADodos?source=search)

[RH - Linha Protheus - GPE - Como efetuar o cadastro de período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052262653-RH-Linha-Protheus-GPE-Como-efetuar-o-cadastro-de-per%C3%ADodo?source=search)

[o de Períodos e Roteiros de Cálculo na versão 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004425452)
