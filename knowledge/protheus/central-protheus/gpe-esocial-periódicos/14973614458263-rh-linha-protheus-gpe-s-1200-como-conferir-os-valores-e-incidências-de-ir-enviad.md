---
article_id: 14973614458263
category: GPE - eSocial - Periódicos
content_hash: 121bd0096f641115c5d389a9ff7211451dc86e29dd3914fa7c6cfa0b9b3c0589
fetched_at: '2026-06-28T22:45:07.462665+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - S-1200 - Como conferir os valores e incidências
  de IR enviadas ao esocial no evento S-1200
type: support-article
updated_at: '2026-06-26T19:46:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14973614458263-RH-Linha-Protheus-GPE-S-1200-Como-conferir-os-valores-e-incid%C3%AAncias-de-IR-enviadas-ao-esocial-no-evento-S-1200
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15280319289879) Tempo aproximado para leitura: **00:06:00** **Dúvida**Como conferir os valores e incidências de IR enviadas ao esocial no evento S-1200?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Ao consultar o portal do eSocial **por trabalhador**, podemos verificar que é **separado por incidência e código de receita, de acordo com o período selecionado.**  
Dessa maneira, devemos gerar o **[relatório do evento S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-GPE-antes-de-integrar-o-evento-peri%C3%B3dico-para-o-TAF)** para analisarmos por funcionário o que estamos enviando com as **incidências** apresentadas no portal, como no exemplo abaixo por trabalhador incidências 11, 31, 7900, entre outras.  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15097889884183)**Abaixo exemplo de como é gerado o relatório do evento S-1200, podemos analisar o **valor gerado**, qual **identificador de cálculo**, a **data de pagamento de cada ideDmDev** e o principal, a **incidência de IR para esocial**.   
Importante ressaltar que a **parametrização do sistema deve ser a mesma do portal eSocial,** pois o eSocial utilizará as incidências das rubricas que enviamos no evento S-1010.  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/14973445682455)**  
  
O eSocial, diferentemente do que faz em relação à contribuição previdenciária, não efetua cálculo do valor devido e apenas consolida o valor informado pelo declarante como efetivamente retido a título de Imposto de Renda. Esse valor é apurado através das rubricas cujo {codIncIRRF} seja igual a [31, 32, 33 34 e 35].  
  
Ao efetuar alteração de verbas, devemos **enviar o S-1010 com competência anterior a do evento S-1200**.  
  
Abaixo retiramos do leiaute do esocial como o governo demostra os valores totalizados de IR por pagamento (FER/FOL/ADI) dentro do mês selecionado.   
Por exemplo para 7900 o esocial vai somar todas as rubricas que vocês enviaram no S-1010 com incidência 9 para IR. Gere o **relatório dos meses que deseja analisar** conforme a documentação acima para analisar todas as verbas que no Protheus contém essa incidência 9 por exemplo, e veja se no esocial a verba está com a mesma parametrização.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15098066855831)  
**Verifique que os descontos que enviamos para o esocial com incidência 31 e 33 o eSocial soma os valores no código 31.**  
  
[Acesse: https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/index.html#evtIrrfBenef](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/index.html#evtIrrfBenef)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15097999047447)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
**[RH - Linha Protheus - GPE - eSocial - Instrução Normativa RFB Nº 2.137, DE 21 DE MARÇO DE 2023 relativos ao IRRF na DCTFWeb](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13403244147735)**  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Diferença entre Rendimento não tributável (7950) e verba transitada pela folha de pagamento (7900)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14230504342935)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus)
