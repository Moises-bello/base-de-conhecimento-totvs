---
content_hash: 658762b15c9cc813690d85c295315a6d6e7889623838c82660c98875141bdbd7
fetched_at: '2026-06-29T00:10:27.012337+00:00'
page_id: '515694110'
product: rm
source: tdn-rm
title: Atualizações para atender o eSocial - Leiaute 2.5 NT 15/2019
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515694110
version: 49
---

A **Nota Técnica nº 15/2019** divulgada pelo Governo no dia 02/08/2019 tem como objetivo implantar as primeiras medidas de **simplificação e modernização do eSocial**, conforme disposto no art. 9º da Portaria nº 300, de 13/06/2019.

A principal mudança é a alteração de diversos grupos e campos **de "OC" (Obrigatórios na Condição) para "F" (Facultativos)**.

## Data de entrada nos ambientes do eSocial

* Produção restrita (testes): **08/10/2019**
* Produção: **11/11/2019**

## Releases que contemplam a Nota Técnica nº 15/2019

* 12.1.24.224
* 12.1.25.155
* 12.1.26.106
* E superiores

**Importante**  
Necessário também atualizar o TAF para o pacote mais atual da Central de Downloads do Portal. Maiores informações [clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=374311673).

Foi criado uma nova versão do leiaute no parametrizador para atender as simplificações da NT 15/2019.

Parâmetro disponível em RH | Folha de pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais 1/6:

| ATENÇÃO: |
| --- |
| Para os grupos facultativos que possuem campos obrigatórios ao gerar o XML o sistema passou a fazer o seguinte tratamento:  Verificar os parâmetros abaixo existentes em RH | Folha de pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais 3/6:   1. Não gerar aviso para registro não obrigatório quando desconsiderado no XML 2. Gerar erro de preenchimento para registro não obrigatório quando tiver algum campo preenchido   Segue abaixo exemplos: 112true2-1Exemplo 1Exemplo 1 Quando o Parâmetro 1 e Parâmetro 2 estiverem desmarcados será gerado uma mensagem de aviso alertando o campo não está preenchido.  Grupo RG passou a ser facultativo, porém existe campos obrigatórios para preenchimento.      Ao gerar o sistema apresentará o aviso    2-2Exemplo 2Exemplo 2 Quando o  Parâmetro 1 e Parâmetro 2 estiverem marcados será gerado uma mensagem de erro.  Grupo RG passou a ser facultativo, porém existe campos obrigatórios para preenchimento.      Ao gerar o sistema apresentará o erro     2-3Exemplo 3Exemplo 3 Quando o Parâmetro 1 estiver marcado e Parâmetro 2 desmarcado não será apresentada nenhuma mensagem de aviso alertando.  Grupo RG passou a ser facultativo, porém existe campos obrigatórios para preenchimento.      Ao gerar o sistema não apresentará nenhuma mensagem   2-4Exemplo 4Exemplo 4 Quando o  Parâmetro 1 estiver desmarcado e Parâmetro 2 marcado será gerado um erro que o campo não está preenchido.  Grupo RG passou a ser facultativo, porém existe campos obrigatórios para preenchimento.      Ao gerar o sistema apresentará o erro |

## Alterações Contempladas:

**S-1000 - Informações do Empregador/Contribuinte/Órgão Público**

* Os grupos abaixo deixam de ser **obrigatórios** e passaram a ser**facultativos**:

| Grupo | Descrição do Grupo |
| --- | --- |
| contato | Informações de contato |
| softwareHouse | Informações do desenvolvedor do Software |
| infoComplementares | Informações complementares sobre o declarante |
| indSitPJ | Indicativo da Situação da Pessoa Jurídica |
| indSitPF | Indicativo da Situação da Pessoa Física |

* Os campos abaixo deixaram de ser **obrigatórios** e passaram a ser **facultativos** e/ou sofreram **alteração:**

| Grupo | Campo | Descrição do Campo | Alterações |
| --- | --- | --- | --- |
| infoCadastro | nmRazao | Nome do contribuinte ou a razão social | Preenchimento facultativo |
| infoCadastro | indEntEd | Indicativo entidade educativa sem fins lucrativos | Preenchimento facultativo |
| infoCadastro | indEtt | Indicativo de Empresa de Trabalho Temporário | Preenchimento facultativo |
| softwareHouse | nmCont | Nome do contato na empresa | Preenchimento facultativo |

