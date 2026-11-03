---
article_id: 360042763413
category: Faturamento - Cadastros
content_hash: 8cd147e41646d8bd956b71bf8624e38328c7cfd36816113fed938bd378d483a8
fetched_at: '2026-06-28T22:38:35.522751+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Error.log
  ao clicar na lupa de seleção do campo: A1_CODSEG - type mismatch on compare  on
  { || &cFilter }(FWBRWTABLE.PRW)'
type: support-article
updated_at: '2025-01-10T20:20:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042763413-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Error-log-ao-clicar-na-lupa-de-sele%C3%A7%C3%A3o-do-campo-A1-CODSEG-type-mismatch-on-compare-on-cFilter-FWBRWTABLE-PRW
---

**Dúvida**

Quando clica na lupa de seleção do campo: **A1\_CODSEG** o sistema gera error.log:  
*type mismatch on compare on { || &cFilter }(FWBRWTABLE.PRW)*  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice(Linha Protheus) - Faturamento(SIGAFAT) –  A partir da versão 12.  
  
**Solução**

Neste caso existe duas soluções para o processo:  
1. Verificar a SXB Consulta Padrão - Prefixo AOV e o campo: XB\_CONTEM se contém a validação:

AOV->AOV\_MSBLQL <>'1';

Prefixo AOVP e o campo : XB\_CONTEM se contém a validação: AOV->AOV\_PRINC == '1' .And. AOV->AOV\_MSBLQL <> '1' 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409715499543/mceclip0.png)

2. Realizar a Limpeza de Profile do Usuário e abaixo consta a documentação, conforme documentação: **[Manutenção de Perfil de Usuário (Profile)](https://tdn.totvs.com/pages/releaseview.action?pageId=271165124)**

**Obs**: Duvidas sobre processo do profile, verificar diretamente com a equipe de Framework.  

**Importante:  Este mesmo erro pode ocorrer com o cadastro de prospect ou suspect ao tentar selecionar o segmento, o procedimento acima também é indicado a estes cadastros para ajuste do problema.**
