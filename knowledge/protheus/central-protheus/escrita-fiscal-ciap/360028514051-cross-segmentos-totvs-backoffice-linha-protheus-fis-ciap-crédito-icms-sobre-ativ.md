---
article_id: 360028514051
category: Escrita Fiscal - CIAP
content_hash: e7768db9eab2eb4dc44608f5e7f8052bc1cac76b6bfc51e852ea74d1af9cf4de
fetched_at: '2026-06-28T22:39:33.801137+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - CIAP - Crédito ICMS
  sobre ativo permanente/Relatório CIAP
type: support-article
updated_at: '2022-02-03T20:01:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028514051-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-CIAP-Cr%C3%A9dito-ICMS-sobre-ativo-permanente-Relat%C3%B3rio-CIAP
---

**Dúvida**CIAP – Crédito ICMS sobre Ativo Permanente   
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**O CIAP – Controle de Crédito do ICMS do Ativo Permanente – dispõe sobre o aproveitamento de crédito do ICMS relativo à mercadoria destinada ao ativo permanente e institui o documento específico de mesmo nome.

Por meio do CIAP, fica assegurado a todo contribuinte do ICMS o direito de se creditar o imposto em operação de que tenha resultado a entrada de mercadoria destinada ao ativo permanente, desde que:

      Guarde relação com a atividade fim do contribuinte;  
      A entrada tenha ocorrido a partir de 1º de novembro de 1996.  
  
Os documentos fiscais relativos a bens do ativo permanente, além de serem escriturados nos livros fiscais próprios, serão também escriturados no documento CIAP, elaborado com a finalidade de determinar o valor do estorno do crédito fiscal, apropriando na entrada dos bens no estabelecimento.

Está disponível no processo de emissão do Livro CIAP (MATR995) a geração de informações consolidadas por filial para atendimento a gestão corporativa, onde foi criada a pergunta Aglutina por CNPJ+IE?, que permite ao usuário selecionar filiais que possuem o mesmo CNPJ de forma unificada.

**Importante**

Quando utilizada a opção de Aglutinação por CNPJ+IE, a janela de seleção de filiais será ordenada por CNPJ + I.E. Para utilizar a aglutinação de informações, o cliente deverá consultar seu departamento jurídico para verificar se o seu ramo de atividade permite tal aglutinação.

O crédito de ICMS pode ser apropriado totalmente depois de transcorridos 48 ou 60 meses da data de aquisição do bem, sendo que, mensalmente, a empresa se apropria do valor do estorno, que será obtido pela multiplicação do valor de crédito apropriado por ocasião da entrada do bem pelo fator mensal, que será a fração do número de meses em que a apropriação será realizada.

Exemplo:

Se a apropriação for finalizada em 48 meses, o valor mensal da apropriação será a fração de 1/48. O valor final da apropriação será a relação entre a soma das saídas e prestações isentas ou não tributadas, e o total das saídas e prestações escrituradas no mês.

**Importante**

Considere 60 meses para bens adquiridos até 31/12/2000;

Considere 48 meses para bens adquiridos a partir de 01/01/2001.

**Tabela SF9 - Manutenção CIAP**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028624132/mceclip0.png)**

**Importante**

Campo criado para informar o número do item de saída do bem, quando existe baixa por venda e para atender o SPED, na geração do bloco G, registro G140.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028623551/mceclip1.png)

**Importante**

Campo criado para informar o tipo de Ativo, a busca é realizada pela mesma Consulta Padrão utilizado no Ativo Fixo (G1) e para atender o SPED, na geração do bloco G, registro G125 e 0300.

Caso o bem estiver cadastrado como componente, ou seja, o campo F9\_TIPO com o conteúdo 03, não será  possível apropriá-lo e o sistema irá apresentar um alerta com as instruções para resolução da inconsistência.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028624352/mceclip2.png)

**Importante**

Campo criado para informar o Código do Ativo Principal ao qual o componente será adicionado e para atender o SPED, na geração do bloco G, registro G125 e 0300.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028624392/mceclip3.png)

**Importante**

Campo criado para informar se o usuário utiliza o bem com parcela reduzida. Conforme o RICMS aprovado pelo decreto 1980 de 21.12.2007, na hipótese de aquisição de bens ainda em fase de implantação, em substituição ao fator de quarenta e oito (48) avos, aplicar o fator obtido entre a diferença de quarenta e oito e a quantidade de meses transcorridos entre a entrada do bem no estabelecimento e o início das atividades.

Ao dar entrada do bem no estabelecimento, o usuário deve informar na rotina de Manutenção CIAP as parcelas a serem consideradas no campo **Num. Parc. (F9\_QTDPARC)**, e o mesmo será replicado ao campo **Saldo Parc. (F9\_SLDPARC)**. Os cálculos sobre a apropriação serão feitos em cima dessa quantidade.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028623691/mceclip4.png)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028624472/mceclip5.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028623771/mceclip6.png)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028624532/mceclip7.png)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028624612/mceclip8.png)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028623991/mceclip9.png)

Tabela **SF4 –** **Tipos de Entrada e Saída**

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028624732/mceclip10.png)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028624071/mceclip11.png)

1.  **Parâmetros**

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028624111/mceclip12.png)

**Importante**

Campo criado para informar o número do item de saída do bem, quando existe baixa por venda e para atender o SPED, na geração do bloco G, registro G140.

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028624892/mceclip13.png)

## Procedimentos para Configuração

1.No **Configurador (SIGACFG)** acesse **Ambientes/ Cadastros/ Parâmetros (CFGX017)**. Crie/configure o(s) parâmetro(s) a seguir:

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028627432/mceclip14.png)

Exemplo para o conteúdo: LCIAPA.TRM

**Importante**

Este parâmetro pode ser criado por meio do processamento da rotina **U\_UPDSIGAFIS.**

**![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028627512/mceclip15.png)**

Exemplo para o conteúdo: LCIAPE.TRM

**Importante**

Este parâmetro pode ser criado por meio do processamento da rotina **U\_UPDSIGAFIS.**

**![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028627572/mceclip16.png)**

**Importante**

Observe quando o conteúdo do parâmetro for igual a **T**, no valor apresentado também serão consideradas as despesas acessórias, ou seja, mais o seguro, o frete e as despesas.

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028627151/mceclip17.png)

Exemplo para o conteúdo: 5101/6101/5102/6102/

