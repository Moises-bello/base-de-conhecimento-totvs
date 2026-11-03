---
article_id: 33093447579799
category: eConsignado (Crédito do Trabalhador)
content_hash: 88d848986e61a70d3d8969e427d4955ad75598b2fc5bc1ef88853153941ae0f9
fetched_at: '2026-06-28T22:43:07.328821+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Mnemônicos eConsignado
type: support-article
updated_at: '2025-08-13T20:46:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33093447579799-RH-Linha-Protheus-GPE-Mnem%C3%B4nicos-eConsignado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33093447567639) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**  
Quais mnemônicos referentes ao eConsignado?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal - Todas as versões  
  
**Solução:**  
  
**Mnemônico P\_LIMECONS:** Limitar o desconto do eConsignado na folha de pagamento de acordo com o mnemônico P\_PERECONS. Deverá ser ativado com **.T.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33094116740759)

**Mnemônico P\_PERECONS:** Percentual de desconto do eConsignado. O valor do desconto será limitado ao percentual definido.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33094133574551)

**Mnemônico P\_DEDCONS:** Verbas que serão consideradas para desconto da margem consignável na folha.   
Esse mnemônico foi criado devido a inexistência de informações completas sobre as verbas que deveriam ser consideradas na formação da base, as verbas aqui informadas devem ser separadas com barras. Exemplo: "001/002/003"  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33094133575191)  
  
**Mnemônico P\_PERCONS: Não utilizado para o eConsignado.**  
Inicialmente o limite de desconto era feito pelo mesmo mnemônico usado para limitar os demais consignados, porém devido a particularidades do novo processo, foi criado o novo mnemônico P\_PERECONS para **uso exclusivo com o consignado referente ao crédito do trabalhador** que estará disponível no expedição contínua do RH a partir de 06/06/2025.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33094138454935)

**Mnemônico P\_ADICONS**: poderá ser incluído outras verbas de provento que devam ser somadas na Margem de Consignação total antes da aplicação do percentual de desconto máximo.  
Esse mnemônico foi criado devido a necessidade de somar a verba de afastamento paga pela empresa nos primeiros 15 dias. As verbas aqui informadas devem ser separadas com barras. Exemplo: "001/002/003"  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34163673392919)

Caso precise realizar alguma alteração nos mnemônicos, siga os passos abaixo:   
  
**1.** No SIGAGPE, acesse Atualizações > Definições de cálculo > Mnemônicos

**2.** Selecione o filtro 'Cod. Mnmemo.' e procure pelo mnemônico desejado:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33093447567895)  
  
**3.** Selecione o mnemônico e clique em 'Alterar':  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33093464351511)

**4.** Altere conforme a necessidade e confirme:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33093447568407)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - eConsignado - Como lançar manualmente em Valores Futuros o Credito do Trabalhador (MP nº 1.292/2025) e calcular desconto na Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31152092269591-RH-Linha-Protheus-GPE-eConsignado-Como-lan%C3%A7ar-manualmente-em-Valores-Futuros-o-Credito-do-Trabalhador-MP-n%C2%BA-1-292-2025-e-calcular-desconto-na-Folha-de-Pagamento)  
[RH - Linha Protheus - GPE - Como deduzir outras verbas de desconto da margem de consignação do Programa Crédito Trabalhador eConsignado (MP 1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32696289251351-RH-Linha-Protheus-GPE-Como-deduzir-outras-verbas-de-desconto-da-margem-de-consigna%C3%A7%C3%A3o-do-Programa-Cr%C3%A9dito-Trabalhador-eConsignado-MP-1-292-2025)