**S-1005 - Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos**

* Os grupos abaixo deixam de ser **obrigatórios** e passaram a ser**facultativos**:

| Grupo | Descrição do Grupo |
| --- | --- |
| infoTrab | Informações Trabalhistas |
| infoApr | Informações relacionadas à contratação de aprendiz |
| infoEntEduc | Identificação da(s) entidade(s) educativa(s) ou de prática desportiva |
| infoPCD | Informações sobre a contratação de pessoa com deficiência (PCD) |

* Os campos abaixo deixaram de ser **obrigatórios** e passaram a ser **facultativos** e/ou sofreram **alteração:**

| Grupo | Campo | Descrição do Campo | Alterações |
| --- | --- | --- | --- |
| infoTrab | regPt | Opção de registro de ponto (jornada) adotada pelo estabelecimento | Preenchimento facultativo |
| infoApr | nrProcJud | Número do processo judicial | Preenchimento facultativo |
| infoApr | contEntEd | Informar se o estabelecimento realiza a contratação de aprendiz por intermédio de entidade educativa sem fins lucrativos que tenha por objetivo a assistência ao adolescente e à educação profissional (art. 430, inciso II, CLT) ou por entidade de prática desportiva filiada ao Sistema Nacional do Desporto ou a Sistema de Desporto de Estado, do Distrito Federal ou de Município (art. 430, inciso III, CLT) | O preenchimento é facultativo se {contApr} for igual a [1, 2]. Não informar se {contApr} for igual a [0]. |
| infoPCD | nrProcJud | Número do processo judicial. | Preenchimento facultativo |

**S-1200 -** **Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social**

* O grupo abaixo deixou de ser **obrigatórios** e passou a ser**facultativo:**

| Grupo | Descrição do Grupo |
| --- | --- |
| infoTrabInterm | Informações da(s) convocação(ões) de trabalho intermitente. |

* Os campos abaixo deixaram de ser **obrigatórios** e passaram a ser **facultativos** e/ou sofreram **alteração:**

| Grupo | Campo | Descrição do Campo | Alterações |
| --- | --- | --- | --- |
| ideADC | tpAcConv | Tipo do instrumento ou situação ensejadora da remuneração relativa a Períodos de Apuração Anteriores | Preenchimento Obrigatório. incluído valor G - Antecipação de diferenças de Acordo, Convenção ou Dissídio Coletivo. |
| ideADC | compAcConv | Competência (formato AAAA-MM) em que é devida a obrigação de pagar os efeitos remuneratórios de lei, acordo coletivo, convenção coletiva ou sentença normativa. | Preenchimento facultativo. Se informada, deve ser maior ou igual ao período de apuração informado em {perApur}.Se informada, deve ser maior ou igual ao mês/ano informado em {dtDeslig} |
| ideADC | dtEfAcConv | Data a partir da qual o instrumento ou legislação mencionada em {tpAcConv} passa a produzir seus efeitos. | Preenchimento facultativo |

**S-2200- Cadastramento Inicial do Vínculo e Admissão/ingresso de Trabalhador**

* Os grupos abaixo  passaram a ser **facultativo:**

| Grupo | Descrição do Grupo |
| --- | --- |
| documentos | Informações dos documentos pessoais do trabalhador |
| CTPS | Informações da Carteira de Trabalho e Previdência Social |
| RIC | Informações do Documento Nacional de Identidade (DNI) |
| RG | Informações do Registro Geral (RG) |
| RNE | Informações do Registro Nacional de Estrangeiro |
| OC | Informações do número de registro em Órgão de Classe (OC) |
| CNH | nformações da Carteira Nacional de Habilitação (CNH) |
| FGTS | Informações do Fundo de Garantia do Tempo de Serviço - FGTS |
| filiacaoSindical | Filiação Sindical do Trabalhador |

