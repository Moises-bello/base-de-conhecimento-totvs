---
article_id: 360014264292
category: Ativo Fixo - Valor recuperável
content_hash: 1458b84c9b028912f9a192d44715e2b607532e0303e41e2df96ac8033339acd9
fetched_at: '2026-06-28T22:41:53.636619+00:00'
product: protheus
section_id: 1500001536001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ATFA012 - ATFA380 Valor recuperável
type: support-article
updated_at: '2021-12-06T13:02:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014264292-Cross-Segmento-Backoffice-Linha-Protheus-ATFA012-ATFA380-Valor-recuper%C3%A1vel
---

**Dúvida**Rotina de Valor recuperável no ativo fixo   
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – A partir da versão 11.80  
  
  
**Solução**

No módulo de Ativo Fixo o ganho ou perda referente a avaliação de ativo com base no valor justo, será controlado através do ativo tipo 10 ou 12.

No exemplo a seguir temos um bem tipo 12 que trata o valor justo do bem e que teve um laudo que prevê um valor residual menor.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411253518359/mceclip2.png)

**Procedimentos para Utilização**

1. Acesse o Ativo Fixo e selecione as opções **Miscelâneas / Acertos / Valor Recuperável (ATFA380)**.

Clique na opção **Incluir**, para criar a simulação de redução ao valor recuperável.

2. Será apresentada a tela com o objetivo da rotina. Clique em **Avançar**.
3. Informe os dados para a simulação e clique em **Avançar**.
4. Informe os parâmetros e clique em **Avançar**.
5. Será exibida a tela com os dados informados para a simulação.
6. Caso seja necessário, os campos **Valor** e **Taxa** podem ser alteados. Clique em **Avançar**.
7. Em seguida, marque a opção **Efetivar** e clique no botão **Finalizar**.
8. Ao final do processamento é exibido o tipo do ativo gerado pela rotina, de acordo com o tipo definido no parâmetro MV\_ATFTIOA:

10-Depreciação Gerencial com Método Linear.

12- Valor Recuperável do Ativo.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411262411159/mceclip5.png)

Analisando a SN4 podemos ver que o bem tipo 12 com valor residual antigo será baixado (n4\_motivo= 08) e um novo tipo com valor atual será incluído.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411262605335/mceclip6.png)

E no cadastro do bem (SN3) o tipo 12 anterior ficará baixado e permanecerá visível para histórico.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411254456727/mceclip7.png)

**Procedimentos para Configuração**

1. Acesse o **Configurador (SIGACFG)**, opção **Ambientes/Cadastros/Parâmetros (CFGX017)** e configure os parâmetros a seguir: -

|  |  |
| --- | --- |
| Nome da Variável | MV\_ATFMTHR |
| Tipo | Numérico |
| Descrição | Número de processo (threads) a ser utilizado no cálculo do valor recuperável do ativo (ATFA380).  Mínimo: 1 ou Máximo: 15 |
| Valor Padrão | 1 |

|  |  |
| --- | --- |
| Nome da Variável | MV\_ATFTIOA |
| Tipo | Caractere |
| Descrição | Tipo do ativo a ser gerado pela rotina Valor Recuperável do Ativo.  10-Depreciação Gerencial com Método Linear; ou  12- Valor Recuperável do Ativo. |
| Valor Padrão | 12 |

2. Agora, na opção **Ambientes/Cadastro/Menu (CFGX013)**, inclua a nova opção de menu do Ativo Fixo, conforme instruções a seguir:

|  |  |
| --- | --- |
| Menu | Miscelâneas |
| Submenu | Acertos |
| Nome da rotina | Valor Recuperável |
| Programa | ATFA380 |
| Módulo | SIGAATF |
| Tipo | Função Protheus |
| Tabelas | SNI/SN1/SN2/SN3/SN4/SN5/SN6/SNA/SNJ |

**Informações Técnicas**

|  |  |
| --- | --- |
| Tabelas Utilizadas | SNI – Simulação Valor Recuperável, SNJ – Movimento Valor Recuperável |

**Observações**

***Importante:***

A tecnologia *Thread* (múltiplos processos) está disponível somente para ambientes que utilizam banco de dados relacional, por intermédio do TopConnect / Totvs DbAcess. Em ambientes ADS será considerado um único processamento.

**Saiba mais**

[CPC - Impacto da convergência contábil IFRS/CPC nos módulos da Controladoria Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=6068474)

[Metodos de Calculo de depreciação](http://tdn.totvs.com.br/pages/releaseview.action?pageId=6067612)

[Tipos de ativo N3\_TIPO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035878114-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Tipos-de-ativo-campo-N3-TIPO-)

[IFRS/CPC no Ativo fixo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411126012439-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-IFRS-CPC-no-Ativo-fixo?source=search)

<https://tdn.totvs.com/pages/releaseview.action?pageId=110428964>
