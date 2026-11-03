---
article_id: 37351955465239
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: a622ad076b2a2306a14e9214c7296ca68847b8d8747cdf49c26ef0ea31319044
fetched_at: '2026-06-28T22:39:09.690942+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Perguntas da rotina
  (SX1) não aparecem no Cadastro do Schedule
type: support-article
updated_at: '2025-12-31T12:14:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37351955465239-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Perguntas-da-rotina-SX1-n%C3%A3o-aparecem-no-Cadastro-do-Schedule
---

Ao cadastrar o Schedule de uma rotina no SIGAEST, pode aparecer a mensagem "Operação inválida para o tipo de rotina informada no agendamento (processo especial)". Isso ocorre porque algumas rotinas dependem da tabela SXD para definir perguntas no "Editar Parâmetros", enquanto outras usam a função Scheddef. Verifique se a rotina está na tabela SXD com grupo de perguntas registrado; caso contrário, pode usar Scheddef, que pode ter restrições para edição via Schedule.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37351955446679) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**

Ao cadastrar o Schedule de uma rotina e clicar no botão "Editar Parâmetros" é exibida a mensagem:

```
Operação inválida
Operação inválida para o tipo de rotina informada no agendamento (processo especial).
```

![SCHEDUL.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/37361866740759)

**Ambiente**

Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - todas as versões

**Causa**

Algumas rotinas do sistema dependem do registro da Tabela SXD para identificar quais perguntas poderão ser preenchidas ao clicar no botão "Editar Parâmetros" no cadastro do Schedule, enquanto outras utilizam a função "[**Scheddef**](https://tdn.totvs.com/x/2bEpE)".

Caso a rotina utilize a Tabela SXD, na tabela estará a informação de qual grupo de perguntas (SX1) será apresentado no Schedule:

![SXD.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37351955451799)

**Solução**

Verifique se a rotina que está cadastrando existe na tabela SXD e se ela possui um Grupo de Perguntas (SX1) registrado no campo "XD\_PERGUNT", caso não exista, é possível que a rotina já utilize a função "[**Scheddef**](https://tdn.totvs.com/x/2bEpE)".

Caso ela já utilize a "Scheddef", a edição dos parâmetros pode ter sido bloqueada por restrição na execução da rotina via Schedule.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