* Os campos abaixo passaram a ser **facultativo:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Grupo** | **Campo** | **Descrição do Grupo** | **Alterações** |
| trabalhador | indPriEmpr | Indicar caso se trate do primeiro emprego do trabalhador:  S - Sim; N - Não. | Validação: Preenchimento facultativo se {cadIni} = [N]. Não informar se {cadIni} = [S]. Valores Válidos: S, N. |
| nascimento | codMunic | Informações do Município | Preenchimento facultativo |
| nascimento | uf | Preencher com a sigla da Unidade da Federação. | Preenchimento facultativo |
| brasil | tpLograd | Tipo de Logradouro | Validação: Se informado, deve ser um código válido, existente na tabela 20. |
| trabtemporario | tpInclContr | Tipo de inclusão de contrato | Preenchimento facultativo |
| localTrabDom | tpLograd | Tipo de Logradouro | Validação: Se informado, deve ser um código válido, existente na tabela 20. |
| localTrabDom | cep | Código de Endereçamento Postal | Validação: Deve ser preenchido apenas com números, com 8 (oito) posições |
| alvaraJudicial | nrProcJud | Preencher com o número do processo judicial | Validação: Deve ser um número de processo judicial válido. |
| sucessaoVinc | tpInscAnt | Preencher com o código correspondente ao tipo de inscrição,conforme tabela 05 | Validação: Deve ser igual a [1] (CNPJ), [2] (CPF) [5] ( ou [6] (CEI) Somente é possível informar [5] se {dtTransf} for igual ou anterior a 01/07/1998. Somente é possível informar [ 6 ] se {dtTransf} for igual ou anterior a 31 12 2011 Valores Válidos: 1, 2, 5 , 6 |
| sucessaoVinc | cnpjEmpregAnt | Informar o número de inscrição do empregador anterior , de acordo com o tipo de inscrição indicado no campo {tpInscAnt} | Validação: Deve ser um número de inscrição válido diferente da inscrição do declarante, considerando as particularidades aplicadas à informação de CNPJ de órgão público em S 1000. Se {tpInscAnt} = [1], deve possuir 14 (catorze) algarismos e ser diferente do CNPJ base do empregador e dos estabelecimentos informados através do evento S 1005. Se {tpInscAnt} = [2], deve possuir 11 (onze) algarismos. Se {tpInscAnt} = [5], deve possuir somente algarismos. Se {tpInscAnt} = 6 ], deve possuir 1 2 do ze) algarismos. |

**S-2205 - Alteração de Dados Cadastrais do Trabalhador**

* O grupo abaixo  passou a ser**facultativo:**

| Grupo | Descrição do Grupo |
| --- | --- |
| documentos | Informações dos documentos pessoais do trabalhador |
| CTPS | Informações da Carteira de Trabalho e Previdência Social |
| RIC | Informações do Documento Nacional de Identidade (DNI) |
| RG | Informações do Registro Geral (RG) |
| RNE | Informações do Registro Nacional de Estrangeiro |
| OC | Informações do número de registro em Órgão de Classe (OC) |
| CNH | nformações da Carteira Nacional de Habilitação (CNH) |
| FGTS | Informações do Fundo de Garantia do Tempo de Serviço - FGTS |

* Os campos abaixo passaram a ser **facultativo:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Grupo** | **Campo** | **Descrição do Grupo** | **Alterações** |
| nascimento | codMunic | Informações do Município | Preenchimento facultativo |
| nascimento | uf | Preencher com a sigla da Unidade da Federação. | Preenchimento facultativo |
| brasil | tpLograd | Tipo de Logradouro | Validação: Se informado, deve ser um código válido, existente na tabela 20. |
| brasil | cep | Código de Endereçamento Postal . Preenchido apenas com números | Validação: Deve ser preenchido apenas com números, com 8 (oito) posições |

**S-2206 - Alteração de Contrato de Trabalho**

* Os grupos abaixo passaram a ser **facultativo:**

| Grupo | Descrição do Grupo | Alterações |
| --- | --- | --- |
| filiacaoSindical | Filiação Sindical do Trabalhador | Preenchimento facultativo |

* Os campos abaixo passaram a ser **facultativo:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Grupo** | **Campo** | **Descrição do Grupo** | **Alterações** |
| localTrabDom | tpLograd | Tipo de Logradouro | Validação: Se informado, deve ser um código válido, existente na tabela 20. |
| localTrabDom | cep | Código de Endereçamento Postal | Validação: Deve ser preenchido apenas com números, com 8 (oito) posições |
| alvaraJudicial | nrProcJud | Preencher com o número do processo judicial | Validação: Deve ser um número de processo judicial válido. |

