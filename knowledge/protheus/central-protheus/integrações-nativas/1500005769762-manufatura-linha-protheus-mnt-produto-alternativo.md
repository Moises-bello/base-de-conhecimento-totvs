---
article_id: 1500005769762
category: Integrações Nativas
content_hash: ba8162a73cbfa319c12b973bd00e9c39a0ef04b529f96e80f1bbb7dfd453d8e7
fetched_at: '2026-06-28T22:42:35.518898+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Produto Alternativo
type: support-article
updated_at: '2021-09-08T14:29:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005769762-Manufatura-Linha-Protheus-MNT-Produto-Alternativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)** Tempo aproximado para leitura: **00:01:00 min** **Dúvida**O que é o **Produto alternativo** utilizado no módulo **Manutenção de Ativos - SIGAMNT**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Versão 12  
  
**Solução****Produto alternativo** é aquele que, na falta de um produto principal, pode ser substituído e usado como produto principal, visto que possui as características semelhantes. Desta forma, ao incluir uma **Ordem de serviço** com o *status* igual a **Liberado** e informando um insumo do tipo **Produto**, será validado o saldo em estoque do produto principal, caso não haja quantidade suficiente do produto principal, será utilizado o produto informado no vínculo de alternativos na tabela **Produtos Alternativos -****SGI**. Assim, enquanto a quantidade do produto não for suficiente para atender a requisição da **Ordem de serviço**, e possuir opções de produtos alternativos na tabela **Produtos Alternativos -****SGI**para o produto principal, será realizada uma busca até encontrar um **Produto alternativo** que atenda a quantidade solicitada.  
  
**Saiba mais**Para ter acesso a documentação deste processo, acesse o *link* [Produto alternativo](https://tdn.totvs.com/display/PROT/Produto+alternativo)
