---
content_hash: 0b527e9f67d6291330699b66a6e2343ed50da81fbca1a6b3bf3c89a5adabdf9a
fetched_at: '2026-06-29T00:11:05.482183+00:00'
page_id: '631317368'
product: rm
source: tdn-rm
title: GIA-ST (Guia Nacional de Informação e Apuração do ICMS por substituição tributária)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=631317368
version: 90
---

#FFA500#FFFACD#FFE766dashedAviso Importante:1%99%

Com o objetivo de proporcionar uma melhor experiência e alinhamento às atualizações mais recentes dos nossos produtos, informamos que a funcionalidade **GIA-ST (Guia Nacional de Informação e Apuração do ICMS por substituição tributária),** já disponível no Módulo Gestão Fiscal, não será mais suportada no produto **RM Liber.exe** a partir da **versão 12.1.2502**

Reforçamos que essa alteração faz parte do nosso processo de evolução tecnológica, com a descontinuidade gradual de funcionalidades no **RM** **Liber.exe**. Para garantir a continuidade do uso e acesso à funcionalidade GIA-ST, recomendamos que a geração seja feita diretamente no **Módulo Gestão Fiscal**.

# Conteúdo

Conteúdonone

# 1. Sobre

A GIA-ST (Guia de Informação e Apuração do ICMS Substituição Tributária) é uma obrigação acessória exigida por algumas unidades federativas brasileiras para controle e recolhimento do ICMS-ST, referente às operações sujeitas ao regime de substituição tributária. O Módulo Fiscal disponibiliza uma solução para a geração dos arquivos digitais no layout exigido pelos estados, garantindo conformidade fiscal e simplificando a prestação de contas. A GIA-ST é composta por diferentes registros que organizam as informações dos contribuintes, operações de devolução, ressarcimentos, transferências e DIFAL, facilitando a gestão tributária e a entrega das obrigações mensais de forma segura e eficiente.

# 2. Como Gerar a GIA-ST?

