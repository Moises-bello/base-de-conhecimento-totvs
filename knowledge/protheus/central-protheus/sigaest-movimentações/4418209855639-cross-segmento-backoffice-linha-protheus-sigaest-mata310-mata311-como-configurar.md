---
article_id: 4418209855639
category: SIGAEST - MOVIMENTAÇÕES
content_hash: d3652935ab5a9ee572af3c02dda2125e5bc8da8a4441feeb2b921b7280a55c9e
fetched_at: '2026-06-28T22:38:54.094135+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310 / MATA311
  - Como configurar ou revisar a configuração da Transferência entre Filiais (MATA310
  / MATA311) no Protheus?
type: support-article
updated_at: '2026-05-06T18:49:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-ou-revisar-a-configura%C3%A7%C3%A3o-da-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus
---

As rotinas MATA310/MATA311 do Protheus facilitam a transferência entre filiais, gerando automaticamente documentos de saída na filial origem e de entrada na filial destino, mas não realizam estornos, que devem ser feitos nas rotinas originais. O processo atualiza pedidos, saldos e documentos, e requer configuração detalhada dos cadastros e parâmetros, com orientações para validar manualmente antes de abrir chamados técnicos.

**Dúvida**  
Como configurar as rotinas de **Transferência entre Filiais (MATA310/MATA311)** no Protheus?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - Todas as versões  
  
**Solução**

**Veja nosso vídeo instrutivo sobre como Configurar a Transferência entre Filiais no Protheus:**

Abaixo também descreveremos de maneira escrita e com prints a configuração

**IMPORTANTE:**

As rotinas **MATA310/MATA311** se tratam apenas um facilitador que gera o Documento de Saída na filial origem**(usa a rotina MATA410)** e Documento de Entrada ou Pré-nota de Entrada na filial de destino**(usa a rotina MATA103)**.

Porém, em caso de exclusão/estorno, as rotinas em si por serem facilitadora, não tem por funcionalidade um "Outras Ações" -> "Estorno".

Ou seja, ela por si só **não estorna**, só gera de maneira automatizada as notas na transferencia.

O estorno/exclusão deve ser feito nas rotinas originais (Documento de Saída e Documento de Entrada/Pré-nota).

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 - Pontos de entrada da rotina Transferência entre Filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003854082-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Pontos-de-entrada-da-rotina-Transfer%C3%AAncia-entre-Filiais)

**OBSERVAÇÃO:** Caso voce esteja ingressando agora no processo de usar a rotina MATA310/MATA311, realizou todas as configurações necessarias, conforme descritas nesse boletim, mas por algum motivo ocorre um erro seja na etapa de gerar o documento de saida, ou de entrada, é extremamente importante que primeiro voce valide diretamente nas rotinas legado o mesmo processo, como?

**PROCESSO MANUAL DE TRANSFERENCIA**

- Acesse o Pedido de Venda da FILIAL DE ORIGEM, e preencha os dados que vai usar na nota de transferencia, fature e então finalize.

- Acesse agora o Documento de entrada da FILIAL DE DESTINO, e preencha os dados iguais da nota da filial de Origem, com a mudança do Cliente por Fornecedor, e tente efetuar a Classificação do Documento de entrada.

Se isso funcionar, as configurações estão corretas, e então pode abrir um ticket para o time "Protheus Estoque Custos", com esses detalhes, informando que o erro ocorre somente nas rotinas MATA310/MATA311, que o processo manual ja foi testado nas rotinas legado.

Se isso não funcionar, então valide em qual momento ocorre o Erro, se for na nota de saida, abra um ticket com o time de "Protheus Faturamento", e se for um erro na classificação do Documento de entrada, abra um ticket com o time "Protheus Compras".

Para facilitar o processo de consulta de saldo em estoque dos produtos e para otimizar a transferência de materiais entre as filias, foi implementada a rotina **“Transferência de Produtos entre Filiais” (MATA310)**, que permite ao usuário consultar os saldos de diversas filiais do sistema em um única tela, de acordo com a parametrização escolhida, e realizar o processo de geração de documentos para transferência de produtos entre as filiais através de uma interface gráfica de fácil utilização.

O processo de transferência de produtos entre filiais atualizará, automaticamente, as tabelas de dados relacionadas aos processos de:

* ***Pedido de Vendas (******Filial Origem******);***
* ***Liberação de Pedidos (******Filial Origem******);***
* ***Documentos de Saída (******Filial Origem******);***
* ***Saldos em Estoque (******Filial Origem*** ***e*** ***Filial Destino******);***
* ***Pré-Nota ou Documento de Entrada (******Filial Destino******).***

A seguir um roteiro de operações para a utilização e configuração desta funcionalidade.

***- Importante:*** Para esse passo a passo ***primeiramente*** altere o parâmetro [**MV\_FILTRF para F**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011717052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-utilizando-o-par%C3%A2metro-MV-FILTRF).

O objetivo deste roteiro **é exemplificar** a transferência de entre duas filiais (Filial 01 e Filial 02) de uma mesma empresa, transferindo saldos em estoque da filial 01 (origem) para a filial 02 (destino). Sendo considerado que, as tabelas de dados foram configuradas com uso exclusivo, ou seja, os dados cadastrais utilizados no exemplo deverão ser digitados em cada filial, conforme seguem os procedimentos.

**Obs.: Antes de iniciar o roteiro coletar o CNPJ  das filiais envolvidas pelo módulo configurador no cadastro das Filiais, veja nos prints abaixo:**

