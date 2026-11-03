---
article_id: 360022934151
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 05bbc2b40155eafe7144478542da739d0411653c52a39b4ab4989bd60610bef1
fetched_at: '2026-06-28T22:38:55.411805+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como utilizar a Solicitação
  de Transferência (MATA311) com controle de alçada? '
type: support-article
updated_at: '2024-03-27T21:24:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022934151-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-utilizar-a-Solicita%C3%A7%C3%A3o-de-Transfer%C3%AAncia-MATA311-com-controle-de-al%C3%A7ada
---

**Dúvida**

Como utilizar a **Solicitação de Transferência** (**MATA311**) com **controle de alçada**?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Para solucionar essa dúvida, realize os seguintes passos:

**- 1 -** Habilitar o parâmetro **MV\_APROVTR** (.T.);

**- 2 -** Habilitar o parâmetro **MV\_ALTPDOC**;

**- 3 -** Habilitar o parâmetro **MV\_STAPROV**. Caso não exista, criar com o tipo caractere. **Obs.:** O conteúdo desse parâmetro, é o **código do Grupo de Aprovadores (SAL\_COD)** responsável pelas aprovações das Solicitações de Transferências. Exemplo no print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22384486704919)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22385146193943)

**Veja também o passo a passo no vídeo abaixo:**

Após a criação dos parâmetros acima, poderá incluir uma **Solicitação de Transferência (MATA311)** que ficará com Status **em aprovação** e só será possível liberar caso acesse à rotina **MATA094 - L****iberação de Documentos.**

\*Caso após a criação dos parâmetros acima, não seja ativado o controle de alçada, reavalie as documentações abaixo para correta configuração:

[MP - SIGACOM - Principais Atualizações do Módulo de Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028041232-MP-SIGACOM-Principais-Atualiza%C3%A7%C3%B5es-do-M%C3%B3dulo-de-Compras?source=search)

[How To | MP - SIGACOM - Alçada Padrão](https://www.youtube.com/watch?v=GXYL5sgXQ_k)

Ao fazer a liberação poderá retornar na rotina de Solicitação de Transferência e efetivar o movimento.

**OBS:** Caso tenha a necessidade de fazer a restrição de acesso a determinado usuário no momento da efetivação da respectiva solicitação de transferência, poderá acessar o configurador e restringir através da opção "Controle de Acesso".

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
