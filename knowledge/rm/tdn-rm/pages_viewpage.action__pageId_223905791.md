---
content_hash: 7c314aa469291b1b6aeebf884e6d3fa498c54ea252ba55d5d07603fab1e50c55
fetched_at: '2026-06-29T00:06:21.941380+00:00'
page_id: '223905791'
product: rm
source: tdn-rm
title: ER_FEM – Cálculo do Fundo de Erradicação da Miséria e Combate à Pobreza - MG
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223905791
version: 34
---

**Módulo**: Gestão Fiscal

**Ação**: Implementação FEM – Calculo do Fundo de Erradicação da Miséria e Combate à Pobreza - MG

**Chamado de Origem**: TTWKG7   
   
 **Legislação**

Decreto 45.934/2012 de Minas Gerais: Na operação interna que tenha como destinatário consumidor final e na operação interestadual que tenha como destinatário pessoa não contribuinte do ICMS, com determinadas mercadoria, a alíquota do ICMS prevista no inciso I do art. 42 do Regulamento do ICMS (RICMS), aprovado pelo Decreto nº 43.080, de 13 de dezembro de 2002, será adicionada de dois pontos percentuais.

*[1 - Link da Legislação](http://www.fazenda.mg.gov.br/empresas/legislacao_tributaria/decretos/2012/d45934_2012.htm)*

Efeitos a partir de **01/01/2016** - Redação dada pelo art. 3° e vigência estabelecida pelo art. 12, II, ambos da  Lei nº 21.781, de 01/10/2015:

Art. 12-A.  Fica estabelecido, para os fins do disposto no § 1° do art. 82 do Ato das Disposições Constitucionais Transitórias da Constituição da República, com vigência até 31 de dezembro de 2019, o adicional de dois pontos percentuais na alíquota prevista para a operação interna que tenha como destinatário consumidor final, contribuinte ou não do imposto, com as mercadorias abaixo relacionadas, inclusive quando a alíquota for fixada no regulamento do imposto:

*[2 - Link da Legislação](http://www.fazenda.mg.gov.br/empresas/legislacao_tributaria/leis/2015/l21781_2015.htm)*

Efeitos a partir de **01/01/2016** - Acrescido pelo art. 3° e vigência estabelecida pelo art. 12, II, ambos da Lei nº 21.781, de 01/10/2015:

I - cervejas sem álcool e bebidas alcoólicas, exceto aguardentes de cana ou de melaço;  
 II - cigarros, exceto os embalados em maço, e produtos de tabacaria;  
 III - armas;  
 IV - refrigerantes, bebidas isotônicas e bebidas energéticas;  
 V - rações tipo pet;  
 VI - perfumes, águas-de-colônia, cosméticos e produtos de toucador, exceto xampus, preparados antissolares e sabões de toucador de uso pessoal;  
 VII - alimentos para atletas;  
 VIII - telefones celulares e Smartphone  
 IX - câmeras fotográficas ou de filmagem e suas partes ou acessórios;  
 X - equipamentos para pesca esportiva, exceto os de segurança;  
 XI - equipamentos de som ou de vídeo para uso automotivo, inclusive alto-falantes, amplificadores e transformadores.

*[3 - Link da Legislação](http://www.fazenda.mg.gov.br/empresas/legislacao_tributaria/leis/l6763_1975_02.htm)*

**ICMS****Próprio**

Seleção dos Dados

* Lançamento de Saída Interno independente da situação do destinatário (Consumidor Final,  Não consumidor Final,  Contribuinte ou Não Contribuinte).
* Os valores do FECP/FEM serão calculados com base nos campos “Base de Calculo ou Outros do ICMS” valores estes informados nos itens dos Lançamentos Fiscais\Sub Pasta Valores ICMS. Somente serão considerados itens que tem o novo campo “%FECP” preenchido no cadastro do Produto.
* Entrada – Devolução de Venda, cuja a saída, é considerada na alíquota mais 2 %.

**Cálculo**

* FECP-MG Apuração ICMS Próprio

Deve ser adicionado à alíquota do ICMS, equivalente a 2% da Base de Cálculo Própria das NF de saída, das operações internas, relativas às mercadorias relacionadas no artigo 2º do Decreto nº 45.934 de 22/03/2012, que não estejam sujeitas à substituição tributária, quando vendidas a consumidor final.

|  |  |  |
| --- | --- | --- |
| Exemplo de Calculo ICMS Próprio |  |  |
|  |  |  |
| Operação Interna |  |  |
| Alíquota Interna | 18% |  |
| % FECP (FEM) | 2% |  |
| Base de Calculo | 1.000,00 |  |
| Alíquota Saída | 20% |  |
| Valor do ICMS | 180,00 | (1.000,00 \* 18%) |
| Valor FECP MG | 20,00 | (1.000,00 \* 2%) |

**ICMS ST** 

Seleção de Dados

* Lançamento de Saída Interno, cujo Tipo do ICMS é Venda com ST, Red. B.C e S.T, Isento ST, informado na Natureza Fiscal\Regra do ICMS.
* Lançamento de Entrada Interno, cujo Tipo do ICMS “ST Retido na Compra”, informado na Natureza Fiscal\Regram do ICMS e o Campo Retenção ICMS ST habilitado Substituto Tributário.
* Os valores do FECP/FEM será calculado com base no campo “Base de Calculo ICMS ST” valor este informado nos itens dos Lançamentos Fiscais\Sub Pasta Valores ICMS. Somente serão considerados itens que tem o novo campo “%FECP” preenchido no cadastro do Produto.
* Adicionar na Alíquota Interna do ICMS ST 2%

**Cálculo**

* FECP-MG Apuração ST

Deve ser adicionado à alíquota do ICMS ST. O valor do FECP é originado em valores destacados nos campos de ICMS ST das Notas Fiscais de saídas internas.

|  |  |  |
| --- | --- | --- |
| Exemplo de Calculo ICMS ST |  |  |
|  |  |  |
| Operação Interna c\ST |  |  |
| Alíquota Interna | 18% |  |
| % FECP (FEM) | 2% |  |
| %Margem de Lucro | 50% |  |
| Base de Calculo | 1.500,00 | (1.000,00+50%) |
| Alíquota Saída | 20% |  |
| Valor do ICMS Próprio | 120,00 | (1.000,00 \* 18%) |
| Valor do ICMS ST | 150,00 | ((1.500,00\*18%)-120)) |
| Valor FECP MG | 30,00 | (1.500,00 \* 2%) |

**Apuração**

* Ao encerrar o Período de Apuração os novos campos "FECP\Próprio" – "FECP\Consumidor Final" – "FECP\ICMS ST – "FECP ICMS ST\Consumidor Final" serão preenchidos automaticamente. Isto será feito através do valor gerado no lançamento de Outros Débitos\Credito.
* A Guia do valor do FECP ICMS e ICMS ST devem ser gerada separada.

**Emissão da NF-e**

* O valor relativo ao adicional de alíquota de 2% do FECP deverá estar incluso no destaque do ICMS ou ICMS ST nos campos próprios da NFe conforme o caso.

**Na Rotina da DAPI - MG**

* Os valores apurados mensalmente no "campo 82.1 – Fundo de Erradicação da Miséria – FEM" para as operações em que o valor do FEM foi incluído no ICMS ST retido;

* Os valores apurados mensalmente no "campo 90.1 – Estorno do FEM" para as operações em que o valor do FEM foi incluído do ICMS da operação própria.

* Os valores apurados por operação no "campo 110.1 – Total do FEM antecipado" para as operações em que o valor do FEM seja recolhido por operação.

Este Campo será preenchido com o valor do FECP dos lançamentos Fiscais de Entrada Interno e Interestadual que na Natureza Fiscal\Regra de ICMS – o Tipo de ICMS Retido na Compra" ou "Normal ST Retido na Compra".(Podemos utilizar como Parâmetro o Registro 108 da Rotina da DAPI).

**Observação**: Conforme alinhamento interno o preenchimento do campo 110.1 não será implementado neste primeiro momento.

**Sped Fiscal**

Serão gerados os seguintes Registros no Sped Fiscal:

**ICMS Próprio**

* Registro E110:  O valor apurado deverá compor o valor total declarado no campo 15 (DEB\_ESP) e o valor total declarado no campo 09 (VL\_ESTORNOS\_DEB) do registro E111.

* Registro E111: Um registro declarando o valor do FEM como "débito especial‟ do período e outro registro estornando o valor do cálculo do ICMS normal do período

* Registro E112: Registro gerado se houver Processo Judicial ou Administrativo associado ao lançamento de Outros Débitos\Créditos.

* Registro E116: Registro gerado com a Guia do ICMS FECP gerado no Período de Apuração.  
    
  **ICMS ST**
* Registro E210: O valor apurado deverá compor o valor total declarado no campo 15 (DEB\_ESP\_ST) e o valor total declarado no campo 06 (VL\_OUT\_CRED\_ST) do registro E220.

* Registro E220: Um registro declarando o valor do FEM como "débito especial" do período e outro registro estornando o valor do cálculo do ICMS ST do período.

* Registro E230:  Registro gerado se houver Processo Judicial ou Administrativo associado ao lançamento de Outros Débitos\Créditos.

* Registro E250: Registro gerado com a Guia do ICMS FECP gerado no Período de Apuração.

**Implementações****Necessárias**

**Gestão Fiscal**

* Lançamento Fiscal\Item – Sub Pasta Dados de ICMS
* Criar um campo novo "Valor FECP". Este campo será calculado automaticamente, após a inclusão dos campos "Base de Calculo do ICMS" na Pasta Dados do ICMS. Sobre a Base de Calculo de ICMS, aplicasse o % informado no Cadastro do Produto.
* Lançamento de Outros Débitos\Credito
* Processos "Gerar Lançamentos Outros Débitos e Créditos do FECP"  
    
  **Observação:** O processo poderá ser visualizado no cadastro de "Lançamento de Outros Débitos\Credito"  
    se a filial estiver parametrizada para utilizar o Fecp  
    
  Gestão Fiscal >>Ambiente >> Parâmetros >> Totvs Gestão Fiscal >> 03.02 - Apuração de Tributos >> 03.02.01 - ICMS >> Apur. ICMS por Filial

**Implementação do processo  “Gerar Lançamentos Outros Débitos e Créditos do FECP”**

* Selecione os períodos dos tributos ICMS e ICMS ST para geração dos lançamentos do FECP/FEM

Por esta opção poderá ser incluído automaticamente até 6 lançamentos de Outros Débitos\Créditos com as seguintes características:

**1. FECP\Proprio**

Tipo de Lançamento: Estorno de Débito

Sub Tipo : FECP\FEM ICMS Próprio 

Valor:  Será a soma do campo “DLAF.VLRICMSFCPESTDEST” dos lançamentos Fiscais de saída  com natureza “5.XXX” cuja operação tributária não seja “Substituição Tributária” e o  campo “Operação Consumidor Final” na pasta outros dados desabilitado.

**2. FECP\Consumidor Final**

Tipo de Laçamento: Estorno de Débito

Sub Tipo : FECP\FEM Consumidor Final 

Valor: Será a soma do campo “DLAF.VLRICMSFCPESTDEST” dos lançamentos Fiscais de saída  com natureza “5.XXX” cuja operação tributária não seja “Substituição Tributária” e o  campo “Operação Consumidor Final” na pasta outros dados habilitado

**3. FECP\ICMS ST**

Tipo de Lançamento: Estorno de Débito

Sub Tipo : FECP\FEM ICMS ST 

Valor: Será a soma do campo “DLAF.VLRICMSFCPESTDEST” dos lançamentos fiscais de saída com natureza “5.XXX”, "1.XXX" ou "2.XXX" cuja operação tributária seja “Substituição Tributária” e o  campo “Operação Consumidor Final” na pasta outros dados desabilitado.

**4. FECP\ICMS ST Consumidor Final**

Tipo de Lançameto: Estorno de Débito

Sub Tipo : FECP\FEM ICMS ST\Consumidor Final

Valor:  Será a soma do campo “DLAF.VLRICMSFCPESTDEST” dos lançamentos fiscais de saída com natureza “5.XXX”, "1.XXX" ou "2.XXX" cuja operação tributária seja “Substituição Tributária” e o  campo “Operação Consumidor Final” na pasta outros dados habilitado.

**Observação aplica - se ao Fecp Icms - ST**: Para Lançamentos com CFOP "**1**.xxx" ou "**2**.xxx" ser considerado deve ter o Tipo Natureza do ICMS com **(3)FlagICMSNormalSTRetCompra** ou  **(J) - FlagIcmsSTRetidoCompra** 

Necessário criar o tipo “**Débito Especial**” no cadastro de Lançamentos outros Débitos/Créditos, este tipo será somente informativo e não afetará a apuração dos tributos ICMS e ICMS ST

**5. ICMS**

Tipo de Lançamento: Débito Especial

Sub Tipo : FECP\FEM ICMS Próprio 

Valor:  Será a soma dos valores dos lançamentos Outros Débitos\Créditos gerados   "1. FECP\FEM ICMS Próprio” e  "2. FECP\FEM Consumidor Final".

**6. ICMS ST**

Tipo de Lançamento: Debito Especial

Sub Tipo : FECP\FEM ICMS ST 

Valor: Será a soma dos valores dos lançamentos Outros Débitos\Créditos gerados   "3. FECP\FEM ICMS ST” e  "4. FECP\FEM ICMS ST\Consumidor Final”.

      **Observações:**

* Os lançamentos com o tipo “Débito Especial” são necessários para correta geração da rotina do Sped Fiscal  nos registros E111 e E220, estes lançamentos não afetam a apuração dos tributos ICMS e ICMS ST.

* Os Lançamentos Outros Débitos e Créditos gerados pelo processo para serem considerados no Sped Fiscal deverá ser informado manualmente o campo "*Código Ajuste SPED*" conforme o código de ajuste da tabela do estado da filial >> [Tabelas Sped Fiscal](http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal).

**Período de Apuração do Tributos ICMS e ICMS - ST**

* Criar os campos  "Valor FECP\Próprio" e "Valor FECP\Consumidor Final"  na sub pasta apuração, será  necessário identificar os valores separados porque a legislação exige gerar as guias separadas.
* As guias deverão ser geradas automaticamente utilizando os valores dos campos  "Valor FECP\Próprio" e "Valor FECP\Consumidor Final"  do período.

**Cadastro Produto**

* No Anexo deste campo Sub Pasta Dados Fiscais por UF – Criar um campo %FECP.

Os campos que calculam o FECP/FEM deve passar a verificar se este campo esta preenchido. Todo o calculo será feito somente para os produtos que esteja com este campo preenchido:

* Lançamento Fiscal - Incluir na linha de itens do lançamento Fiscal o campo "Valor FECP"

* Escrituração - Tratar o calculo do campo "Valor FECP" no item do lançamento fiscal.

* Rotina DAPI - Implementar os campos abaixo:

                 campo 82.1   –  "Fundo de Erradicação da Miséria – FEM"

                 campo 90.1   –  "Estorno do FEM"

  campo 110.1 – "Total do FEM antecipado"  *Não Implementado*

* NFe - Incluir na NFe a consistência do campo % FECP

# Especificação Técnica

## **1 - Cadastro Produto**

**Implementação de campo para o Valor do % do FECP.**

Base de Dados:

| Tabela | Campo | Tipo |
| --- | --- | --- |
| TPRDCODFISCAL | PERFECP | RMDVALOR4 |

Este campo será utilizado para o calculo do Valor do FECP na inclusão de Lançamentos Fiscais.

Campo livre para digitação de valores.

Tela - Dados Fiscais do Produto:

**2 - Lançamento Fiscal**

**Implementação do calculo do Valor do FECP no Lançamento Fiscal.**

Base de Dados:

| Tabela | Campo | Tipo |
| --- | --- | --- |
| DITEM | PERFECPITEM | RMDVALOR4 |

O Campo % FECP do item será originado do % do FECP cadastrado no Anexo Produtos por UF.

Campo Editável pelo usuário.

Com base na Base de ICMS do Produto o sistema irá calcular o Valor ICMS FECP do Item (Campo Não Editável).

Obs.: Este campo apenas será calculado para operações de Saída Interna ou Saída Interestadual com a opção

"Operação destinada a Consumidor Final" marcada na inclusão do Lançamento.

Estes valores gravados nos Itens, serão somados e gravados automaticamente na Situação Tributária do Lançamento Fiscal no

campo Valor ICMS FECP ao salvar o Lançamento (Campo Não Editável).

Obs.: A partir do momento que o campo "% FECP" for criado no Cadastro de Produtos por UF o campo "% FECP da Natureza" na

Situação Tributária não será mais preenchido.

O Calculo será feito todo nos Itens do Lançamento Fiscal e ao final somado o Valor na Situação Tributária, quando não existir percentual no Cadastro do Produto o sistema irá utilizar

o percentual da Regra de ICMS para o calculo nos Itens, porem este percentual não será gravado na Situação Tributária do Lançamento Fiscal.

Obs.: Como a partir da versão 12.1.10 o campo do “% do FECP” do Produto (Dados Fiscais do Produto) vai ser criado para todos os clientes pelo Conversor

o "% FECP Natureza" da parcela será descontinuado, o cálculo do “Valor do FECP” na Parcela do Lançamento Fiscal será calculado apenas pelo

somatório dos “Valores do FECP” do Item do Lançamento.

Para o cálculo do “Valor do FECP” no Item do Lançamento o sistema irá utilizar o “% do FECP” do Produto, caso não exista valor para o estado em questão o sistema irá utilizar o “% do FECP”  da Natureza.

**3 - Apuração dos Tributos ICMS e ICMS-ST**

**Preenchimento dos campos Valor FECP e Valor FECP Consumidor Final no Processo de Encerramento do Período de Apuração.**

Base de Dados:

| Tabela | Campo | Tipo |
| --- | --- | --- |
| DPERIODO | VLRFECP | RMDVALOR4 |
| DPERIODO | VLRFECPCFINAL | RMDVALOR4 |

Os Valor dos campos "Valor FECP"  e valor FECP Consumidor Final serão preenchidos com base nos Lançamentos de Outros Débitos/Créditos criados na Base pelo novo Processo,

(Gerar Lançamentos de Outros Débitos e Créditos do FECP).

Tipo: Estorno de Debito. e  SubTipo: FECP ICMS Próprio e FECP Consumidor Final.

Estes campos serão utilizados para a geração das Guias do FECP que serão geradas a partir do processo já existente juntamente com o

valor do Saldo Devedor do Período.

**4 - Escrituração de Lançamentos Fiscais**

No Processo de Escrituração de Lançamentos Fiscais o sistema irá calcular automaticamente o Valor do FECP por Item, quando

o Lançamento for uma Saída Interna ou uma Saída Interestadual com a opção "Operação Destinada a Consumidor Final" marcada

e o Item estiver com % de FECP preenchido na Base, para o Estado ao qual o Lançamento esta sendo criado.

Os Valores dos Itens serão somados e gravados na Situação Tributária do Lançamento Fiscal.

**5 - Importação/Exportação do Lançamento Fiscal TXT**

Foi disponibilizado o campo % FECP *DITEM.PERFECPITEM com tamanho 15* para importação/exportação.
