---
article_id: 360024607474
category: RH - Cadastros
content_hash: 975fdda97c055969edcdded3e70391b0c9fd4b80770cd121afeded16f99c16e0
fetched_at: '2026-06-28T22:44:52.963068+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Descontar DSR apenas de uma Falta 1/2 Período
type: support-article
updated_at: '2026-02-04T14:11:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024607474-RH-Linha-Protheus-PON-Descontar-DSR-apenas-de-uma-Falta-1-2-Per%C3%ADodo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29779011985815) Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
Quando o apontamento é por Tipo de Marcação (Apon. Tip Marc no Cadastro de Turno = SIM), como descontar o DSR apenas de uma das Faltas 1/2 Período?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
É válido ressaltar que só será possível efetuar o desconto de falta meio período quando o funcionário trabalha meio período quando a regra de apontamento for horário fixo ou só com mobilidade no intervalo. Para horário móvel no expediente completo não gerará falta meio período.   
  
No módulo Ponto Eletrônico, em **Atualizações > Cadastros Ponto > Eventos** configurar o evento **008A** Falta 1/2 Período com sim para Desc. DSR:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29779011991191)**  
- Para mais detalhes sobre o desconto de DSR [**clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004970391-RH-Linha-Protheus-PON-Como-efetuar-o-desconto-do-DSR-no-Ponto-Eletr%C3%B4nico-quando-existe-Falta-Atraso-ou-Sa%C3%ADda-Antecipada)

Evento de DSR com cadastro da verba:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29779011995671)**

No cadastro de turno de trabalho configurar o apontamento por tipo de marcação.   
- Para mais detalhes sobre tipo de marcação [**clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024756513-RH-Linha-Protheus-PON-Como-fazer-o-apontamento-considerando-o-Tipo-de-marca%C3%A7%C3%A3o-Apontamento-por-marca%C3%A7%C3%A3o)

Acessar em **Atualizações > Cadastros Ponto > Arredondamentos** e cadastre dois arredondamentos de DSR, exemplo:

- Primeira Linha: 0,01 a 4,00 = 3,66 (que é Metade do DSR total)  
- Segunda Linha: 4,01 a 999,99 = 7,33

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29779059283863)

Acessar o modulo configurador-SIGACFG e deixar configurado o parâmetro **MV\_DSRPROP**=**N**  
  
Veja o exemplo de apontamento com falta 1/2 período:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29779059286935)

Após isso, faça o reapontamento, seja pela rotina de manutenção integrados ou marcações, ou pela rotina de leitura/apontamento.   
- Para mais detalhes sobre reapontamento [**clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052257014-RH-Linha-Protheus-PON-Como-gerar-os-Apontamentos-a-partir-das-marca%C3%A7%C3%B5es-lidas-no-Ponto-Eletr%C3%B4nico)

Posteriormente, efetuar o cálculo mensal.   
- Para mais detalhes sobre o calculo mensal [**clique aqui.**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051550453-RH-Linha-Protheus-PON-Como-fazer-e-qual-a-finalidade-do-C%C3%A1lculo-Mensal)

O sistema descontará apenas 3,66 (04,06) de DSR, referente a uma das faltas 1/2 período.  
  
Exemplo após o calculo em resultados:  
- Sem converter em centesimal com o parâmetro **MV\_HORASDE**=**S**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29779012008343)

- Convertendo em centesimal com o parâmetro **MV\_HORASDE**=**N**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29779059292183)

**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
