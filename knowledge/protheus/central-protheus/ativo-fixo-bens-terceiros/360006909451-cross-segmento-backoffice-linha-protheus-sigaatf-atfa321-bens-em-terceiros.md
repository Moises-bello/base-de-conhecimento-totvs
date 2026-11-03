---
article_id: 360006909451
category: Ativo Fixo - Bens terceiros
content_hash: fcc78b1b75611de7c519bf2394cfcf1fc1e55634515f4c195c60daacd8174c40
fetched_at: '2026-06-28T22:41:44.447663+00:00'
product: protheus
section_id: 1500001536381
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA321 - Bens em terceiros
type: support-article
updated_at: '2022-06-09T20:40:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006909451-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA321-Bens-em-terceiros
---

**Dúvida**Controle de bens em terceiros?  
**Ambiente**Protheus  – Ativo Fixo – A partir da versão 11.80  
  
**Solução:**Como controlar :

**Rotina ATFA321**

Essa rotina permite classificar a cessão de uso de bens em terceiros, tais como:

\* Concessão de direito real de uso;

\* Locação de bens;

\* Permissão de uso de bens.

"Antes de executar o controle de Bens em Terceiros, é necessário cadastrar/classificar o Bem, após este processo utilizar a rotina própria para cadastrar o  Bens em Terceiros (**ATFA321**)"

1. Cadastrar o bem (rotina de cadastro **ATFA012** ou classificação **ATFA240**)  
2. Em seguida siga em **Atualizações** /**Cadastro** / **Bens em Terceiros (ATFA321**)  
3. Ao entrar em incluir, no campo **NP\_CBASE** selecione o bem , campo **NP\_FORNEC** selecione o cliente e campo **NP\_TIPCES** selecione o tipo de concessão

Através de ações relacionadas é possível :

\*Visualizar Dados

Exibe os dados do controle de terceiros para visualização.

\*Visualizar Bem

Exibe os dados da ficha do ativo imobilizado para visualização.

\*Atualizar Dados

Altera e atualiza os dados da linha de seqüência de vigência ativa.

\*Renovar Dados

Renova os dados do bem de controle de terceiros. Gera uma nova linha de seqüência de vigência ativa e encerra a linha anterior.

\*Transferir Controle

Efetua a transferência de bens e encerra o controle de bens em terceiros, permitindo um novo cadastro de controle de terceiros para o bem. Esta ação não modifica o status do bem ou a classificação do tipo de controle configurada.

\* Excluir Dados

Exclui um bem em Terceiros. Esta ação somente pode ser executada quando o bem não possuir movimentações tais como: cálculos de depreciação e se não estiver bloqueado.

Ao realizar esta ação, o bem tem seus status alterado para bloqueado, não permitindo movimentações ou quaisquer tipos de cálculos e ajustes.

\* Demonstrativo

Emite a listagem dos bens em poder de terceiros exibindo: dados cadastrais do bem, posição valorizada atual do bem, dados do terceiro retentor dos bens e dados das sequências de vigência.
