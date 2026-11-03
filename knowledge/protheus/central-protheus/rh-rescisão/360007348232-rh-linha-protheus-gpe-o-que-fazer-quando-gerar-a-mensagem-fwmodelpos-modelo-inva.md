---
article_id: 360007348232
category: RH - Rescisão
content_hash: 223811fee2bb3e89e898ade6f5d95b7fe607af56482e6ef400f8e193e7877fd4
fetched_at: '2026-06-28T22:43:49.810108+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - O que fazer quando gerar a mensagem FWMODELPOS
  - MODELO INVALIDO ao incluir uma rescisão?
type: support-article
updated_at: '2025-06-12T12:30:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007348232-RH-Linha-Protheus-GPE-O-que-fazer-quando-gerar-a-mensagem-FWMODELPOS-MODELO-INVALIDO-ao-incluir-uma-rescis%C3%A3o
---

**Dúvida**O que fazer quando gerar a mensagem FWMODELPOS - MODELO INVALIDO ao incluir uma rescisão e/ou rescisão complementar?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Primeiramente devemos verificar se as verbas geradas no cálculo da rescisão, estão com o **campo Natureza (RV\_NATUREZ)** no cadastro de verbas, aba eSocial devidamente preenchidos. Caso o campo esteja em branco, será necessário realizar a alteração para que o sistema não gere a mensagem novamente.

Outra verificação importante é no roteiro de cálculo RES, que deve ser habilitado de acordo com o mês que a rescisão está sendo calculada. Portanto, analise no **cadastro de períodos** se o campo **Per.Selec** do roteiro **RES** está **informado com Sim**, de acordo com o mês que a rescisão está sendo calculada. Se o campo estiver com a informação Não, altere para Sim e inclua novamente a rescisão.  
  
O **roteiro RES** do mês seguinte da rescisão precisa estar criado, porém o campo **Per.Sel** deve ficar como **Não**.

**Saiba Mais**  
Para essa mensagem também é possível aplicar o pacote acumulado com as últimas atualizações.

Acesse o *link* a seguir para baixar o pacote acumulado RH:

[RH ACUMULADO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
