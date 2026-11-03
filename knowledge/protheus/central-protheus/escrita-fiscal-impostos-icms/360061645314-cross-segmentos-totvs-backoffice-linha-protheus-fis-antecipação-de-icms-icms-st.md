---
article_id: 360061645314
category: Escrita Fiscal - Impostos - ICMS
content_hash: 8c53030742b8f69d37311283f5bdb0c17659e6602885b2ec66aee1607d48d804
fetched_at: '2026-06-28T22:39:24.278465+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Antecipação de ICMS/
  ICMS-ST - Entrada
type: support-article
updated_at: '2022-10-20T19:54:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061645314-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Antecipa%C3%A7%C3%A3o-de-ICMS-ICMS-ST-Entrada
---

**Dúvida**Como calcular a Antecipação de ICMS/ ICMS-ST na entrada?  
  
**Ambiente**Protheus - Todas as versões  
  
**Solução** **1) Compra para consumo, configurar TES:**

Calcula ICMS = Sim

L. Fiscal ICMS = Diferente de Não

Calc. Dif ICM = Sim

Material de Consumo = Sim

Antecip. ICMS = Sim

**2) Compra para Industrialização ou Comercialização:**

Calcula ICMS = Sim

L. Fiscal ICMS = Diferente de Não

Calc. Dif ICM = Não

Material de Consumo = Não

Antecip. ICMS = Sim

**3) Compra com ICMS-ST:**

Para que o cálculo da Antecipação tributária total (ICMS-ST) seja feito, siga as instruções:

1. No **Livros Fiscais (SIGAFIS)** acesse **Atualizações/** **Cadastro de TES (MATA080)**configure o campo
2. Informe o campo **Antecipação Tribut. ICMS (F4\_ANTICMS)** tratando-se de estabelecimento atacadista, inclusive distribuidor.
3. Para o valor da Antecipação tributária total (ICMS-ST) ser apresentado corretamente na apuração de ICMS-ST, preencha o campo **Solidário na Observação (F4\_OBSSOL)** com **SIM**.
4. Configurar o parâmetro (**MV\_MESANTI**) com **F**.

Para empresas localizadas no Estado de São Paulo (MV\_ESTADO = SP) é aplicada a seguinte regra para cálculo da antecipação:

Na apuração, caso o campo Est Var/Atac (F4\_VARATAC) estiver preenchido com a opção Varejista, o valor TOTAL do ICMS/ST será escriturado na aba Apuração-ICMS conforme abaixo:  
002.12 – Pagamento Antecipado – Art. 277 do RICMS.  
007.99 – Recolhimento Antecipado – Art. 426-A do RICMS.

Na apuração, caso o campo Est Var/Atac (F4\_VARATAC) estiver preenchido como Atacadista, o valor do ICMS/ST será escriturado através da operação aritmética abaixo:

Exemplo:  
Base de Cálculo do Item = 1.000,00  
Valor ICMS\_ST = 121,00  
Alíquota Interna do Produto = 18%  
Alíquota Interestadual do ICMS = 12%  
Valor Antecipado = (Base de Cálculo do Item \* Alíquota Interna do Produto/100) – (Base de Cálculo do Item \* Alíquota Interestadual do ICMS/100)  
Valor Antecipado = (1.000,00 \* 0,18) – (1.000,00 \* 0,12)  
Valor Antecipado = 60,00  
Valor ICMS/ST = (Valor ICMS ST) – Antecipação  
Valor ICMS/ST = 121,00 – 60,00  
Valor ICMS/ST = 61,00

O Valor Antecipado deve ser gerado na coluna Apuração-ICMS conforme abaixo:  
002.12 – Pagamento Antecipado – Art. 277 do RICMS.  
007.99 – Recolhimento Antecipado – Art. 426-A do RICMS.

O Valor ICMS/ST deve ser gerado na coluna Apuração-ST conforme abaixo:

002.99 – Pagamento Antecipado – Art. 277 do RICMS.  
007.99 – Recolhimento Antecipado – Art. 426-A do RICMS.

A operação citada acima é realizada para cada item do documento fiscal, então caso em uma NF possua um item como Atacadista e outro como Varejista, para cada um será aplicada a respectiva regra.

Para os demais Estados, se o campo Est Var/Atac (F4\_VARATAC) estiver preenchido com a opção Atacadista segue abaixo a escrituração no registro de apuração do ICMS Próprio e ICMS ST:  
ICMS Próprio:  
002.12 – Pagamento Antecipado – Art. 277 do RICMS.  
007.99 – Recolhimento Antecipado – Art. 426-A do RICMS.

ICMS ST:  
002.99 – Pagamento Antecipado – Art. 277 do RICMS.  
007.99 – Recolhimento Antecipado – Art. 426-A do RICMS.

Se campo Est Var/Atac (F4\_VARATAC) estiver preenchido com a opção Varejista segue abaixo a escrituração no registro de apuração do ICMS ST:  
002.99 – Pagamento Antecipado – Art. 277 do RICMS.  
007.99 – Recolhimento Antecipado – Art. 426-A do RICMS.

**Para gerar título da Antecipação:**

No documento de Entrada, clicar F12:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102097834/mceclip0.png)

**Assuntos relacionados:**

Antecipação Tributária ICMS ST

<https://tdn.totvs.com/pages/releaseview.action?pageId=616230585>

Documento de Entrada - Geração de ICMS antecipado via documento de entrada.

<https://tdn.totvs.com/pages/releaseview.action?pageId=334341740>

[Apuração de ICMS - MATA953 - Fiscal - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=270894388)

[Orientações Consultoria de Segmentos - TVBZRE - Antecipação tributária do imposto - entrada de mercadoria proveniente de outra UF - SP](https://tdn.totvs.com/pages/viewpage.action?pageId=236596252)
