---
article_id: 360024619954
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 2e88230b6eb7a4bd901c36651e1ad4ddb17f438d3c7dd9c1af99ed4adb5cc743
fetched_at: '2026-06-28T22:42:11.775238+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Informações
  Adicionais da Apuração de ICMS (E115 e 1925)
type: support-article
updated_at: '2022-08-18T14:01:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024619954-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Informa%C3%A7%C3%B5es-Adicionais-da-Apura%C3%A7%C3%A3o-de-ICMS-E115-e-1925
---

**Dúvida**  
Procedimentos de Configuração e Utilização da rotina Informações Adicionais da Apuração de ICMS (E115 e 1925) - MATA017.  
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Disponibilizada rotina de Cadastro de Valores Declaratórios para composição do registro E115 - Informações Adicionais da Apuração - Valores Declaratório, obedecendo a tabela 5.2 - Tabela de Informações Adicionais da Apuração - Valores Declaratórios, do Sistema Público de Escrituração Fiscal - EFD ICMS/IPI.

Esta rotina também é utilizada para compor registro 1925 - Informações Adicionais da Sub-apuração – Valores Declaratórios

**Procedimento para Configuração**

No Configurador (SIGACFG) acesse Ambiente/ Cadastros/ Menus e inclua, no menu do módulo Livros Fiscais (SIGAFIS), conforme especificação a seguir:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360037949534/mceclip0.png)

No **Configurador (SIGACFG)** acesse **Base de Dados / Dicionário / Base de Dados**, inclua/verifique os campos necessários:

## **SIX - Índices**

**Ordem 1**

**Chave:**

CDV\_FILIAL+CDV\_PERIOD+CDV\_CODAJU+CDV\_LIVRO+CDV\_DOC+CDV\_SERIE+CDV\_CLIFOR+CDV\_LOJA+CDV\_CFOP

**Descrição:**

Data+Cod. Ajuste.+Livro+Doc+Serie+Cli/For+Loja+Data+Cod. Ajuste.+Doc+Serie+Cli/For+Loja+CFOP

**Ordem 2**

**Chave:**

CDV\_FILIAL+CDV\_PERIOD+CDV\_LIVRO","Data+Livro","Data+Livro","Data+Livro

**Descrição:**

Filial+Data+Livro

**Ordem 3**

Chave:

CDV\_FILIAL+CDV\_PERIOD+CDV\_CODAJU+CDV\_CFOP

**Descrição:**

Filial+Data+Cod.Aju+CFOP

**Ordem 4**

**Chave:**

CDV\_FILIAL + CDV\_TPMOVI + CDV\_ESPECI + CDV\_FORMUL + CDV\_DOC + CDV\_SERIE + CDV\_CLIFOR + CDV\_LOJA + CDV\_NUMITE + CDV\_SEQ + CDV\_CODAJU

**Descrição:**

Filial+Tp movimento+Espec. Doc.+Formul. Prop+Documento++Serie+Cliente+Loja+Nu  
  
**SX2 – Tabelas**   
  
**Tabela**: CDV  
**Descrição:** Informações adicionais da Apuração  
**Chave:** CDV\_FILIAL+CDV\_PERIOD+CDV\_CODAJU+CDV\_LIVRO+CDV\_DOC+CDV\_SERIE+CDV\_CLIFOR+CDV\_LOJA+CDV\_CFOP

**SX3 - Campos:**

**Campo:** CDV\_CODAJU  
**Tipo:** Caracter  
**Tamanho:** 8  
**Formato:** @!  
**Título:** Cod. Ajuste  
**Descrição:** Cod Ajuste  
**Usado:** Sim  
**Obrigatório:** Sim  
**Valid:** Existcpo('CDY')  
**Consulta Padrão:** CDY  
**Help:** Código de Ajuste  
  
**Campo:** CDV\_PERIOD  
**Tipo:** Caracter  
**Tamanho:** 6  
**Formato:** @!  
**Título:** Per(AAAAMM)  
**Descrição:** Per(AAAAMM)  
**Usado:** Sim  
**Obrigatório:** Sim  
**Valid:** PerValido(M->CDV\_PERIOD)  
**Help:** Período de apuracão (AAAAMM)

**Campo:** CDV\_DESCR  
**Tipo:** Caracter  
**Tamanho:** 47  
**Formato:** @!  
**Título:** Desc.Compl.do Ajuste  
**Descrição:** Desc.Compl.do Ajuste  
**Usado:** Sim  
**Help:** Informe a descrição ref. ao código de ajuste informado.  
  
