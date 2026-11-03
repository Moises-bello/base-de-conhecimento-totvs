---
article_id: 12128731487511
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: ea684ec8e68acdbe2dd31727640f96a72bd3625927025cb878566c8340da3cf3
fetched_at: '2026-06-28T22:42:02.309250+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Conceito da Regra de Cálculo da FISA116.
type: support-article
updated_at: '2023-02-16T13:08:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12128731487511-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Conceito-da-Regra-de-C%C3%A1lculo-da-FISA116
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00**:05:00 min** **Dúvida**Qual o conceito da regra de cálculo aplicada na FISA116?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

A base de cálculo será calculada em função da regra selecionada pelo usuário, porém a alíquota interna será gerada da mesma forma em todas as regras, considerando alíquota informada no cadastro de produto **Aliq. ICMS -** **B1\_PICM**, ou então a do parâmetro **MV\_ICMPAD** caso o campo **Aliq. ICMS-** **B1\_PICM** estiver zerado.

#### **Regra 1- Média Ponderada da Base de ICMS ST**

#### Esta regra basicamente irá fazer a média ponderada da base de cálculo do ICMS ST das últimas aquisições do produto processado, considerando a quantidade em estoque, ou seja, se houver 100 unidades do produto em estoque, então deverão ser consideradas tantas notas fiscais necessárias para compor a quantidade de 100 unidades, e então fazer a média ponderada: **Base de cálculo unitária = Somatório da Base de Cálculo ICMS ST / Quantidade em estoque**

Caso a Pergunta *Detalha por CST*esteja selecionada com a Opção "Sim", a Base de Cálculo Unitária irá considerar de forma proporcional o somatório da Base de Cálculo ICMS ST por CST do Produto contido no Documento de Entrada.

#### **Regra 2 -Custo Médio com MVA**

Nesta regra o cálculo será feito considerando o valor do custo médio já calculado pelo estoque, devendo somente aplicar o MVA. Então ficará da seguinte maneira:  
**Base de cálculo unitária = Valor do Custo Médio \* (1 + (MVA do produto / 100) )**  
Lembrando que o MVA poderá ser informado nos cadastros de Produto, Exceção Fiscal e UFxUF, porém não conseguimos obter o MVA destes cadastros, por exemplo se o MVA for definido na Exceção Fiscal, não conseguiremos posicionar na linha correta somente com código de produto, não podemos utilizar MVA gravados na nota, pois é o valor utilizado na época, pode ter sido alterado, além do cenário da exclusão do ST, os cadastros não terão mais o MVA preenchido. Por este motivo para esta regra de cálculo o usuário deverá informar manualmente o valor do MVA vigente após o processamento do do inventario.

#### **Regra 3 -Preço + seguro + frete – IPI** Já para esta regra, a base de cálculo será obtida pelo somatório do valor do preço + seguro + frete – IPI das últimas aquisições do produto. As notas de aquisições a serem consideradas deverão ser as mais recentes, e as notas deverão ser suficientes para compor a quantidade informada em estoque, ou seja, se houver 100 unidades do produto em estoque, então deverão ser consideradas tantas notas fiscais necessárias para compor a quantidade de 100 unidades, e então fazer a média ponderada, já que a base de cálculo é unitária. **Base de Cálculo unitária = (Somatório do preço de aquisição + seguro + frete – IPI) / Quantidade em estoque**

Caso a Pergunta **Detalha por CST** esteja selecionada com a Opção "Sim", a Base de Cálculo Unitária irá considerar de forma proporcional o somatório do Preço de aquisição + seguro + frete - IPI por CST do Produto contido no Documento de Entrada.

#### **Regra 4 -Valor definido através de legislação específica**

Esta regra será aplicada para as situações onde a base de cálculo unitária deverá ser definida através de valores publicados na legislação que trata deste produto no regime de ST, que podem ser diversas legislações de diversos produtos variando ainda por Estado, além de poderem ser alteradas, ficando assim inviável realizar o mapeamento destas informações no sistema. Por este motivo, quando selecionada esta regra, a rotina irá preencher somente o CST de ICMS e alíquota interna do produto, ficando por conta do usuário informar o valor da base de cálculo unitária da legislação específica.

#### **Regra 5-Média ponderada da base de ICMS ST rec. anteriormente**

Esta regra basicamente irá fazer a média ponderada da base de cálculo do ICMS ST das últimas aquisições do produto processado, considerando a quantidade em estoque, ou seja, se houver 100 unidades do produto em estoque, então deverão ser consideradas tantas notas fiscais necessárias para compor a quantidade de 100 unidades, e então fazer a média ponderada:  
**Base de cálculo unitária = Somatório da Base de Cálculo ICMS ST / Quantidade em estoque**  
  
**Importante**

Esta regra considera apenas produtos cujo classificação fiscal de estoque (B1\_CLASFIS) seja**60 - Recolhido anteriormente**

Documentação complementar;

<https://tdn.totvs.com/pages/releaseview.action?pageId=702825120#SPDFISComposi%C3%A7%C3%A3odevalorespararegistroH020doarquivomagn%C3%A9ticoSPEDFiscal-M%C3%A9diaPonderadadaBasedeICMSST>
