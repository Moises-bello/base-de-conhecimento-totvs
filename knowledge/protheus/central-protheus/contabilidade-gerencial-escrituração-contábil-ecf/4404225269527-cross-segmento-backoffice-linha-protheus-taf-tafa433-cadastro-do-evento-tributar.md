---
article_id: 4404225269527
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 5b0fc08b576510eb6638a20f50310a2818cb69138b64b1d41bddf1f2c690ae85
fetched_at: '2026-06-28T22:40:48.948739+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - TAF- TAFA433 - Cadastro do Evento
  tributario, BLOCO M e BLOCO N
type: support-article
updated_at: '2025-09-12T14:25:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404225269527-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA433-Cadastro-do-Evento-tributario-BLOCO-M-e-BLOCO-N
---

**Dúvida**TAFA433- Cadastro do Evento tributário, BLOCO M e BLOCO N  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - TAF - Todas as versões

**Solução**

**Requisitos  para gerar os Blocos M e N**

* [CADASTRO, APURAÇÃO E INTEGRAÇÃO COM ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831-MP-SIGACTB-LALUR-LACS-CADASTRO-APURA%C3%87%C3%83O-E-INTEGRA%C3%87%C3%83O-COM-ECF?source=search)
* [ECF LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006910571-MP-SIGACTB-ECF-LALUR-?source=search)
* [ECF - Parâmetros de Integração CTB/TAF](https://centraldeatendimento.totvs.com/hc/pt/articles/360006564072-MP-SIGACTB-ECF-Par%C3%A2metros-de-Integra%C3%A7%C3%A3o-CTB-TAF-)

[Evento Tributário (TAFA433)](https://tdn.totvs.com/pages/releaseview.action?pageId=248578386)

Esse cadastro é muito importante e é usado como base para apuração dos tributos, nele também existem opções como a simulação do calculo dos impostos e cópia de eventos tributário visando facilitar os cadastros [Maiores detalhes.](https://tdn.totvs.com/x/UgHRDg)

Para cadastrar um evento tributário é necessário escolher a Forma de Tributação, neste documento será tratado a tributação de Lucro Real por levantamento de Balanço.

* Evento tributário código 000001- LUCRO REAL (refere-se ao ajuste anual)
* Evento tributário código 000002- Lucro Real, Estimativa por levantamento de Balanço

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24975648609687)

Para Apuração Lucro Real e Levantamento de balanço as abas e opções para preenchimentos são iguais.

**1)** Na aba REGRA TRIBUTÁRIA + BASE DE CALCULO, temos 6 opções para composição da base de calculo.

**REGRA TRIBUTÁRIA + BASE DE CALCULO= BLOCO M300**

**1.1-** REGRA TRIBUTÁRIA + BASE DE CALCULO + **Resultado Operacional** ( Código Grupo 01 )

**1.2-**REGRA TRIBUTÁRIA + BASE DE CALCULO + **Resultado NÃO Operacional** ( Código Grupo 02 )

Os principais campos são: Filial, Conta Contábil, C.C. e código LALUR

O campo Origem aceita apena CONTA CONTÁBIL ANALITICA [Não informar conta sintética](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404263485719-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA433-Posso-informar-conta-sint%C3%A9tica-no-evento-tribut%C3%A1rio)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404225450647)

**1.3-** REGRA TRIBUTÁRIA + BASE DE CALCULO **+ Adições do Lucro** ( Código Grupo 09 )

**1.4-** REGRA TRIBUTÁRIA + BASE DE CALCULO **+ Adições Doações** ( Código Grupo 10 )

**1.5-** REGRA TRIBUTÁRIA + BASE DE CALCULO **+ Exclusão do Lucro** ( Código Grupo 11 )

Os principais campos são: Filial, Conta Contábil, C.C., Efeito Lalur, Código Lalur e Código Parte B.

No relacionamento do Lançamento da **Parte A**:

1 - Com Conta da Parte B

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404371963543)

2 - Com Conta Contábil

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404361128855)

3 – Com Conta da parte B e Conta Contábil

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404371353367)

