---
article_id: 360025320552
category: esocial - Periódicos
content_hash: 03814d93d67d3e220d817a7916bccdf8188c100c58d38c30a685e449baa3c40a
fetched_at: '2026-06-28T22:47:09.454267+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Pensão Alimentícia na geração do S-1210
type: support-article
updated_at: '2026-01-20T13:10:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025320552-RH-RM-FOP-eSocial-Pens%C3%A3o-Aliment%C3%ADcia-na-gera%C3%A7%C3%A3o-do-S-1210
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20152198979351)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Como configurar o sistema para correta geração das informações de pensão alimentícia (grupo penAlim) na geração do evento S-1210 (S-1.2) ?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.2302.235, 12.1.2306.182, 12.1.2310.116 e superiores.  
  
**Solução**

O grupo **penAlim** representa os beneficiários da **pensão alimentícia** e é composto por três informações:

|  |  |  |
| --- | --- | --- |
| **TAG** | **INFORMAÇÃO** | **ORIGEM NO SISTEMA** |
| **tpRend** | Tipo de Rendimento | Caso o código de incidência tributária da rubrica (codIncIRRF) seja igual a 51 e possua eventos de RRA (código de cálculo CC206 ou CC394) será retornado 18 caso contrário será retornado 11;  Caso o código de incidência tributária da rubrica (codIncIRRF) seja igual a 52 e possua eventos de RRA (código de cálculo CC214 ou CC395) será retornado 18 caso contrário será retornado 12;  Caso o código de incidência tributária da rubrica (codIncIRRF) seja igual a 53 e possua eventos de RRA (código de cálculo CC210, CC396 ou CC397) será retornado 18 caso contrário será retornado 13;  Caso o código de incidência tributária da rubrica (codIncIRRF) seja igual a 54 será retornado 14. |
| **cpfDep** | CPF do Dependente/Beneficiário da pensão alimentícia | Recupera o valor do campo PFDEPEND.CPF informado no cadastro de dependentes |
| **vlrDedPenAlim** | Valor relativo à rendimento tributável correspondente a pagamento de pensão alimentícia | Será feito o somatório do movimento de pensão alimentícia do beneficiário na competência de acordo com o código de incidência tributária da rubrica para o IRRF. |

Para a correção geração do grupo é necessário observar então os seguintes pontos:

* **Cadastro do Dependente**

O dependente deve possui em seu cadastro, aba **Incidências**, o parâmetro **Pensão** selecionado. O sistema **não** irá validar eventuais incidências relacionadas à pensão marcadas em **Outras Incidências**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21863145053719)

Para os dependentes de pensão com o parâmetro supracitado marcado, na aba Identificação será utilizado a informação do campo CPF para geração no S-1210. A informação é **obrigatória** conforme leiaute.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21863145082519)

* **Movimentação da Pensão**

Ainda no cadastro do dependente, anexo **Movimentação da Pensão de Dependentes**, deve haver um registro correspondente ao lançamento efetuado para o funcionário, ou seja, os dados de mês, ano, período, tipo de movimento e valor devem estar de acordo com o lançamento efetuado.

⚠️ O código de cálculo utilizado e o tipo de movimento do movimento precisam ser correspondentes, conforme pode ser verificado na documentação abaixo:

• [Código de Cálculo x Tipo de Movimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036360433)

No **exemplo** abaixo (vide *gif*) temos dois lançamentos diferentes realizados na competência 01/2024:

• Pensão Judicial (CC 13) → R$ 1500 → Pgto 05/02/2024 → Período 1  
• Pensão Participação nos Lucros Informada (CC 321) → R$ 500 → Pgto 05/02/2024 → Período 2

⚠️ Quanto há **fórmula** no evento ou  utilizar um código de cálculo **INFORMADO** (Ex.: Pensão Alimentícia PLR Informada; Pensão Alimentícia Judicial informada), o sistema **não** **alimenta** **automaticamente** o movimento da pensão, devendo este ser informado **manualmente** ou via **importação**.

Após inserir a movimentação da pensão referente ao CC 321, geramos o XML do período de apuração 02/2024, já que a data de pagamento das verbas é Fevereiro/2024. O XML apresentou corretamente um grupo com:

• **tpRend** 11 - Rendimento Mensal → **vlrDedPenAlim** R$ 1500,00  
• **tpRend** 14 - Rendimento Mensal → **vlrDedPenAlim** R$ 500,00

![Pensão_Envelope_XML.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/21863145108375)

**Importante**  
O código de cálculo e a incidência deve ser compatíveis, assim, sugerimos verificar o [mapeamento dos eventos S-1210](https://tdn.totvs.com/display/public/LRM/Evento+S-1210) e o [mapeamento do S-1010](https://tdn.totvs.com/display/public/LRM/Evento+S-1010).  
  
**Saiba mais**  
Para mais informações, acesse:

* [Ao gerar o evento S-1210 ocorre o erro: Não foi encontrado Movimentação da Pensão de Dependente e a informação é obrigatória para o eSocial (S-1.2)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036360433-RH-RM-FOP-eSocial-Ao-gerar-o-evento-S-1210-ocorre-o-erro-N%C3%A3o-foi-encontrado-Movimenta%C3%A7%C3%A3o-da-Pens%C3%A3o-de-Dependente-e-a-informa%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3ria-para-o-eSocial-S-1-2)
