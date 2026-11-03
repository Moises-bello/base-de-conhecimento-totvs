---
article_id: 20985439519511
category: Financeiro - Reinf
content_hash: 687e4995f7bcc194238e6678b325fe81e92b1436f87cd2ded8a46d119110dad0
fetched_at: '2026-06-28T22:37:51.864003+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Títulos sem
  impostos com campo FKW_TPIMP=SEMIMP
type: support-article
updated_at: '2024-12-19T11:46:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20985439519511-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-T%C3%ADtulos-sem-impostos-com-campo-FKW-TPIMP-SEMIMP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20986373763351) Tempo aproximado para leitura: 00:08:00 min

**Dúvida**

Como criar títulos isentos de impostos e enviar para o reinf?

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Reinf -  A partir da versão 12.1.33

**Solução**

Para a geração dos títulos isentos de impostos no Reinf, é imprescindível incluir no título a natureza de rendimento isenta.

Quando no título possuir a natureza de rendimento isenta será gerado na tabela FKW o campo **FKW\_TPIMP=SEMIMP.**  
 **Exemplo de natureza de rendimento:**  
Pagamentos classificados com a **natureza de rendimento** "**10010-Bolsa ao médico residente**" ou "**12001-Lucro e Dividendo**"       
Ao incluir um título no **Financeiro** ou **documento de entrada** sem gerar o cálculo dos impostos, **IRRF** e/ou **PCC**, será gerado na **FKW** um registro referente ao título com o preenchimento do campo **FKW\_TPIMP** **=SEMIMP**, conforme imagem abaixo, indicando que o título não tem impostos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25654364586135)

Após executar o **extrator fiscal** será gerado o **T154** e **T158** com o valor base, mas sem tributos, conforme exemplo a seguir:

|T154|01||F01 01|20240814|0||||||10000|||||||||0|0|0|0|0|0|0|0|0|0||||0||||3||||||||||0|0|0|||||  
|T154AB|1|10000|

|T158|01||F01 01|20240814|0||20240814|01|||  
**|T158AA|16006|10000|2||||||**

**Importante**

Apenas os títulos isentos de impostos que utilizam uma natureza de rendimento válida para **zero impostos** serão incluídos no painel do **TAF**. Caso esteja usando uma natureza que exija impostos, esses **títulos não serão incluídos no painel**.

**Saiba mais**

[Fique por dentro das atualizações Reinf Protheus](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro#Eventos--839875140)

[How To - Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19775578473751)
