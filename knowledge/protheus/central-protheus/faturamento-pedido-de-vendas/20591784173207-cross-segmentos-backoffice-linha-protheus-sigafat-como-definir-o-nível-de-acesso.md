---
article_id: 20591784173207
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 8bb9247719beadf6e17a3d8e2245560dbb80d42117bce0bd67e14489194cc280
fetched_at: '2026-06-28T22:38:42.470929+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT - Como definir o nível
  de acesso dos usuários para um determinado campo.
type: support-article
updated_at: '2024-01-16T11:30:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20591784173207-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Como-definir-o-n%C3%ADvel-de-acesso-dos-usu%C3%A1rios-para-um-determinado-campo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20591784119191) Tempo aproximado para leitura: **00:07:00 min****Dúvida:**Como definir o **nível de acesso** dos usuários para um determinado campo?  
  
**Ambiente:**Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões  
  
**Solução:**

No Protheus podemos através das configurações de níveis, definir quais campos (SX3) podem ser visualizados, isso faz com que determinados campos sejam acessados apenas por usuários que tem nível de acesso igual ou superior com esses campos.

**Por exemplo:**

Utilizaremos como exemplo o campo C5\_BANCO, da tabela SC5.

No Pedido de Venda do Protheus nós definimos para um usuário específico o nível de acesso 5 e para o campo C5\_BANCO definimos o nível de acesso 6, isso significa que este usuário não terá mais acesso ao campo, pois o nível do campo é maior do que o nível do usuário. Somente usuários que tem nível de acesso igual ou superior a 6 poderão visualizar esse campo.

**Observação:** Campos obrigatórios não se considera os níveis, ou seja, esses campos sempre vão aparecer para o usuário, já que eles devem ser informados obrigatoriamente.

Para configurar, siga os passos abaixo:

1 - Acesse o ambiente **configurador do Protheus - SIGACFG;**

**![cfg.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20591784122135)**

**2 - Acesse Usuários > Senhas > Usuários. Defina primeiramente o nível de acesso do usuário para o módulo SIGAFAT, clique na na aba Restrições de Acesso e depois em Ambientes, posicione no módulo 05 e no final da linha, informe o campo Nível, neste exemplo, parametrizado com 5;**

**![usuá.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20591801419799)**

**3 - Configure o nível de acesso do campo, acesse Base de Dados -> Dicionário -> Base de Dados. Ao entrar na rotina de Base de Dados, clique em Dicionário de Dados e depois na lupa para pesquisar a tabela de pedidos de venda - SC5.**

**![SC5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20591801422487)**

**4 - Encontrada a tabela SC5, clique em editar, clique em Campos, selecione o campo C5\_BANCO e clique em editar. Ao entrar na configuração do campo C5\_BANCO, clique na aba Validações, informe no campo nível o conteúdo 6, salve as alterações e atualize a base de dados.**

![banco.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20591801426455)

Após estas configurações, apenas usuários com nível 6 ou maior, conseguirão ver o campo **C5\_BANCO**.

![recording-2024-01-15-15-17-50.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/20592315080855)

**Observação:**

Caso ainda haja alguma dúvida neste processo, não deixe de entrar em contato com o nosso time de Framework.
