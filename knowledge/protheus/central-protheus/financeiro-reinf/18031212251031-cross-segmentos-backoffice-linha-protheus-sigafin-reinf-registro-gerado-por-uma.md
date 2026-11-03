---
article_id: 18031212251031
category: Financeiro - Reinf
content_hash: 4672a8f49623bf32f104053231d54a99b3911c506e7fbec1ea94b224b5512397
fetched_at: '2026-06-28T22:37:51.736146+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: ' Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Registro
  gerado por uma liquidação (FINA565) ou Fatura (FINA290) como será enviado'
type: support-article
updated_at: '2023-12-28T08:55:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18031212251031--Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Registro-gerado-por-uma-liquida%C3%A7%C3%A3o-FINA565-ou-Fatura-FINA290-como-ser%C3%A1-enviado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18031195398935) Tempo aproximado para leitura: **00:07:00 min** **Dúvida**  
Quando for gerado uma Liquidação (FINA565) ou Fatura (FINA290) de títulos a pagar tendo impostos com fato gerador no pagamento, como fica os tributos quando houver essa renegociação ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33  
  
**Solução**

* Caso o(s) título(s) de origem da **Fatura** (**FINA290**) ou **Liquidação** (**FINA565**) tenham **IR e/ou PCC na Emissão**, esses tributos não serão migrados para o(s) novo(s) título(s) gerado(s) pela renegociação. Portanto, serão integrados ao **TAF** vinculados aos títulos de origem da **fatura/liquidação**.
  + No caso dos impostos **PIS/COFINS/CSLL**, quanto estiverem configurados na emissão (**MV\_BX10925=2**), como o fato gerador para a **REINF** é o pagamento, serão integrados ao **TAF** após a **baixa dos títulos** (baixados pela fatura/liquidação);  
      
    Exemplo:  
    Inclusão do título, retenção dos impostos e gravação da tabela impostos X natureza de rendimento ( FKW ): 16/08/2023  
    Geração da Fatura: 18/09/2023  
    Na rotina do **Extrator Fiscal**, aba **Geração** configuração dos campos **Date de**: 16/08/2023 **Data até**: 18/09/2023
* Caso o(s) título(s) de origem da **Fatura** (**FINA290**) ou **Liquidação** (**FINA565**) tenham **IR e/ou PCC na Baixa**, e na renegociação tenha sido vinculada uma **Natureza Financeira** (**SED**) com as mesmas características de impostos, a retenção será migrada para os títulos gerados pela renegociação (novos), sendo enviado ao **TAF** somente após esses **títulos serem baixados**;
  + Nesse caso, os dados da **FKW** do(s) título(s) de origem serão migrados para a **FKW** dos títulos novos da renegociação, considerado os valores proporcionalizados pelos novos valores e as **naturezas de rendimento** vinculadas ao(s) título(s) de origem;
  + Caso a **Natureza de Rendimento** não tenha sido vinculada aos títulos de origem, o vinculo poderá ocorrer através do botão "**Complemento de Título**" na rotina de **Contas a Pagar** (**FINA050**);
* Se a renegociação for gerada com uma **Natureza Financeira** (**SED**) sem **IR/PCC**, sendo que o título de origem possuía **IR/PCC** na **baixa**, não haverá a migração dos dados de **natureza de** **rendimento** para a **FKW**, já que não haverá a geração do **TX**. Nessa situação a retenção não ocorrerá, e portanto não serão enviados os tributos ao **TAF**;

**Saiba mais:**  
Para saber mais sobre as gravações das tabelas auxiliares do REINF bloco 40 (FKW/FKY) em relação ao processo de negociação, consulte: [Gravação dos Impostos x Natureza de rendimentos](https://tdn.totvs.com/pages/viewpage.action?pageId=728637277)  
[Fique por dentro das atualizações Reinf Protheus](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro#Eventos--839875140)  
[How To - Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19775578473751)
