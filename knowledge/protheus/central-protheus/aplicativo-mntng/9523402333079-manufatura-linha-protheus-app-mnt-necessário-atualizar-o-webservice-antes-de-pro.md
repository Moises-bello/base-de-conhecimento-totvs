---
article_id: 9523402333079
category: 'Aplicativo MNTNG '
content_hash: 3b509e580609ad9e2ba3b41109dfa0c9d869ced53533e0bb7f871bd852eeaef6
fetched_at: '2026-06-28T22:42:37.732584+00:00'
product: protheus
section_id: 360010992174
source: central-protheus
title: Manufatura - Linha Protheus - APP MNT - Necessário atualizar o webservice antes
  de prosseguir
type: support-article
updated_at: '2022-10-13T19:13:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9523402333079-Manufatura-Linha-Protheus-APP-MNT-Necess%C3%A1rio-atualizar-o-webservice-antes-de-prosseguir
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min  
  
Ocorrência**Ao validar o ambiente no [Portal mobile NGI](https://portalmobile.ngi.com.br/Manage/Settings) retorna a mensagem **Aviso - Necessário atualizar o webservice antes de prosseguir**.

**![cliente.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9523177401879)**

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Aplicativo MNTNG - Todas as versões  
  
**Causa**A situação acontece porque os programas do aplicativo no **RPO** - **Repositório de Objetos Protheus** estão desatualizados.   
  
**Solução**  
Para realizar a atualização do *webservice* será necessário aplicar o [pacote de atualização](https://tdn.totvs.com/pages/releaseview.action?pageId=522005297) no serviço **REST**. Lembrando de certificar-se que o pacote está sendo aplicado no **RPO** apontado na configuração do **REST** pela chave **SourcePath**.  
  
**Saiba mais**Detalhes da atualização do módulo no *link* [Manufatura - Linha Protheus - MNT - Atualização do Manutenção de Ativos e Gestão de Frotas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040697714-Manufatura-Linha-Protheus-MNT-Atualiza%C3%A7%C3%A3o-do-Manuten%C3%A7%C3%A3o-de-Ativos-e-Gest%C3%A3o-de-Frotas)
