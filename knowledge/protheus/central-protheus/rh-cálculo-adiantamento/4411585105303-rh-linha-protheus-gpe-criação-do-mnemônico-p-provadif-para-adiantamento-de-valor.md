---
article_id: 4411585105303
category: RH - Cálculo Adiantamento
content_hash: c6a34d71cc2d816daee0d828144822a494dcd05f0c585bf9b325b96dbf819553
fetched_at: '2026-06-28T22:43:14.296605+00:00'
product: protheus
section_id: 360011983213
source: central-protheus
title: RH - Linha Protheus - GPE - Criação do mnemônico  P_PROVADIF para adiantamento
  de valores no Adiantamento
type: support-article
updated_at: '2025-04-15T12:29:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411585105303-RH-Linha-Protheus-GPE-Cria%C3%A7%C3%A3o-do-mnem%C3%B4nico-P-PROVADIF-para-adiantamento-de-valores-no-Adiantamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24581718202903)** Tempo aproximado para leitura:**00:01:30 min****Dúvida**Criação do mnemônico P\_PROVADIF para adiantamento de valores no Adiantamento  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Situação:**

Ao utilizar no cálculo de um Adiantamento (roteiro ADI) uma verba com o campo Ref. Adiant. (**RV\_ADIANTA**) igual a **SIM** o Sistema repete a mesma verba no cálculo da Folha de Pagamento (Roteiro FOL).  
  
**Exemplo**  
Trabalhador CLT com adiantamento **mensal** configurado com **40%**  (SRA) e no roteiro **ADI** também lanço um **Provento** de Adiantamento de **Comissão** que está configurada no c**adastro de verbas** (SRV) com o campo **Ref. Adiant.** (RV\_ADIANTA) igual a **Sim**.

Quando **fecho** o roteiro **ADI,** a verba de Provento de Adiantamento de **Comissão** lançada se repete no roteiro **FOL** com o mesmo valor.

Por ser apresentada nos dois roteiros, a verba também é duplicada no **eSocial** e pode ocasionar **diferença** na apuração dos encargos.

**Solução:**

Criado o Mnemônico **P\_PROVADIF** - para que seja possível gerar provento de adiantamento na folha (Outras Verbas) ou não.  
  
O valor padrão dele é verdadeiro **.T.**  onde o sistema mantem o comportamento padrão de **gerar** tanto o **provento do adiantamento** informado quanto sua **contrapartida** de **desconto** na **folha.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31423865441047)**

Ao alterar o mnemônico para falso **.F.**, o sistema **Não** deve gerar a verba Informada (Provento/Desconto) no roteiro da folha, mas **continuará gerando** sua **contra-partida** nas verbas de **adiantamento** (Id 0006/0007).

Quando o mnemônico **P\_PROVADIF = .F.**,  é esperado que na folha exista o **lançamento** de uma verba com o **valor total** do provento/desconto que foi adiantado. Este valor corresponde ao que é devido **integralmente** ao/pelo funcionário e deverá possuir **correspondência de incidências** com a verba que foi paga/descontada no adiantamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31423865443223)

**Importante**Antes de realizar o fechamento do período, certifique-se de que o mnemônico foi devidamente criado, acessando o cadastro de mnemônicos em **Atualizações > Defiunições de Cálculo > Mnemônicos**.  
  
**Saiba Mais**

[RH - Linha Protheus - GPE - Adiantamento Salarial - Configurações e Conceitos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052166714-RH-Linha-Protheus-GPE-Adiantamento-Salarial-Configura%C3%A7%C3%B5es-e-Conceitos?source=search)

[RH - Cálculo Adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983213-RH-C%C3%A1lculo-Adiantamento)
