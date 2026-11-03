---
article_id: 1500005679301
category: Integrações Nativas
content_hash: df18cab2eb0fb90ba11ac57254b736d66c79fafe2835f0d7b46ac00c7928481f
fetched_at: '2026-06-28T22:42:35.473923+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Movimentações de Estoque originadas pelo
  Manutenção de Ativos
type: support-article
updated_at: '2022-05-25T16:55:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005679301-Manufatura-Linha-Protheus-MNT-Movimenta%C3%A7%C3%B5es-de-Estoque-originadas-pelo-Manuten%C3%A7%C3%A3o-de-Ativos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)** Tempo aproximado para leitura: **00:01:30 min****Dúvida**Quais são os processos de **Movimentação - SD3** originados pelo **SIGAMNT -** **Manutenção de Ativos**?  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Versão 12  
 **Solução**Toda a movimentação originada por **O.S.'s- Ordens de serviço** utiliza o campo **Tipo de Movimento - D3\_TM** pelos códigos informados nos parâmetros:

* **MV\_MNTDEV - Tipo de movimento para devolução no SIGAMNT**
* **MV\_MNTREQ - Tipo de movimento para requisição no SIGAMNT**

Ao realizar a aplicação de insumos realizados do tipo **Produto** ou **Mão de Obra**serão gerados automaticamente registros de movimentações de **Requisição** para os produtos, relacionando com a **Ordem de Produção - D3\_OP** associada a **O.S.** que está sendo feito os reportes.   
Na finalização de **O.S.** são gerados dois registros de na **SD3**, sendo uma**Requisição** e uma**Devolução** utilizando-se do produto padrão de manutenção o qual pode ser alterado pelo parâmetro **M****V\_PRODMNT**, sendo o seu conteúdo o código padrão **MANUTENCAO**. Este processo é independente de qualquer ação do usuário e tem como finalidade agregar os custos da manutenção.  
  
**Saiba mais**  
Para informações complementares a respeito dos parâmetros, veja o link [Parâmetros para realizar movimentações de estoque](https://tdn.totvs.com/pages/viewpage.action?pageId=679937062)   
E para detalhes das especificações do movimento referente ao campo **Tipo RE/DE - D3\_CF** veja no *link*: [MP - SIGAEST – Quais os significados dos códigos dos tipos de Movimentos Internos RE/DE?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007057091)
