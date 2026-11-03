---
article_id: 360028738371
category: Escrita Fiscal - CIAP
content_hash: 42c1fd492999fb1da9bbd4977d11a185063e1c60037dccfcd62bab382600de5b
fetched_at: '2026-06-28T22:39:33.958289+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Qual data fiscal
  e data ativo correta para a Emissão do Livro CIAP Modelo C?
type: support-article
updated_at: '2021-07-29T11:51:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028738371-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-data-fiscal-e-data-ativo-correta-para-a-Emiss%C3%A3o-do-Livro-CIAP-Modelo-C
---

**Dúvida**

Qual data fiscal e data ativo correta para a Emissão do Livro CIAP Modelo C?

**Ambiente**

Protheus - Livros Fiscais - A partir da versão 11.80

**Importante :**

**1.** É destinado à apuração do valor do crédito a ser mensalmente apropriado, nos termos do Art. 20 § 5º, da Lei Complementar nº. 87. Estes modelos referem-se a bens adquiridos a partir do ano de 2000

**2.** Composição do Relatório Modelo C

As informações dos quadros são provenientes dos arquivos Manutenção CIAP (SF9), Estorno Mensal CIAP (SFA), Livros Fiscais (SF3), Itens de Venda da NF (SD2) e Tipos de Entrada e Saída (SF4).

**3.**O controle dos créditos do ICMS dos bens do ativo permanente será efetuado como um todo. Sua escrituração será feita com a identificação dos dados do contribuinte, demonstrativo da base do estorno do crédito a ser apropriado e demonstrativo da apuração do estorno de crédito a ser efetivamente apropriado, mês a mês.

**4.** Para contribuintes do estado de DF (Distrito Federal) o Modelo A segue o padrão utilizado no Modelo C.

**Solução :**

****Processo a executar:****

**1.** No **Livros Fiscais (SIGAFIS)**, acesse **Relatórios/ Livros Oficiais/ Emissão Livro CIAP (MATR995)**, clique em **Parâmetros** e preencha os dados conforme orientações a seguir:

**2. Confira os parâmetros e configure a impressão do relatório :**

**Código de =** Vazio

**Código até** =  ZZZZ

**Modelo** = C

**Data Fiscal de** =  Primeiro dia/ primeiro Mês/ Ano Vigente ( ex: 01/01/2020)

**Data Fiscal até** = Ultimo dia/ Ultimo Mês/ Ano Vigente ( ex: 31/12/2020)

**Taxa da UFIR** = Vazio e/ou Informe o valor da UFIR em vigor se o estado do declarante exigir a conversão dos valores para UFIR.

**Ac. Demonst. de Apuração** = Sim /Não (As colunas **Base de Crédito** e **Crédito a ser apropriado** devem ser acumuladas?)

**Data ativo de** = Primeiro dia/ primeiro Mês/ Ano referente a 48 meses( ex: 01/01/2016)

**Data ativo até** = Informe a data da ultima movimentação de apropriação do ativo (Ex. 31/08/2020)

**Imprime** = Livro ( ou  apenas os termos e/ou os livros e termos).

**Nº da Ordem** = Vazio  (ou  Número da ordem dos Termos de Abertura / Encerramento).

**Nº da Página Inicial** = Vazio (ou  Número da página inicial que será impressa nos Termos de Abertura / Encerramento).

**Qtd. Páginas / Feixe** = Vazio ( ou Quantidade de folhas que o livro contém).

**Observações** = Vazio ( ou  Observações necessárias que serão impressas no Termo de Abertura).

**Último Lançamento** = Vazio (ou  Data do último lançamento que será impressa no Termo de Encerramento).

**Taxa UPF-RS** = Taxa de conversão em UPF. Esta pergunta é válida somente para o estado do Rio Grande do Sul, conforme a IN DRP 45 de26/10/98 - RS.

**Modelo D em Folha Única** = Não

**Seleciona Filiais** = Sim e/ou  se NÃO apenas a filial corrente será afetada.

**Aglutina CNPJ+IE** = Não  (Aglutina a impressão do relatório por CNPJ+IE respeitando a seleção de filiais realizada pelo usuário. Este tratamento somente será realizado quando utilizada a pergunta de seleção de filiais. Tratamento disponível somente para ambientes DBAccess).

**Exibe detalhes no quadro 2** = Sim  (Exibe detalhes de baixas dos itens/bens no quadro 2 do  modelo C , quando existir

**1. Evidencia do preenchimento dos parâmetros geração do Livro Emissão CIAP modelo C :**

**Ultima movimentação de aproveitamento do credito 31/08/2020**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071857914/mceclip0.png)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073075133/mceclip1.png)**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071858114/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071858194/mceclip4.png)

**2. Evidencia como é apresentado a informação do ativo após gerar o****Livro Emissão CIAP modelo C :**

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071858574/mceclip5.png)**
