---
article_id: 37535573918359
category: Contabilidade Gerencial - Visão Gerencial
content_hash: 544067094cf815895691b535ccd119b270818a11ee7bcfa85c7431e76fd7353f
fetched_at: '2026-06-28T22:40:50.626561+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA161 - Ao tentar
  importar uma visão o sistema apresenta help de visão ja existente.
type: support-article
updated_at: '2026-01-12T11:52:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37535573918359-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA161-Ao-tentar-importar-uma-vis%C3%A3o-o-sistema-apresenta-help-de-vis%C3%A3o-ja-existente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37535573890583) Tempo aproximado para leitura: 00**:10 min**

**Dúvida**

Ao tentar realizar o processo de exportação/importação (cópia) de visões gerenciais através da rotina **CTBA161**, o sistema impede a gravação informando que o código da visão já existe.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37535558204823)  
  
**Ambiente**

 Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial - Todas as versões

**Solução**

O incidente ocorre devido à existência prévia do registro na tabela **CVF** (Cabeçalho das Visões Gerenciais).

O sistema realiza uma validação de integridade no campo **CVF\_CODIGO**. Se o código (ex: "001") já estiver gravado na tabela, o Protheus bloqueia a importação para evitar inconsistências com as tabelas relacionadas (**CVE**, **CVD** e **CVG**), prevenindo a duplicidade de chaves primárias e garantindo que a estrutura da visão não seja corrompida.

Essa situação ocorre quando a tabela **CVF** está compartilhada ou quando registros de tentativas anteriores permaneceram no banco de dados, mesmo que não estejam visíveis no filtro da rotina.

**Passos**

Deve solicitar ao DBA da empresa que filtre pelo campo **CVF\_CODIGO** e verifique se o código que você deseja importar já consta na tabela;

Caso o registro exista, verificar se ele pertence a outra filial ou se é um registro órfão:

* Se a tabela for **compartilhada**, você não poderá repetir o código "001" para diferentes filiais;
* Se for necessário ter visões distintas, altere o código da visão no arquivo de exportação ou no ambiente de origem antes de gerar o novo arquivo.

Após validar/limpar os dados na **CVF**, realize novamente o processo de importação na filial 03 através da rotina **CTBA161**.

**Saiba Mais**

* [Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como importar Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007545672-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-importar-Vis%C3%A3o-Gerencial)
* [Visão Gerencial (CTBA161)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001548642-Contabilidade-Gerencial-Vis%C3%A3o-Gerencial)
