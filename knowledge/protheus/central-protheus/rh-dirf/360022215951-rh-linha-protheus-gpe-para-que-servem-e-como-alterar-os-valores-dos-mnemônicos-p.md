---
article_id: 360022215951
category: RH – DIRF
content_hash: a4598dd243e9b9472c356c84d54ff2a1e1b0d2242b62abf4b55f27d5fdd90e86
fetched_at: '2026-06-28T22:44:07.126531+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Para que servem e como alterar os valores dos mnemônicos
  P_VLLIMDIRF e P_VLLIMOUT para DIRF
type: support-article
updated_at: '2025-08-04T19:16:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022215951-RH-Linha-Protheus-GPE-Para-que-servem-e-como-alterar-os-valores-dos-mnem%C3%B4nicos-P-VLLIMDIRF-e-P-VLLIMOUT-para-DIRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33939361028503) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Para que servem e como alterar os valores dos mnemônicos **P\_VLLIMDIRF** e **P\_VLLIMOUT** para DIRF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões.  
  
**Solução**Os mnemônicos **P\_VLLIMDIRF** e **P\_VLLIMOUT** definem a partir de qual valor os rendimentos serão enviados no arquivo magnético da DIRF.  
  
O mnemônico **P\_VLLIMDIRF** define o valor mínimo dos rendimentos a ser considerado para a geração do arquivo da DIRF para beneficiário de trabalho assalariado. Seu valor padrão é R$ 17989.80 e, caso necessário, este pode ser alterado.  
  
O mnemônico **P\_VLLIMOUT** define o valor mínimo dos rendimentos a ser considerado para a geração do arquivo da DIRF referente aos rendimentos sem vínculo empregatício, de aluguéis e de royalties. Seu valor padrão é  6000.00 e, caso necessário, este pode ser alterado.  
  
Para alterar, acesse a rotina **Mnemônicos** pelo caminho **>Atualizações >Definições de cálculos >Mnemônicos**. Localize os mnemônicos e altere conforme necessidade:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9204368423703)  
  
Os valores **não** devem conter vírgula, somente ponto. Conforme exemplo a seguir:  
**P\_VLLIMDIRF - 28559.70**  
**P\_VLLIMOUT - 6000.00**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9204244990615)

**Importante:** Se houver desconto de IRRF para o beneficiário, mesmo que o rendimento tributável seja inferior ao valor informado nos mnemônicos P\_VLLIMDIRF e P\_VLLIMOUT, o beneficiário será gerado no arquivo magnético da DIRF.

**Saiba Mais:**[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
