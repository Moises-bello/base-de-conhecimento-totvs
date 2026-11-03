---
article_id: 360050352073
category: RH - Cadastros
content_hash: 4ad794f775360dde21fd478a3680c3b0726156b52fd055012c5117f3a7e3c5a0
fetched_at: '2026-06-28T22:44:53.113136+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Sistema gera Apontamento de DSR automático na primeira
  semana do período
type: support-article
updated_at: '2026-02-10T17:49:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050352073-RH-Linha-Protheus-PON-Sistema-gera-Apontamento-de-DSR-autom%C3%A1tico-na-primeira-semana-do-per%C3%ADodo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33774099433367) Tempo aproximado para leitura: 01:30:00 min**  
  
**Ocorrência**  
Quando ocorre falta na primeira semana do período, o sistema está gerando apontamento de DSR automático no dia.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**  
Quando ocorre uma **falta na primeira semana do período e o** **1ª F. Folga** está = **SIM,** o sistema não gera apontamento para este primeiro dia trabalhado do período, considerando como um dia não trabalhado por motivo de folga.  
  
**Solução**  
No cadastro do [Turno de Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410322419095-RH-Linha-Protheus-PON-Como-cadastrar-um-Turno-de-Trabalho) **(Atualizações > Cadastros Gerais > Turno de Trabalho)**, o campo **1ª F. Folga** está com = **SIM**, o sistema não gera falta no primeiro dia trabalhado do período. Aplicando assim automaticamente como Folga no 1° dia normal do período. Veja:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32080081013143)   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32080081017495)  
  
Caso não deseja que o primeiro dia trabalhado do período seja como Folga no [Turno de Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410322419095-RH-Linha-Protheus-PON-Como-cadastrar-um-Turno-de-Trabalho) **(Atualizações > Cadastros Gerais > Turno de Trabalho)**, o campo **1ª F. Folga** deve ser ajustado para **N-Não.**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32080081018391)**  
  
Após isto, faça o reapontamento e veja que o dia ficará com falta para tratativa do ponto:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32080081022103)**  
  
  
**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