Os CFOPs devem estar separados por barras ( **/** ).

**Importante**

O parâmetro **MV\_CIAPCFO** pode ser utilizado para definir quais CFOPs devem compor a coluna de Saídas e Prestações Tributadas (coluna 1) e Total de Saídas e Prestações (coluna 2).

Quando estiver preenchido, são processados apenas os CFOPs informados no parâmetro, totalizando as colunas 1 e 2 da mesma forma. Se não for informado, todas as movimentações de saídas estaduais e interestaduais serão consideradas, classificando as tributadas (coluna 1) por meio do TES utilizado na movimentação.

**![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631472/mceclip18.png)**

O conteúdo pode ser preenchido com:

* **T** - Para verificar o TES na composição das colunas Saídas e Prestações Tributadas (coluna 1) e Total de Saídas e Prestações (coluna 2).
* **F** - Para que os mesmos valores sejam apresentados nas colunas Saídas e Prestações Tributadas (coluna 1) e Total de Saídas e Prestações (coluna 2).

Em ambos os casos, são processados apenas os movimentos que tenham sido efetuados com os CFOPs indicados no parâmetro **MV\_CIAPCFO**.

![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631712/mceclip19.png)

Exemplo para o conteúdo: 20010101

![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631131/mceclip20.png)

Exemplo para o conteúdo: SP

![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631151/mceclip21.png)

Exemplo para o conteúdo: 1

![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631191/mceclip22.png)

Exemplo para o conteúdo: 5101/6101

Os CFOPs devem estar separados por barras ( **/** ).

**Importante**

Caso o parâmetro **MV\_CFOEXP** não exista ou seu conteúdo esteja em branco, para o cálculo das exportações, são considerados apenas os CFOPs iniciados por **7**, ou seja, apenas as movimentações de exportação, não sendo possível identificar movimentos equiparados à exportação.

![mceclip23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631832/mceclip23.png)

Exemplo para o conteúdo: 7101/7102