**Campo:** CDV\_LIVRO  
**Tipo:** Caracter  
**Tamanho:** 1  
**Formato:** @!  
**Título:** Livro  
**Descrição:** Livro  
**Usado:** Sim  
**Obrigatório:** Sim  
**Help:** Informe o número do livro, este campo deve ser preenchido somente para sub-apuração do ICMS.  
  
**Campo:** CDV\_VALOR  
**Tipo:** Numérico  
**Tamanho:** 14  
**Decimal:** 2  
**Formato:** @E 999,999,999.99  
**Título:** Valor de Referencia  
**Descrição:** Valor de Referencia  
**Usado:** Sim  
**Obrigatório:** Sim  
**Valid:** Positivo()  
**Help:** Informe o saldo inicial de ICMS do produto.  
  
**Campo:** CDV\_DOC  
**Tipo:** Caracter  
**Tamanho:** Tamanho campo F3\_NFISCAL  
**Formato:** @!  
**Título:** Numero NF  
**Descrição:** Numero NF  
**Grupo:** 018  
**Usado:** Sim  
**Help:** Informe o Documento Fiscal, informação levada para o Sped Fiscal no Registro E115.  
  
**Campo:** CDV\_SERIE  
**Tipo:** Caracter  
**Tamanho:** 3  
**Formato:** @!  
**Título:** Série  
**Descrição:** Série  
**Usado:** Sim  
**Help:** Informe série do documento, informação levada para o Sped Fiscal.  
  
**Campo:** CDV\_CLIFOR  
**Tipo:** Caracter   
**Tamanho:** Tamanho campo A1\_CLIENTE  
**Formato:** @!  
**Título:** Cli/For  
**Descrição:** Cli/For  
**Grupo:** 001  
**Usado:** Sim  
**Help:** Informe o Cliente/Fornecedor, informação levada para o Sped Fiscal no Registro E115  
  
**Campo:** CDV\_LOJA  
**Tipo:** Caracter  
**Tamanho:** Tamanho campo A1\_LOJA  
**Formato:** @!  
**Título:** Loja  
**Descrição:** Loja  
**Grupo:** 002  
**Usado:** Sim  
**Help:** Informe a loja, informação levada para o Sped Fiscal no Registro E115  
  
**Campo:** CDV\_CFOP  
**Tipo:** Caracter  
**Tamanho:** 5  
**Formato:** @!  
**Título:** CFOP  
**Descrição:** CFOP  
**Nível:** 1  
**Usado:** Sim  
**Valid:** ExistCpo('SX5','13'+M->CDV\_CFOP)  
**Help:** Cód. Fiscal - CFOP  
  
**Campo:** CDV\_TPMOVI  
**Tipo:** Caracter  
**Tamanho:** 1  
**Decimal:** 0  
**Formato:** @!  
**Título:** Tp Movimento  
**Usado:** Sim  
**Obrigatório:** Não  
**Browse:** Sim  
**Opções:** E=Entrada; S=Saída  
**Val. Sistema:** Pertence(" ES")  
**Contexto:** Real   
**Propriedade:** Alterar   
**Ordem:** 13  
  
**Campo:** CDV\_NUMITE  
**Tipo:** Caracter   
**Tamanho:** 4  
**Decimal:** 0  
**Formato:** @!   
**Título:** Num. Item  
**Descrição:** Número do Item   
**Usado:** Sim  
**Obrigatório:** Não  
**Browse:** Sim  
**Contexto:** Real  
**Propriedade:** Alterar   
**Ordem:** 14  
  
**Campo:** CDV\_SEQ  
**Tipo:** Caracter  
**Tamanho:** 3  
**Decimal:** 0  
**Formato:** @!  
**Título:** Seq. Manut.  
**Descrição:**Sequência Manutenção  
**Usado:** Sim  
**Obrigatório:** Não   
**Browse:** Sim  
**Contexto:** Real   
**Propriedade:** Visualizar   
**Ordem:** 15  
  
**Campo:** CDV\_ID  
**Tipo:** Caracter  
**Tamanho:** 36  
**Decimal:** 0  
**Formato:** @!  
**Título:** Chave  
**Descrição:** Chave  
**Usado:** Não  
**Obrigatório:** Não  
**Browse:** Sim  
**Inic. Padrão:** FWUUID("FISA140")  
**Contexto:** Real  
**Propriedade:** Visualizar   
**Ordem:** 16  
  
