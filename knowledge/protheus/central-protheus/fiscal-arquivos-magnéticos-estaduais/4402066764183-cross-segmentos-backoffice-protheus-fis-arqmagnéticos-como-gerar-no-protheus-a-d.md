---
article_id: 4402066764183
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: ed6e938ad463e55b7ed32c798c13a9113ab74208c0479f91539910daeecc6411
fetched_at: '2026-06-28T22:42:10.344294+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como Gerar no
  Protheus a Declaração de Informações Econômico-Fiscais (DIEF-MA)
type: support-article
updated_at: '2022-08-17T19:34:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402066764183-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-Gerar-no-Protheus-a-Declara%C3%A7%C3%A3o-de-Informa%C3%A7%C3%B5es-Econ%C3%B4mico-Fiscais-DIEF-MA
---

**Dúvida**Como gerar no Protheus a Declaração de Informações Econômico-Fiscais (DIEF-MA)  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**  
A **Declaração de Informações Econômico-Fiscais (DIEF-MA**) segue exatamente o mesmo *layout* do Sintegra.

A configuração abaixo está contemplando o SINTEGRA

1. Copie para a diretório \SYSTEM, a arquivo de configuração o SINTEG05.INI.

2. No Configurador (SIGACFG) acesse Ambientes /Cadastros /Menus e inclua, no menu do modulo Livros Fiscais (SIGAFIS), a opção para execução do SINTEGRA, conforme especificação a seguir:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7247709128087/mceclip0.png)

 No Configurador (SIGACFG], acesse Ambiente /Cadastros /Parâmetros verifique as parâmetros a seguir ou crie-as, caso não existam:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7247913142423/mceclip2.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7247925533079/mceclip1.png)

Este parâmetro é utilizado para a geração do SINTEGRA, com a finalidade 4 (Retificação Corretiva do Arquivo), somente para o estado do Espirito Santo — ES.

E verificando em conjunto com a parâmetro MV ESTADO que, nesse caso, deve obrigatoriamente estar preenchido como ES, e se estiver próximo a estes dois parâmetros, é ignorado o conteúdo do campo Finalidade.

Se o parâmetro MV\_FINA4ES estiver preenchido com .T. e o parâmetro MV ESTADO estiver preenchido como ES, é apresenta da uma tela alertando sobre a Retificação Corretiva. Verifique e proceda de acordo com sua necessidade.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248016778391/mceclip3.png)

Este parâmetro é utilizado nos casas em que exista uma nota fiscal conjugada, sendo um item com o CFOP 5101, par exemplo, e outro item de serviço (exemplo: CFOP 5933), para a correta geração dos registros 50 e 54.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248085206807/mceclip4.png)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248186244119/mceclip5.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248174953495/mceclip6.png)

Caso a parâmetro MV\_SINTEG nao exista ou não esteja preenchido, o programa a desconsidera os CFOPs constantes na portaria.

Se estiver preenchido, desconsidera os CFOPs informados no parâmetro. Os CFOPs sao informados a critério do cliente.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248216619671/mceclip7.png)

Caso o parâmetro esteja como F (desabilita ), o valor do IPI nas notas fiscais de comerciantes nao atacadistas, é apresentado normalmente no arquivo magnético. Caso o parâmetro esteja como T (habilita), a valor do IPI nas notas fiscais de comerciantes nao atacadistas não é apresentado.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248271863447/mceclip8.png)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248273114391/mceclip9.png)

Devem ser lançados os CFOPs de serviços, incluindo os de serviços de transporte. Este parâmetro é utilizado nos casos em que a nota fiscal possua um item com IPI que possa ser lançado no Registro Tipo 51 (exemplo: CFOP 1101) e outro item de serviço, que não deve ser lançado nesse registro. Os CFOps devem ser informados a critério do cliente.

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248329958167/mceclip10.png)

Este parâmetro é utilizado pelo relatório Registro de Inventario p7 para indicar se, no momento do calculo dos Saldos em Processo, o Sistema deve utilizar:

• O calculo novo (1) = a Sistema considera as saldos em processo proporcionais, ou seja, quando feito um apontamento de produção parcial, a quantidade não apontada permanece sendo considerada como saldo em processo;

• O calculo antigo (2) = a Sistema nao considera mais as saldos em processo quando feito um apontamento de produção, mesmo que parcial.

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248376824599/mceclip11.png)

Este parâmetro apenas é utilizado em caso de integração com o modulo de Exportação (SIGAEEC).

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248413573015/mceclip12.png)

No Registro 85, existe um campo denominado Tipo do Conhecimento. Deve ser apresentado com o conteúdo descrito pelo Convenio 20/04. Como essa informação na o esta disponível no Sistema, o conteúdo informado no parâmetro MV TPCONHE é a dotado para todos os Registros do tipo 85. Caso esse parâmetro não exista ou esteja em branco, serão gerados registros conteúdo a código 99 (Outras).

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248434631447/mceclip13.png)

