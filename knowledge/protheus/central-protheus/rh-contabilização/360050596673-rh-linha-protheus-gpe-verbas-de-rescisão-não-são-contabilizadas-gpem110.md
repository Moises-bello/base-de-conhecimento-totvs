---
article_id: 360050596673
category: RH - Contabilização
content_hash: 595fa75293e24780283a470175c70005dfb3c0bfc41d72b9c33b3013d33e3c32
fetched_at: '2026-06-28T22:43:46.162758+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Verbas de rescisão não são contabilizadas (GPEM110)
type: support-article
updated_at: '2021-06-07T13:24:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050596673-RH-Linha-Protheus-GPE-Verbas-de-rescis%C3%A3o-n%C3%A3o-s%C3%A3o-contabilizadas-GPEM110
---

**Dúvida**  
Verbas de rescisão não são contabilizadas  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Para contabilização das verbas de rescisão é obrigatório que no cadastro de verbas exista amarração com lançamento padrão.

Visto isso, e considerando que outros valores de rescisão são apresentados na contabilização, será necessário verificar se ocorreu a integração corretamente.

Acesse **Relatórios-> Periódicos ->Folha de pagamento** e verifique se os valores da rescisão são apresentados no relatório. Em caso negativo, se a folha de pagamento estiver aberta, siga o seguinte procedimento:

1) Acesse Miscelânea -> Cálculos -> Integrações;  
2) Cancele a integração do roteiro RES;  
3) refaça o processo de integração do roteiro RES;  
4) Verifique se os valores são apresentados na folha de pagamento;  
5)  Refaça o processo de contabilização.  
  
Caso já tenha realizado  o fechamento da folha de pagamento, será necessário solicitar um analista in loco através  do seu executivo de contas TOTVS, uma vez que este atendimento é realizado somente através de consultoria.

 Essa **ação** deve ser **selecionada** e **retirada** **manualmente** somente quando for necessário **Criar** ou **Ajustar** um **Artigo** na Central de Atendimento (Zendesk).  
  
Servirá para que possamos **contabilizar corretamente o tempo gasto** nesse processo e sermos mais assertivos na **criação das escalas das equipes** utilizando a ferramenta de *Workforce*.]
