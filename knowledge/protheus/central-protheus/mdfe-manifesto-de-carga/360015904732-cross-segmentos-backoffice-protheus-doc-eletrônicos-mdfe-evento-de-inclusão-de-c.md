---
article_id: 360015904732
category: MDFe - Manifesto de Carga
content_hash: 7256813ce053dc443e7ed039d1d6efb6f36c91bc1dc51eb418bcea92d263f5cb
fetched_at: '2026-06-28T22:40:08.272948+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - Evento de
  Inclusão de Condutor
type: support-article
updated_at: '2025-06-10T19:18:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015904732-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Evento-de-Inclus%C3%A3o-de-Condutor
---

**Dúvida**Como fazer o evento de inclusão de condutor ?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**Este **não é um evento obrigatório** e deve ser feito somente quando houver alterações necessárias no condutor do veículo.

Este evento de inclusão de condutor deve seguir as regras:

* O documento MDF-e já deve ter sido emitido e autorizado
* Ainda não tenha sido encerrado ou cancelado
* Esse evento é exclusivamente para transporte via modal Rodoviário.

**Importante:**  
Para que o botão **Incluir Condutor** esteja disponível no sistema é necessário que o fonte SPEDMDFE.PRW esteja igual

ou superior a **31/03/2016**.

## Procedimento para Utilização

       1.            No Faturamento  (SIGAFAT), acesse Faturamento/MDF-e (SPEDMDFE).

O sistema apresenta a janela de MDFe;

       2.           No menu de opções (outras ações), clique em Gerenciar MDFe.

       3.           Marque o MDFe que esteja autorizado e depois clique no botão Outras Ações - Eventos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23871797119895)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23871831927447)

1 - Este campo é preenchido através da tabela DA4 cadastro de Motorista.

- O item **Codigo** é derivado do campo DA4\_NOME.  
- O item **Nome do Condutor** é derivado do campo DA4\_CGC.  
- O item **CPF** é derivado do campo DA4\_COD.

2 -  Transmite o evento de condutor para Sefaz.

3 -  Atualiza o retorno do MDF-e com a resposta da Sefaz.

4 -  Mostra o XML de retorno da Sefaz.

5 -  Apresenta o status do evento de condutor.

6 - Fecha a Tela.

7 - Caso tenha duvidas referente a impressão do DAMDFE verificar conforme documentação abaixo:

**[Cross Segmentos - Backoffice Protheus - TSS - MDFE - Imprimir DAMDFE com alteração de condutor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051694694-MP-MDFE-Imprimir-DAMDFE-com-altera%C3%A7%C3%A3o-de-condutor)**

[Evento de inclusao de condutor](http://tdn.totvs.com/pages/viewpage.action?pageId=235309671)
