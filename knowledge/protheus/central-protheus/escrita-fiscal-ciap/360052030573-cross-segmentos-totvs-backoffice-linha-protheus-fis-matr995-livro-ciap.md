---
article_id: 360052030573
category: Escrita Fiscal - CIAP
content_hash: 64375b90ebac63279739b6a612efa137e1dd70a86ba766384a451002791c9a44
fetched_at: '2026-06-28T22:39:33.920844+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - MATR995 Livro CIAP
type: support-article
updated_at: '2024-12-12T13:34:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052030573-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-MATR995-Livro-CIAP
---

**Dúvida**Procedimentos para configurar o livro CIAP - MATR995

**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Emissão Livro CIAP (MATR995)

Por meio desta opção de relatório, será emitido o Livro com os Registros do CIAP destinado à apuração do crédito a ser mensalmente apropriado referente à aquisição de bem do ativo permanente.

Os Modelos A e B são destinados à apuração do valor da base do estorno de crédito e do total do estorno mensal do crédito, relativamente ao crédito apropriado nos termos do Art. 20 § 5º da Lei Complementar nº. 87. Estes modelos referem-se a bens adquiridos até o ano 2000.

Os Modelos C e D são destinados à apuração do valor do crédito a ser mensalmente apropriado, nos termos do Art. 20 § 5º, da Lei Complementar nº. 87. Estes modelos referem-se a bens adquiridos a partir do ano de 2000.

Considerações

Nos Modelos A e C, o controle dos créditos do ICMS dos bens do ativo permanente será efetuado como um todo. Sua escrituração será feita com a identificação dos dados do contribuinte, demonstrativo da base do estorno do crédito a ser apropriado e demonstrativo da apuração do estorno de crédito a ser efetivamente apropriado, mês a mês.

Nos Modelos B e D, o controle dos créditos do ICMS dos bens do ativo permanente será efetuado individualmente. Sua escrituração será feita por bem, com a identificação dos dados do contribuinte, os dados referentes às entradas, saídas, perdas e apropriação mensal do crédito, no período estabelecido para apropriação, mês a mês.

Estas informações são dispostas por meio de **quadros**, obedecendo à legislação de cada modelo, sendo:

Composição do Relatório Modelo A

As informações dos quadros são provenientes dos arquivos de Manutenção CIAP (SF9), Estorno Mensal CIAP (SFA) e Livros Fiscais (SF3).

**Importante**

Para contribuintes do estado de DF (Distrito Federal) o Modelo A segue o padrão utilizado no Modelo C.

Composição do Relatório Modelo B

As informações dos quadros são provenientes dos arquivos Manutenção CIAP (SF9), Cadastro de Fornecedores (SA2) e Estorno Mensal CIAP (SFA).

Composição do Relatório Modelo C

As informações dos quadros são provenientes dos arquivos Manutenção CIAP (SF9), Estorno Mensal CIAP (SFA), Livros Fiscais (SF3), Itens de Venda da NF (SD2) e Tipos de Entrada e Saída (SF4).

Composição do Relatório Modelo D

As informações dos quadros são provenientes dos arquivos Manutenção CIAP (SF9), Cadastro de Fornecedores (SA2), e Estorno Mensal CIAP (SFA).

**Importante**

A adoção dos modelos A ou B e C ou D é feita de acordo com o disposto na legislação de cada Unidade Federada. Desta forma, sugerimos consultar a legislação referente à sua unidade.

## Procedimentos para Utilização

1. No **Livros Fiscais (SIGAFIS)**, acesse **Relatórios/ Livros Oficiais/ Emissão Livro CIAP (MATR995)**, clique em **Parâmetros** e preencha os dados conforme orientações a seguir:

* Código de?

Informe o código do ativo inicial a ser processado.

* Código até?

Informe o código do ativo final a ser processado.

* Modelo A,B,C ou D?

Informe qual modelo de livro do CIAP deseja imprimir. A adoção dos modelos de livros para a escrituração (A ou B e C ou D) será feita de acordo com o disposto na legislação de cada Unidade Federada.

* Data Fiscal de?

Informe a data inicial para o processamento das movimentações fiscais do período (faturamentos).

* Data Fiscal até?

Informe a data final para o processamento das movimentações fiscais do período (faturamentos).

* Taxa da UFIR?

Informe o valor da UFIR em vigor se o estado do declarante exigir a conversão dos valores para UFIR.

* Ac. Demonst. de Apuração?

Informe se as colunas **Base de Crédito** e **Crédito a ser apropriado** devem ser acumuladas.

* Data ativo de?

Para impressão do modelo C, informe a data inicial de aquisição dos ativos.

* Data ativo até?

Para impressão do modelo C, informe a data final de aquisição dos ativos.

* Imprime

Informe se deseja imprimir: apenas os livros, apenas os termos ou os livros e termos.

* Nº da Ordem

Informe o número da ordem dos Termos de Abertura / Encerramento.

* Nº da Página Inicial

Informe o número da página inicial que será impressa nos Termos de Abertura / Encerramento.

* Qtd. Páginas / Feixe

Informe a quantidade de folhas que o livro contém.

* Nº da Junta Comercial

Informe o número da Junta Comercial que será impresso nos Termos de Abertura / Encerramento.

* Observações

Informe as observações necessárias que serão impressas no Termo de Abertura.

* CRC do Contador

Informe o CRC do contador que será impresso nos Termos de Abertura / Encerramento.

* Último Lançamento

Informe a data do último lançamento que será impressa no Termo de Encerramento.

* Taxa UPF-RS

Informe a taxa de conversão em UPF. Esta pergunta é válida somente para o estado do Rio Grande do Sul, conforme a IN DRP 45 de26/10/98 - RS.

* Modelo D em Folha Única?

Informe se o relatório modelo D será impresso em folha única, contendo os quatro quadros na mesma página, ou se deve ser emitido em duas páginas, com os quadros 1 e 2 na primeira página e os quadros 3 e 4 na segunda.

* Seleciona Filiais?

Seleciona as filiais desejadas. Se NÃO apenas a filial corrente será afetada.

* Aglutina CNPJ+IE?

Aglutina a impressão do relatório por CNPJ+IE respeitando a seleção de filiais realizada pelo usuário. Este tratamento somente será realizado quando utilizada a pergunta de seleção de filiais.

Tratamento disponível somente para ambientes DBAccess.

* Exibe detalhes no Quadro 2?

Exibe detalhes de baixas dos itens/bens no **quadro 2** do **modelo C**, quando existirem.

1. Confira os parâmetros e configure a impressão do relatório.

Link para acessar documentação completa:

<https://tdn.totvs.com/pages/releaseview.action?pageId=226527899>
