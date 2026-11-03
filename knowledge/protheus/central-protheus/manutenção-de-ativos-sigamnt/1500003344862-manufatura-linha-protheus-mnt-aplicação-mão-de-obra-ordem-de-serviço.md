---
article_id: 1500003344862
category: Manutenção de Ativos (SIGAMNT)
content_hash: 54b1dcb5496d2e300c294a7ce2b6847a6b9fce9507f6fd6a135a43671af60929
fetched_at: '2026-06-28T22:42:32.738760+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Aplicação Mão de Obra Ordem de Serviço
type: support-article
updated_at: '2024-09-16T11:28:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003344862-Manufatura-Linha-Protheus-MNT-Aplica%C3%A7%C3%A3o-M%C3%A3o-de-Obra-Ordem-de-Servi%C3%A7o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26395803856663)*** Tempo aproximado para leitura: **00:01:45 min****Dúvida**Como funciona a aplicação de **Mão-de-obra** em **O.S - Ordem de Serviço**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**Para aplicação é necessário seguir os passos abaixo:

1. Acessar o **Manutenção de Ativos e Gestão de Frotas - SIGAMNT**;
2. Incluir uma **O.S corretiva** em **Atualizações / Controle de Oficina / Ordem de Serviço /** **Corretiva - MNTA420** com data inferior da data atual do Sistema;
3. Em **Atualizações / Controle de Oficina / Retorno O.S. / Retorno mod. 2 - MNTA435** reportar um insumo do tipo **Produto** e o segundo **Mão-de-obra** na mesma data da **O.S**;
4. Acessar o **Estoque/Custos - SIGAEST**;
5. Em **Atualizações / Movimentações / Internas / Armazém / Solicitar - MATA105**incluir uma **S.A - Solicitação de Armazém** com data atual informando um **Produto**;
6. Em **Atualizações / Movimentações / Internas / Armazém / Liberar Solicit. - MATA107**liberar a **S.A**;
7. Em **Atualizações / Movimentações / Internas / Armazém / Gerar Pré-requis. -** **MATA106**gerar uma pré-requisição;
8. Em **Atualizações / Movimentações / Internas / Armazém / Baixar Pré-requis. -** **MATA185** baixar a pré-requisição;
9. Retornar ao **Manutenção de Ativos e Gestão de Frotas - SIGAMNT**;
10. Em **Atualizações / Controle de Oficina / Retorno O.S. / Retorno mod. 2 - MNTA435** verificar a data do insumo de **mão-de-obra**.

**Importante**  
Em um cenário real, um produto não é aplicado/utilizado em uma **O.S**. sozinho, normalmente necessita-se de uma **mão-de-obra** para fazer uso deste produto em uma **O.S**. A regra de negócio então, estabelece que caso haja **mão-de-obra** aplicada na **O.S.**, a baixa/aplicação de um produto, realizada pelo estoque, irá utilizar a data da **mão-de-obra** já aplicada, entendendo que este produto foi utilizado no momento desta **mão-de-obra**.
