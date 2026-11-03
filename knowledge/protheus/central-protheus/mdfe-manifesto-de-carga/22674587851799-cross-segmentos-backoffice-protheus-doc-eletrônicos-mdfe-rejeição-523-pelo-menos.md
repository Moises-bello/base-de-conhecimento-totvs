---
article_id: 22674587851799
category: MDFe - Manifesto de Carga
content_hash: c58ed77b84979e664803a4b83ae2e5882bbde00c8fd98eae593091aa83b855dd
fetched_at: '2026-06-28T22:40:08.083182+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - Rejeição
  523: Pelo menos um reboque deve ser colocado na composição em um transporte com
  cavalo mecânico'
type: support-article
updated_at: '2025-06-10T19:44:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22674587851799-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Rejei%C3%A7%C3%A3o-523-Pelo-menos-um-reboque-deve-ser-colocado-na-composi%C3%A7%C3%A3o-em-um-transporte-com-cavalo-mec%C3%A2nico
---

**Dúvida**Como proceder com Rejeição 523: Pelo menos um reboque deve ser colocado na composição em um transporte com cavalo mecânico. ?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22674610629143)**

A SEFAZ passou a validar a rejeição 523 na emissão do MDFe com o tprod = 3 e sem reboque  
Esta validação entrou em vigor no dia  08/04 a partir das validações da **NT 2024.001**  
   
Sendo assim, caso queira emitir o MDFe com o tpRod = 3 Cavalo mecânico deverá ser informado Reboque no envio do MDFe.

A informação do tipo do veiculo fica amarrada ao cadastro do veiculo **OMSA060** pelo campo **DA3\_TIPVEI** e pode ser alterado no cadastro do tipo de veiculo **TMSA530**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22674587837463)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22674587839255)

Para correção pode alterar no cadastro do tipo de veiculo o campo **Tp.Rod** para uma opção diferente de 3 e refazer o MDF-e ou informar um Reboque no campo de reboque na inclusão do MDFe.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22674610637335)

Também pode trazer o reboque de forma automática ao clicar em **Outras ações - Reboque**

![](https://totvssuporte.zendesk.com/attachments/token/SI6uxcEX55AV2ylmD9ZGJmt2G/?name=image.png)

Mas para isso é necessário que tenha feito os vínculos do veiculo e reboque em **Faturamento - Expedições**, selecione a nota e depois clique em **Manutenção**

![](https://totvssuporte.zendesk.com/attachments/token/gjZyjj7QW2RUILiwnOCLft4DP/?name=image.png)

Você pode inserir os veículos nos campos **F2\_VEICUL1** e **F2\_VEICUL2**. Se houver mais de um veículo, certifique-se de preencher os campos correspondentes. Lembre-se de que o **veículo 1** deve ser o cavalo, enquanto os demais serão considerados **reboques**.

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar reboque no MDFe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016390991--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-reboque-no-MDFe?source=search)

**OBS: Apos os ajustes caso ocorra erro de rejeição na TAG  <tpRod>  valide conforme a documentação abaixo:**

**[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Falha de Schema tpRod](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016125731--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Falha-de-Schema-tpRod?source=search)**
