---
article_id: 1500007496002
category: RH - Tipos de Ausências
content_hash: c569bb29763f360586688dad8438efb5c54cb65ee4ad16a20dfe1b029a3e0835
fetched_at: '2026-06-28T22:43:20.980133+00:00'
product: protheus
section_id: 360011967353
source: central-protheus
title: RH - Linha Protheus - GPE - Como deve ser preenchido o novo campo RCM_PDSUP
  (Verba Susp.) no cadastro do tipo de ausência
type: support-article
updated_at: '2025-08-22T14:52:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007496002-RH-Linha-Protheus-GPE-Como-deve-ser-preenchido-o-novo-campo-RCM-PDSUP-Verba-Susp-no-cadastro-do-tipo-de-aus%C3%AAncia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29455885495575) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como deve ser preenchido o novo campo RCM\_PDSUP (Verba Susp.) no cadastro do tipo de ausência?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O primeiro passo é incluir **novas verbas de provento**, com base no **auxílio doença** e no **auxílio acidente**, mas **sem incidência para INSS** para folha e **sem incidência para o eSocial.**Verifique a **documentação** a seguir para **auxiliar no cadastro das verbas** sem incidência de INSS: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007487421>   
  
O segundo passo é alterar os tipos de ausência padrão e vincular as verbas criada sem incidência para INSS:

|  |  |  |  |
| --- | --- | --- | --- |
| **Código** | **Descrição** | **Cod.Verba (RCM\_PD)** | **Verba Sup. (RCM\_PDSUP)** |
| 3 | Afastamento Temporário Acidente Trabalho | 123 | 261 |
| 4 | Afastamento Temporário por Doença | 122 | 260 |

**Exemplo** de como preencher nos casos de **Afastamento Temporário por Doença.**  
Ao informar a **verba sem incidência pra INSS**, o **cadastro será concluído.** No exemplo abaixo foi criada a verba de código 260.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500010712541)

**Exemplo**: No tipo de ausência Aux Doença, se informar a verba com id 0042 por exemplo, no campo RCM\_PDSUP, que tem incidência pra INSS, será exibido a mensagem abaixo impossibilitando o cadastro:

![](https://tdn.totvs.com/download/attachments/608545018/image2021-4-12_22-29-49.png?version=1&modificationDate=1618277393177&api=v2)  
  
 **Saiba Mais**  
[Documentação Técnica](https://tdn.totvs.com/pages/releaseview.action?pageId=608545018#Exemplosdec%C3%A1lculo-1811452821)  
[RH - Linha Protheus - GPE - Como configurar o sistema para afastamento superior a 15 dias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004741422-RH-Linha-Protheus-GPE-Como-configurar-o-sistema-para-afastamento-superior-a-15-dias)  
[RH - Linha Protheus - GPE - Não aparece verba cadastrada para vincular ao Tipo de Ausência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15669629352343-RH-Linha-Protheus-GPE-N%C3%A3o-aparece-verba-cadastrada-para-vincular-ao-Tipo-de-Aus%C3%AAncia)  
[RH - Linha Protheus - GPE - Campo Verba Sup - RCM\_PDSUP bloqueado para edição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005088861-RH-Linha-Protheus-GPE-Campo-Verba-Sup-RCM-PDSUP-bloqueado-para-edi%C3%A7%C3%A3o)  
[RH - Linha Protheus - GPE - Verba não aparece para ser selecionada nos campos de Verba do Tipo de ausência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15114225514519-RH-Linha-Protheus-GPE-Verba-n%C3%A3o-aparece-para-ser-selecionada-nos-campos-de-Verba-do-Tipo-de-aus%C3%AAncia)
