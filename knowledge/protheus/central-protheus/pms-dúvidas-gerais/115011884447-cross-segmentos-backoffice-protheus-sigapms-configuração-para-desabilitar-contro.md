---
article_id: 115011884447
category: PMS - Dúvidas Gerais
content_hash: 666930c45c60cddece6163d77304b3fd5ae2e841645ce35455dc3fdbe2574c02
fetched_at: '2026-06-28T22:37:17.640859+00:00'
product: protheus
section_id: 1500001539681
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Configuração para Desabilitar
  Controle Usuários
type: support-article
updated_at: '2024-02-23T12:37:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011884447-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Configura%C3%A7%C3%A3o-para-Desabilitar-Controle-Usu%C3%A1rios
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21563948810519)** Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**Após incluir um contrato via integração do RM com o Protheus, apenas o Usuário Administrados consegue acessar o contrato.

**Causa**Essa ocorrência acontece pelo fato que na integração não determinamos um usuário que seria o responsável pelo contrato com isso por padrão o sistema sem coloca o cod 000000 no campo de usuário AFX\_USER e deixa o campo de grupo AFX\_GRPUSR em branco, porem além desse campo existe também o campo da tabela AF8, AF8\_CTRUSER que informa se o projeto ira ter controle de usuários, que por padrão vem como 1 (Habilitado).

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - A partir da versão 12.1.16

**Solução**

Temos duas opções:

1 - Acessar o modulo 44, Gestão de Projetos (SIGAPMS) > Acessar a rotina PMSA410 Projeto modelo 2 > Localizar o projeto que deseja efetuar a alteração > Clicar em alterar > E por último basta alterar o campo **AF8\_CTRUSER** controle de usuários, de **1 - Habilitado** para **2 - Desabilitado**.

```
Obs: Recomendado para casos esporádicos.
```

2 - Outra forma é acessar o modulo Configurador (SIGACFG) > Acessar Base de Dados > Localizar a tabela **AF8 - Projetos** > Alterar para expandir os campos > Localizar o campo **AF8\_CTRUSER** > Alterar o conteúdo de seu inicializador padrão de **1** para **2**.   
Com isso todos os Projetos integrados via XML do RM pro Protheus irão nascer liberados para acesso.
