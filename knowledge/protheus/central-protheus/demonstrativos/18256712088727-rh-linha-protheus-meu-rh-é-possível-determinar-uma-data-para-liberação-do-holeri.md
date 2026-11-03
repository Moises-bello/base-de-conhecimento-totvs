---
article_id: 18256712088727
category: DEMONSTRATIVOS
content_hash: 82fb21bca25cd62804523a63db5aa5a8c54fec8e3ff71636652b1f34df24d6f9
fetched_at: '2026-06-28T22:44:38.380213+00:00'
product: protheus
section_id: 10299629664279
source: central-protheus
title: RH - Linha Protheus - Meu RH - É possível determinar uma data para liberação
  do holerite da 2ª parcela do 13º salário pelo App Meu RH MV_TCFD132 e MV_TCFD131
type: support-article
updated_at: '2025-11-28T17:26:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256712088727-RH-Linha-Protheus-Meu-RH-%C3%89-poss%C3%ADvel-determinar-uma-data-para-libera%C3%A7%C3%A3o-do-holerite-da-2%C2%AA-parcela-do-13%C2%BA-sal%C3%A1rio-pelo-App-Meu-RH-MV-TCFD132-e-MV-TCFD131
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18256737960471) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
É possível determinar uma data para liberação do holerite da 2ª parcela do 13º salário pelo App Meu RH?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Há um parâmetro no **Configurador do Sistema Protheus** que, irá **determinar o dia do mês** que, o holerite da **2ª parcela do 13º salário** será demonstrado via **App Meu RH.**

Antes de qualquer análise deve ser verificado a configuração do [**MV\_TCF013A**](https://tdn.totvs.com/display/public/PROT/RHO0006_Tipos_de_demonstrativos_para_consulta_do_RH_On-line) abaixo:  
  
MV\_TCF013A -> (exemplo de conteúdo: 01.02.03.04.05.06.07) -> Opções de consulta do demonstrativo de pagamento:  
**01** - Adiantamento  
**02** - Folha  
**03** - 1ª parcela do 13º  
**04** - 2ª parcela do 13º   
**05** - PLR  
**06** - Autônomos  
**07** - Valores Extras  
  
É necessário acessar o **Configurador**, programa inicial **SIGACFG** e, na rotina **Ambiente > Cadastros > Parâmetros**, localizar o parâmetro **MV\_TCFD132** e editar.  
  
O  conteúdo padrão do parâmetro é 20, isso significa que, **quando houver o roteiro 132 no período do GPE**, no **dia 20 daquele mês**, o holerite de **13º salário - 2ª parcela** será demonstrado no **App Meu RH**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18256690148375)

**Formula de cálculo da montagem da data de liberação:**

1 - Conteúdo do paramêtro MV\_TCFD132 + o mês e ano da data de pagamento do roteiro 132 no cadastro do período. Digamos que o conteúdo do paramêtro MV\_TCFD132 é 20 e a data de pagamento é 10/12/2025.

2 - A data de liberação será 20/12/2025 ou seja quando a data do windows for maior ou igual a 20/12/2025 será demonstrado o recibo do roteiro 132 no Meu Rh.  
  
OBS: Sistema não faz redução de data caso o paramêtro esteja com conteúdo negativo exemplo -10. Ele sempre pega o conteúdo do paramêtro despresa o sinal de negativo e usar como dia da data de liberação.  
  
**Essa regra vale também para o paramêtro MV\_TCFD131**  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
