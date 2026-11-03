---
article_id: 4409540708887
category: RH - Provisão
content_hash: 4fc9bd8cb3cab60d400aee8f406004f82dd65e759200ac2e584ac10f51d2f444
fetched_at: '2026-06-28T22:43:55.794420+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Definir Médias em Horas nos Adicionais das
  Provisões de Férias e 13º Salário
type: support-article
updated_at: '2024-10-25T19:21:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409540708887-RH-Linha-Protheus-GPE-Como-Definir-M%C3%A9dias-em-Horas-nos-Adicionais-das-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27337081674775) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como Definir Médias em Horas nos Adicionais das Provisões de Férias e 13º Salário?  
  
**Ambiente**TOTVS RH  TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17

**Solução**Em alguns casos, ao conferir o Relatório de Provisão com o Relatório de Médias é identificado que as Médias de Horas Extras ou Adicional noturno estão sendo calculados em Valor e não em Horas.   
Com isto, quando há alteração salarial, a médias não são recalculadas com o salário atualizado.

No Exemplo abaixo, veja que  verba de Hora Extra 100% está sendo totalizada em Valor e não em Horas:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409527601303)  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409527627287)

Caso este funcionário sofresse alguma alteração salarial, este valor não seria reajustado.  
  
Para solucionar essa dúvida, realize os seguintes passos:

1. Acesse: Atualizações / Definições de Cálculo / Verbas (GPEA040), Localize a verba que está sendo considerada em Valor e clique em Alterar;  
  
2. Na Aba Incidências, altere o campo "Hora Extra" (RV\_HE) para Sim como no exemplo abaixo, e em seguida clique em Confirmar:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409527313175)  
Observação: A alteração deste campo não tem impacto nos cálculos de Horas Extras.   
  
3. Acesse: Relatórios / Lançamentos / Demonstrativos de Médias (GPER080), e emita o Relatório de Médias do funcionário:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409538854679)  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409538884503)  
Veja que após a alteração, o sistema apresenta todos os valores como Médias de Horas Extras.   
Com isto, caso haja alteração salarial, todos os valores apresentados no relatório de Médias serão valorizados..

Outra opção, é emitir o Relatório de Médias pela rotina de Provisão, clicando no botão Médias na rotina de Provisão de Férias/13º Salário (GPEA070):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27337074919959)

Para mai informações sobre como emitir o relatório de médias pela rotina de Provisão [Clique Aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13972932615063-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-M%C3%A9dias-pela-Rotina-de-Provis%C3%A3o?source=search)  
  
4. Acesse: Miscelânea / Provisões / Provisões de Férias/13 Salário (GPEA070), Localize o funcionário e exclua e reprocesse os cálculos de provisão somente deste funcionário como exemplo.  
Para saber como realizar este processo [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036636774-RH-Linha-Protheus-GPE-Como-Excluir-o-C%C3%A1lculo-das-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio).  
  
5. Emita o Relatório de Provisão, e verifique se o Valor apresentado na coluna "Adicionais" está correto:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409540623639)

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