**S-2230 - Afastamento Temporário**

* Os grupos abaixo deixam de ser **obrigatórios** e passaram a ser**facultativos**:

| Grupo | Descrição do Grupo |
| --- | --- |
| infoAtestado | Informações complementares relativas ao atestado médico |
| emitente | Médico/Dentista que emitiu o atestado |

* Os campos abaixo deixaram de ser **obrigatórios** e passaram a ser **facultativos** e/ou sofreram **alteração:**

| Grupo | Campo | Descrição do Campo | Alterações |
| --- | --- | --- | --- |
| infoAtestado | codCID | código na tabela de Classificação Internacional de Doenças - CID | O preenchimento deste campo é facultativo. Se informado, deve ser preenchido com caracteres alfanuméricos conforme opções constantes na tabela CID |
| infoAtestado | qtdDiasAfast | Quantidade de dias de afastamento concedidos pelo médico | Preenchimento facultativo |
| infoAtestado | dtTermAfast | Preencher com a data do término do afastamento do trabalhador | Realizada alterações no gatilho do evento. Maiores informações [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=517118804) |

**S-2299 - Desligamento**

* Os grupos abaixo deixam de ser **obrigatórios** e passaram a ser**facultativo:**

| Grupo | Descrição do Grupo |
| --- | --- |
| infoTrabInterm | Informações da(s) convocação(ões) de trabalho intermitente. |

* Os campos abaixo deixaram de ser **obrigatórios** e passaram a ser **facultativos** e/ou sofreram **alteração:**

| Grupo | Campo | Descrição do Campo | Alterações |
| --- | --- | --- | --- |
| infoTrabInterm | codConv | Código atribuído pela empresa que identifica a convocação para trabalho intermitente | Preenchimento facultativo |
| infoDeslig | mtvDeslig | Código de Motivo do Desligamento | Deve ser um código existente na tabela. Os códigos [19,20,21,22,23,24,25] só podem ser utilizados para desligamento de trabalhador pertencente à categoria de agente público (301 a 309). O código [34] só pode ser utilizado para desligamento de trabalhador doméstico (código de categoria [104]). |
| infoDeslig | nrCertObito | Número da certidão de óbito | Preenchimento facultativo |
| infoDeslig | indCumprParc | Indicador de cumprimento de aviso prévio | Preenchimento facultativo |
| ideADC | tpAcConv | Tipo do instrumento ou situação ensejadora da remuneração relativa a Períodos de Apuração Anteriores | Preenchimento Obrigatório. Incluído valor G - Antecipação de diferenças de Acordo, Convenção ou Dissídio Coletivo. |
| ideADC | compAcConv | Competência (formato AAAA-MM) em que é devida a obrigação de pagar os efeitos remuneratórios de lei, acordo coletivo, convenção coletiva ou sentença normativa. | Preenchimento facultativo. Se informada, deve ser maior ou igual ao mês/ano informado em \{dtDeslig} |
| ideADC | dtEfAcConv | Data a partir da qual o instrumento ou legislação mencionada em {tpAcConv} passa a produzir seus efeitos. | Preenchimento facultativo |

**S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário - Início**

* Os grupos abaixo  passaram a ser **facultativo:**

| Grupo | Descrição do Grupo |
| --- | --- |
| documentos | Informações dos documentos pessoais do trabalhador |
| CTPS | Informações da Carteira de Trabalho e Previdência Social |
| RIC | Informações do Documento Nacional de Identidade (DNI) |
| RG | Informações do Registro Geral (RG) |
| RNE | Informações do Registro Nacional de Estrangeiro |
| OC | Informações do número de registro em Órgão de Classe (OC) |
| CNH | Informações da Carteira Nacional de Habilitação (CNH) |

* Os campos abaixo deixaram de ser **obrigatórios** e passaram a ser **facultativos** e/ou sofreram **alteração:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Grupo** | **Campo** | **Descrição do Grupo** | **Alterações** |
| nascimento | codMunic | Informações do Município | Preenchimento facultativo |
| nascimento | uf | Preencher com a sigla da Unidade da Federação. | Preenchimento facultativo |
| brasil | tpLograd | Tipo de Logradouro | Validação: Se informado, deve ser um código válido, existente na tabela 20. |