A GIA-ST está disponível no Módulo Fiscal a partir da , para utilizá-la basta baixar o layout **FISLAY0024 - GIA-ST.TotvsGen** disponível no [TOTVS Compartilhamento](https://tdn.totvs.com/pages/viewpage.action?pageId=348297816)

## 2.1 Pré-requisitos

* **Atualização do Layout**: Certifique-se de que está utilizando o layout mais recente da GIA-ST.

## 2.2 Regras de geração

* Defina corretamente as Naturezas, somente Lançamentos cujos CFOPs sejam "Fiscal" serão considerados;
* O valor do ICMS-ST deve ser maior que zero para que a operação seja considerada;
* O arquivo será gerado considerando os Lançamentos relacionados a UF informada na tela de geração;
  + Na tela de geração da rotina é possível selecionar mais de uma UF ao mesmo tempo, será gerado um arquivo para cada Estado selecionado.
* São desconsiderados Lançamentos Fiscais com o “Status Cancelados” e de “Ativo Imobilizado.
* O período de de Apuração do ICMSST deve estar encerrado para geração das guias  no arquivo final da rotina.

# 3. Registros Gerados

O arquivo da GIAST é composto por 5 registros.

* **Registro A0 - Dados do Contribuinte:** é o cabeçalho principal do arquivo e contém as informações de identificação do contribuinte e os totais consolidados das operações realizadas no período de apuração;
* **Registro A1 - Anexo 1: Operações de Devolução de Venda:** detalha as notas fiscais referentes às devoluções de vendas, identificando cada documento fiscal e seus valores correspondentes;
* **Registro A2 - Anexo 2: Valores de Ressarcimento:** é utilizado para informar os valores de ICMS-ST que foram ressarcidos ao contribuinte;
* **Registro A3 - Anexo 3: Transferência de ICMS-ST:** destina-se a registrar as transferências de valores de ICMS-ST realizadas entre estabelecimentos do mesmo contribuinte ou para terceiros;
* **Registro A4 - EC 87/15: Valores de DIFAL:**  é responsável por registrar os valores do Diferencial de Alíquota (DIFAL) referente às operações interestaduais com consumidor final, conforme exigido pela Emenda Constitucional 87/15.

false2lefttrue1Registro A0

**Filtro do Registro Principal:** Lançamentos Fiscais de Entrada e/ou Saída com CFOP Fiscal associada e Valor de ICMS ST maior que 0 e seja do mesmo Estado informado na Tela de Geração.

**IMPORTANTE**: Para gerar o arquivo da rotina devem estar cadastradas as Inscrições Estaduais no seguinte caminho: **Filiais | Anexos | Inscrição Estadual ST**

ImagemRegistro Principal

|  |  |  |  |
| --- | --- | --- | --- |
| **Registro Principal** | | | |
| **Campo** | **Conteúdo** | **Descrição** | **Origem da Informação** |
| ID Registro | A0 |  | Valor Fixo **A0** |
| Fixo | GST |  | Valor Fixo **GST** |
| Versão | 03 |  | Valor Fixo **03** |
| 05 | Período Referência – Formato: MMAAAA | Mês e ano do período de apuração do ICMSST | Período Informado na Tela de Geração |
| 06 | Inscrição Estadual – Alinhamento a Esquerda |  | Gerado com a IE da Inscrição Estadual ST  **(Filiais | Anexos | Inscrição Estadual ST)** |
| 01 | GIA Sem Movimento (Sim/Não) |  | Gerado conforme informação da Tela |
| 02 | Substituição de GIA (Sim/Não) |  | Gerado conforme informação da Tela |
| 03 | Data do 1º Vencimento do ICMS-ST – Formato: AAAAMMDD | Consideradas até 06 guias Lançadas no Período de Apuração do Tributo ICMS ST | Gerado conforme as informações das Guias\GNR incluídas no Período de Apuração do ICMS. *Guias com mesma data de vencimento são consolidadas na geração do arquivo.* |
| Valor do ICMS-ST Referente ao 1º Vencimento |
| Data do 2º Vencimento do ICMS-ST – Formato: AAAAMMDD |
| Valor do ICMS-ST Referente ao 2º Vencimento |
| Data do 3º Vencimento do ICMS-ST – Formato: AAAAMMDD |
| Valor do ICMS-ST Referente ao 3º Vencimento |
| Data do 4º Vencimento do ICMS-ST – Formato: AAAAMMDD |
| Valor do ICMS-ST Referente ao 4º Vencimento |
| Data do 5º Vencimento do ICMS-ST – Formato: AAAAMMDD |
| Valor do ICMS-ST Referente ao 5º Vencimento |
| Data do 6º Vencimento do ICMS-ST – Formato: AAAAMMDD |
| Valor do ICMS-ST Referente ao 6º Vencimento |
| 04 | Sigla da UF Favorecida | Sigla da UF favorecida; | Gerado conforme informado na Tela da Rotina UF onde o Estabelecimento possui Inscrição Estadual Substituta. |
| 07 | Valor dos Produtos | Valor total dos produtos sujeitos à substituição tributária.  Quando destinados à Zona Franca de Manaus e Áreas de Livre Comércio, informado como se devido fosse o ICMS. | Valor  Total dos produtos dos Lançamentos Fiscais DLAF.VALORMERC |
| 08 | Valor do IPI | Valor do IPI incidente sobre os produtos sujeitos à substituição tributária;. | Valor do IPI |
| 09 | Despesas Acessórias | Valor do frete, seguro e outras despesas acessórias cobradas ou debitadas ao destinatário. | Soma dos campos:  DLAF.FRETE + DLAF.SEGURO + DALF.ACRESCIMO + DLAF.OUTROSACREC |
| 10 | Base de Cálculo do ICMS Próprio | Valor que serviu de base para o cálculo do ICMS próprio. Quando destinados à Zona Franca de Manaus e áreas de livre comércio, informar o valor da base de cálculo do crédito presumido. | Gerado com o Campo Base de Cálculo do ICMS.   DLAF.BASEICMS |
| 11 | ICMS Próprio | Valor total do ICMS Próprio. Quando destinados à Zona Franca de Manaus e áreas de livre comércio, informar o valor do crédito presumido. | Gerado com o Campo Valor do ICMS.  DLAF.VALORICMS |
| 12 | Base de Cálculo do ICMS ST | Valor total da base que serviu de cálculo para retenção do ICMS. | Gerado com o Campo Base Tributada ST.  DLAF.BASESUBT |
| 13 | ICMS Retido por ST | Valor do ICMS retido por substituição tributária. | Gerado com o Campo Valor ST.  DLAF.VALORSUBT |
| 14 | ICMS de Devoluções de Mercadorias | Valor correspondente ao ICMS creditado em função de devolução de mercadorias sujeitas a substituição tributária. | Gerado com o Valor ST.   DLAF.VALORSUBT  Considerar os Lançamentos Fiscais de Entrada que o CFOP seja de Devolução |
| 15 | ICMS de Ressarcimentos | Valor do ressarcimento de ICMS que possa ser apropriado no período de referência. | Gerado com Lançamento de Outros Créditos\Débitos – Tipo Credito |
| 16 | Crédito do Período Anterior | Valor do crédito apurado na GIA-ST do período anterior quando for o caso. | Gerado com o Saldo Credor do Período do ICMSST do Período anterior  DPERIODOST.SALDOTRBANT |
| 17 | Pagamentos Antecipados |  | Não é gerado |
| 18 | ICMS-ST Devido |  | DPERIODOST.SALDOTRBATUAL |
| 19 | Repasse – ICMS Retido por Refinarias/Complementos | Relativo às operações de vendas de combustíveis derivados de petróleo, cujo imposto foi recolhido anteriormente. | Será gerado sob Demanda. Pois o Campo  “Distribuidor de Combustíveis ou TRR com Operações para UF Favorecida “ é gerado como fixo “NÃO” |
| 20 | Crédito para Período Seguinte | Valor do crédito do ICMS-ST a ser apropriado no período seguinte, no caso em que a soma dos valores dos campos 13, 14 e 15 seja superior ao valor do campo 12. | Gerado com o Saldo Devedor\Credor quando o valor for positivo   DPERIODOST.SALDOTRBATUAL |
| 21 | Total do ICMS-ST a Recolher | Valor do ICMS substituição tributária a recolher. | Gerado com o Valor do Campo Total da Substituição Tributária a Pagar do Período de Apuração.  DPERIODOST.TOTALVALORAPAGAR |
| 28 | CNPJ – Cadastro Nacional de Pessoas Jurídicas | Número da inscrição do substituto no Cadastro Nacional de Pessoa Jurídica; | Gerado com o Campo Inscrição Estadual do Cadastro da Filial.  DFILIAL.INSCESTADUAL |
| 29 | Nome do Declarante | Informações do Representante ou Contador Legal da Filial. | DFILIAL.NOMEREPRES |
| 30 | CPF do Declarante | DFILIAL.CPFREPRES |
| 31 | Cargo do Declarante na Empresa | Todos os dados gerados nestes   Campos estão no Cadastro da Filial\Anexo\ Sub Pasta Representante | DFILIAL.CARGOREPRES |
| 32 | Telefone DDD | DFILIAL.DDDREPRESENTANTE |
| Telefone Número | DFILIAL.TELREPRES |
| 33 | Fax DDD | DFILIAL.DDDFAXREPRESENTANTE |
| Fax Número | DFILIAL.FAXREPRES |
| 34 | e-mail do Declarante | DFILIAL.EMAILREPRES |
| 35 | Local | Local de Preenchimento | Gerado conforme informação da Tela de Geração |
| Data – Formato: AAAAMMDD | Data de Preenchimento | Gerado conforme informação da Tela de Geração DATA ATUAL |
| 36 | Informações Complementares – 1ª linha | Informações relevantes para a compreensão do preenchimento da GIAST | Campo Gerado conforme tela de Geração da Rotina |
| Informações Complementares – 2ª linha |
| Informações Complementares – 3ª linha |
| 37 | Distribuidor de Combustíveis ou TRR com Operações para UF Favorecida (Sim/Não) | Se distribuidora de combustíveis ou TRR:   * Somente se for distribuidora de combustíveis ou TRR, assinalar no quadrículo correspondente, se realizou operações destinadas a unidade federada favorecida, de combustíveis derivados de petróleo cujo imposto já tenha sido retido anteriormente; | Gerado conforme a Tela da Rotina  Atualmente é gerado com valor Fixo igual a “NÃO”. |
| 38 | Efetuou Transferências para UF Favorecida (Sim/Não) | Transferências efetuadas:   * Transferências efetuadas para filial do sujeito passivo por substituição tributária, localizada na unidade federada favorecida, relativo a produtos sujeitos à substituição tributária | Gerado conforme a Tela da Rotina |
| Código Entrega GIA | Reservado para uso Futuro | Reservado para uso Futuro | Não Gerado no Momento |
|  | Quantidade de Total de Linhas do Anexo I |  | Gerado automaticamente, necessário implementar. |
| Quantidade de Total de Linhas do Anexo II |  |
| Quantidade de Total de Linhas do Anexo III |  |
| 39 | Repasse – ICMS Retido por Outros Contribuintes |  | Será gerado sob Demanda, pois o Campo  "Distribuidor de Combustíveis ou TRR com Operações para UF Favorecida " é gerado como fixo "NÃO". |
|  | EC N° 87/15 com Movimento (Sim/Não) |  | Gerado conforme campo na Tela de Geração |
|  | Valor do ICMS-ST FCP Referente ao 1º Vencimento |  | Gerado sob Demanda |
|  | Valor do ICMS-ST FCP Referente ao 2º Vencimento |  |
|  | Valor do ICMS-ST FCP Referente ao 3º Vencimento |  |
|  | Valor do ICMS-ST FCP Referente ao 4º Vencimento |  |
|  | Valor do ICMS-ST FCP Referente ao 5º Vencimento |  |
|  | Valor do ICMS-ST FCP Referente ao 6º Vencimento |  |
|  | Valor do ICMS Devido à UF de Destino |  | Gerado quando o valor do Saldo Devedor\Credor for negativo, período de Apuração\Sub Pasta Valores Diferencial de Alíquota.  DPERIODODIFAL.SALDOCREDORDEVEDOR  Considerar as informações da UF selecionada na tela da Rotina e  o Campo  “EC N° 87/15 com Movimento” igual a SIM. |
|  | Devoluções ou Anulações |  | Gerado com o Valor do DIFAL dos Lançamentos Fiscais com o Tipo de CFOP “Devolução” |
|  | Pagamentos Antecipados |  | Não Geramos |
|  | Total do ICMS Devido à UF de Destino |  | Gerado quando o valor do Saldo Devedor\Credor for negativo, período de Apuração\Sub Pasta Valores Diferencial de Alíquota  DPERIODODIFAL.SALDOCREDORDEVEDOR  Considerar as informações da UF selecionada na tela da Rotina |
|  | Total ICMS FCP |  | Gerado quando o valor do Saldo Devedor\Credor FCP for negativo, período de Apuração\Sub Pasta Valores Diferencial de Alíquota  DPERIODODIFAL.SALDOCREDORDEVEDORFCP  Considerar as informações da UF selecionada na tela da Rotina |

**Observações:**

O Campo 39 – Repasse de ICMS Retido por outros contribuintes, diz respeito apenas às refinarias e distribuidoras de combustível.

2Registro A1

**Filtro do Registro Anexo I:**Lançamentos Fiscais de Entrada que o Tipo de CFOP associado seja Devolução com valor Substituição maior que zero onde o Fornecedor Origem/Destino seja do mesmo Estado informado na Tela de Geração.

Registro Anexo I

|  |  |  |  |
| --- | --- | --- | --- |
| **Registro Anexo I** | | | |
| **Campo** | **Conteúdo** | **Descrição** | **Origem da Informação** |
| Id Registro | A1 |  | Valor Fixo **A1** |
| Número da Nota Fiscal | Número da nota fiscal de devolução | Gerado com o Número do Lançamento de Entrada e que o CFOP seja do Tipo Devolução  DLAF.DOCINI |
| Série da Nota Fiscal |  | Gerado com o Campo Serie do Lançamento  DLAF.SERIEDOC |
| Inscrição Estadual | Inscrição estadual do contribuinte que está procedendo a mesma | Gerar com a Inscrição Estadual do Cliente\Fornecedor associado ao Lançamento Fiscal.  FCFO.INSCESTADUAL |
| Data de Emissão da Nota Fiscal – Formato: AAAAMMDD |  | Gerado com o Campo Data Emissão do Lançamento   DLAF.DATAEMISSAO |
| Valor do ICMS-ST de Devolução |  | Gerado com o Campo Valor Subst do Lançamento  DLAF.VALORSUBT |

3Registro A2

**Filtro do Registro Anexo II:** Lançamentos de Referencia de Outros Débitos/Créditos vinculados ao Período de ICMS-ST onde o Estado da Referência seja o mesmo da tela de Geração.

Registro Anexo II

|  |  |  |  |
| --- | --- | --- | --- |
| **Registro Anexo II** | | | |
| **Campo** | **Conteúdo** | **Descrição** | **Origem da Informação** |
| Id Registro | A2 |  | Valor Fixo **A2** |
| Número da Nota Fiscal |  | Gerado como Número do Lançamento Fiscal associado ao Lançamento de Outros Débitos\Créditos  DLAF.DOCINI  Ou   Com os Dados dos Lançamentos “Não Cadastrado”  DLDCNF..DOCINI |
| Série da Nota Fiscal |  | Gerado com a Série   DLAF.SERIEDOC  Ou   Com os Dados dos Lançamentos "Não Cadastrado"  DLDCNF.SERIEDOC |
| Inscrição Estadual | Inscrição estadual do destinatário | Gerado com a Inscrição Estadual do Cliente\Fornecedor associado ao Lançamento Fiscais.  Ou  Com os Dados dos Lançamentos "Não Cadastrado"  DLDCNF.INSCESTADUAL |
| Data de Emissão da Nota Fiscal – Formato: AAAAMMDD |  | Gerado com a Data de Emissão  DALF.DATAEMISSAO  Ou  Com os Dados dos Lançamentos "Não Cadastrado"  DLDCNF.DATAEMISSAO |
| Valor do ICMS-ST de Ressarcimento |  | Gerado com o Valor do Campo   DLDC.VALORLDC |

4Registro A3

**Filtro do Registro Anexo III:** Lançamentos de Saída, com CFOP Transferência do tipo Empresa\Empresa com Parâmetro de Geração "**Efetuou Transferências para UF Favorecida**" estiver igual a "SIM" e com o Valor de ST maior que zero.

Registro Anexo III

|  |  |  |  |
| --- | --- | --- | --- |
| **Registro Anexo III** | | | |
| **Campo** | **Conteúdo** | **Descrição** | **Origem da Informação** |
| ID Registro |  |  | Valor Fixo **A3** |
| Inscrição Estadual | Inscrição estadual do destinatário | Inscrição Estadual da Filial Destino |
| Base de Cálculo |  | Gerado com o Campo Base de Cálculo ST  DLAF.BASESUBST |
| Valor do ICMS destacado |  | Gerado com o Campo Valor ST  DLAF.VALORSUBST |

Informações

Para gerar o Anexo III, além de atender os requisitos descritos, é necessário que na tela de geração da rotina o Parâmetro "**Efetuou Transferências para a UF favorecida**" esteja selecionado com "SIM";

5Registro A4

**Filtro do Registro Anexo EC 87/15:** será preenchido com os valores correspondentes a totalização dos campos “Total do ICMS Devido à UF de Destino” e “Total ICMS FCP” quando existirem no Registro Principal. 

O anexo será gerado com as informações das Guias GNR geradas no Período do Tributo ICMS. 

Registro Anexo EC 87/15

|  |  |  |  |
| --- | --- | --- | --- |
| **Registro Anexo EC 87/15** | | | |
| **Campo** | **Conteúdo** | **Descrição** | **Origem da Informação** |
| ID Registro | A4 |  | Valor Fixo **A4** |
| Data de Vencimento do ICMS Devido à UF de Destino – Formato: AAAAMMDD |  | Gerada com campo Data Vencimento da Guia GNR no Período do Tributo ICMS  DGUIAPERIODO.DATAVENC  Que o Código de Obrigação na Sub Pasta Outro Dados igual a “003” |
| Valor do ICMS |  | Gerado com o Campo Valor Apurado da Guia GNR no Período do Tributo ICMS   DGUIAPERIODO.VALORAPURADO  Que o Código de Obrigação na Sub Pasta Outro Dados igual a "003" |
| Data de Vencimento FCP – Formato: AAAAMMDD |  | Gerada com campo Data Vencimento da Guia GNR no Período do Tributo ICMS  DGUIAPERIODODATAVENC  Que o Código de Obrigação na Sub Pasta Outro Dados igual a "006" |
| Valor do ICMS FCP |  | Gerada com campo Valor Apurado da Guia GNR no Período do Tributo ICMS  DGUIAPERIODODATAVENC  Que o Código de Obrigação na Sub Pasta Outro Dados igual a "006" |

Informações

Para gerar o Anexo EC 8/15, além de atender os requisitos descritos, é necessário que na tela de geração da rotina o Parâmetro "**EC Nº 87/15 com Movimento**" esteja selecionado com "SIM";

# 4. Vídeos How To

Para auxiliar no entendimento e na utilização da GIA-ST, disponibilizamos uma série de vídeos tutoriais que demonstram, de maneira prática, como executar o processo dentro do Módulo Gestão Fiscal

4left1Anexo I

648432

2Anexo II

648432

3Anexo III

648432

4Anexo EC 87/15

648432

# 5. Outras informações

Manual GIA ST - Versão 3:

<https://receita.fazenda.rs.gov.br/conteudo/5322/arquivos---gia-st-(guia-nacional-de-informacao-e-apuracao-do-icms-substituicao-tributaria)>