**Campo:** CDV\_ESPECI  
**Tipo:** Caracter   
**Tamanho:** 5  
**Decimal:** 0  
**Formato:** @!  
**Título:** Espec. Doc.  
**Descrição:** Espécie Documento  
**Usado:** Sim  
**Obrigatório:** Não   
**Browse:** Sim  
**Inic. Padrão:** EXISTCPO("SX5", "42" + M->CDV\_ESPECI)  
**Contexto:** Real  
**Propriedade:** Alterar   
**Cons. Padrão:** 42  
**Ordem:** 17

**Campo:** CDV\_FORMUL  
**Tipo:** Caracter  
**Tamanho:** 1  
**Decimal:** 0  
**Formato:** @!   
**Título:** Formul. Prop  
**Descrição:** Formulátio Próprio  
**Usado:** Sim   
**Obrigatório:** Não  
**Browse:** Sim  
**Opções:** S=Sim; N=Nao  
**Val. Sistema:** Pertence(" SN")  
**Contexto:** Real   
**Propriedade:** Alterar   
**Ordem:** 18  
  
**Campo:** CDV\_AUTO  
**Tipo:** Caracter   
**Tamanho:** 1  
**Decimal:** 0  
**Formato:** @!  
**Título:** Apur. Auto  
**Descrição:** Apur. Auto  
**Usado:** Sim  
**Obrigatório:** Não   
**Browse:** Sim  
**Opções:** 1=Calc.Sistema; 2=Calc. Usuário;  S=Apuração  
**Inic. Padrão:** 2  
**Val. Sistema:** Pertence(" 12S")  
**Contexto:** Real  
**Propriedade:** Visualizar  
**Ordem:** 19

**Procedimentos para Utilização**

Os códigos referentes as informações adicionais da apuração - Valores Declaratórios são automaticamente importados para a tabela CDY - Cód. Inf. Adicionais da Apuração, quando é rodada a rotina IMPSPED ou automaticamente pelo compatibilizador UPDFIS(Exclusivo da versão 11).

Ao executar o compatiblizador U\_IMPSPED como programa inicial, será necessário informar o diretório que contém os arquivos com código da Tabela 5.2, disponibilizada pelo estado (no formato .\*txt) para que o sistema possa importá-los automaticamente.

Portanto previamente, baixe estes arquivos do site do SPED e copie-os para uma pasta no servidor.

É importante observar que alguns Estados ainda não fizeram a publicação das tabelas, sendo que para estes é necessário aguardar a liberação e processar novamente o IMPSPED, para efetuar a importação.

Para verificar a lista completa dos lançamentos e os Estados que já publicaram os códigos, acesse a seção de Tabelas de Códigos no site do SPED.

**- CDY – Publicada no site do SPED como Valores Declaratórios.**

**Importante**

**Para importação correta na tabela CDY deve-se renomear o arquivo TXT baixado do site do SPED referente a tabela 5.2 para TABELA52.txt**

Após a importação desses códigos, para a correta geração do registro faça a declaração dos valores por meio da rotina Informações Adicionais da Apuração.

Adicione ao menu e cadastre os valores a serem levados para o **Bloco E - Livros Fiscais de Apuração do ICMS e do IPI, no Registro tipo E115 - Informações Adicionais da Apuração do ICMS – Valores Declaratórios**.

Este registro é gerado para Informações Adicionais da Apuração do ICMS vinculadas à rotina Inf. Adic. da Apuração.

Na rotina **Inf. Adic. da Apuração,** deve ser informada manualmente pelo usuário as informações adicionais da apuração, sendo obrigatório incluir o período ao qual se refere essa informação adicional e o código de ajuste referente. Após a inclusão do código de ajuste, o sistema efetua o gatilho da descrição do ajuste.

O registro E115 trata de valores declaratórios relativos ao ICMS, conforme definição da legislação estadual pertinente.

Esses valores são meramente declaratórios e não são computados na apuração do ICMS.

Portanto, deverão ser informados no sistema através da rotina Inf. Adic. Da Apur. (MATA017).

Após realizada a Apuração de ICMS (MATA953), na rotina**Inf. Adic. Da Apur (MATA017)** inclua as informações de acordo com legislação estadual, respeitando os códigos de apuração disponibilizado pela SEFAZ, por estado através da tabela 5.2 - Tabela de Informações Adicionais da Apuração.

**Importante**

