---
article_id: 16733251120919
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: badcf47800457b0aeef369e487b407a7eb7d23012ca07074123613e9a11b0c7c
fetched_at: '2026-06-28T22:37:56.264787+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 -  Bloquear
  Painel de Controle, Movimentações, Comunicação Bancária
type: support-article
updated_at: '2026-06-01T12:21:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16733251120919-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Bloquear-Painel-de-Controle-Movimenta%C3%A7%C3%B5es-Comunica%C3%A7%C3%A3o-Banc%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16733282353303) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como bloquear o acesso às opções de **"Painel de Controle, Movimentações Financeiras, Comunicação Bancária"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16732952774807)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33  
  
**Solução**  
Para bloquear as opções de "**Painel de Controle, Movimentações ou Comunicação Bancária**", deve acessar o modulo **Configurador(SIGACFG) >> Usuários >> Senhas >> Privilégios** e criar a seguinte regra:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16733029378839)

Criar uma nova regra de acesso, exemplo, bloqueio de **movimentações financeiras**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16733329845527)

Permitir ou não acesso à rotina **FINA710 - Novo Gestor Financeiro**

**Importante**  
Se estiver como "**Negado**", a rotina não aparece no menu de acesso do usuário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16733047174935)

**Funcionalidades das transações/rotinas**, alterar as rotinas que deseja que o usuário não possua acesso para "**Negado**"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16733303897367)

Acessar o cadastro de usuários em **Configurador(SIGACFG) >> Usuários >> Senhas >> Usuários**e posicionar sobre o cadastro de usuário e clicar em **"Outras Opções >> Privilégios"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16733142438167)

Adicionar a regra criada para acesso na **empresa/filial**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16733138778391)

Ao acessar a rotina , no exemplo acima, o usuário não terá acesso às **Movimentações Financeiras**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16733253419287)

**Saiba mais:**  
[Novo Gestor Financeiro - (FINA710 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=611007335)  
[Cadastro de Regras/Privilégios Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030862273)