**1.6-** REGRA TRIBUTÁRIA + BASE DE CALCULO **+ Compensação de prejuízo/Base negativa** ( Código Grupo - Não Possui )

Os principais campos são: % Ded.Comp, Código Limite, Filial, Efeito Lalur, Código Lalur e Código Parte B

O campo Origem aceita somente LALUR- PARTE B

"Compensação de prejuízo/Base negativa" informamos a conta da parte B, código para ficha de reflexo na parte A, o percentual de compensação e qual o limite que o percentual será aplicado.

[COMPENSACAO DE PREJUIZO PARTE B COM REFLEXO NA PARTE A](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037921673-MP-SIGACTB-LALUR-COMPENSA%C3%87%C3%83O-DE-PREJU%C3%8DZO-PARTE-B-COM-REFLEXO-NA-PARTE-A-)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24975632875927)

**2)** Na aba R**EGRA TRIBUTÁRIA + CALCULO DO TRIBUTO= BLOCO N**

**2.1 Adicionais do tributo** ( Código Grupo 16 )

Os principais campos são: Código ECF, Filial, Conta Contábil, CC e Código Parte B

1 - Com Conta da Parte B

Campo TIPO: Somente crédito ou movimentação da conta.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404374070039)

2 - Com Conta Contábil

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404374219671)

Obs. Não é possível vincular a conta contábil com parte B

**2.2 Deduções do tributo** ( Código Grupo 14 )

Os principais campos são: Código ECF, % Ded.Comp, Código Limite, Filial, Conta Contábil, C.C., Efeito Lalur, Evento e Código Parte B

1 - Com Conta da Parte B

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404374437271)**

2 - Com Conta Contábil

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404374780055)

3 – Com Conta da parte B e Conta Contábil

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404374484631)

**2.3 Compensação do tributo** ( Código Grupo 14 )

Os principais campos são: Código ECF, % Ded.Comp, Código Limite, Filial, Conta Contábil, C.C., Efeito Lalur e Código Parte B

1 - Com Conta da Parte B

Campo TIPO: Somente crédito ou movimentação da conta.

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404375058839)

2 - Com Conta Contábil

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404374982167)

3 – Com Conta da parte B e Conta Contábil

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404375127063)

3) Na aba **Lançamento Manual**

Os principais campos são: Código Grupo, Código ECF, Código Lalur, Data, Valor e Tipo.

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404375236119)

obs. A Aba de Lançamento Manual, possui todos os grupos da regra tributária ( exceto o de compensação de prejuízo ou base negativa ).

**Importante!**

* No evento tributário, quando a operação for = **Subtração**, o sistema irá pegar o valor calculado e inverter o sinal (se o resultado for positivo, o resultado final será negativo e vice versa).
* Como podemos visualizar nos itens acima (1 e 2), os únicos grupos que possuem o campo Código ECF são os grupos 14, 15 e 16. Quando o grupo selecionado for alguma dessas 3 opções ( Adicionais, Deduções ou Compensação do Tributo ), a consulta padrão do campo Código ECF apresentará as opções.
* Os grupos 01, 02, 09, 10 e 11 (item 2.1), não possuem o campo código ECF, por esse motivo a consulta padrão não apresenta nenhuma opção.
* Quando o grupo selecionado for alguma dessas  opções: Resultado Contábil Operacional, Resultado Contábil Não Operacional, Adições de Lucro, Adições por Doação e Exclusões do Lucro, a consulta padrão do campo Código Lalur apresentará as opções.

**Saiba mais**

Boletim Técnico TDN: [Evento tributário - TAFA433](https://tdn.totvs.com/pages/releaseview.action?pageId=248578386)

Contas Evento Tributário: [Contas Evento Tributário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404263485719-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA433-Posso-informar-conta-sint%C3%A9tica-no-evento-tribut%C3%A1rio)

Compensação de Prejuízo: [COMPENSACAO DE PREJUIZO PARTE B COM REFLEXO NA PARTE A](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037921673-MP-SIGACTB-LALUR-COMPENSA%C3%87%C3%83O-DE-PREJU%C3%8DZO-PARTE-B-COM-REFLEXO-NA-PARTE-A-)