As informações referentes ao**Quadro C**, campos **31- Faturamento**, **32 - Número de empregados no último dia do mês** e **33- Valor da folha de salários** da GIA/RS, devem ser incluídas na rotina**Inf. Adic. Da Apur (MATA017)** com o código de lançamento referente a cada registro e campo. Ao gerar o arquivo EFD ICMS/IPI, para importação na GIA/RS, será apresentado um registro **E115** para cada código informado.

# **Exemplo de utilização de forma manual**:

Efetuar lançamento na rotina MATA017 com período que devera ser considera para geração dos registros os registros E115 e 1925.

**Caminho -> Livros Fiscais/Atualização/SPED/Inf. Adic. Da Apur**

Efetuar inclusão manual das informações nos campos conforme lançamento de Nota fiscal, número de livro cadastrado na TES e código de ajuste AM051001 ou utilizado na operação.

Deve ser preenchido os campos abaixo.

Per(AAAAMM) (CDV\_PERIOD)    = Ano e mês da apuração

Cod. Ajuste (CDV\_CODAJU) = Utilizado na nota fiscal exemplo AM051001

Número NF (CDV\_DOC) = Número da nota fiscal

Serie (CDV\_SERIE) = Série da nota fiscal

Cli/for (CDV\_CLIFOR) = Cliente ou Fornecedor da nota fiscal

Loja (CDV\_LOJA) = Código da loja

Valor de Ref (CDV\_VALOR) = Valor da nota fiscal.

Livro (CVD\_LIVRO) = Conteúdo informado no TES, campo  **Livro (F4\_NRLIVRO).**

**Processo para gerar automaticamente valor declaratório na inclusão da nota**  
 Acessar modulo de livros fiscais > Atualizações > Sped > Prod. x Cod.V.Decl.  
 Manual do cadastro Prod. x Cod.V.Decl.: <http://tdn.totvs.com/pages/viewpage.action?pageId=286029741>

-Incluir no cadastro da rotina de Produto X Código de Valores declaratórios (FISA140) uma regra de cálculo para ser executada no momento de inclusão da nota.  
Nesta regra deve ser definido reflexo que contem calculo para código de ajuste cadastrado.

Importante

O campo de reflexo estará disponível na rotina Produto X Código de Valores declaratórios (FISA140) somente quando parâmetro MV\_GIAEFD estiver como desativado (.F.)

-O cálculo será aplicado quando a nota possuir o mesmo Produto, CFOP e CST do cadastro realizado na rotina de Produto X Código de Calores declaratórios.  
  
-Para valor calculado sera respeitada a regra definida dentro do cadastro de reflexo vinculado no produto através da rotina de Produto X Código de Valores declaratórios

Pelas rotinas abaixo é possível inserir código e valor manualmente:  
MATA103 - Documento de Entrada  
MATA910 - Nota Manual de Entrada  
MATA920 - Nota Manual de Saída

Foi adicionada na aba de Lançamentos de apuração botões para alternar entre ajustes de apuração de ICMS e código declaratório.

Exemplo:   
![](http://tdn.totvs.com/download/attachments/286498628/image2018-10-9_13-48-35.png?version=1&modificationDate=1539103964447&api=v2)

No pedido de venda (MATA461) sera exibido na planilha financeira botão de Valores Declaratórios para exibir cálculo aplicado no pedido.

Exemplo:

![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360037965234/mceclip16.png)

Manuais relacionados

SPED fiscal

<http://tdn.totvs.com/display/PROT/FIS0005_SPED_FISCAL>

FISA140 – Produto X Código de valor declaratório

[http://tdn.totvs.com/pages/viewpage.action?pageId=286029741FIS0085\_Produto x Código de Valores Declaratórios\_F3K](http://tdn.totvs.com/pages/viewpage.action?pageId=286029741)

FISA072 – Códigos de Reflexos

http://tdn.totvs.com/pages/viewpage.action?pageId=185750580

MATA017 - Informações Adicionais da Sub-apuração – Valores Declaratórios

http://tdn.totvs.com/pages/viewpage.action?pageId=286498628

Informações Técnicas: 

Tabelas Utilizadas: CDV - Informações adicionais da Apuração  
Rotinas Envolvidas: MATA017 - Cadastro das informações adicionais da Apuração  
Sistemas Operacionais: Windows e Linux. 

Link contendo as informações acima: 

<http://tdn.totvs.com/pages/releaseview.action?pageId=286498628>