![fILIAL_01_E_02.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4418225453847)

![fILIAL_01_E_02_CNPJS.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4418229612951)

**- Roteiro de operações para a utilização de transferência de produtos entre filiais:**

***- FILIAL 01***

**1.** Cadastramento de produtos (Filial 01).

**2.** Cadastramento de TES de saída que serão utilizados na geração de documentos fiscais (Filial 01).

**3.** Cadastramento de clientes (Filial 01).

**4.** Cadastramento da condição de pagamento (Filial 01).

**5.** Cadastramento dos saldos iniciais dos produtos que serão movimentados entre as filiais (Filial 01).

***- FILIAL 02***

**6.** Cadastramento de produtos (Filial 02).

**7.** Cadastramento dos saldos iniciais dos produtos que serão movimentados entre as filiais (Filial 02). **Revise** se deseja utilizar o parâmetro **MV\_SB2AUTO** habilitado ([Clique aqui e veja a FAQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23642634053271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-Saldo-em-branco-sem-Armaz%C3%A9m-nas-Filiais-Destino))

**8.** Cadastramento de TES de entrada que serão utilizados na geração dos documentos entrada de materiais (Filial 02).

**9.** Cadastramento da condição de pagamento (Filial 02).

**10.** Cadastramento de fornecedores (Filial 02)

***- UTILIZANDO O PROCESSO***

**11.** Seleção dos produtos que serão utilizados na transferência de materiais (Filial 02). Início da execução da rotina “Transferência de Produtos entre Filiais”.

**12.** Apresentação da tela de transferência de produtos, exibindo os registros filtrados para o processamento em ordem de produto e em ordem de armazém (Filial 02).

**13.** Procedimentos para a transferência de saldos entre as filiais (Filial 02).

**14.** Utilização do botão “Relação” da rotina (Filial 02).

**15.** Consulta aos resultados da transferência de produtos.

```
1. Cadastramento de produtos Filial 01
```

![PRODUTO_FILIAL_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418238176535)

```
2. Cadastramento de TES de saída que serão utilizados na geração de documentos Filial 01
```

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418230139159)

```
3. Cadastramento de clientes CNPJ da Filial 01 na rotina MATA030
```

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418238316567)

```
4. Cadastramento da condição de pagamento Filial 01 na rotina MATA360
```

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418238420759)

```
5. Inclusão de saldos iniciais dos produtos Filial 01
```

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418226178199)

```
6. Cadastramento de produtos Filial 02
```

![PRODUTO_FILIAL_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418226277655)

```
7. Inclusão de saldos iniciais dos produtos Filial 02
```

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418238626455)

```
8. Cadastrar TES de entrada que será utilizada na geração dos documentos entrada na Filial 02
```

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418226463255)

```
9. Cadastramento da condição de pagamento Filial 02 na rotina MATA360
```

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418226606359)

```
10. Cadastrar o fornecedor na Filial 02 nesse caso CNPJ da Filial 01
```

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418238984343)

```
11. Selecionar produtos que serão transferidos para a (Filial 02)
```

![parametros_MATA310.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418227606295)

```
12. Tela da rotina MATA310, exibindo os registros filtrados para o processamento em ordem de produto e em ordem de armazém Filial 02
```

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418232186903)

```
13. Procedimentos para a transferência de saldos entre as filiais Filial 02
```

![mata310_tela_procedimento.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418228113559)

```
14. Utilização do botão “Relação” da rotina Filial 02 digite a quantidade e confirme
```

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418232960279)

```
15. Confirmar a transferência e a geração dos documentos relacionados Filial 02
```

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418233066519)

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418240430359)

```
16. Consulta aos resultados da transferência de produtos
```

![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418228543895)

## Dúvida:

* **Existe um relatório que demonstre esse processo de transferencia entre filiais?**

R: Sim, temos os relatórios MATR715, MATR103, e no Smartview o relatório ESTSV029 conforme documentação:

[Smart View - Transferência entre Filiais](https://tdn.totvs.com/pages/viewpage.action?pageId=807229766)

* **É possivel fazer simultaneamente mais de uma transferencia entre filiais?**

R: Sim, utilizando a rotina Transferencia entre Filiais (MATA311) conforme demonstrado neste video a partir do minuto 1:45:

**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[*SIGAEST - MATA310/MATA311 - Transferência entre Filiais utilizando o parâmetro MV\_FILTRF*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011717052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-utilizando-o-par%C3%A2metro-MV-FILTRF)

[*SIGAEST - MATA310/MATA311 - Como estornar Solicitações de Transferência entre Filiais?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12728743784087-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-estornar-Solicita%C3%A7%C3%B5es-de-Transfer%C3%AAncia-entre-Filiais-)

[*SIGAEST - MATA310 MATA311 - Como configurar tabela de preços para as Transferências?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8552373360023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-tabela-de-pre%C3%A7os-para-as-Transfer%C3%AAncias-)

[*SIGAEST - MATA310/MATA311 - Pontos de entrada da rotina Transferência entre Filiais*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003854082-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Pontos-de-entrada-da-rotina-Transfer%C3%AAncia-entre-Filiais)

[*SIGAEST - Help PV BLOQUEADO na rotina de Transferência entre Filiais (MATA310 e MATA311)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024378631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Help-PV-BLOQUEADO-na-rotina-de-Transfer%C3%AAncia-entre-Filiais-MATA310-e-MATA311-)
