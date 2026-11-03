---
article_id: 41466998232087
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 6f59cdcacbf3ced26482a23d2ba574db58bc80f9d2444b004a7f526d1a89acf4
fetched_at: '2026-06-28T22:41:05.117389+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - CTBA960 - As
  Stored Procedures de Fechamento Contábil encontram-se desatualizadas.
type: support-article
updated_at: '2026-06-24T21:26:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41466998232087-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-CTBA960-As-Stored-Procedures-de-Fechamento-Cont%C3%A1bil-encontram-se-desatualizadas
---

Ao acessar a rotina de Fechamento Contábil no TOTVS Backoffice (Protheus), pode surgir a mensagem indicando que as Stored Procedures 01 e 29 estão desatualizadas. Para resolver, acesse Configurador Dicionário Base de dados Stored Procedures, selecione a empresa, marque as procedures 01 e 29, clique no ícone para instalar e confirme após a atualização.

**Dúvida**   
Ao acessar a rotina de Fechamento Contábil, o sistema apresenta a seguinte mensagem de validação no ecrã:   
"As Stored Procedures de Fechamento Contábil encontram-se desatualizadas. Necessário instalar os processos 01 e 29 para o módulo Contabilidade Gerencial".   
  
Como proceder para instalar as referidas procedures?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41466983210903)

**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial (SIGACTB) - 2410 e superior.

**Solução**   
Para solucionar esta ocorrência e prosseguir com o fechamento, é necessário atualizar as Stored Procedures 01 e 29 no sistema.   
  
Siga os passos abaixo para atualizar as procedures:

1. Aplique o pacote de atualização:  
   [Pacotes de Atualização - Contabilidade Gerencial - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)
2. Acessa o configurador > Dicionário > Base de dados > Stored Procedures;
3. Selecione a empresa pretendida;
4. Marque as procedures 01 e 29;
5. Clique no ícone representado por uma caixa marrom com uma seta verde para iniciar a instalação;
6. Após terminar o processo de atualização, clique em confirmar.

**Saiba Mais**   
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - SIGAATF - SIGAPCO - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30076556464023-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-SIGAATF-SIGAPCO-Procedure-Desatualizada-ou-Incompat%C3%ADvel)  
[Stored Procedures - Novo gerenciador de pacotes - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes)
