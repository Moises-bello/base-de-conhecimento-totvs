---
article_id: 360026648673
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: 27105f99184ce3d7879a360619cb4f428f99af9760eb1c839909356c7e73d479
fetched_at: '2026-06-28T22:39:47.694465+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - EIC - Como configurar Redução
  de ICMS no EIC
type: support-article
updated_at: '2025-08-08T20:02:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026648673-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-EIC-Como-configurar-Redu%C3%A7%C3%A3o-de-ICMS-no-EIC
---

**Dúvida**Como configurar Redução de ICMS no EIC?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control - Todas as versões

**Solução**

Essa é uma regra de diminuição de tributação que beneficia operações e prestações específicas, reduzindo em determinado percentual o valor que serve para base de cálculo do ICMS.  
  
**Utilizando Carga Tributária Equivalente**  
Base de cálculo do ICMS cheia = R$ 200.000,00  
Percentual a tributar de 12% para 8,80% = 100 / 12% = 8,333333 x 8,80% = 73,333333  
Base de cálculo do ICMS cheia = R$ 200.000,00 x 73,333333% = Base reduzida = R$ 146.666,66  
Valor do ICMS = R$ 146.666,66 x 12% = R$ 17.600,00

**Comprovação do cálculo:**  
Para achar o valor do ICMS, basta multiplicar base cheia pela a carga tributária:  
R$ 200.000,00 x 8,80% = R$ 17.600,00  
Para achar a base de cálculo do ICMS, basta dividir o valor do ICMS pela alíquota da operação:  
R$ 17.600,00 / 12% = R$ 146.666,66

**Aplicando o percentual de Redução na Base de Cálculo**  
Base de cálculo do ICMS cheia = RS 200.000,00  
Percentual de Redução de Base de Cálculo = 26,666666  
Valor de redução da base de cálculo= R$ 200.000,00 x 26,666666= R$ 53.333,33  
Base de cálculo do ICMS cheia = R$ 200.000,00 – R$ 53.333,33  = Base Reduzida = R$ 146.666,67  
Valor do ICMS = R$ 146.666,67 x 12% = R$ 17.600,00

Para redução de ICMS é necessário ter no Cadastro de CFO uma operação de redução onde alguns campos precisam ser configurados:  
**Aliq. ICMS**: Percentual cheio da alíquota de ICMS  
**Car. Tr. Eq**. : Percentual da carga tributária equivalente ao valor de redução ou Red. B.C. : Percentual de redução de ICMS na base de cálculo.  
**ICMS s/ PIS**: ICMS usado na base de cálculo de PIS e COFINS  
  
Utilizando Carga Tributária Equivalente - exemplo

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042187213)

Observações gerais:  
- No cadastro de CFO deve-se usar a carga tributária equivalente ou a redução de ICMS, nunca os dois campos preenchidos juntos.  
- Verifique se o cliente tem o parâmetro MV\_EIC0029 o qual faz o cálculo do ICMS Reduzido de forma que o valor a integrar a própria base de cálculo seja obtido a partir a alíquota de ICMS normal ou da Alíquota reduzida conforme a parametrização. Desta forma, o cálculo do ICMS Reduzido por carga tributária equivalente fica flexível à legislação fiscal que vigora sobre cada tipo de mercadoria importada.

**Observação**  
O **ICMS ST** é diferente do ICMS de importação que enviamos para a pré-nota no momento do recebimento de importação. O fato gerador do mesmo é a transferência da mercadoria para outro estado, ou seja, esta ocorrendo em território nacional. Desta forma, é necessário verificar a configuração da TES para realizar este tratamento no momento da classificação da Nota Fiscal, com a equipe Fiscal.

**Saiba mais:**

**[C.F.O. (EICOP100 - SIGAEIC)](https://tdn.totvs.com/pages/releaseview.action?pageId=306858507)**

**[Criar campo configuração da redução da base do ICMS no cadastro de CFOP](https://tdn.totvs.com/pages/releaseview.action?pageId=725727891)**

**[Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Divergência de Nota Fiscal de Importação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021393491-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Diverg%C3%AAncia-de-Nota-Fiscal-de-Importa%C3%A7%C3%A3o)**

**[3057376\_DTRADE-49\_DT\_Cálculo do FECP (Fundo Estadual de Combate à Pobreza e às Desigualdades Sociais) no ICMS](https://tdn.totvs.com/pages/releaseview.action?pageId=267801906)**

**[How To | MP - SIGAEIC Recebimento de Import. ICMS Redução de base](https://youtu.be/w-JyYIgFGnM)**

**[How To | MP-SIGAEIC - Recebimento de Importação - ICMS](https://www.youtube.com/watch?v=gz8DbzxExH4&ab_channel=TOTVSSolu%C3%A7%C3%B5es)**

**[How To | MP - SIGAEIC - Recebimento de Importação ICMS Parâmetros](https://www.youtube.com/watch?v=CNZHyyEw7sk&ab_channel=TOTVSSolu%C3%A7%C3%B5es)**

**[How To MP-SIGAEIC - Recebimento de Importação - EICDI154](https://www.youtube.com/watch?v=P6JICIwDHJs&ab_channel=TOTVSSolu%C3%A7%C3%B5es)**
