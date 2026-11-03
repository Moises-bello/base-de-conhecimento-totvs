---
article_id: 360048495234
category: Escrita Fiscal - CIAP
content_hash: ef1dd7df5133bd0a65995323fdb78f0bf9660dd2ef66cd387e1afb14c5a63589
fetched_at: '2026-06-28T22:39:33.964950+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Qual data fiscal
  e data ativo correta para a emissão do Livro CIAP Modelo D?
type: support-article
updated_at: '2021-07-29T11:47:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048495234-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-data-fiscal-e-data-ativo-correta-para-a-emiss%C3%A3o-do-Livro-CIAP-Modelo-D
---

**Dúvida**

Qual data fiscal e data ativo correta para a Emissão do Livro CIAP Modelo D?  
  
**Ambiente**

Protheus - Livros Fiscais - A partir da versão 11.80

**Importante :**

1. É destinado à apuração do valor do crédito a ser mensalmente apropriado, nos termos do Art. 20 § 5º, da Lei Complementar nº. 87. Estes modelos referem-se a bens adquiridos a partir do ano de 2000

2. Composição do Relatório Modelo D

As informações dos quadros são provenientes dos arquivos Manutenção CIAP (SF9), Cadastro de Fornecedores (SA2), e Estorno Mensal CIAP (SFA).

3. O controle dos créditos do ICMS dos bens do ativo permanente será efetuado individualmente. Sua escrituração será feita por bem, com a identificação dos dados do contribuinte, os dados referentes às entradas, saídas, perdas e apropriação mensal do crédito, no período estabelecido para apropriação, mês a mês.

**Solução :**

****Processo a executar:****

**1.** No **Livros Fiscais (SIGAFIS)**, acesse **Relatórios/ Livros Oficiais/ Emissão Livro CIAP (MATR995)**, clique em **Parâmetros** e preencha os dados conforme orientações a seguir:

**2. Confira os parâmetros e configure a impressão do relatório :**

**Código de =** Informe o código do ativo

**Código até** =  Informe o código do ativo

**Modelo** = D

**Data Fiscal de** = informe a data inicial de aquisição do ativo

**Data Fiscal até** = Informe a data da ultima movimentação de apropriação do ativo

**Taxa da UFIR** = Vazio e/ou Informe o valor da UFIR em vigor se o estado do declarante exigir a conversão dos valores para UFIR.

**Ac. Demonst. de Apuração** = Sim /Não (As colunas **Base de Crédito** e **Crédito a ser apropriado** devem ser acumuladas?)

**Data ativo de** = Informe a data inicial de aquisição do ativo

**Data ativo até** = Informe a data da ultima movimentação de apropriação do ativo

**Imprime** = Livro ( ou  apenas os termos e/ou os livros e termos).

**Nº da Ordem** = Vazio  (ou  Número da ordem dos Termos de Abertura / Encerramento).

**Nº da Página Inicial** = Vazio (ou  Número da página inicial que será impressa nos Termos de Abertura / Encerramento).

**Qtd. Páginas / Feixe** = Vazio ( ou Quantidade de folhas que o livro contém).

**Observações** = Vazio ( ou  Observações necessárias que serão impressas no Termo de Abertura).

**Último Lançamento** = Data do último lançamento que será impressa no Termo de Encerramento.

**Taxa UPF-RS** = Taxa de conversão em UPF. Esta pergunta é válida somente para o estado do Rio Grande do Sul, conforme a IN DRP 45 de26/10/98 - RS.

**Modelo D em Folha Única** = Relatório modelo D será impresso em folha única, contendo os quatro quadros na mesma página, ou se deve ser emitido em duas páginas, com os quadros 1 e 2 na primeira página e os quadros 3 e 4 na segunda.

**Seleciona Filiais** = Sim e/ou  se NÃO apenas a filial corrente será afetada.

**Aglutina CNPJ+IE** = Não  (Aglutina a impressão do relatório por CNPJ+IE respeitando a seleção de filiais realizada pelo usuário. Este tratamento somente será realizado quando utilizada a pergunta de seleção de filiais. Tratamento disponível somente para ambientes DBAccess).

**Exibe detalhes no quadro 2** = Sim/Não ( Modelo D essa pergunta não interfere)

**1. Evidencia do preenchimento dos parâmetros geração do Livro Emissão CIAP modelo D :**

**Código Ciap  000005**

**Aquisição 25/05/2020**

**Ultima movimentação de aproveitamento do credito 31/08/2020**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071832134/mceclip0.png)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073054453/mceclip1.png)**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071832434/mceclip2.png)**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073055053/mceclip3.png)**

**2. Evidencia como é apresentado a informação do ativo após gerar o****Livro Emissão CIAP modelo D :**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071833874/mceclip4.png)**
