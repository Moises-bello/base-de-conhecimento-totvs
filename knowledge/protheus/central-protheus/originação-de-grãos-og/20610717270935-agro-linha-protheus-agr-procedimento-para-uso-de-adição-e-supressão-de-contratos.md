---
article_id: 20610717270935
category: Originação de Grãos (OG)
content_hash: 983c719394d0b08214d2218a50840e97c8ed40f1b21703651bbe1a9afa811eda
fetched_at: '2026-06-28T22:45:43.757763+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Procedimento para uso de adição e supressão de
  contratos
type: support-article
updated_at: '2025-06-13T21:12:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20610717270935-Agro-Linha-Protheus-AGR-Procedimento-para-uso-de-adi%C3%A7%C3%A3o-e-supress%C3%A3o-de-contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20610717233047) Tempo aproximado para leitura: **00:01:55 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para adicionar ou suprimir saldo no contrato é apresentada a ocorrência **Procedimento para uso de adição e supressão de contratos**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois é preciso realizar o processo para adicionar ou suprimir saldo no contrato no Sistema.  
  
**Solução**  
Para solucionar essa ocorrência, efetue o processo corretamente, realize os seguintes passos:

**1.** Acesse a rotina **OGA0140 -****Motivo Alter. Ctr.,** inclua um motivo da alteração, que pode ser uma adição ou supressão;   
A **Adição** ou **Supressão** é usada para situações em que haja a necessidade de receber uma quantidade em um contrato sem saldo - **Adição** e **Supressão** quando se deseja deixar o contrato sem saldo - **tirar quantidade do contrato** para que possa finalizar o contrato, ou outra finalidade.

![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20610706457239)

![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20610717235351)

**2.** Acessar o contrato que deseja fazer a alteração, **OGA280 -****Contrato de Compra**, **OGA290 -****Contrato de Venda**, **OGA270 -****Contrato Depto em 3** ou **OGA260 -****Contrato Depto de 3**. Acessar **Outras Ações** **> Mais ações >** **Adic./Supres.**  
  
**2.1** - Incluir a **Adição** ou **Supressão** para o contrato. Ao confirmar, o registro é inserido com sucesso;  
  
**2.2** - Porém a confirmação da alteração não é efetuada neste momento, portanto para confirmar precisa acessar **Outras Ações** e **Confirmar**;

![3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20610706460951)

**2.3** - É apresentada uma tela com as informações das alterações, com a quantidade da alteração do contrato e com a quantidade total depois da alteração, depois deve confirmar se estiver tudo correto.

![4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20610706462231)
