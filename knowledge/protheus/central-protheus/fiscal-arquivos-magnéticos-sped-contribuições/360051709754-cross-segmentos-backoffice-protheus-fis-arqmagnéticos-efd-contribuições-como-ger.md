---
article_id: 360051709754
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: fe144ea471bc21f3a59602bdf163f572738d071bcd7ee986882bd98304d2408f
fetched_at: '2026-06-28T22:42:05.410819+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  como gerar os registros C111 e 1010 ou 1020
type: support-article
updated_at: '2022-09-15T22:13:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051709754-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-como-gerar-os-registros-C111-e-1010-ou-1020
---

Dúvida

Como gerar o Registro **C111** e **1010** ou **1020**

Observação

Necessário gerar o Registro **C111** para geração dos Registros **1010** ou **1020**

Solução

1. Realize o Cadastro de **Processos Referenciados** (Rotina **MATA967**, Tabela **CCF**) para gerar o Registro **1010** ou **1020,**

Caminho: **Módulo Livros Fiscais > Atualizações > Sped > Processos Referenciados**

Para mais informações, acesse [https://tdn.totvs.com/x/WeEIHw;](https://tdn.totvs.com/x/WeEIHw)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083204673/mceclip0.png)

2. Gere um Documento de Entrada ou Saída;

3. Acesse a Rotina **MATA920** ou **MATA910** > Caminho:  **Módulo Livros Fiscais > Atualizações > Movimentos > Nota Fiscal Manual de Entrada ou Saída > Selecione a linha do Documento > Clicar em Outras Opções > Complementos > Informações Complementares > Processos Referenciados**: preencher todos os campos da Tabela **CDG**. No campo **CDG\_PROCES**: informe o cadastro realizado na rotina **MATA967.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082067614/mceclip1.png)

Para preencher o complemento de forma automática, existe o Ponto de Entrada **MATUCOMP**.

Segue documentação do Ponto de Entrada:

<http://tdn.totvs.com/pages/releaseview.action?pageId=6077107>

Caso haja dúvidas com relação a configuração do ponto de entrada, por gentileza, entrar em contato com Suporte de **ADVPL**.

Documentação Completa:

Apuração:<https://tdn.totvs.com/pages/releaseview.action?pageId=212896468>

Arquivos: <https://tdn.totvs.com/pages/releaseview.action?pageId=212895074>
