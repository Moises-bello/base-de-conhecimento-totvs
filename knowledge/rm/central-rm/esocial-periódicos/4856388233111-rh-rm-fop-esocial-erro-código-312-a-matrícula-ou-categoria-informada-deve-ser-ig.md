---
article_id: 4856388233111
category: esocial - Periódicos
content_hash: 512f08ba36e97e436448ffeaf63a6e5e329dc05dadb5b130021308539d7e2b1b
fetched_at: '2026-06-28T22:47:09.345483+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro código 312: A matrícula ou categoria informada
  deve ser igual a existente no cadastro do trabalhador'
type: support-article
updated_at: '2026-03-03T18:11:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4856388233111-RH-RM-FOP-eSocial-Erro-c%C3%B3digo-312-A-matr%C3%ADcula-ou-categoria-informada-deve-ser-igual-a-existente-no-cadastro-do-trabalhador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38776248381719) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao enviar o evento S-1200 de um trabalhador ocorre o erro: **Código do erro: 312 - Descrição:** **A matrícula xxx ou categoria yyy informada deve ser igual a existente no cadastro do trabalhador no Ambiente Nacional do eSocial**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6801775790231)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Esse incidente ocorre devido divergência das informações referente ao trabalhador enviadas no *XML* do evento S-1200 com o cadastro inicial S-2200/S-2300 enviado ao ambiente do governo (RET).  
  
**Solução**

Para solucionar essa ocorrência, é necessário que confronte os dados do trabalhador presente no ambiente do governo (CPF, PIS, Matrícula, etc.) com o *XML* do evento S-1200.

Caso exista qualquer divergência, será necessário que exclua ou retifique o evento S-2200/S-2300 e envie novamente com as informações devidamente corrigidas. Após isso, faça o reenvio do S-1200.  
  
**Importante**  
No leiaute S-1.0 o governo passou a exigir matrícula para todas as novas admissões, inclusive de funcionários autônomos. Assim, todas as admissões enviadas a partir de 22/05/2022 precisam ter matrícula enviada. Se a alteração do leiaute eSocial não tiver ocorrido antes dessa data no RM, é necessário alterar a data da mudança do leiaute (via banco de dados) para correta geração dos XMLs.

Tabela: PPARAMADICIONAIS | Campo: VALORSTR | Coluna: ESOCIALDATALEIAUTESIMPLIFICADO

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7012100671767)

**Saiba mais**  
Para mais informações, acesse:  
     - [Utilização do S-3000 para exclusão de eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034224074)  
     - [Retificação dos eventos de funcionários - S-2200, S-2205, S-2206, S2300 e S-2306](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005056141)
