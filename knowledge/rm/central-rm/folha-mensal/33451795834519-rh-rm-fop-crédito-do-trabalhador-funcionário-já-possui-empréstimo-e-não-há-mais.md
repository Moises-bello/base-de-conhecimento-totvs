---
article_id: 33451795834519
category: Folha Mensal
content_hash: ac73c9c9103e61100edac990290e1fb5ab075466cbf926945c941ac13e99c9c9
fetched_at: '2026-06-28T22:46:58.034637+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Crédito do Trabalhador - Funcionário já possui empréstimo e
  não há mais eventos disponíveis no Cadastro de Eventos
type: support-article
updated_at: '2025-09-02T17:39:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33451795834519-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Funcion%C3%A1rio-j%C3%A1-possui-empr%C3%A9stimo-e-n%C3%A3o-h%C3%A1-mais-eventos-dispon%C3%ADveis-no-Cadastro-de-Eventos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33451834079767) Tempo aproximado para leitura: **02:34 min**  
  
**Ocorrência**  
Ao realizar a importação do arquivo Crédito Trabalhador, o sistema emite a seguinte mensagem de erro: **Funcionário já possui empréstimo e não há mais eventos disponíveis no Cadastro de Eventos com código de cálculo 480 e natureza 9253 para a coligada: X (Chapa: XXXXX).**  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

* 12.1.2406.294
* 12.1.2410.267
* 12.1.2502.170
* 12.1.2506.114

**Causa**

Esse incidente ocorre porque o funcionário possui mais de um contrato de empréstimo ativo e não foi cadastrado mais um evento com o código de cálculo 480. Para que o controle do eSocial seja realizado corretamente, o desconto de cada empréstimo deve ser lançado em eventos distintos, uma vez que cada contrato de empréstimo é tratado separadamente.  
  
**Solução**  
Para que seja realizado o cadastro do evento, é necessário que realize os seguintes processos:  
  
1. Acesse:**Administração de Pessoal | Eventos | Eventos**:

Nela, o sistema apresentará seus eventos já cadastrados, caso tenha em sua base. Para cadastrar um evento​, basta clicar no botão incluir:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33451795814423)

2. O evento deverá ficar da seguinte forma:

![image (1).png](https://centraldeatendimento.totvs.com/hc/article_attachments/33451795815191)

2.1 Observe que ambos os eventos têm o mesmo código de cálculo e rubrica. Apenas o código do evento deve ser diferente. No exemplo abaixo, foram criados dois eventos, com os códigos 0480 e 1480, mas que utilizam o mesmo cálculo e natureza de rubrica:

![Recording 2025-07-11 at 11.10.23.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33451834082199)

Para mais informações, acesse o artigo: [RH - RM - FOP - Crédito do Trabalhador - Importação de Múltiplos Empréstimos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33401965386135-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Importa%C3%A7%C3%A3o-de-M%C3%BAltiplos-Empr%C3%A9stimos)

**SAIBA MAIS:**

[Importação Empréstimos FEBRABAN / Crédito do Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719677)

[Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/releaseview.action?pageId=925361639)

[FAQ - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=946423249)

[RH - RM - FOP - Dúvidas frequentes: Crédito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33227187529495-RH-RM-FOP-D%C3%BAvidas-frequentes-Cr%C3%A9dito-do-Trabalhador)
