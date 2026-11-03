---
article_id: 360011717052
category: SIGAEST - MOVIMENTAÇÕES
content_hash: a9e2f35e838b307aa1abe4340c940995eef9d4cd8133b29c6ba22f2981629f76
fetched_at: '2026-06-28T22:38:54.114506+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 -
  Transferência entre Filiais utilizando o parâmetro MV_FILTRF
type: support-article
updated_at: '2025-12-19T15:01:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011717052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-utilizando-o-par%C3%A2metro-MV-FILTRF
---

**Dúvida**  
Como configurar e utilizar a rotina de Transferência entre Filiais (MATA310/MATA311) com o parâmetro MV\_FILTRF?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Neste artigo abordaremos as configurações e o processo prático de uma Transferência entre Filiais usando as rotinas facilitadoras.

**Tópicos**

1. [Configurações necessárias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011717052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-utilizando-o-par%C3%A2metro-MV-FILTRF#:~:text=1.%20Configura%C3%A7%C3%B5es%20necess%C3%A1rias%3A)
2. [Processo usando a rotina MATA310](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011717052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-utilizando-o-par%C3%A2metro-MV-FILTRF#:~:text=2.%20Processo%20usando%20a%20rotina%20MATA310)
3. [Processo usando a rotina MATA311](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011717052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-utilizando-o-par%C3%A2metro-MV-FILTRF#:~:text=3.%20Processo%20usando%20a%20rotina%20MATA311)
4. [Outros Assuntos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011717052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-utilizando-o-par%C3%A2metro-MV-FILTRF#:~:text=MATA410%20e%20MATA103.-,4.%20Outros%20Assuntos,-Existe%20a%20possibilidade)

**Maneira de automatização com o uso das rotinas:**

Sera gerado o **Documento de Saída** na filial de origem e depois o **Documento de Entrada** ou **Pré-nota** de Entrada na filial de destino, de acordo com a Classificação ou não selecionada.

Dessa forma, as rotinas visam agilizar o processo e reduzir a necessidade de lançamentos manuais.

**Procedimento de Estorno/Exclusão**

Por se tratarem de funcionalidades facilitadoras, **MATA310/MATA311 não possuem a opção de "Outras Ações" -> "Estorno"**. Ou seja, essas rotinas **não realizam estornos ou exclusões automaticamente**, pois seu escopo é apenas a geração dos documentos de forma automatizada.

Para proceder com a exclusão ou estorno, é necessário realizar a operação diretamente nas rotinas originais correspondentes:

* **Documento de Saída** na filial de origem.(MATA410)
* **Documento de Entrada** ou **Pré-nota** de Entrada na filial de destino.(MATA103/MATA140)

Curiosidade:

Entendi sua necessidade, mas no caso não ha como. Pedido em aberto, não gera movimentação(SD2). A premissa da transferencia entre as filiais, é você efetuar o documento de entrada, com os dados da nota de saida faturada. Minha sugestão, é avaliação dos PE's disponiveis, talvez o seu analista Desenvolvedor possa verificar um deles sobre a geração de pedido <https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003854082-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Pontos-de-entrada-da-rotina-Transfer%C3%AAncia-entre-Filiais>, por exemplo o PE - M310PPED - Ponto que permite fazer tratamentos após a inclusão do pedido de vendas da transferência de filiais.

**A quem possa interessar:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 - Pontos de entrada da rotina Transferência entre Filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003854082-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Pontos-de-entrada-da-rotina-Transfer%C3%AAncia-entre-Filiais)

**1. Configurações necessárias:**

**Habilitar o parâmetro MV\_FILTRF para Transferência:**

**![mvfiltrf.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29664980229399)**

**1 - Configuração de TES**:  
Devera existir a TES de entrada e SAIDA nas duas filiais com o mesmo código. habilitando o campo **"Trans Filial" (F4\_TRANFIL) como SIM.**

![tesfiliais.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29664934886807)![tranfil.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29664980233495)

**2 - Cadastrando Fornecedores**  
Gerar um cadastro de Fornecedor em cada filial com o campo **"Fil. Transf"**, que informa para qual filial será realizada a transferência preenchido vice e versa.

![filtransf.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29664980235415)

**3 - Cadastrando Clientes**  
Gerar um Cadastro de Cliente em cada filial com o campo **"Fil. Transf"** que informa para qual filial será realizada a transferência.

![filtransfcli.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29664980236311)

**2. Processo usando a rotina MATA310**

**1-  Acessar à rotina MATA310 e efetue a parametrização de acordo sua necessidade, abaixo segue parametrização que sera utilizada nesse exemplo**

|  |  |
| --- | --- |
| **De  produto ?** | 0099 |
| **Ate produto ?** | 0099 |
| **De filial ?** | 01010001 |
| **Ate filial ?** | 01010002 |
| **De  armazem ?** |  |
| **Ate armazem ?** | ZZ |
| **De tipo ?** |  |
| **Ate tipo ?** | ZZ |
| **De  grupo ?** |  |
| **Ate grupo ?** | ZZZZ |
| **Filtra produtos por categ. ?** | Não |
| **Quebra informacoes ?** | Por Produto |
| **TES para notas de saida ?** | 950 |
| **Gera documento de entrada ?** | Classificado |
| **TES para notas de entrada ?** | 450 |
| **Condicao de pagamento ?** | 001 |
| **Considera como preco no PV ?** | C Unitario |
| **Dados da origem ?** | Todas filiais |
| **Utilizar Saldo de Terceiros ?** | Não |
| **Espécie documento de entrada ?** | NF |
| **Descrição de produtos ?** | Não |
| **TP Oper. Saida ?** |  |
| **TP Oper. Entrada ?** |  |
| **Informa prod. manualmente ?** | Não |
| **Abre tela da nota de entrada ?** | Não |

**2 - Selecione o item desejado, em ambas as filiais, e então clique em "Ações Relacionadas", e entre em "Relação", digitando a quantidade que deseja transferir e confirme;**

![mta1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29664934897431)

![mta2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29664934901271)

**3 - Veja que o saldo esta distribuido, após isso, clique em confirmar, o sistema irá gerar o número da transferência e fechará a rotina.**

![mta3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29664980244119)

![mta4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29664980247191)

**4 - Valide se vai precisar usar alguma parametrização adicional nessa etapa, caso não basta clicar em ok**

![mta5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29664980248215)

**5 - Para confirmar se realmente foi realizado o movimento, acesse à rotina de Pedido de Vendas (MATA410) e lá vai estar como último registro o movimento realizado:**

![mta6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29664980250135)

**6 - Para conferir se a entrega foi feita, vá na filial de recebimento e entre na rotina MATA103 (Documento de Entrada) e lá vai estar registrado o movimento (dependendo da configuração da empresa será necessário classificar a nota para que o saldo fique disponível para uso).**

![MTA7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29664934929943)

**3. Processo usando a rotina MATA311**

**1-  Acessar à rotina MATA311 e efetue a parametrização de acordo sua necessidade, abaixo segue parametrização que sera utilizada nesse exemplo:**

* Preenchido os campos:
* Especie NF
* Produto origem e destino
* Armazém origem e destino
* Filial de Destino
* Tes de saída e entrada configuradas

**2-  Após preenchido, clique em confirmar, sera apresentado o documento para efetivar, clique em outras ações e efetivar.**

![mta9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29664980256919)

![mta10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29664934933015)

**3-  Após a efetivação, sera aberto novamente a tela de conclusão, basta clicar em confirmar e seguir com a validação da transferencia, com a mesma consulta através das rotinas MATA410 e MATA103.**

![mta11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29664934933911)

**4. Outros Assuntos**

**Existe a possibilidade de gerar a transferência sem o pedido de venda ser faturado?**

*R: No padrão não, Pedido em aberto, não gera movimentação(SD2). A premissa da transferencia entre as filiais, é você efetuar o documento de entrada, com os dados da nota de saida faturada. Uma dica é avaliar essa possibilidade no* [*PE - M310PPED*](https://tdn.totvs.com/x/H0ICE)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como alterar o custo de entrada na transferência entre filiais*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4638410759319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-alterar-o-custo-de-entrada-na-transfer%C3%AAncia-entre-filiais)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST – Custo nas transferências entre filiais*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024874171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Custo-nas-transfer%C3%AAncias-entre-filiais)

**Ao fazer** **transferência entre filiais, com o campo F4\_TRANFIL = NÃO na TES de entrada e na TES de saída o campo F4\_TRANFIL  = SIM, ao efetivar a transferência apresenta uma mensagem " A TES XX está configurada para ser utilizada no processo de transferência entre filiais. Deseja continuar o processo?" como avaliar nesse caso mesmo não pode ter o campo F4\_TRANFIL diferente de 2, na TES de entrada, pois a nota de entrada precisa agregar um custo diferente da sua origem.** **?**

*R:* A mensagem de alerta exibida atualmente não pode ser inibida, contudo, *ela não impede a continuidade do processo*  para a geração de documentos fiscais utilizando uma TES com o campo 'Trans Filial' (F4\_TRANFIL) configurado como '2'.

A mensagem — *'A TES XX está configurada para ser utilizada no processo de transferência entre filiais. Deseja continuar o processo?'* — é um alerta preventivo. Sua finalidade é evitar divergências no custo da mercadoria nos documentos fiscais, cabendo ao usuário a decisão de prosseguir ou não com a operação.

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310 / MATA311 - Como configurar a Transferência entre Filiais (MATA310 / MATA311) no Protheus?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-a-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus-?source=search)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 - Como definir o Preço de Venda do Pedido de Venda derivado do processo de Transferência entre Filiais ?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021390332-MP-SIGAEST-Custo-do-produto-derivado-do-processo-de-transfer%C3%AAncia-via-MATA311-)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
