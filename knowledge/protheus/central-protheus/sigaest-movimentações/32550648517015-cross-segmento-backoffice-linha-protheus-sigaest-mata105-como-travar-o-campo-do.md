---
article_id: 32550648517015
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 57513e4c3111f73a00119a10995ea69065b9dacd6c83cd85431f78400ef9c46b
fetched_at: '2026-06-28T22:38:54.041297+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA105 - Como travar
  o campo do Solicitante na rotina de Solicitação ao Armazém?
type: support-article
updated_at: '2025-12-11T20:51:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32550648517015-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA105-Como-travar-o-campo-do-Solicitante-na-rotina-de-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m
---

Para travar a alteração do campo Solicitante (CP\_SOLICIT) na rotina de Solicitação ao Armazém no Protheus, acesse o Configurador em Base de Dados Dicionário Base de Dados, busque a tabela SCP, edite o campo CP\_SOLICIT e altere a propriedade para "Visualizar". Salve as alterações e o campo ficará bloqueado, mantendo o usuário logado como padrão.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32550648488599) Tempo aproximado para leitura: **00:02:37 min**  
  
**Dúvida**

Como travar a alteração do campo do **Solicitante (CP\_SOLICIT)** na rotina de Solicitação ao Armazém?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para o campo ser travado para alteração, basta:

 - 1 - Acessar ao Configurador no menu Base de Dados -> Dicionário -> Base de Dados

 - 2 - Pesquisar pela tabela SCP

 - 3 - Localizar o campo CP\_SOLICIT e clicar para "Alterar" no ícone do lápis vermelho no cabeçalho

 - 4 - Abrirá a tela de edição do campo, onde deve-se alterar o campo "Propriedade" para ***Visualizar***

![CPSOLICIT.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32550655663767)

5 - Salve as alterações no dicionário de dados por meio do ícone do disquete:

![Salvar.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32550648492311)

6 - Com isso, ao abrir a rotina, o campo **Solicitante** estará travado para alteração. Sempre deixando como valor default o usuário logado na rotina.

![Salvar2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32550648496023)

**Saiba mais:**

[SIGAEST - Solicitação, Pré-Requisição e Baixa da Pré-Requisição - MATA105 - MATA106 - MATA185](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018562511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Solicita%C3%A7%C3%A3o-Pr%C3%A9-Requisi%C3%A7%C3%A3o-e-Baixa-da-Pr%C3%A9-Requisi%C3%A7%C3%A3o-MATA105-MATA106-MATA185)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