Utilize esse parâmetro somente se a informação é realmente necessária.

No Configurador (SIGACFG), acesse Base de Dados / Dicionário / Base de Dados, verifique os campos informados nos parâmetros da rotina e inclua-os, quando necessário:

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248572873879/mceclip14.png)

O campo Tp. Conhec. (YQ\_TDC) esta vinculado a Tabela YK, que deve ser lançada na consulta padrão com a seguinte estrutura (as informações apresentadas nessa consulta têm par base a tabela de Tipo de Documento de Carga do SISCOME X):

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248606948375/mceclip15.png)

![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248609161367/mceclip16.png)

Caso o campo Tp. Conhec. (YQ\_TDC) nao exista, o campo Tipo de Conhecimento de Transporte do Registro Tipo 85 é gerado com o padrão, lançado no parâmetro MV\_TPCONHE.

Esse parâmetro apenas é utilizado caso exista integração com o modulo de Exportação• (SIGAEEC).

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248650655511/mceclip17.png)

A criação do campo Autenticação (F6 AUTENT) permite identificar a numero da autenticação bancaria. Caso o campo nao exista ou seu conteúdo não seja preenchido, é assumido o Numero da GNRE (F6 NUMERO) como padrão.

Caso seja necessário utilizar pontos de entrada disponibilizados para a geração de alguns registros do SINTEGRA, configure -os conforme indicações a seguir:

Para o Registro. Tipo 54

• A940NCM - Ponto de entrada que permite a tratamento para a NCM.

0 registro 56 é gerado por meio dos pontos de entrada:

• MTA56S — Preencha a arquivo temporário (R56) com os itens dos movimentos de saída.

• MTA56E - Preencha a arquivo temporário (R56) com as itens dos movimentos de entrada.

A estrutura do arquivo temporário R56 que deve ser preenchido nos dois pontos de entrada, é a mesma:

![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7248977031063/mceclip18.png)

O Registro 70 pode ser gerado par meio do ponto de entrada:

• MTATIP70 -  Preencha o arquivo temporário (R70).  
Esse ponto de entrada é chamado cada vez que for processado um novo registro do Livro Fiscal (SF3) referente a nota fiscal de transporte.

A estrutura do arquivo temporário R70 é:

![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7249069172631/mceclip19.png)

![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7249070315287/mceclip20.png)

0 Registro 71 é gerado por meio do ponto de entrada:

* **MTATIP71** - preencha o arquivo temporário (R71).

Esse ponto de entrada é chamado cada vez que for processado um novo registro do Livro Fiscal (SF3) referente a nota fiscal de transporte.

A estrutura do arquivo temporário R71 é:

![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7249073805463/mceclip21.png)

Os Registros 85 e 86 podem ser gerados por meio dos pontos de entrada descritos a seguir:

• MTA85B6 - preencha os arquivos temporários (RBS/R86).

0 arquivo para o registro do tipo 85 deve conter um registro para cada averbação efetuada no período, de forma independente da data de emissão da nota fiscal de exportação.

0 arquivo para o registro do tipo 86 deve conter um registro para cada item da averbação efetuada no período, de forma independente da data de emissão da nota fiscal de exportação.

A estrutura dos arquivos temporários R85 e R86 é a seguinte:

![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7249169192471/mceclip22.png)

![mceclip23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7249170633495/mceclip23.png)

![mceclip25.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7249177739799/mceclip25.png)

Alguns campos digitados no arquivo temporário possuem tamanho diferente do informado no layout do SINTEGRA para geração dos registros 85 e 86.

Essa diferença se deve ao fato de que esses registros sao gerados par meio da integração com o modulo de .” Exportação (SIGAEEC). Assim, o tamanho dos campos foi mantido de acordo com a existente hoje, no padrão do modulo de Exportação i (SIGAEEC]. Vale lembrar que o arquivo .INI processado, trunca a informação de acordo com a tamanho do layout.

O campo Declaração de Exportação (ABS DECL) possui 20 caracteres no arquivo temporário, mas a informação de Declaração de Exportação (ABS DECL) do registro tipo 85 possui apenas 11 caracteres. Neste caso, se este campo estivesse preenchido com o conteúdo 12345678901bbbbbbbbb (sendo as caracteres b caracteres em branco) no arquivo magnético gerado, somente seriam apresentadas as 11primeiras posições (no caso 12345678901).

Desta forma, as informações são apresentadas de acordo com a informado no arquivo .INI, independente do tamanho do campo processado.  
Exemplos de campos com diferença no tamanho do arquivo temporário para o layout do SINTEGRA:

