---
article_id: 24481698905751
category: Financeiro - Reinf
content_hash: a0bf13f3e17f32305b11ad7f4a912efab23b98d955541345347c90b7e74bb27c
fetched_at: '2026-06-28T22:37:51.833047+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - IR gerado por
  fundo de investimento é processado pelo Extrator fiscal?
type: support-article
updated_at: '2024-06-27T19:22:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24481698905751-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-IR-gerado-por-fundo-de-investimento-%C3%A9-processado-pelo-Extrator-fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24481698870807) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**IR gerado por fundo de investimento é processado pelo Extrator fiscal?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - REINF - A partir da versão 12.1.33  
  
**Solução**

Os fundos de investimentos são incluídos na rotina **FINA716 - Rotina de aplicação e Empréstimo**, porém o IR gerado por essa rotina não é processado pelo extrator fiscal com isso não é enviado para o **REINF**

Exemplo:

[FAQ - 0014 - Quais dados da serie R-4000 não possuem tratamento no extrator?](https://tdn.totvs.com/pages/viewpage.action?pageId=736166064)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24482408331287)

No entendimento que foi construído o processo do **REINF**, essas retenção do **IR**, são feita pelo banco, logo quem deve enviar para o **REINF**, é o **banco**.

Ao incluir o valor do IR do seu fundo de investimento usando a rotina  **FINA100 - Movimentação Bancária**, essa informação também não será enviada para o **REINF**, pois essa rotina não tem a possibilidade de incluir a **natureza de rendimento**, onde geralmente essa natureza de rendimento é amarrada na inclusão do titulo no momento da inclusão pelo **contas a pagar** e ou **contas a receber** através da opção: **(Outras Ações > Complemento do Título)**.

**Saiba mais:   
[Fique por dentro das atualizações Reinf Protheus](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro#Eventos--839875140)  
[How To - Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19775578473751)**
