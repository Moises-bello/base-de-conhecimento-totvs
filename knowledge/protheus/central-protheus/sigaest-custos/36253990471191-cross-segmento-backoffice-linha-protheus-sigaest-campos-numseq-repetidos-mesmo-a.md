---
article_id: 36253990471191
category: SIGAEST - CUSTOS
content_hash: 949074955d9ac4c179a8e1b083286c9ea44805bf9d2b1b64eb5d47ef88117d5c
fetched_at: '2026-06-28T22:39:00.301228+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Campos _NUMSEQ repetidos
  mesmo após apagar  lsnumber.val e reiniciar o License Server
type: support-article
updated_at: '2026-04-20T12:19:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36253990471191-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Campos-NUMSEQ-repetidos-mesmo-ap%C3%B3s-apagar-lsnumber-val-e-reiniciar-o-License-Server
---

O problema ocorre devido à inconsistência entre os arquivos RPO do ambiente, causando chaves incorretas no License Server. É essencial equalizar e atualizar todos os RPOs para evitar erros na numeração automática, que pode ser controlada pelo License Server ou DBAccess. A partir da versão 20260525, só é permitido usar uma única versão de RPO no ambiente.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36253978729623) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**

Com as instruções [***desse link***](https://tdn.totvs.com/x/XgodMg), mesmo ao refazer as numerações, apagar o arquivo **lsnumber.val e reiniciar o License Server**, ao efetuar uma Transferência Interna através do ambiente, foi criada a chave incorreta no License Server. O que devo avaliar no ambiente?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

O problema ocorre devido a uma inconsistência ou falta de equalização entre os arquivos de repositório (RPOs) do ambiente. O License Server utiliza uma configuração padrão para o controle de numeração dos campos NumSeq, assumindo o Alias "SD2". Se o ambiente possuir mais de um RPO e estes estiverem com versões ou atualizações distintas, um RPO pode estar utilizando a nova estrutura de chave enquanto o outro ainda utiliza o formato antigo, gerando sequências incorretas ou duplicadas ao realizar movimentações.  
  
A partir do Release 12.1.2510, é possível optar pelo controle de numeração via License Server ou via DBAccess. As estruturas de chave variam conforme a escolha ([Controle de lock e numeração automática via dbaccess](https://tdn.totvs.com/x/XBYpOg) / [Controle de Numeração](https://tdn.totvs.com.br/pages/releaseview.action?pageId=949425872#DeckLockNum--183377369)):

* **Controle pelo License Server:** A chave segue o formato **SpecialKey+@@@+SD2+Código da Empresa+0**
* **Controle pelo DBAccess:** A chave é criada sem a Special Key, seguindo o formato **@@@SD2+Código da Empresa+0**.

Chaves que não atendam a essas especificações deixam de ser validadas pelas rotinas de movimentação após atualizações do sistema.

Para correção, é necessário garantir que todos os RPOs do ambiente estejam devidamente equalizados e atualizados com os pacotes mais recentes disponíveis no Portal do Cliente.

**Importante:**

A partir da versão 20260525, o sistema só permitirá o acesso ao mesmo ambiente utilizando uma única versão de RPO. Mais detalhes: [**Bloqueio no uso de RPOs distintos no mesmo ambiente**](https://tdn.totvs.com/x/ZNKoPg)

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[SIGAEST - Erro no calculo do custo \_NUMSEQ duplicado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35855256093207-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-no-calculo-do-custo-NUMSEQ-duplicado)

[Tabelas e campos envolvidos](https://tdn.totvs.com/x/IsP7Og)
