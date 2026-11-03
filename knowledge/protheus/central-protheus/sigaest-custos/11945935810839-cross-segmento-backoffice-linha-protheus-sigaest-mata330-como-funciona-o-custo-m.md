---
article_id: 11945935810839
category: SIGAEST - CUSTOS
content_hash: 3142d814d294a73229522e35ec104747ac52f9bc8e80e3df107519283435f345
fetched_at: '2026-06-28T22:39:02.125143+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como funciona
  o Custo Médio por Empresa?
type: support-article
updated_at: '2025-03-12T12:23:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11945935810839-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-funciona-o-Custo-M%C3%A9dio-por-Empresa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:07:02min**

**Dúvida**  
Como funciona o calculo de custo aglutinado por Empresa?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O recálculo do custo médio possibilita o processamento do custo médio por empresa, permitindo associar o custo das notas de transferência de material ocorridas entre as filiais.

Essa funcionalidade se destina às empresas que possuem mais de uma filial utilizando o mesmo Sistema e que utilizem esta rotina.

O Sistema processa o custo médio das filiais desejadas de uma única vez, permitindo associar o custo das notas de transferência de material ocorridas entre as filiais.

|  |
| --- |
| Help_button**Importante:**       Para que essa opção possa ser utilizada, observe o preenchimento do campo [Trans. Filial](https://tdn.totvs.com/pages/viewpage.action?pageId=338378568), criado para atender esta necessidade, no Cadastro de TES. |

**Exemplo:**

Este exemplo demonstra o processo de recálculo do custo médio padrão e o processo de valorização de documentos de transferência entre as filiais do Sistema.

Para tanto, foram considerados no cálculo:

* o uso de um TES de transferência entre as filiais.
* o CNPJ do cliente da nota fiscal de saída e do CNPJ do fornecedor da nota fiscal de entrada são validados com os dados do arquivo de empresas e filiais (SM0), indicando desta forma a transferência.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11945122022039)

Para existir uma nota fiscal de saída na filial SP e uma nota de entrada na filial MG, realizar a transferência de cem peças do produto X da filial SP para a filial MG.

Com base nas informações fornecidas, acompanhe nos quadros a seguir a exemplificação do recálculo do custo médio padrão representado pelo quadro Modelo Atual Recálculo do CM e do recálculo do custo médio por filiais, valorizando a transferência de documentos, representada pelo quadro Novo modelo Recálculo do CM.

**Modelo Padrão do Recálculo do Custo Médio**

No modelo padrão do recálculo do custo médio, o custo na entrada da nota fiscal de transferência é calculado como uma entrada normal, por meio do valor da nota e do TES utilizado.

A seguir, observe as linhas destacadas para o tipo de documento NFT e seus respectivos custos de entrada em cada filial:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11945504098583)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11945511999639)

**Novo Modelo do Recálculo do Custo Médio**

No novo modelo de recálculo do custo médio, quando ocorre a transferência, o custo da nota fiscal de entrada no destino da transferência será o mesmo que o custo da nota fiscal de saída na origem da transferência.

A seguir, observe as linhas destacadas para o tipo de documento NFT e seus respectivos custos em cada filial:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11945576636055)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11945689762327)

|  |
| --- |
| **Help_buttonObservação:**  Se o parâmetro Cálculo do Custo por estiver configurado com a opção Filial Corrente, o processamento do recálculo do custo médio será com base nas informações da filial corrente do Sistema e terá seu funcionamento padrão inalterado. A diferença ocorre, especificamente, no processo de valorização de documentos de transferência entre filiais, para isto, o parâmetro deverá estar configurado com Todas Filiais ou Selec. Filiais. |

|  |
| --- |
| Help_button**Dica:**  Quando o parâmetro [MV\_CUSFIL](https://tdn.totvs.com/pages/viewpage.action?pageId=312165205) é configurado para utilizar o custo unificado por empresa, a rotina **Recálculo de Custo Médio** recalcula o custo de todas as filiais da empresa corrente e atualiza os campos padrões de fechamento de estoque da tabela**SB2 – Saldos em Estoque**, bem como os campos de fechamento do custo em partes, quando utilizado.  Campos padrões de fechamento do estoque:  Vlr. Final(B2\_VFIM1),Vlr. Fin. 2ª M(B2\_VFIM2),Vlr. Fin. 3ª M(B2\_VFIM3),Vlr. Fin. 4ª M(B2\_VFIM4),Vlr. Fin. 5ª M(B2\_VFIM5),C Unitário(B2\_CM1),Cus. Uni. 2ª. M(B2\_CM2),Cus. Uni. 3ª. M(B2\_CM3),Cus. Uni. 4ª. M(B2\_CM4) e Cus. Uni. 5ª. M(B2\_CM5).  Campos de fechamento do custo em partes:  Custo Final(B2\_CPF) e Custo Unitário(B2\_CP). |

**Exemplo de cálculo do custo unificado por empresa:**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11945994331543)

|  |
| --- |
| Help_button**Importante:**  Com o uso do conceito de custo unificado por empresa, ao processar o recálculo de custo médio, o Sistema sempre considera para o cálculo todas as filiais da empresa corrente, independentemente da seleção do parâmetro **Cálculo de Custos por?**, existente na rotina. |

---

**Aplicação Prática**

Considerando uma empresa que possua duas filiais, como por exemplo, a **filial 01 – São Paulo** e a **filial 02**–**Rio de Janeiro**, com movimentações de estoque, verifique como calcula o custo unificado por empresa.

O parâmetro [MV\_CUSFIL](https://tdn.totvs.com/pages/viewpage.action?pageId=312165205) deve estar configurado com E (custo unificado por empresa).

Na filial 01 - São Paulo foi registrado o documento de entrada **000001/U** com as seguintes características:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11946039052439)

3. Na filial02 -**Rio de Janeiro** foi registrado o documento de entrada **009000/U** com as seguintes características:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11946074838807)

4. Após a execução da rotina **Recálculo de Custo Médio**, o Sistema atualiza o campo **Vlr. Final**(B2\_VFIM1), da tabela **SB2 - Saldo em Estoque**, com o custo unificado. Para verificar o resultado do cálculo, utilize a consulta genérica pelas opções **Consultas+Genéricas.**

**Exemplo do cálculo:**

**Filial 01 - São Paulo**

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11946054434839)

**Filial 02 - Rio de Janeiro**

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11946077159831)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://tdn.totvs.com/pages/releaseview.action?pageId=393356051)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como funciona o Custo Médio Offline por Armazém?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11944424817047)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como funciona o Custo Médio Offline por Filial?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11944742266647)*
