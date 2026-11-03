---
article_id: 4417491549335
category: Funcionários
content_hash: 30efc6f58f650f38646e030bd6309a15ce94cbf69689699ec99082bddcde7e71
fetched_at: '2026-06-28T22:47:03.360168+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: 'RH - RM - FOP - Erro: Não será possível executar essa consulta, pois não foi
  possível aplicar o filtro por perfil.'
type: support-article
updated_at: '2025-03-06T18:26:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417491549335-RH-RM-FOP-Erro-N%C3%A3o-ser%C3%A1-poss%C3%ADvel-executar-essa-consulta-pois-n%C3%A3o-foi-poss%C3%ADvel-aplicar-o-filtro-por-perfil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:01:30 min****Dúvida**Ao realizar Cadastro de Funcionário está apresentando a seguinte mensagem de erro:

**Não será possível executar essa consulta, pois não foi possível aplicar o filtro por perfil.****A Consulta deverá conter o (s) seguinte (s) campo (s) da Tabela PFUNC: CODTIPO, CODTIPO.**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O erro apresentado ocorre em função do usuário possuir filtro por perfil para a tabela PFUNC. Dessa forma, ao executar algum tipo de rotina que executa cálculos através de fórmulas ou que executa consultas SQL que estão associadas ao perfil e esta(s) consulta(s) não possuem os campos utilizados pelo filtro por perfil, logo será apresentado o erro. Sendo assim, segue as seguintes opções para correção do erro:

1. Tendo a opção de desabilitar o parâmetro que controla essa aplicação nas execuções que envolvem consultas SQL do filtro por usuário.    
Acesse: **Ambiente | Parâmetros | Parâmetros Globais | Consultas SQL - Ativa segurança na execução de Consultas SQL segurança de campos e filtro por usuário.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10754522667031)**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10754545963415)

**Importante**Essa funcionalidade será permitida somente em banco de dados **MS-SQL Server** e somente para consultas SQL's que não sejam visíveis para todas as Coligadas. Para bancos de dados **Oracle**, os campos da consulta SQL devem ser escritos por completo. Exemplo: **SELECT PFUNC.NOME FROM PFUNC**.

2. Caso preferir existe a opção de Incluir os campos exigidos pelo filtro por perfil nas consultas SQL.

Acesse: **Serviços Globais | Segurança | Perfis | Anexos | Filtro por Perfil** e adicionar um filtro indicando as informações que deseja filtrar.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10754813832471)

**Saiba mais**

[RM - Frame - Como criar Filtro por Perfil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000250427-RM-Frame-Como-criar-Filtro-por-Perfil?source=search)  
[Parâmetros - Consultas SQL](https://tdn.totvs.com/pages/releaseview.action?pageId=421385203)
