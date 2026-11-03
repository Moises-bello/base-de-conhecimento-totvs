---
article_id: 18059555243543
category: RH - Folha de Pagamento
content_hash: e0991524b4819ce6582ca808b69441e91d1e2ab1690860910f104f69669d03c9
fetched_at: '2026-06-28T22:44:14.945269+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Erro validador AUDESP ao importar XML referente
  a Folha Ordinária verbas referente a 1/3 de férias indenizadas pagas na Rescisão
type: support-article
updated_at: '2025-06-13T20:50:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18059555243543-RH-Linha-Protheus-GPE-Erro-validador-AUDESP-ao-importar-XML-referente-a-Folha-Ordin%C3%A1ria-verbas-referente-a-1-3-de-f%C3%A9rias-indenizadas-pagas-na-Rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18059577774615) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Erro validador AUDESP ao importar XML referente a Folha Ordinária, verbas referente a 1/3 de férias indenizadas pagas na Rescisão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18057716804887)  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Ao gerar o XML, a verba de 1/3 de férias indenizadas que transitou na rescisão, estava com o código do tipo de verba remuneratória **123-Férias Indenizadas** informado no campo **RV\_CODREMU**, o qual exige a quantidade de dias de férias de acordo com o *layout* vigente da AUDESP:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18058781111191)

**Solução**Conforme orientação do Tribunal de Contas do Estado de São Paulo, para verbas referente a 1/3 de férias, mesmo que seja indenizada, deve ser utilizado o código de verba remuneratória **106-Férias 1/3**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18058881597335)

Para correção, acesse o cadastro da sua verba referente a 1/3 de férias indenizada, e no campo **Cod Remuner - RV\_CODREMU,** informe o código **106-Férias 1/3**:

Caminho rotina Verbas -Atualizações - Definições Cálculo - Verbas - aba Outros:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18059252133271)

Após o ajuste, gere novamente o XML.

Os códigos do Tipo de Verbas Remuneratórias, disponíveis para serem amarrados as verbas, constam na tabela **S124**:

Atualizações - Definições Cálculo - Manutenção tabelas.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18059322068375)

**Saiba Mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - AUDESP - Como gerar verbas remuneratórias na folha ordinária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058619654-RH-Linha-Protheus-GPE-AUDESP-Como-gerar-verbas-remunerat%C3%B3rias-na-folha-ordin%C3%A1ria)  
[MRH-8278\_DT\_Audesp\_Manutencao\_Geracao\_Dados](https://tdn.totvs.com/display/public/PROT/MRH-8278_DT_Audesp_Manutencao_Geracao_Dados)

[AUDESP - Remuneração](https://www.tce.sp.gov.br/legislacao/comunicado/atualizacao-modulo-remuneracao-fase-iii-sistema-audesp)
