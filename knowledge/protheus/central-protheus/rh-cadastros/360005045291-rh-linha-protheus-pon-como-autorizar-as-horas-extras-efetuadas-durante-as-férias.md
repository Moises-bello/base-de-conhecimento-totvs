---
article_id: 360005045291
category: RH - Cadastros
content_hash: a29d95343b8980e99c8e4cc7f85be0d2c46075a8f38bfd9a39bf354f9905245d
fetched_at: '2026-06-28T22:44:52.793056+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como autorizar as horas extras efetuadas durante
  as férias
type: support-article
updated_at: '2026-01-15T14:03:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005045291-RH-Linha-Protheus-PON-Como-autorizar-as-horas-extras-efetuadas-durante-as-f%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37696896738711)****Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Como autorizar as horas extras apontadas quando funcionário ainda está com status de férias?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
O sistema possui funcionalidade que possibilita determinar se as horas trabalhadas por um funcionário em **férias**, serão ou não consideradas como autorizadas.  
O procedimento padrão do sistema para esta situação é considerar as horas extras como autorizadas.  
  
Procedimento para utilização:  
- Acessar o modulo  **Configurador - SIGACFG** e localizar o parâmetro **MV\_APODFER**, deixar configurado com o conteúdo com a informação **S**:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32698146806167)**  
  
- Após, acessar o módulo **Ponto Eletrônico**, na rotina **Atualizações > Cadastros gerais > Turnos de Trabalho**, deixar os campos **Ap.Marc.Fer.** (Apuração de Marcações de Férias) e **Aut. HE Fer** (Autoriza Hora Extra nas Férias), com a informação **SIM.** Abaixo os campos que impactam nesse apontamento:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32698118921879)**  
  
**Observação:** O apontamento de horas para funcionários em férias possui tratamento específico, definido pelos campos do **Cadastro de Turnos**. Por exemplo, as marcações do trabalhador serão apuradas somente se o campo **Ap. Marc. Fer**. (Apuração de Marcações de Férias) estiver configurado para **Sim**. Caso contrário, os campos da regra para autorização das horas extras não terão efeito sobre os apontamentos referentes ao período de férias do trabalhador.  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[MP - PON0003 - GPEA080 - Como autorizar as horas extras efetuadas durante as férias?](http://tdn.totvs.com/pages/viewpage.action?pageId=233744546)
