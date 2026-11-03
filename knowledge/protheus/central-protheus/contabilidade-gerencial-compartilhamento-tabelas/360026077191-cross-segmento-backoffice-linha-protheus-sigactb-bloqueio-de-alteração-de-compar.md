---
article_id: 360026077191
category: Contabilidade Gerencial - Compartilhamento Tabelas
content_hash: 36828f94d188474d88991f4df3c81d8db0615de468f9a8d9e84896e60b9369d2
fetched_at: '2026-06-28T22:40:57.794963+00:00'
product: protheus
section_id: 1500001537461
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - BLOQUEIO DE ALTERAÇÃO
  DE COMPARTILHAMENTO A PARTIR LIB versão 20181015
type: support-article
updated_at: '2022-03-29T20:04:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026077191-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-BLOQUEIO-DE-ALTERA%C3%87%C3%83O-DE-COMPARTILHAMENTO-A-PARTIR-LIB-vers%C3%A3o-20181015
---

**Ocorrência**Bloqueio no compartilhamento de tabelas realizado a partir da LIB versão 20181015  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Causa**Para evitar a alteração do **compartilhamento da tabela** entre empresas quando a tabela já possui registros, o que pode gerar inconsistência de dados, foi implementada uma trava no Configurador que faz com que os campos **Ac. Filial**, **Ac. Unidade** e **Ac. Empresa** fiquem bloqueados para alteração quando a tabela já estiver alimentada, evitando a alteração do seu **tipo de compartilhamento**. A alteração só poderá ser feita em **tabelas vazias**.

**Exemplo de tela:**

# Tabela SA3 vazia, campos "Ac" liberados  
Configurador > Base de Dados > Dicionário > Bases de Dados > Tabela SA3  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025153751/mceclip0.png)

# Tabela SA3 alimentada, campos "Ac" bloqueados  
Configurador > Base de Dados > Dicionário > Bases de Dados > Tabela SA3  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025153811/mceclip1.png)

**Solução:**

Caso necessite realizar a alteração do compartilhamento de tabelas após já [ter realizado movimentações](https://tdn.totvs.com/pages/releaseview.action?pageId=412886207) nas mesmas (registros no banco de dados), é altamente recomendável a presença de um analista in loco para a realização dos procedimentos de acordo com a análise prévia de sua estrutura empresarial.

Não recomendamos a alteração de compartilhamento após a implantação do ERP sem presença de um  especialista . Vários efeitos colaterais podem ocorrer no sistema caso seja alterado erroneamente 

Para solicitação de um analista in loco, entre em contato com seu Executivo de Conta TOTVS. 

Caso tenha em sua empresa um especialista Protheus, temos disponível um passo a passo para apoio.

***Acesse: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024744151>***

***OBS: O apoio a execução deste procedimento não faz parte do escopo de atendimento do Suporte HelpDesk.***