![mceclip26.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7249270502039/mceclip26.png)

Todas as informações serão apresentadas com a tamanho especificado no *layout.*

Ponto de entrada **MTGETS** - Ponto de entrada localizado em Instruções Normativas (MATA950], na função FisGetSer. Este ponto

de entrada foi criado para retornar a série da nota fiscal valida para as validadores.

Ponto de **entrada** MATA940A — Este ponto de entrada é chamado antes do programa gravar a arquivo pré-formatado. Se u objetivo é tratar eventuais casos particulares.

O arquivo a ser gerado e importado para a DIEF/MA é o mesmo gerado para a SINTEGRA, desta forma utilize a SINTEG05.INI e gere o arquivo a partir da rotina MATA940 **(SINTEGRA),** importe para a programa da DIEF-MA e preencha as demais informações requeridas pelo programa.

 

1. Em **Livros Fiscais (SIGAFIS),** acesse **Miscelânea/**  **Magnéticos/ SINTEGRA** (MATA940) e configure os para metros da rotina:

**Data Inicial?**

Informe a data inicial para geração das informações.

**Data Fina I\***

Informe a data final para geração das informações.

**Layout?**

E par meio da configuração desse parâmetro que o Sistema determina a arquivo a ser gerado. Deve ser informado o nome do arquivo

.**INI** de configuração do *layout.* Para esse caso, informe **SINTEG05**.

**Arquivo Destino?**

Informe o nome do arquivo magnético a ser gerado. Exemplo: **SINTEGRA.txt**

**Finalidade?**

Selecione a opção que contemple as operações efetuadas no período (Normal, Retificação Total, Retificação Aditiva, Retificação Corretiva ou Desfazimento), sendo:

* Retifica sao Total: Substituição total de informações prestadas pelo contribuinte, referentes ao período;
* Retifica sao Aditiva: Acréscimo de informação nao incluída em arquivos ja apresentados;
* Desfazimento: Arquivo  de informação referente a operações/prestações nao efetivadas.

**UF Orig./Dest.\***

Informe o estado de origem e/ou destino das operações realizadas no período a ser considerado na geração do arquivo magnético.

### Importante

Quando há necessidade de gerar todas as operações, independente do Estado de origem/destino, esse parâmetro deve ser deixado em branco.

**Processa UF?**

* Selecione Somente UF quando desejar gerar somente as operações com Estado de origem/destino igual ao Estado informado no parâmetro
* Selecione Exceto UF quando desejar gerar somente as operações com estado de origem/destino diferente do Estado informado no parâmetro

**Numero do Livro?**

Numero do livro a ser considerado. Se nao houver classificação de livros por numero, este campo deve ser preenchido com asterisco (\*)

**Equipamento?**

Informe  a descrição  do equipamento  utilizado na geração do arquivo magnético.

**Gera Inventario?**                                                                                                                                                                                                   ,

Preencha este parâmetro com **Sim**, se for necessário gerar a registro de inventario Tipo 74.                                                                                                                                                                                         

**Notas Fiscais?**

Selecione a tipo de movimentação de notas fiscais a ser considerada na geração do arquivo magnético (entrada/saída/ambas).                                                                                                                                       

**Gera Registro 60D?**

Se for necessário gerar o registro 60D, selecione a opção Sim. A geração desse registro fica facultada a cada Unidade Federação.                                                                                                                                                                                                  '

**Drive Destino?** Informe o *drive* destino em que deve ser gerado o arquivo destino.

**Transportadora?**

A partir da indicação da transportadora, o Sistema seleciona os documentos de saída que utilizaram o código da transportadora indicado, para geração do SINTEGRA Amazonas.

**Data Fechamento?**

Deve ser informada a data de fecha mento do estoque, somente quando efetuar registro de inventario retroativo.

**Gera Registro 60R?**

Selecione a opção Sim para gerar a Registro 60R, caso seja exigido pela Unidade de Federação.

**Gera Registro 61R?**

Selecione a opção Sim para gerar a Registro 61R, caso seja exigido pela Unidade de Federação.

**Gera NF Produtor?**

Selecione a opção Sim para gerar a arquivo do SINTEGRA, incluindo as dados das notas fiscais do produtor, caso seja exigido pela Unidade de Federação.

**Meio Magnético?**

Informe o tipo de meio magnético onde deve ser gravado o arquivo gerado para entrega a Receita Federal.

**Fator de Bloco?**

Fator de bloco de gravação (numero de volumes) do meio magnético em que deve ser gravado o arquivo gerado para entrega a Receita Federal. Exemplo: 1/2.

**Natureza das Operações?**

Informe a natureza das operações apresentadas: Interestaduais com Substituição Tributaria, Interestaduais ou Totalidade (para geração do Registro 10).

**Destaca PIS/COFINS\***

Informe se o contribuinte destaca as valores de PIS/ CO FI NS no corpo do documento fiscal.

**NF De?**

Informe a numero da nota fiscal de venda inicial para filtrar quais notas fiscais devem ser apresentadas no meio magnético. Esse parâmetro deve ser utilizado pelas usinas que efetuam venda de álcool, para os contribuintes inscritos no estado da Bahia, para geração do arquivo magnético N FE - Nota Fiscal  Eletrônica.

**NF Até?**

Informe a numero da nota fiscal de venda final para filtrar quais notas fiscais devem ser apresentadas no meio magnético. Esse parâmetro deve ser utilizado pelas usinas que efetuam venda de álcool, para as contribuintes inscritos no estado da Bahia, para geração do arquivo magnético N FE - Nota Fiscal Eletrônica.

**Filial De?**

Informe a filial inicial para o processamento centralizado. Caso a processamento nao seja centralizado, deixe esta pergunta em branco.

**Filial Até?**

Informe a filial final para a processamento centralizado. Caso o processamento nao seja centralizado, deixe esta pergunta em branco.

**Consolidação na mesma UF?**

Atendimento ao Art. 121 do Anexo 5 do RICMS/SC. Esse artigo determina que todo prestador de serviço de transporte deve apresentar as obrigações acessórias de forma consolidada pelo estabelecimento matriz e esta consolidação deve abranger somente as empresas que estiverem domiciliadas no mesmo estado do estabelecimento matriz. A opção sim indica que é considerado esse tratamento; a opção não indica o contrario.

### Importante

Os Filtros a seguir somente serão considerados quando o parâmetro **Gera Inventario** estiver preenchido como **Sim**.

0s mesmos foram criados para que as dados gerados no registro de inventario do SINTEGRA coincidam com as dados gerados no relatório oficial P7 de inventario ou alguma necessidade especifica do contribuinte.

E de total responsabilidade do contribuinte a configuração dos mesmos. Recomendamos que todos as parâmetros sejam informados, de maneira a considerar todos os produtos solicitados pelo FISCO.

**Filtro Tipo Produto**

Informe se necessário a filtro dos Tipos de Produtos que devem ser gerados no inventario. Caso nao utilize nenhum tipo de filtro, deixe o campo em branco.

### Importante

Caso seja necessário filtrar varios tipos de produtos, separe-os com virgulas. Exemplo: PA, II, MO.

**Produto De**

Informe o produto inicial a ser processado. Caso queira que todos os produtos sejam considerados deixar campo em branco.

**Produto Até**

Informe se necessário a produto final a ser processado. Caso queira que todos os produtos sejam considerados preencher com ZZZZZZZZZZZZZZZZZZZ.

**Armazém De**

Informe a armazém inicial a ser processado. Caso queira que as produtos de todos os armazéns sejam considerados deixar campo em branco.

**Armazém Até**

Informe o armazém final a ser processado. Caso queira que as produtos de todos as armazéns sejam considerados preencher com ZZ.

**Prods.c/Saldo Neg.**

Selecione a opção Sim para que a registro de inventario do SINTEGRA considere as produtos com saldo em estoque negativo.

**Prods.c/Saldo Zera.**

Selecione a opção Sim para que a registro de inventario do SINTEGRA considere as produtos com saldo em estoque zerado.

**Prods.c/Saldo Poder 3°.**

* Selecione a opção **Sim** para que a registro de inventario do SINTEGRA considere a saldo De/Em
* Selecione a opção **Não** para que o registro de inventario do SINTEGRA não considere a saldo De/Em
* Selecione a opção **De Terceiros** para que o registro de inventario do SINTEGRA considere a saldo  de terceiros.
* Selecione a opção **Em Terceiros** para que a registro de inventario do SINTEGRA considere a saldo Em **Prods.c/Custo Zera.**

Selecione a opção **Sim** para que a registro de inventario do SINTEGRA considere as produtos com custo zerado.

**Gera 88 MG?**

Essa pergunta somente tem efeito para geração do SINTEGRA de Minas Gerais. Informe se, para a SINTEGR de Minas Gerais os registros 88 - ressarcimento deve ser apresentado. Para isso, é necessário processar o estoque na data informada próxima pergunta.

**Data BB?**

Essa pergunta somente tem efeito para geração do SINTEGRA de Minas Gerais. Informe a data a ser considerada na geração dos registros 88 para o processo de ressarcimento de ICMS ST do SINTEGRA de Minas Gerais. Como existe a possibilidade de a Registro de Inventario (74) ser gerado com data diferente dos registros 88, a informação dessa data se faz necessária.

**Gera Relat. Rest. MG?**

Essa pergunta somente tem efeito para geração do SINTEGRA de Minas Gerais. Imprime relatório de conferência de restituição de ICMS ST de Minas Gerais.   

 **Saldo Processo?**

Considera saldos em processo para geração das informações de inventario. Se essa pergunta for preenchida como sim, além dos saldos físicos, o Sistema levara para o registro 74, os saldos em processo da empresa.                                                                                                                            

**Lista MOD Processo?**

Utilizada para verificar se as requisições para MOD com saldo em processo devem ser impressas. Essa informação somente é considerada se a pergunta **Saldo em Processo** estiver preenchida com **Sim**.

### Importante

As perguntas P**roduto De, Produto Até, Armazém De, Armazém Até, Prods.c/Saldo Neg., Prods.c/Saldo Zera., Prods.c/Saldo Poder 3°., Prods.c/Custo Zera., Saldo Processo? e Lista MOD Processo?,** tem a finalidade de efetuar as mesmas filtros do livro Reg. Inventario P7 (MATR460), apresentando as mesmas informações das duas obrigações acessórias, desde que a data de fechamento do estoque e as perguntas referentes ao estoque para a geração do SINTEGRA sejam as mesmas informadas na geração do relatório.

**Processa filiais?**

Informe se deseja processar filiais. Neste caso, é aberta uma janela para informar quais filiais deseja processar, desconsiderando as perguntas de filial de/até.

Gera Registro 60I?

Se for necessário gerar o registro 601, selecione a opção Sim. A geração desse registro fica facultada a cada Unidade de Federação.

**Gera Reg. Tipo BB Det. 06?**

Informe se para a GIM - Paraíba, as registros do tipo 88 detalhe 06 devem ser apresentadas.

**Gera Reg. 8827 e BB28?**

Informe se deve gerar os detalhes 27 e dois do registro 88 da GIM da Paraíba.

**Gera Reg. 8830?**

Informe se para a GIM - Paraíba, a registro do tipo 88 detalhe 30 deve ser apresentado.

**Simples Nacional?**

Contribuinte Inscrito no Regime Simples Nacional.

**Arq. Período Atual ?**

Informe o nome do arquivo da apuração do Simples NacionaI relativo a apura Rao atua l.

**Gera Reg. 53 (Entradas)?**

Informe se para o SINTEGOS, a registro 53 deve ser gerado para Entradas.

Confira os parâmetros e confirme clicando em **Finalizar**.

Após a confirmação dos parâmetros, a Sistema apresenta uma tela de parametrização de impressão. Configure a impressão e confirme. Ao final do processamento, é impressa uma listagem de acompanhamento dos registros gerados.

**Tabela de Modelos de Notas Fiscais**  
Os modelos das notas fiscais do Sistema sao obtidos par meio da tabela:

![mceclip27.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7250362601239/mceclip27.png)

Para qualquer espécie de nota fiscal que seja diferente desta tabela, o Sistema assume como padrão a Modelo 01. Caso tenha criado uma espécie de nota fiscal diferente das relacionadas na tabela, pode ser utilizado a ponto de entrada MTMODNOT, que esta localizado na função AMODNOT(), dentro do programa FISXFUN.PRX.

**Tratamento de códigos de produto**

Ao final do processamento da rotina é apresentada uma mensagem ao usuário responsável, ou seja, um alerta de informações inconsistentes no arquivo magnético gerado. Esta mensagem é apresentada caso a rotina encontre no período produtos que tenham códigos com numero maior ou menor que 14 caracteres.

Devido a esse tratamento sistémico que foi implementado para contornar uma limitação do Sintegra, a aplicação nao considera mais a código original do produto para compor os registros deste arquivo, e sim a classificação NCM do mesmo (se não utilizar a PE A940pRD ) mais a valor da função RECNO () - que retorna a numero do registro atualmente posicionado na área de trabalho, isso somente para as produtos que superam esse limite do software validador do SINTEGRA, que segundo o layout, permite no máximo 14 caracteres para o código do produto para os registros pertinentes, por exemplo, a registro 54, a registro 74, etc.

Esse tratamento, caso seja feito somente para uma parte dos produtos, poderá ocasionar erros na entrega da obrigação, pois não aglutinara corretamente os produtos e consequentemente não terá seus valores do registro 74 (I inventário) coincidindo com a própria Livro Oficial P7.

O tratamento ideal para este item é que todos os produtos estejam com quantidade de caracteres em seu código, superior a 14 posições, ou que todos sejam inferiores. Se o ambiente tiver somente a metade do cadastro de uma forma, e a outra metade diferente, o problema relatado acima ocorrera.

**Observação:**  
O Sistema busca a RECNO mais o NCM para não ocasionar problemas com duplicidade de produtos que utilizam o mesmo NCM.

As notas em lote e as notas de ISS sao desconsideradas na geração do arquivo magnético

**Registro Tipo 10  - Mestre do Estabelecimento**

As informações contidas neste registro são obtidas par meio do cadastro da empresa no Sistema.

**Registro Tipo 11- Dados complementares do informante**

As informações contidas neste registro são obtidas por meio do cadastro da empresa no Sistema.

**Registro Tipo 50 - Notas Fiscais**

Este registro é gerado a partir do livro fiscal e é composto de notas fiscais dos seguintes modelos:

• Nota Fiscal Modelo 1 ou 1-A;

• Nota Fiscal de Serviço de Comunicação, Modelo 21;

• Nota Fiscal de Produtor, Modelo 4;

• Nota Fiscal/Conta de Energia Elétrica, Modelo 6;

• Nota Fiscal de Serviço de Telecomunicações, Modelo 22;

• Nota Fiscal Modelo 55 (SPED);

• Nota Conhecimento de Transporte Modelo 57 (SPED);

• Nota Fiscal sem Modelo (em branco, com exceção das Notas Fiscais de Serviço ).

So é emitido registro para nota fiscal de produtor (Modelo 4), quando a pergunta Tipo Nota Produtor estiver preenchida como Registro 50.

Atualmente, o Sistema não trata Lançamento Extemporâneo, pois a regra deste documento fiscal é desconhecida. 0s documentos de Uso Denegado e Uso Inutilizado ja são tratados pelo Sistema, conforme Convenio ICMS 42, de 03/07/2009.

**Registro Tipo 51 - Total da Nota Fiscal quanto ao IPI**

Este registro é gerado a partir do Livro Fiscal, e é composto de notas fiscais dos seguintes modelos:

• NF Modelo 1;  
• Nota Fiscal Modelo 55 (SPED);  
• NF sem Modelo (em branco).  
A nota fiscal deve possuir a valor de IPI (Tributado, Isento ou Outras).

**Registro Tipo 53 - Substituição Tributária**

Este registro é obrigatório para contribuinte Substituto Tributário, e é gerado a partir do Livro Fiscal.

**Registro Tipo 54 - Itens dos Documentos Fiscais**

Este registro é gerado a partir dos arquivos: Cabeçalho NF de Entrada, Itens da NF de Entrada, Cabeçalho da NF de Saída, Itens da NF de Saída e Livros Fiscais. E gerado um registro 54 para cada produto/serviço constante no documento fiscal e contempla notas fiscais dos modelos:

* Nota Fiscal Modelo 1;
* Nota Fiscal Modelo 55 (SPED);
* Nota Fiscal de Produtor 04;
* Nota Fiscal sem Modelo (em branco).

Em atenção ao item 14.1.1.1 do Manual de Orientação da Portaria CAT n°. 32/96, que dispõe sobre a geração dos registros 54 (Mercadoria e Serviço) do SINTEGRA, é gerado um registro para cada mercadoria/produto ou serviço constante no documento fiscal, exceto para aqueles que se refiram aos seguintes CFOPs:

* CFOps de 3 dígitos: 73, 2.73, 1.74, 2.74, 1.91, 2.91, 3.91, 1.92, 2.92, 1.97, 2.97, 3.97, 1.98, 2.98, 5.91, 6.91, 6.92, 5.95, 6.96
* CFOps de 4 dígitos: 406, 2.406, 1407, 2407, 1551, 1556, 2551, 2556, 3551, 3556, 1552, 1557, 2552, 2557, 5551, 6551, 7551,5552, 5557, 6552, 6557, 5553, 5556, 6553, 6556, 7553, 7556

O Sistema trata esse procedimento automaticamente, mas, caso o contribuinte necessite alterar as CFOPs citados, deve editar o parâmetro **MV\_SINTEG,** pelo modulo Configurador **(SIGACFG),** atribuindo ao seu conteúdo todos os CFOPs que devem ser desconsiderados na geração do registro.

0 registro 54 referente a PIS/COFINS (numero sequencial do item 993) deve ser gerado apenas quando houver destaque do valor no corpo do documento fiscal. Assim, somente é gerado quando a pergunta Destaca PIS/COFINS estiver preenchida com Sim.

Esse registro nao é gerado quando o documento fiscal for Modelo 4 (Produtor Rural). Consequentemente, também nao é gerado o Registro Tipo 75.

Caso seja uma nota fiscal conjugada que contenha varios CFOPs diferentes na mesma nota fiscal, sendo pelo menos um deles de serviço, também é pré-requisito para a gera tão do Registro Tipo 54.

**Registro Tipo 55 - Guia Nacional de Recolhimento de Tributos Estaduais**

Este registro é gerado a partir da Guia Nacional de Recolhimento

**Registro Tipo 56 - Operações com veículos automotores novos**

Este registro deve ser gerado par meio de programa personalizado, pois a Sistema não possui todas as informações necessárias.

Informe todas as movimentações efetuadas no período com veículos automotores novos.

**Registro Tipo 60 - Cupom Fiscal**

Este registro é gerado a partir do Cadastro de Resumo de Redução Z, e é utilizado somente para operações de saída em que foi emitido cupom fiscal, contemplando os seguintes modelos de documentos fiscais:

* Cupom Fiscal;
* Cupom Fiscal - PDV;
* Bilhete de Passagem Rodoviário, Modelo 13;
* Bilhete de Passagem Aquaviário, Modelo 14;
* Bilhete de Passagem e Nota de Bagagem, Modelo 15;
* Bilhete de Passagem Ferroviário, Modelo 16;

**Registro Tipo 60M - Mestre: Identificador do equipamento**

Este registro é gerado a partir do Cadastro de Resumo de Redução Z, e é utilizado somente para operações de saída em que foi emitido cupom fiscal.

Observe que, caso o parâmetro UF Origem/ Destino seja diferente do cadastro da empresa no Sistema, nao são gerados as registros referentes ao cupom fiscal.

**Registro Tipo 60A Subtipo 60A Analítico: Identificador de Substituição Tributária**

Este registro é gerado a partir do Cadastro de Resumo de Redução Z, e é utilizado somente para operações de saída em que foi emitido cupom fiscal.

Observe que, caso a parâmetro UF Origem/ Destino, seja diferente do cadastro da empresa no Sistema, nao são gerados os registros referentes ao cupom fiscal.

**Registro Tipo 60 - Subtipo 60D - Resumo Diário**

Este registro é gerado a partir dos itens da nota fiscal de saída e do parâmetro Gera de saída. Observe os seguintes aspectos:

* O campo **Numero PDV,** d os Itens de Venda da Nota Fiscal, deve estar preenchido ;
* 0 campo Série ECF, do Cabeçalho das Notas Fiscais de Saída, deve estar preenchido com e é composto par notas fiscais

**Registro Tipo 60 - Subtipo 60I - Item do Documento Fiscal**

Este registro é gerado a partir dos itens da nota fiscal de saída e do parâmetro Gera Registro 60I, e é composto par notas fiscais de saída. Observe os seguintes aspectos:

* O campo **Numero PDV,** d os Itens de Venda da Nota Fiscal, deve ser preenchido;
* O campo Série ECF, do Cabeçalho das Notas Fiscais de Saída, deve ser preenchido com S.

**Registro Tipo 60 - Subtipo 60R - Resumo Mensal**

Este registro é gerado a partir dos itens da nota fiscal de saída e do parâmetro Gera Registro 60R, e é composto par notas fiscais de saída. Observe os seguintes aspectos:

* O campo **Numero PDV,** d os Itens de Venda da Nota Fiscal, deve ser preenchido;
* O campo Série ECF, do Cabeçalho das Notas Fiscais de Saída, deve ser preenchido com

### Importante

Na geração do registro 60R não sao considerados as Vendas de CST CANC (Canceladas) e DESC (Descontos).

Este registro é gerado a partir do Livro Fiscal, e é composto por notas fiscais dos seguintes modelos (quando nao emitidos por equipamentos emissores de cupom fiscal):

* Bilhete de Passagem Aquaviario, Modelo 14;
* Bilhete de Passagem e Nota de Bagagem - Modelo 15;
* Bilhete de Passagem Ferroviário, Modelo 1;
* Bilhete de Passagem Rodoviário, Modelo 13;
* Nota Fiscal de Venda ao Consumidor, Modelo 2;
* Nota Fiscal de Produtor, Modelo 4;
* Nota Fiscal de Serviço de Transporte, Modelo 7 (exceto quando emitida por prestador de serviços de transporte ferroviário de cargas).

### Importante

Para que o Sistema capture corretamente as subséries, para as notas que as necessitam indicar no campo serie da nota fiscal a serie e a subsérie junta (sem a utilização do caractere —, exemplos:

D1, D2, DU......

**Registro Tipo 61R**

Este registro é gerado a partir das notas fiscais de saída, contendo os dados das notas fiscais de venda ao consumidor nao emitidas por ECF. Se o parâmetro **Gera NF Produtor** estiver configurado com **Sim**, são incluídos as dados da nota fiscal de produtor.

### Importante

Esse registro nao é obrigatório, cabendo a cada Unidade de Federação optar, ou nao, pela sua geração.

**Registro Tipo 70 - Nota Fiscal de Serviço de****Transporte**

Este registro é gerado a partir do Livro Fiscal, e é composto de notas fiscais dos modelos: Nota Fiscal de serviço de Transporte;

* Conhecimento de Transporte Rodoviário de Cargas;
* Conhecimento de Transporte Aquaviário de Cargas;
* Conhecimento de Transporte Ferroviário de Cargas;
* Conhecimento de Transporte Eletrônico;
* Conhecimento Aéreo.

Para usuários que nao possuem integração com a modulo **Gestão**de **Transporte (SIGATMS),** e geram O registro tipo 71 par meio ‹ de personalização, esta disponível a criação de um ponto de entrada para a geração desse registro, e a exemplo de construção, para que nao tenha inconsistências entre os registros 70 e 71.

**Registro Tipo 71 - Informação da Carga Transportada**                                                                           Este registro somente é gerado automaticamente para as usuários que possuem integração com a modulo Gestão de  Transportes (SIGATMS). Para as demais, o registro pode ser gerado par meio de personalização, pois a Sistema não possui todas as informações necessárias.   
Devem ser apresentadas apenas as notas fiscais de saída.

**Registro Tipo 74 - Inventário**

Este registro é gerado a partir do cadastro de produtos, saldo físico e financeiro e saldo em poder de terceiros. São gerados as registros dos produtos que tiveram movimentação durante o período selecionado.

**Registro Tipo 75 - Código do Produto ou Serviço**

Especifica cada código de produto/serviço que conste no Registro 54, apresentando dados cadastrais e seguindo as mesmas regras de geração do Registro 54. Somente é gerado o registro 75 de produtos/serviços que possuem pelo menos um Registro 54 equivalente.

**Registro Tipo 76 - Nota Fiscal de Comunicação: telecomunicações**

• Nota Fiscal de Serviços de Comunicação (Mod. 21) nas prestações de serviço;

• Nota Fiscal de Comunicação e Telecomunicação (Mod. 22) nas prestações de serviço.

### Importante

Utilizado somente para notas fiscais de saída.

**Registro Tipo 77 - Serviço de Comunicação e Telecomunicação**

Este registro é gerado a partir do Livro Fiscal, e é composto de notas fiscais dos seguintes modelos:

• Nota Fiscal de Serviços de Comunicação (Mod. 21) nas prestações de serviço;

• Nota Fiscal de Comunicação e Telecomunicação (Mod. 22) nas prestações de serviço.

**Registro Tipo 85 - Informações de Exportações**

Este registro informa dados relativos a exportação, e é obrigatório para as empresas comerciais exportadoras e Trading Compani’es. Tem as seguintes características:

Contém cada declaração de exportação averbada, e é gerado para os clientes que possuem integração com o modulo de Exportação (SIGAEEC], que contém informações referentes as exportações, ou por meio de personalização.  
E gerado um registro do tipo 85 para cada exportação averbada no período, de forma independente da data de emissão da nota fiscal de exportação.

A integração com o modulo de Exportação (SIGAEEC) é feita por meio do parâmetro MV\_EECFAT.

**Registro Tipo 86 - Informações complementares de Exportação**

Esse registro informa dados relativos a exportação, e é obrigatório para as empresas comerciais exportadoras e Trading Compani’es. Tem as seguintes características:

É gerado um Registro 86 para cada Registro de Exportação/Nota Fiscal de Remessa, informando os dados relativos aos produtos envolvidos na exportação.  
Esse registro é gerado para os clientes que tem integração com o modulo de Exportação (SIGAEEC), que contém informações referentes as exportações, ou par meio de personalização.

E gerado um registro do tipo 86 para cada item contido na exportação averbada no período, de forma independente da data de emissão da nota fiscal de exportação.

O registro apenas é gerado para movimentações equiparadas a exportação. Exportações diretas geram apenas o Registro tipo 85.

**Registro Tipo 90 - Totalização do Arquivo**

Contém os totalizadores de todos as tipos de registros existentes no arquivo magnético.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7264085260695/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7264071216663/mceclip2.png)

Para geração do arquivo é utilizado o arquivo de layout **SINTEG05.INI** no qual deverá ser inserido na pasta system do Protheus.

O arquivo **SINTEG05.INI** esta disponível no link abaixo dentro da pasta ESTADUAL

<https://suporte.totvs.com/portal/p/10098/download#detail/947481>

Fontes que são utilizados para geração da DIEF-MA:  
  
MATA940 (Sintegra) e MATXMAG  
  
Abaixo Link referente a expedição continua do módulo fiscal para que possa baixar e efetuar testes com os fontes mencionados acima:

Link centralizador com todas as releases  
<https://tdn.totvs.com/pages/releaseview.action?pageId=525823851>

Para testes pontuais referente a geração da DIEF-MA, a principio, não será necessário efetuar aplicação do dicionário de dados contido nas  atualizações acima.
