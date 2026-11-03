---
article_id: 29930063096343
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: b94f30b05cba9f8f24fbd02a19ccf47f46b2896b05637e55fcec26b80da558e1
fetched_at: '2026-06-28T22:38:48.246058+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 variable
  is not an object  on AC.CONFIG.PROFILE.SERVICE.ACPROFSERVICE:GETCONFIGPROFILE(ACPROFSERVICE.TLPP)
  17/01/2025 09:33:02 line : 123'
type: support-article
updated_at: '2025-12-15T17:38:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29930063096343-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-variable-is-not-an-object-on-AC-CONFIG-PROFILE-SERVICE-ACPROFSERVICE-GETCONFIGPROFILE-ACPROFSERVICE-TLPP-17-01-2025-09-33-02-line-123
---

O erro "variable is not an object" na rotina Acompanha Custos do Protheus está relacionado ao método do grupo de perguntas SX1 das rotinas Custo Médio e Virada de Saldos ou ao Profile do usuário. Para corrigir, verifique se o grupo de perguntas existe na tabela SX1 e limpe o profile do usuário. Também é recomendado usar o método GET da API REST para validar os dados.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29930078444567) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao acessar a rotina Acompanha Custos é gerado um erro de Internal Server Error e ao validar no arquivo console.log é o gerado o erro: **"variable is not an object on AC.CONFIG.PROFILE.SERVICE.ACPROFSERVICE:GETCONFIGPROFILE(ACPROFSERVICE.TLPP) 17/01/2025 09:33:02 line : 123"**, o que fazer para corrigir esse erro? ![Captura de tela 2025-02-12 083452.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29930063079831)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da release 12.1.33

**Solução**

Com as últimas inovações como a funcionalidade que estará disponível sobre o **bloqueio de perguntas** conforme o TDN abaixo:

[***https://tdn.totvs.com/x/tWLzNQ***](https://tdn.totvs.com/x/tWLzNQ)

Esse erro está relacionado ao método do grupo de perguntas do SX1 das rotinas de Custo Médio e Virada de Saldos ou do Profile de usuário:

![Captura de tela 2025-02-12 091237.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29930063080599)

Esse ConfigProfile é uma API do Rest:

![Captura de tela 2025-02-12 091604.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29930078447383)

O sistema manda um método "GET" para pegar esses dados, então pode colocar no REST e fazer um GET no Postman:

![Captura de tela 2025-02-12 091915.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29930078447639)

E observar qual é o retorno, nos nossos testes foi o retorno do grupo de perguntas das rotinas virada de saldo (**MTA280**) e Custo Médio (**MTA330**).

Nesse caso por gentileza avaliar se tem esse grupo de perguntas na tabela SX1.

E caso tenha, favor fazer a limpeza do profile do usuário.

[Framework - Linha Protheus - Manutenção de Profile de Usuários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025097012-Framework-Linha-Protheus-Manuten%C3%A7%C3%A3o-de-Profile-de-Usu%C3%A1rios)

Além de fazer a chamada do método do GET no REST no Postman e avaliar o resultado.

**Saiba Mais**

[*Clique aqui e veja mais artigos sobre o Acompanha Custos*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-MONITOR-DE-CUSTOS)
