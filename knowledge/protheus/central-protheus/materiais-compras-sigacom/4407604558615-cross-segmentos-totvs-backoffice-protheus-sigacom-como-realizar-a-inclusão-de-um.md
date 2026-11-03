---
article_id: 4407604558615
category: Materiais - Compras (SIGACOM)
content_hash: a6218b83a6e46ab2af3b3403746a6a0bd4a76355ec3c66c67f9f0f0e659978d4
fetched_at: '2026-06-28T22:41:08.670750+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar a inclusão
  de um Documento de Entrada - MATA103
type: support-article
updated_at: '2025-03-06T19:39:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407604558615-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-inclus%C3%A3o-de-um-Documento-de-Entrada-MATA103
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19541973302039) Tempo aproximado para leitura: **00:20:00 min****Dúvida:**

Como realizar a inclusão de um documento de entrada pelo modulo de Compras ?  
  
**Ambiente:**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS  Compras - Todas as versões

**Solução**Para realizar a inclusão de um documento de entrada pelo modulo de compras, basta seguir os passos abaixo:

**1.** Acessar a rotina de documento de entrada MATA103. A rotina se encontra dentro do modulo de compras em: **Atualizações/Movimentos/Documento de Entrada.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407598171415)

**2**. Ao acessar a rotina clique em incluir e selecione a filial que o documento será incluso. Após isso defina no cabeçalho da rotina o **Numero do Documento/Serie/Fornecedor/ Espécie do Documento/UF Origem:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407603829527)**

**3.** Na linha do item você terá os campos respectivos ao **Produto/Quantidade/Valor/TES/Impostos/Classes Contábeis.** Preencha os campos da forma que deseja, com as informações que deseja gerar o documento.

Os campos Produto, Quantidade, Vlr. Unitário e TES são de preenchimento **obrigatório**.

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407609731479)**

Após a inclusão das informações acima, o documento estará dessa forma. Verifique se esta tudo de acordo com o que deseja e salve o documento. O Documento é gerado.

![imagem4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19541973306519)

***Obs1:***

Ao se preencher o Produto no Item da NF, serão trazidas automaticamente informações que estiverem amarradas no seu cadastro de produto. Por exemplo: Unidade de Medida do Produto, tipo de entrada, entidades contábeis e natureza de rendimento.

***Obs2:***

Para que a inclusão do documento de entrada, gere um título a pagar no módulo financeiro (integração com o financeiro), é necessário que a TES utilizada esteja configurada para Gerar Duplicata (F4\_DUPLIC). Dessa forma, no menu inferior, na aba "Duplicatas", será obrigatório selecionar a Cond. Pagto (Condição de Pagamento).

![imagem3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19541960586903)

***Obs3:***

Caso se deseje anexar ou vincular algum arquivo/documento à NF de Entrada inserida, no Browse da rotina, posicionando o cursor no Browse sobre a NF de Entrada, pode-se utilizar a opção "Outras Ações->Conhecimento" da imagem abaixo para este vinculo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19541960587415)

Tabelas :

* SF1 - Arquivo de Cabeçalho das Notas Fiscais de Entrada.
* SF3 - Registros Fiscais.
* SFT - Livro Fiscal por item de nota.
* SE2 - Arquivo de Contas a Pagar.
* SED - Arquivo de Naturezas.
* SN1 - Ativo Imobilizado.
* SN2 - Descrições Estendidas.
* SN3 - Saldos e Valores.
* SN4 - Movimentações do Ativo Fixo.

***Saiba Mais :***

[Manual e Artigos - Documento de Entrada - MATA103](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000244307-MP-SIGACOM-Manual-e-Artigos-Rotina-Documento-de-Entrada-MATA103?source=search)

[DOCUMENTO DE ENTRADA GERAL - CENTRALIZADORA de COMPRAS](https://tdn.totvs.com/x/H3PQHw)

[MP - SIGACOM - Como incluir Documento de Entrada com Solicitação de Compras e Pedido de Compras?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037447974)

[Tabelas MATA103 - SIGACOM](https://tdn.totvs.com/pages/viewpage.action?pageId=306851624)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