Os CFOPs devem estar separados por barras ( **/** ).

**Importante**

O parâmetro **MV\_CFOEXC** pode ser utilizado quando existir a necessidade de desconsiderar determinados CFOPs no cálculo das exportações. Caso ele não exista ou seu conteúdo não seja informado, todas as operações de exportação serão consideradas.

**![mceclip24.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631912/mceclip24.png)**

**Importante**

Por padrão, o conteúdo desse parâmetro é falso, ou seja, não considera as movimentações que controlam poder de terceiro.

![mceclip25.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631211/mceclip25.png)

**Importante**

O parâmetro **MV\_ FATCIAP** somente tem efeito na emissão do Livro CIAP nos *layouts* B e D, não sendo utilizados nos *layouts* A e C. Deve ser utilizado quando o valor do Fator a ser impresso no Livro for o proporcional e não o Fator cheio informado no momento da Apropriação.

Este parâmetro trabalhará em conjunto com o campo **Fator Prop. (FA\_FATPRO)**.

Ex:

Fator cheio 0.9967

Fator Proporcional (0.9967/48) = 0.02014

![mceclip26.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631932/mceclip26.png)

![mceclip27.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631271/mceclip27.png)

Exemplo para o conteúdo: 7101/7102

Essa rotina também disponibiliza a impressão dos termos de abertura e encerramento do livro. Para tanto, é necessário que os arquivos de impressão dos termos estejam no diretório correspondente ao **\SIGAADV** (se versão 7.10) ou **\SYSTEM** (se versão 8.11 ou 10), conforme instalação do sistema. Os arquivos a seguir são disponibilizados como padrões:

* Termo de Abertura: LCIAPA.TRM
* Termo de Encerramento: LCIAPE.TRM

1. No **Configurador (SIGACFG)**, acesse **Ambiente/ Cadastros/ Parâmetros**, observe os parâmetros a seguir ou crie-os, quando necessário:

![mceclip28.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631972/mceclip28.png)

No conteúdo desse parâmetro, informe:

T – para habilitar os campos mencionados;

F – para não habilitar os campos mencionados.

![mceclip29.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631371/mceclip29.png)

Exemplo de conteúdo: 48

**Importante**

Este parâmetro não será respeitado em casos de aquisições internas no estado do RS, pois neste caso será definido com  24 meses conforme decreto 50.756.

 Nas aquisições internas de mercadoria destinada ao ativo permanente produzida por empresa fabricante localizada no Estado.

![mceclip30.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631451/mceclip30.png)

Exemplo de conteúdo: 20010101

![mceclip31.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028632092/mceclip31.png)

Sugestão para o conteúdo: F9\_FILTRAN

![mceclip32.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028632212/mceclip32.png)

Ao final do processamento da apropriação, o valor calculado será arredondado ou truncado em duas casas decimais, dependendo da configuração do parâmetro. No conteúdo do parâmetro, informe:

T = para arredondar;

F = para truncar.

![mceclip33.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028632232/mceclip33.png)

No conteúdo informe:

T = para considerar tal tratamento;

F = para não considerar.

**Importante**

Esse parâmetro trabalha em conjunto com o campo **Fração Mensal (FA\_FRACAOM)**, citado a seguir, portanto, é de extrema necessidade que esse campo também esteja criado.

![mceclip34.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631691/mceclip34.png)

Sugestão para o conteúdo: F9\_ITEMNFE

![mceclip35.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631771/mceclip35.png)

Sugestão para o conteúdo: F9\_CODPROD

![mceclip36.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028631811/mceclip36.png)

Sugestão para o conteúdo: F9\_ESPNF

![mceclip37.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028632512/mceclip37.png)

Sugestão para o conteúdo: F9\_CENCUS

![mceclip38.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028632171/mceclip38.png)

Sugestão para o conteúdo: F9\_CENCUS

![mceclip39.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028632211/mceclip39.png)

Sugestão para o conteúdo: F9\_VLICMSF

![mceclip40.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028632952/mceclip40.png)

Sugestão para o conteúdo: F9\_VLICMSO

![mceclip41.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028633012/mceclip41.png)

1. **No Configurador (SIGACFG)** acesse **Base de Dados/ Dicionário/ Base de Dados**, crie os campos a seguir: Exemplo de campo a ser relacionado no parâmetro **MV\_FILTRAN**.

* Tabela **SF9 - Manutenção CIAP**

**![mceclip42.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028632771/mceclip42.png)**

**Sugestão para o nome do campo: F9\_FILTRAN**

**![mceclip43.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028633852/mceclip43.png)**

O campo **Fração Mensal (FA\_FRACAOM)** armazena o fator para cálculo da Fração *pro rata die*

* Tabela **SFA -** **Estorno Mensal CIAP**

**![mceclip44.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028636612/mceclip44.png)**

O campo **Fator Prop. (FA\_FATPRO)** armazena o fator proporcional do cálculo da Apropriação do CIAP.

Fator cheio 0.9967

Fator Proporcional (0.9967/48) = 0.02014

**![mceclip45.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028636631/mceclip45.png)**

**Importante**

Este campo pode ser criado por meio do processamento da rotina **U\_UPDSIGAFIS.**

**![mceclip46.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028637391/mceclip46.png)**

**![mceclip47.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028637871/mceclip47.png)**

## Controle Individual

1. No **Configurador (SIGACFG)** acesse **Base de Dados/ Dicionário/ Base de Dados**, crie os seguintes campos:

 Tabela **SF9 - Manutenção CIAP**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028638932/mceclip0.png)

**Importante**

Este campo deve ser alimentado manualmente no Cadastro do Ativo, indicando o número de parcelas em que deve ocorrer o crédito. O valor do ICMS também deve ser o valor que resta a ser apropriado.

**Exemplo:** Suponha que um valor de R$ 1.000,00 referente a um determinado ativo foi estornado por outro Sistema, 18/48 parcelas, portanto, restando 30 parcelas e totalizando R$ 625,00. Neste caso, esse ativo deve ser inserido no sistema com o campo **Valor ICMS** **(F9\_VALICMS)** igual a R$ 625,00 e o campo **Num. Parc.** **(F9\_QTDPARC)** com 30, ou seja, o valor e as parcelas restantes.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028639151/mceclip1.png)

**Importante**

Informe este campo manualmente no Cadastro do Ativo, pois deve indicar quantas parcelas ainda restam a ser apropriadas para um determinado ativo.

Este campo somente deve ser informado na inclusão do ativo com o mesmo número inserido no campo **Num. Parc.** **(F9\_QTDPARC)**, pois seu valor decresce à medida que o ativo sofre apropriações. Este campo deve indicar as parcelas que realmente restam para o referido ativo. Quando seu conteúdo for zero, representa que todas as parcelas já foram creditadas.

Conforme exemplo citado, esse campo deve ser inserido com conteúdo 30, pois indica que o bem ainda não foi apropriado pelo sistema atual. À medida que for sofrendo estornos, o campo vai diminuindo, até chegar à zero, indicando que foi totalmente estornado.

1. Para os já usuários do Sistema Protheus® (não sendo nova implantação) que necessitem utilizar **Controle individual de parcelas por ativo**, é necessário executar os passos de 3 a 5.
2. No **Configurador (SIGACFG)**, acesse **Ambiente/ Cadastros/ Menus**, inclua no menu do módulo **Livros Fiscais (SIGAFIS)** a opção para execução da função **Atualiza SF9 (M906SF9)**, conforme especificação a seguir:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028639571/mceclip2.png)

**Importante**

Somente o administrador do sistema deve possuir acesso a esta rotina, que deve ser executada na implantação do processo ou quando houver a necessidade de atualizar o saldo de parcelas do bem (nos casos em que não houveram saídas tributadas em determinado mês para realizar a apropriação), pois efetua a atualização dos campos **Num. Parc.** **(F9\_QTDPARC)** e **Saldo Parc.** **(F9\_SLDPARC)** de acordo com a tabela Estorno dos Créditos (SFA) e do parâmetro **MV\_LC102**, que indica o número de parcelas a serem estornadas para os ativos. Por esse motivo, é necessário que a **tabela Estorno dos Créditos (SFA)** esteja com os lançamentos corretos.

## Complemento do Documento CIAP

1. Execute a opção **Miscelânea/ Acertos/ Atualiza SF9 (M906SF9)**:
2. Clique em **Parâmetros.** São apresentadas as seguintes informações:

INDIQUE O TIPO DE ATUALIZAÇÃO

A atualização da tabela Tipos de Entrada e Saída (SF4) pode ocorrer de duas formas distintas (nas duas opções, a janela apresenta uma breve explicação dos processos que serão executados):

**1 = Parcial**: Indica que somente atualizará os ativos que possuírem o campo **Num. Parc**. (F9\_QTDPARC) zerado (sem valor). Com a seleção dessa opção e confirmação da rotina, se nenhuma alteração for efetuada, é apresentada a mensagem **Nenhuma atualização efetuada**. Clique em **Ok** para prosseguir.

**2 = Geral**: Indica que, independente dos campos possuírem ou não valores inseridos, são recalculados e atualizados conforme tabela Tipos de Entrada e Saída (SF4). Com a seleção desta opção e confirmação e processamento da rotina, é apresentado um relatório CIAP resumo para os ativos atualizados.

O processo completo do CIAP envolve a movimentação e a emissão dos relatórios CIAP. Para tanto, esse documento está dividido em seções distintas, em que:

**Seção 1 – Manutenção do CIAP (MATA905)**

**Seção 2 – Estorno CIAP (MATA906)**

**Seção 3 – Controle individual de parcelas por ativo (MATA906)**

**Seção 4 – Emissão do Livro CIAP (MATR995)**

Seção 1 – Manutenção do CIAP (MATA905)

A rotina de **Manutenção CIAP (MATA905)** permite incluir, alterar, excluir, pesquisar e visualizar o cadastro de crédito de ICMS referente à aquisição de ativo permanente. A inclusão dos dados desse cadastro pode ser efetuada de duas formas distintas. De qualquer forma, é possível manipular as informações do CIAP no menu **Atualizações/ Cadastro/ Manutenção CIAP (MATA905)**.

Formas de inclusão dos bens do ativo permanente no CIAP:

* **Por meio do Documento de Entrada**

Nos ambientes de **Compras (SIGACOM)** e/ou **Estoque (SIGAEST)**, todas as movimentações de entrada com TES - Tipo de Entrada/Saída (SF4) que permita o controle do CIAP, lançam automaticamente o bem para as movimentações do CIAP. Para tanto, é necessário que o TES utilizado seja configurado da seguinte forma:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028640091/mceclip3.png)

* **Manualmente**

Outra forma é incluir os ativos um a um, com a referência das respectivas notas fiscais, pela rotina **Manutenção CIAP (MATA905)**.

Executando o MATA905 – Manutenção CIAP

1. No **Livros Fiscais (SIGAFIS)** acesse **Atualizações/ Cadastro/ Manutenção CIAP (MATA905)**. Nesta opção, é possível visualizar, incluir, alterar ou excluir bens do CIAP.

Opção Visualizar

Por meio de a opção Visualizar, somente são apresentados os campos cadastrados referentes ao bem selecionado.

Opção Incluir

Por meio de a opção Incluir é possível incluir manualmente o ativo imobilizado no CIAP, informando os campos solicitados pela rotina.

Có[d.do](http://d.do) Ativo

Informe o código do bem que o identificará no CIAP.

Descrição

Informe a descrição do bem. Essa descrição será impressa no relatório CIAP.

Fornecedor

Informe de qual fornecedor foi adquirido o bem, conforme a nota fiscal de entrada.

Loja For.

Informe a loja do fornecedor em que foi adquirido o bem, conforme a nota fiscal de entrada.

N.Fiscal (E)

Informe o número da nota fiscal de entrada que registrou a aquisição do ativo.

Série (E)

Informe a série da nota fiscal de entrada que registrou a aquisição do ativo.

Item NFE

Informe o número do item na nota fiscal de entrada. Caso este campo seja informado, será feita uma validação com a nota fiscal de entrada.

Form. Próprio

Informe se a nota fiscal de entrada foi emitida em formulário próprio ou não.

N. Livro Ent.

Informe o número do Livro de Registro de Entradas em que foi escriturado o crédito do bem.

Folha L. Ent.

Informe a folha do Livro de Registro de Entradas em que foi escriturado o crédito do bem.

Dt. Digit. NFE

Informe a data de entrada da nota fiscal de entrada.

Dt. Emis. NFE

Informe a data de emissão da nota fiscal de entrada.

Cliente

Informe o código do cliente responsável pela compra do bem, quando for o caso de venda do ativo imobilizado.

Loja Cliente

Informe a loja do cliente responsável pela compra do bem, quando for o caso de venda do ativo imobilizado.

N.Fiscal (S)

Informe o número da nota fiscal de saída que tenha registrado a venda do bem selecionado.

Série (S)

Informe a série da nota fiscal de saída que tenha registrado a venda do bem selecionado.

Dt. Emis. NFS

Informe a data de emissão da nota fiscal de saída que tenha registrado a venda do bem selecionado.

Mot. Estorno

Campo desabilitado. Apenas será apresentado nos casos em que o bem já possua estornos lançados.

Valor ICMS

Informe o valor do ICMS recolhido na nota fiscal. Caso tenham sido informados os dados de notas fiscais de entrada e de saída, o valor do imposto informado deve ser a soma dos valores obtidos nas duas notas. Para usuários do **Controle Individual de Parcelas por Ativo** (seção 3 desse documento), informe o valor restante do ICMS a ser apropriado.

CFOP da Ent.

Informe o CFOP utilizado no documento de entrada do bem.

ICMS Imobil.

Este campo apresenta o valor de ICMS do ativo imobilizado, caso este bem tenha sido apropriado.

Fator FCA

Informe o Fator de Conversão e Atualização Monetária. Deve ser informado o fator da data da aquisição do bem (apenas para o estado do Paraná).

Num. Parc.

Apenas para usuários do **Controle Individual de Parcelas por Ativo** (Seção 3 desse documento). Informe o número de parcelas em que deve ocorrer o crédito.

Saldo Parc.

Apenas para usuários do **Controle Individual de Parcelas por Ativo** (Seção 3 desse documento). Informe quantas parcelas ainda restam a ser apropriadas para um determinado ativo.

It Nf Saída.

Informar o item da nota de saída que tenha registrado a venda do bem selecionado.

**Dt.Ini.Uti.**

Informar a data de início da utilização do bem.

Por padrão, quando o bem for cadastrado através módulo de **Compras (SIGACOM)**, este campo será preenchido com a data de entrada do bem, podendo ser alterada conforme início de utilização do bem. Lembrando que o bem somente poderá ser apropriado a partir da data informada neste campo.

Opção Alterar

Por meio dessa opção, é possível alterar alguns campos que não interferem na apropriação do ICMS no CIAP.

Opção Excluir

Por meio dessa opção, é possível excluir algum bem do CIAP desde que não tenha sido efetuada nenhuma apropriação.

Opção Componente

Por meio dessa opção, é possível realizar o controle de Componentes do Ativo, utilizada para a geração dos registros G125 e 0300 do SPED.

Sub-Menu: Ativo Principal

Por meio dessa opção, é possível realizar o cadastro do bem Principal para utilização nos componentes, não informar valor de ICMS, pois o mesmo não dever ser apropriado até a baixa dos componentes.

Sub-Menu: Baix. Comp.

Por meio dessa opção, é possível realizar Baixa dos Componentes agregando os seus valores (saldos) no bem Principal. Está Rotina também altera o bem principal possibilitando que o mesmo seja apropriado.

Ativo Principal: Informar o código do bem principal, lembrando que todos os componentes devem estar amarrados para que possam ser localizados.

Sub-Menu:  Est. B. Comp.

Por meio dessa opção, é possível realizar Estorno da Baixa de Componentes retornando todos os envolvidos a seus estados anteriores, não realizar esta operação se o bem Principal já esteja apropriado.

Ativo Principal: Informar o código do bem principal, lembrando que todos os componentes devem estar amarrados para que possam ser localizados.

Opção Legenda

Por meio da opção Legenda, é possível visualizar o status de cada bem, de forma individual.

* **Ativo sem ocorrências** identifica que o bem teve sua entrada no Sistema, mas não houve com ele nenhuma movimentação do tipo baixa, apropriação ou transferência.
* **Ativo baixado** identifica que o bem foi baixado por perda ou venda. Ou ativo incorporado.
* **Ativo transferido** identifica que o bem foi baixado por transferência para outra filial.
* **Ativo baixado por período** identifica que o bem foi baixado por ter sido totalmente apropriado.
* **Ativo apropriado** identifica que o bem teve alguma parcela já apropriada.
* **Ativo com baixa parcial** - identifica que o bem foi baixado parcialmente.
* **Ativo Principal** - identifica o bem Principal o qual os componentes fazem parte.

Seção 2 – Estorno CIAP (MATA906)

A rotina de **Estorno do CIAP (MATA906)** permite baixar, por motivo de perda, saída, transferência, devolução ou outras saídas do imobilizado e apropriar os registros do CIAP.

O bem somente pode ser baixado totalmente por motivo de perda, deterioração ou roubo, por meio do módulo **Livros Fiscais (SIGAFIS)**. Assim, no **Cadastro de Ativos**, constará como bem excluído, isso quando o TES utilizado também atualizar o ativo. Caso contrário, o bem pode ser baixado normalmente.

Por meio da opção **Apropriação**, o bem pode ser **depreciado**, ou seja, seu valor de aquisição sofre um cálculo por meio do fator de coeficiente de participação das saídas e prestações isentas ou não tributadas, no total das saídas e prestações escrituradas no mês, considerando-se um mínimo de quatro casas decimais.

O valor do estorno será obtido pela multiplicação do fator pelo valor de crédito apropriado por ocasião da entrada do bem, deduzindo, se for o caso, o valor dos estornos mensais ocorridos no ano da saída ou perda.

Quando um bem é apropriado, é calculado mediante a divisão do valor das saídas e das prestações isentas ou não tributadas pelo valor total das saídas e prestações.

Executando o MATA906 – Estorno CIAP

1. No **Livros Fiscais (SIGAFIS)** acesse **Atualizações/Cadastro/Estorno CIAP (MATA906)**. Nesta opção, é possível visualizar, baixar, cancelar ou apropriar bens do CIAP.

Opção Visualizar

Por meio de a opção Visualizar, somente são apresentados os campos e valores cadastrados referentes ao bem selecionado.

Opção Baixar

A opção **Baixar** tem por objetivo excluir o bem da obrigatoriedade do CIAP, seja qual for o motivo, desde que legal. Essa opção não exclui o bem do Cadastro de Ativos, apenas não o inclui mais no cálculo do CIAP.

**Importante**

Caso o bem tenha sido lançado pelo ambiente de Compras, utilizando um TES configurado para atualizar automaticamente o **Cadastro de Ativos (F4\_ATUATF = Sim)**, somente será possível efetuar a baixa do bem por meio do ambiente **Ativo Fixo (SIGAATF)**. Efetuando a baixa por meio desse ambiente, o CIAP será atualizado automaticamente.

**Importante**

MT906CTM - Ponto de entrada que permite a gravação de um campo customizado na tabela SFA.

**Importante**

**MT906VLD** – Ponto de Entrada que recebe como Parâmetros os campos “Nfs, Série, Dt. Saída, Cliente, Loja, Item, Tipo do Evento e Filial” informados ao efetuar a baixa, e deve retornar .T. ou .F. para continuar a realizar a Baixa do Ativo.

**Importante**

O bem somente será considerado no processamento de apropriação a partir da **Data de Início de Atividade (F9\_DTINIUT)**.  **Exemplo**: Se o bem estiver com data de início de utilização em 01/06/2013 e teve entrada na empresa em 01/01/2013, nas apropriações de janeiro até maio este bem não será considerado, somente a partir de junho que as apropriações deste bem serão iniciadas.

**Observação**: Caso este campo esteja vazio o bem será considerado para apropriação normalmente.

Processamento da Rotina

Para executar essa opção, selecione o bem a ser baixado e clique em **Baixar**. São apresentadas as informações referentes à entrada do bem no estabelecimento: código, nota fiscal de entrada, série da nota fiscal de entrada, fornecedor, loja do fornecedor e data de entrada do bem. Os demais campos devem ser informados, pois correspondem aos dados da baixa do bem.

Nfs

Informe o número da nota fiscal referente à saída do bem do estabelecimento.

Série

Informe a série da nota fiscal referente à saída do bem do estabelecimento.

Dt. Saída

Informe a data de saída do bem do estabelecimento.

Cliente

Informe o cliente para o qual foi emitida a nota fiscal de saída do bem.

Loja

Informe a loja do cliente para o qual foi emitida a nota fiscal de saída do bem.

Item

Informe o número do item da nota fiscal de saída do bem do estabelecimento.

Valor

Informe o valor da nota fiscal de saída do bem do estabelecimento.

Tipo do Evento

Informe o motivo de baixa do bem, que pode ser:

* **Perda**: Quando o bem não for mais útil (quebra, deterioração e outros).
* **Saída**: Quando o bem for vendido;
* **Transferência**: Quando o bem for transferido para outro estabelecimento. A baixa do crédito do ativo por transferência deve ser efetuada no mês subsequente à última apropriação, de forma que esse crédito seja apropriado corretamente no intervalo de tempo, já que, pelo entendimento da Lei, essa apropriação é mensal. Consequentemente, seu lançamento na filial destino deve ser efetuado no mês da baixa na filial origem da transferência, pois o crédito CIAP origina-se na entrada no bem no estabelecimento.
* **Devolução**: Quando o bem for devolvido para o fornecedor.
* **Outras**: Outras saídas do imobilizado, por exemplo, por fusão ou incorporação.

Filial

Informe a filial para qual o bem será transferido (somente quando o motivo da baixa for transferência).

Crédito *Pro Rata Die*

Valor do crédito proporcional aos dias em que o ativo esteve em poder do estabelecimento antes de sofrer baixa.

Exemplo:

Exemplo do procedimento considerando pro rata die na baixa por motivo de transferência (3):

Supondo que, em 01/01/2006, foi adquirido um bem e, após 3 apropriações, ou seja, no mês 3, este bem deva ser transferido da filial X para a filial Y.

Para este caso, devem-se efetuar as apropriações dos meses de janeiro, fevereiro e março. No mês de abril, deve-se efetuar a baixa do crédito com data base posicionado no dia correto de sua transferência, indicando motivo 3 (transferência), que, consequentemente, exigirá a digitação da filial destino, no caso, a filial Y.

Verifique que as perguntas da apropriação são apresentadas devido à necessidade de gerar, junto com a baixa, uma apropriação residual ***pro rata die*** referente os dias restantes do mês de abril em que o bem ficou em poder do estabelecimento. As perguntas devem ser configuradas conforme tópico a seguir: **Opção Apropriar**.

Após confirmar as perguntas para a correta apropriação, será apresentada a tela de baixa, em que é possível verificar o valor do bem a ser baixado no campo **Valor** e o valor do **Crédito *Pro Rata Die*** gerado junto com a baixa. Basta confirmar e o ativo estará baixado. Vale lembrar que, para ocorrer à baixa do ativo, não deve haver para ele nenhuma ocorrência no período.

Para a entrada do bem na filial destino da transferência (Y), deve ser efetuado o lançamento do crédito do ativo, normalmente informando a nota fiscal de entrada e as outras informações, inclusive o valor do crédito subtraído dos valores apropriados na filial (X). Porém, esta filial também deve estar com o parâmetro ***Pro Rata Die*** habilitado para que os dias restantes do período também sejam calculados, caso contrário, será assumido o mês cheio, duplicando os dias apropriados na filial origem, o que está incorreto perante a Lei.

Supondo que, para o caso citado, o valor do crédito seja R$ 96,00 referente à entrada de um ativo em 08/01/2007 e baixado em 10/04/2007 por transferência, em que as respectivas parcelas dos meses ficariam:

* **Mês 1 (Janeiro)** = 1,48, referente ao período de 08/01/2007 a 31/01/2007, ou seja, 23 dias em que, dividido pelos 31 dias do mês de janeiro, resultaria numa fração de 0,7419 que, multiplicado pelo valor da parcela cheia no mês ( R$2,00 ), apresentaria o valor de R$1,48;
* **Mês 2 (Fevereiro) e 3 (Março)** = R$2,00 (referente ao mês cheio);
* **Mês 4 (Abril)** = 0,6666, referente ao período de 01/04/2007 a 10/04/2007, ou seja, 10 dias em que, dividido pelos 30 dias do mês de abril, resultaria numa fração de 0,3333 que, multiplicado pelo valor da parcela cheia no mês (R$2,00), apresentaria o valor de R$0,6666;

O cálculo do ***pro rata die*** apresenta o valor da apropriação gerado junto com a baixa do ativo por transferência, no entanto, o processo é repetido para datas diferentes ao se lançar na filial destino da transferência, chegando a outros valores pelos mesmos cálculos, desde que o parâmetro ***pro rata die*** (**MV\_PRORDIE**) também esteja habilitado nesta filial.

Exemplo:

Exemplo do procedimento sem considerar ***pro rata die*** na baixa por motivo de transferência *(3):*

Supondo que, em 27/01/2004, foi adquirido um bem e, após 10 apropriações, esse bem deva ser transferido da filial X para a filial Y.

Para esse caso, deve-se efetuar a baixa com data base correta para o dia do evento, indicando o motivo 3 (transferência), que, consequentemente, exigirá a digitação da filial destino, no caso, a filial Y.

Após a digitação das informações, basta confirmar e o ativo estará baixado. Vale lembrar que, para ocorrer à baixa do ativo, não deve haver nenhuma outra ocorrência CIAP no período, e, no mês em que o ativo for baixado (com exceção da baixa depreciação total), quem tem direito a se creditar da parcela do mês da baixa e posteriores é o estabelecimento que estiver entrando com este ativo.

Para a entrada do bem na filial destino da transferência (Y) no mês da baixa, deve ser efetuado o lançamento do crédito do ativo, normalmente informando a nota fiscal de entrada e as outras informações, inclusive o valor do crédito subtraído dos valores apropriados na filial (X). Porém, ao se tratar de apropriações, deve-se utilizar um fator de 1/38 ou 1/50, que, ao somar aos 38 ou 50, resulta a proporção correta exigida por Lei na apropriação (48 ou 60).

Supondo que, para o caso citado, o valor do crédito seja R$ 1.000,00 com entrada 27/01/2004 e que, a cada apropriação (R$ 20,83 = 1/48) nos meses subsequentes, some um total de R$ 208,30 após as 10 apropriações (mês 10 - outubro). Como no décimo primeiro mês (novembro) houve a baixa do crédito, deve ser lançado com valor de R$ 791,70 no mesmo mês na filial Y, para que a apropriação utilize a proporção de 1/38, resultando o mesmo valor mês. Com o exemplo citado, observe que o crédito inicia-se sempre no mês de entrada do ativo no estabelecimento (conforme LC 87 de 13/09/1996).

Opção Cancelar

Esta rotina efetua o cancelamento de apropriações. O Sistema visa, além do cancelamento da baixa já contemplada, o cancelamento da apropriação errônea do mês/ano definido pela data base do Sistema.

Ao clicar na opção **Cancelar**, deve-se escolher qual operação será executada: Baixa do Ativo ou Apropriação.

Opções de Cancelamento

* **Baixa do Ativo**

Indica que será feito o cancelamento de uma baixa por perda ou venda já efetuada anteriormente. Esta rotina tem por objetivo fazer com que o bem baixado erroneamente, volte à obrigatoriedade do CIAP. O cancelamento de baixa do ativo apenas pode ser efetuado para o registro selecionado.

* **Apropriação**

Esta opção determina o cancelamento de uma apropriação errônea efetuada anteriormente. Visa somente cancelar a última apropriação efetuada, preenchendo-se a data base do Sistema com o mês e o ano da apropriação a ser cancelada.

**Exemplo:**

Em um cancelamento de uma apropriação efetuada em 25/01/2001, deve-se posicionar a data base do Sistema em qualquer dia do mesmo mês e ano da apropriação a ser cancelada, para este caso ??/01/2001.

Ao selecionar a opção **Apropriação**, automaticamente é liberada a lista de opções para designar se a operação de cancelamento abrange somente o registro selecionado ou todos os registros. Para a opção **Todos os Registros**, é liberado um ícone que possibilita a utilização de algum filtro para o cancelamento.

Depois de selecionadas as opções desejadas, confirme, para que todas as apropriações canceladas sejam exibidas em um relatório para conferência. Esse relatório está disponível apenas quando houver cancelamento de apropriação para **Todos os Registros** simultaneamente. Vale ressaltar que a data base do Sistema é a origem para todos os cancelamentos, tanto para o **Reg. Selecionado** ou **Todos os Registros**.

Opção Apropriar

Esta rotina efetua as apropriações mensais do ICMS, de acordo com os parâmetros informados, que devem ser efetuadas da seguinte maneira:

* Bens adquiridos até o ano de 2000 são apropriados à proporção de 1/60;
* Bens adquiridos a partir de 2000 são apropriados à proporção de 1/48.

Assim, o valor do crédito do ICMS, no momento da compra do bem do ativo imobilizado, pode ser creditado em parcelas mensais, de acordo com a data de entrada do bem no estabelecimento.

**Importante**

Caso exista integração com o SIGAATF, o bem deverá ser classificado anteriormente no módulo Ativo Fixo e posteriormente apropriar o CIAP na rotina MATA906.

Parâmetros para a apropriação:

Data de Referência?

Informe a data de referência para a apropriação do bem, sendo sempre o último dia do mês referente à apropriação.

Ao mudar o foco para a próxima pergunta, é exibida uma tela de sugestão para o coeficiente de apropriação, conforme segue:

* Os campos **Data Inicial** e **Data Final** apresentam informações de acordo com a **Data de Referência** digitada na tela anterior. Exemplo: Na tela anterior, a **Data de Referência** é 31/01/01, referente ao período de 01/01/01 a 31/01/01.
* O campo **Fator Atual** apresenta a informação contida na pergunta **Fator ou Fator LC 102/200**, que é definido conforme o parâmetro **MV\_DATCIAP**. Se período for anterior à data cadastrada no parâmetro **MV\_DATCIAP**, o conteúdo desse campo virá do campo **Fator** da tela anterior; caso contrário, virá do campo **Fator LC 102/2000**.
* O campo **Total das Saídas e Prestações Tributadas**, como o próprio nome indica, refere-se a todas as saídas e prestações tributadas no período definido por meio da **Data Inicial** e **Data Final** desta mesma tela.
* O campo **Total de todas as Saídas e Prestações** apresentam o total de todas as saídas e prestações, independente de tributadas ou não no período definido por meio da **Data Inicial** e **Data Final** desta mesma tela.
* O campo **Coeficiente de Apropriação** **(Fator Sugerido)** é o resultado da divisão entre os dois campos anteriores (**Totais das Saídas** e **Prestações Tributadas** por **Totais de todas as Saídas e Prestações**).
* Ao confirmar a rotina, o valor do **Coeficiente de Apropriação (Fator Sugerido)**, será transportado para seu respectivo campo na tela anterior, **Fator ou Fator LC 102/2000**.
* Ao cancelar, o **Coeficiente de Apropriação (Fator Sugerido)** será desconsiderado, mantendo o **Fator Atual**.
* Na versão 8.11, a opção de filtro para as movimentações de saída que compõem esta sugestão de coeficiente de apropriação pode ser customizada por meio do ponto de entrada A906CFAP, em que a **Data Inicial** e a **Data Final** devem ser passadas por parâmetro e tratadas na customização como PARAMIXB[1] e PARAMIXB[2]. O ponto de entrada deve retornar o *alias* utilizado, conforme exemplo a seguir:

USER FUNCTION A906CFAP ()

                Local cAliasSD2 := ""

                Local cQuery             := ""

                Local cArqD2             := ""

                //

                #IFDEF TOP

                               Local nx := 0

                               //

                               cAliasSD2:=              "AliasSD2"

                               aStruSD2 :=              SD2->(dbStruct())

                               cQuery      :=             "SELECT "

                               cQuery      +=            " \* "

                               cQuery      +=            "FROM "+RetSqlName("SD2")+" SD2 "

                               cQuery      +=            "WHERE "

                               cQuery      +=            "SD2.D2\_FILIAL='"+xFilial("SD2")+"' AND "

                               cQuery      +=            "SD2.D\_E\_L\_E\_T\_=' ' AND "

                               cQuery      +=            "SD2.D2\_EMISSAO>='"+DTOS(**PARAMIXB[1]**)+"' AND SD2.D2\_EMISSAO<='"+DTOS(**PARAMIXB[2]**)+"' "

                               cQuery      +=            "AND (SD2.D2\_CF LIKE '5%' OR SD2.D2\_CF LIKE '6%' OR SD2.D2\_CF LIKE '7%') "

                               cQuery      +=            "ORDER BY "+SqlOrder(SD2->(IndexKey ()))

                               cQuery      :=             ChangeQuery (cQuery)

                               //

                               DbUseArea (.T., "TOPCONN", TcGenQry (,, cQuery), cAliasSD2, .T., .T.)

                               //

                               For nX := 1 To Len (aStruSD2)

                                               If (aStruSD2[nX][2]<>"C")

                                                               TcSetField (cAliasSD2, aStruSD2[nX][1], aStruSD2[nX][2], aStruSD2[nX][3], aStruSD2[nX][4])

                                               EndIf

                               Next nX

                #ELSE

                               cAliasSD2 := "SD2"

                               cArqD2     :=             CriaTrab (Nil, .F.)

                               cQuery      :=             'SD2->D2\_FILIAL=="'+xFilial ("SD2")+'" .And. DToS (SD2->D2\_EMISSAO)>="'

                               cQuery      +=            DToS (**PARAMIXB[1]**)+'" .And. DToS (SD2->D2\_EMISSAO)<="'+DToS (**PARAMIXB[2]**)

                               cQuery      +=            '" .And. Left (SD2->D2\_CF, 1)$"567"'

                               IndRegua (cAliasSD2, cArqD2, SD2->(IndexKey ()),, cQuery)

                #ENDIF

                //

                DbSelectArea (cAliasSD2)

                (cAliasSD2)->(DbGoTop ())

**RETURN (cAliasSD2)**

**Importante**

É importante ressaltar que a customização desse ponto de entrada substitui o filtro padrão utilizado pelo Microsiga Protheus®.

Fator?

Informe o coeficiente de apropriações para movimentações até o ano de 2000 ou mantenha o calculado na **Sugestão para o Coeficiente de Apropriação**.

Fator LC 102/2000?

Informe o coeficiente de apropriações para movimentações após o ano de 2000 ou mantenha o calculado na **Sugestão para o Coeficiente de Apropriação**.

Mostra Lanc. Contáb.?

Informe se deseja apresentar os lançamentos contábeis.

Aglut. Lançamentos?

Informe se deseja efetuar a aglutinação dos lançamentos contábeis.

Lanc. Conta. On-line?

Informe se deseja efetuar contabilização *on-line*.

Grupo de?

Informe o grupo inicial do ativo imobilizado a ser considerado no cálculo.

Grupo até?

Informe o grupo final do ativo imobilizado a ser considerado no cálculo.

Código de?

Informe o código inicial do ativo imobilizado a ser considerado no cálculo.

Código até?

Informe o código final do ativo imobilizado a ser considerado no cálculo.

Fator FCA?

Informe o fator de conversão FCA a ser processado no momento da apropriação (para o estado do Paraná).

Lançamentos padronizados

Para a contabilização de Apropriação e Estorno CIAP, estão disponíveis os lançamentos.

|  |  |
| --- | --- |
| **Código** | **Lançamento** |
| **755** | Contabilização no momento da Apropriação CIAP. |
| **756** | Contabilização no momento do Estorno CIAP. |

Opção Legenda

Por meio da opção **Legenda**, é possível visualizar o status de cada bem, de forma independente.

* **Ativo sem ocorrências** - Identifica que o bem teve sua entrada no Sistema, mas não houve com ele nenhuma movimentação do tipo baixa, apropriação ou transferência.
* **Ativo baixado** - Identifica que o bem foi baixado por perda ou venda.
* **Ativo transferido** - Identifica que o bem foi baixado por transferência para outra filial.
* **Ativo baixado por período** - Identifica que o bem foi baixado por ter sido totalmente apropriado.
* **Ativo apropriado** - Identifica que o bem teve alguma parcela já apropriada.
* **Ativo com baixa parcial** - Identifica que o bem foi baixado parcialmente.

Seção 3 – Controle individual de parcelas por ativo (MATA906)

Esta rotina tem o objetivo de considerar um controle individual por ativo para o número de parcelas a serem estornadas. Com isso, é possível:

* Controlar ativos que já sofreram estornos em outros tipos de Sistemas de controle e que estão sendo migrados, sem que tenha ocorrido o término dos estornos das parcelas com direito ao crédito;
* Controlar ativos especiais, que apresentam números de parcelas para apropriação diferentes do padrão (48 ou 60 meses).
* Consumir parcelas quando houver a necessidade de atualizar o saldo de parcelas do bem, nos casos em que não houverem saídas tributadas em determinado mês para realizar a apropriação.

1. No **Livros Fiscais (SIGAFIS)**  acesse **Miscelânea/ Acertos/ Atualiza SF9** **(M906SF9)**, conforme indicado a seguir:

1. Nos parâmetros da rotina, é apresentada a seguinte solicitação:

Indique o tipo de atualização

A atualização da tabela SFA pode ocorrer de duas formas distintas (nas duas opções, a janela apresentará uma breve explicação dos processos que serão executados):

**1 = Parcial:** Indica que somente atualizará os ativos que possuírem o campo **Num. Parc.** **(F9\_QTDPARC ZERADO)**, ou seja, sem valor. Com a seleção desta opção e confirmação da rotina, se nenhuma alteração for efetuada será apresentada uma mensagem.

**2 = Geral:** Indica que independente dos campos possuírem ou não valores inseridos, serão recalculados e atualizados conforme tabela SFA. Com a seleção desta opção e confirmação e processamento da rotina, será apresentado um relatório resumo para os ativos atualizados.

**Importante**

Quando houver a necessidade de atualizar o saldo de parcelas do bem devido, quando não ocorreram saídas tributadas em determinado mês para realizar a apropriação, esta rotina deve ser executada com o tipo de atualização GERAL Desta forma, as parcelas devem ser contadas (consumidas do saldo de parcelas campo **Saldo Parc.** **F9\_SLDPARC**) mesmo nos mês onde NÃO houver apropriação, isto pode ocorrer quando a apropriação não foi realizada no mês (por não haver nenhuma saída tributada para o abatimento).

**Exemplo**: Um bem incluído em Jan/2010 para um período de 48 meses de apropriação se forem realizadas apropriações m jan/2010, Fev/2010, Abril/2010, no campo **Saldo Parc.(** **F9\_SLDPARC)** constará 45 (Resultado de 48 – 3 apropriações), contudo, o período decorrido da inclusão do bem se refere a 4 meses (Janeiro, Fevereiro, Março e Abril) 48 – 4 = 44. A partir daí, execute a rotina para analisar todas as apropriações e seus períodos, para que nestes casos o Sistema atualize o saldo de parcelas.

Seção 4 - Emissão Livro CIAP (MATR995)

Por meio desta opção de relatório, será emitido o Livro com os Registros do CIAP destinado à apuração do crédito a ser mensalmente apropriado referente à aquisição de bem do ativo permanente.

Os Modelos A e B são destinados à apuração do valor da base do estorno de crédito e do total do estorno mensal do crédito, relativamente ao crédito apropriado nos termos do Art. 20 § 5º da Lei Complementar nº. 87. Estes modelos referem-se a bens adquiridos até o ano 2000.

Os Modelos C e D são destinados à apuração do valor do crédito a ser mensalmente apropriado, nos termos do Art. 20 § 5º, da Lei Complementar nº. 87. Estes modelos referem-se a bens adquiridos a partir do ano de 2000.

Considerações

Nos Modelos A e C, o controle dos créditos do ICMS dos bens do ativo permanente será efetuado como um todo. Sua escrituração será feita com a identificação dos dados do contribuinte, demonstrativo da base do estorno do crédito a ser apropriado e demonstrativo da apuração do estorno de crédito a ser efetivamente apropriado, mês a mês.

Nos Modelos B e D, o controle dos créditos do ICMS dos bens do ativo permanente será efetuado individualmente. Sua escrituração será feita por bem, com a identificação dos dados do contribuinte, os dados referentes às entradas, saídas, perdas e apropriação mensal do crédito, no período estabelecido para apropriação, mês a mês.

Estas informações são dispostas por meio de **quadros**, obedecendo à legislação de cada modelo, sendo:

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

1. No **Livros Fiscais (SIGAFIS)**, acesse **Relatórios/ Livros Oficiais/ Emissão Livro CIAP (MATR995)**, clique em **Parâmetros** e preencha os dados conforme orientações a seguir:

Código de?

Informe o código do ativo inicial a ser processado.

Código até?

Informe o código do ativo final a ser processado.

Modelo A,B,C ou D?

Informe qual modelo de livro do CIAP deseja imprimir. A adoção dos modelos de livros para a escrituração (A ou B e C ou D) será feita de acordo com o disposto na legislação de cada Unidade Federada.

Data Fiscal de?

Informe a data inicial para o processamento das movimentações fiscais do período (faturamentos).

Data Fiscal até?

Informe a data final para o processamento das movimentações fiscais do período (faturamentos).

Taxa da UFIR?

Informe o valor da UFIR em vigor se o estado do declarante exigir a conversão dos valores para UFIR.

Ac. Demonst. de Apuração?

Informe se as colunas **Base de Crédito** e **Crédito a ser apropriado** devem ser acumuladas.

Data ativo de?

Para impressão do modelo C, informe a data inicial de aquisição dos ativos.

Data ativo até?

Para impressão do modelo C, informe a data final de aquisição dos ativos.

Imprime

Informe se deseja imprimir: apenas os livros, apenas os termos ou os livros e termos.

Nº da Ordem

Informe o número da ordem dos Termos de Abertura / Encerramento.

Nº da Página Inicial

Informe o número da página inicial que será impressa nos Termos de Abertura / Encerramento.

Qtd. Páginas / Feixe

Informe a quantidade de folhas que o livro contém.

Nº da Junta Comercial

Informe o número da Junta Comercial que será impresso nos Termos de Abertura / Encerramento.

Observações

Informe as observações necessárias que serão impressas no Termo de Abertura.

CRC do Contador

Informe o CRC do contador que será impresso nos Termos de Abertura / Encerramento.

Último Lançamento

Informe a data do último lançamento que será impressa no Termo de Encerramento.

Taxa UPF-RS

Informe a taxa de conversão em UPF. Esta pergunta é válida somente para o estado do Rio Grande do Sul, conforme a IN DRP 45 de26/10/98 - RS.

Modelo D em Folha Única?

Informe se o relatório modelo D será impresso em folha única, contendo os quatro quadros na mesma página, ou se deve ser emitido em duas páginas, com os quadros 1 e 2 na primeira página e os quadros 3 e 4 na segunda.

Seleciona Filiais?

Seleciona as filiais desejadas. Se NÃO apenas a filial corrente será afetada.

Aglutina CNPJ+IE?

Aglutina a impressão do relatório por CNPJ+IE respeitando a seleção de filiais realizada pelo usuário. Este tratamento somente será realizado quando utilizada a pergunta de seleção de filiais. Tratamento disponível somente para ambientes DBAccess.

1. Confira os parâmetros e configure a impressão do relatório

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028641212/mceclip4.png)
