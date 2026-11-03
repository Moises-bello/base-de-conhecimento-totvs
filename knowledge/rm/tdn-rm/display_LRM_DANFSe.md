---
content_hash: a0daf17d6d86cd9e9ce189e23e6b28915b84df1dc68df4a75ed2fd3f810b67cf
fetched_at: '2026-06-29T00:05:53.935224+00:00'
page_id: '1072001744'
product: rm
source: tdn-rm
title: DANFSe
type: documentation
url: https://tdn.totvs.com/display/LRM/DANFSe
version: 32
---

# 

# Conteúdo

**Conteúdonone**

# 1. Visão Geral

O **DANFSe** é a representação gráfica simplificada da **NFS-e**. Ele funciona como um documento auxiliar da NFS-e impresso em papel com os objetivos de:

* Facilitar a consulta resumida dos dados da NFS-e, provendo a necessidade de  
  representações impressas previstas na legislação;
* Auxiliar os processos administrativos e financeiros do destinatário não credenciado  
  como emissor de NFS-e.

A responsabilidade pelo envio correto das informações e pelo cumprimento da obrigação acessória é inteiramente do contribuinte. Por isso, é essencial que os dados cadastrais, fiscais e operacionais estejam consistentes, garantindo a emissão adequada da NFS-e e evitando rejeições, inconsistências ou questionamentos dos órgãos competentes.

É importante destacar que o DANFSe **não substitui a NFS-e** e **não possui validade jurídica por si só**, sendo apenas uma representação para consulta e apoio operacional. A validade legal permanece vinculada ao arquivo eletrônico da NFS-e (xml), devidamente autorizado pela SEFAZ.

# 2. Configurações iniciais

Para acessar o processo **Imprimir DANFSe (smartview)**, no menu *Documentos Eletrônicos | Nota Fiscal de Serviço (NFS-e)*, é necessário fornecer a permissão conforme abaixo:

ConfigPermissões Usuários

Para dar permissão de acesso ao menu da NFS-e a um usuário, siga os passos abaixo:

* Acesse o perfil vinculado ao usuário desejado do módulo TOTVS Gestão de Estoque, Compras e Faturamento e edite o perfil;
* Vá até a aba **Acesso a Menus**, siga o caminho **[*04] Vendas | [04.02] Documentos Eletrônicos***, selecione **[04.02.01.07] Nota Fiscal de Comunicação Eletrônica (NFCom), [04.02.01.07.05] Imprimir DANFE** e logo após, clique em **Permitir Acesso**.

Segurança - Acesso - Perfis

# 3. SMART VIEW

A impressão do **DANFSe** é realizada por meio do [SMART VIEW](https://tdn.totvs.com/display/TREP/SMART+VIEW). Para instalar e configurar o SMART VIEW, consulte o guia oficial disponível em:

smart\_viewTipo relatório DANFSe

É necessário executar o RM Atualizador. Ao executá-lo será criado o tipo "**333 - DANFSE Nacional**" nos recursos do SMART VIEW, este tipo é necessário para a correta importação do relatório DANFSe.

Compartilhamento de Recursos Smart View

Durante o fluxo de uso de um recurso Smart View, é necessário o gerenciamento dos níveis de permissões dos usuários que acessarão os recursos. Na documentação abaixo você encontrará uma explicação detalhada sobre como gerenciar o acesso aos seus recursos.

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/16106157353623-Cross-Segmentos-Backoffice-RM-BI-Compartilhamento-de-recursos-no-Smart-View-Categoria>

Caso o cadastro da categoria não seja feito corretamente ou o perfil do usuário não estiver vinculado à categoria ao tentar visualizar ou salvar o relatório será exibida uma mensagem de erro com o seguinte texto: "Usuário não possui permissões de uso ao recurso".

# 4. Processo Imprimir DANFSe

O relatório **DANFSe** pode ser obtido diretamente no [TOTVS Compartilhamento](https://tdn.totvs.com/pages/viewpage.action?pageId=348297816), sendo sua impressão realizada pelo processo **Imprimir DANFSe (SmartView)**.

TOTVS Compartilhamento

* NUCREL00002 - DANFSE - V2.0 - Retrato

O processo poderá ser executado para **NFS-E** com um dos status abaixo:

* **Autorizada:** Com este status o DANFSe pode ser impresso na versão oficial para ser enviado ao cliente;
* **Cancelada**;

Caso a nota seja impressa em ambiente de homologação, será impresso em seu cabeçalho a seguinte mensagem:

* **Homologação****:** Neste caso o DANFSe será impresso com a mensagem "NFS-e SEM VALIDADE JURÍDICA". Este tipo de impressão permite a visualização do relatório antes de autorizar a nota;

O relatório pode ser gerado conforme opções abaixo:

Tipos de impressãoVisualização#002233dashed

No processo **Imprimir DANFESE**, o recurso **SmartView** já é carregado com os dados preenchidos.

Temos o tipo de geração "**Visualiza Impressão"**:

Nesta etapa basta clicar em **Enviar,** que veremos a execução do recurso **SmartView** exibindo o DANFESE para visualização:

Para o tipo de geração "**Visualizar Impressão**", só é possível realizar a impressão individual.

Impressão#002233dashed

Para imprimir a partir da Visualização basta clicar no ícone de impressão conforme destacado abaixo e selecionar a impressora de destino:

A impressão também pode ser feita após selecionar o Tipo de Geração "**Salvar em PDF**" e mandar o arquivo gerado para impressora.

Salvar em Arquivo PDF#002233dashed

O tipo de geração “**Salvar em PDF**” armazena o arquivo no diretório selecionado, utilizando como nome o **identificador do movimento**, seguido da extensão “**.PDF**”.  
Exemplo: 1440972.PDF

#002233dashed

O tipo de geração "**Visualizar Impressão**", também permite exportar o DANFESE em formato PDF:

Impressão de múltiplas NFSe

Para **Impressão Múltipla,** deve ser realizado o salvamento em formato PDF:

Após a geração dos arquivos, basta enviá-los para impressão:

# 5. Detalhamento Relatório DANFSe

A seguir, são detalhadas as divisões que compõem o DANFSe:

## 5.1 Divisão I - Informações do Cabeçalho

O cabeçalho deverá indicar obrigatoriamente os seguintes dados:

Informações do Cabeçalho#002233dashed

### DANFSe - Informações do Cabeçalho

#002233dashed

### Campos NFS-e

| Nomes | Tipos | Campos Xml |
| --- | --- | --- |
| Logomarca da NFSE | Imagem |  |
| Quadro descrição "DANFSe..." | Literal |  |
| Município | Literal | exLocEmi + UF |
| Ambiente Gerador | Literal | ambGer |
| Tipo de Ambiente | Literal | tpAmb |

## 5.2 Divisão II –  Dados da NFS-e

Local onde deverá ser impressas as informações dos dados de identificação da NFS-e:

Dados da NFS-e#002233dashed

### DANFSe - Dados da NFS-e

#002233dashed

### Campos NFS-e

| Nomes | Tipos | Campos Xml |
| --- | --- | --- |
| Chave de Acesso da NFS-e | Literal | infNFSe id |
| Número da NFS-e | Literal | nNFSe |
| Competência da NFS-e | Literal | dCompet |
| Data e Hora da Emissão da NFS-e | Literal | dhProc |
| Número da DPS | Literal | nDPS |
| Série da DPS | Literal | serie |
| Data e Hora da Emissão da DPS | Literal | dhEmi |
| Emitente da NFS-e | Literal | tpEmit |
| Situação da NFS-e | Literal | cStat |
| Finalidade | Literal | finNFSe |

## 5.3 Divisão III – Prestador /Fornecedor

Local onde deverá ser impressas as informações dos dados de Prestador / Fornecedor da NFS-e:

Prestador / Fornecedor#002233dashed

### DANFSe - Prestador / Fornecedor

#002233dashed

### Campos NFS-e

| Nomes | Tipos | Campos Xml |
| --- | --- | --- |
| CNPJ / CPF / NIF | Literal | CNPJ / CPF / NIF |
| Indicador Municipal (Inscrição) | Literal | IM |
| Telefone | Literal | fone |
| Nome / Nome Empresarial | Literal | xNome |
| Município / Sigla UF | Literal | cMun ou xCidade |
| Código IBGE / CEP | Literal | cMun + CEP ou cEndPost |
| Endereço | Literal | xLgr + nro + xCpl + xBairro |
| Email | Literal | email |
| Situação Nacional da Data de Competência | Literal | opSimpNac |
| Regime de Apuração Tributária pelo SN | Literal | regApTribSN |

## 5.4 Divisão IV – Tomador/ Adquirente

Local onde deverá ser impressas as informações dos dados de Tomador / Adquirente da NFS-e:

Tomador/ Adquirente#002233dashed

### DANFSe - Tomador / Adquirinte

#002233dashed

### Campos NFS-e

| Nomes | Tipos | Campos Xml |
| --- | --- | --- |
| CNPJ / CPF / NIF | Literal | CNPJ / CPF / NIF |
| Indicador Municipal (Inscrição) | Literal | IM |
| Telefone | Literal | fone |
| Nome / Nome Empresarial | Literal | xNome |
| Município / Sigla UF | Literal | cMun ou xCidade |
| Código IBGE / CEP | Literal | cMun + CEP ou cEndPost |
| Endereço | Literal | xLgr + nro + xCpl + xBairro |
| Email | Literal | email |

## 5.5 Divisão V – Destinatário da Operação

Local onde deverá ser impressas as informações dos dados do Destinatário da Operação da NFS-e:

Destinatário da Operação#002233dashed

### DANFSe - Destinatário da Operação

#002233dashed

### Campos NFS-e

| Nomes | Tipos | Campos Xml |
| --- | --- | --- |
| CNPJ / CPF / NIF | Literal | CNPJ / CPF / NIF |
| Telefone | Literal | fone |
| Nome / Nome Empresarial | Literal | xNome |
| Município / Sigla UF | Literal | cMun ou xCidade |
| Código IBGE / CEP | Literal | cMun + CEP ou cEndPost |
| Endereço | Literal | xLgr + nro + xCpl + xBairro |
| Email | Literal | email |

## 5.6 Divisão VI – Intermediário da Operação

Local onde deverá ser impressas as informações dos dados do Intermediário da Operação da NFS-e:

Intermediário da Operação#002233dashed

### DANFSe - Intermediário da Operação

#002233dashed

### Campos NFS-e

| Nomes | Tipos | Campos Xml |
| --- | --- | --- |
| CNPJ / CPF / NIF | Literal | CNPJ / CPF / NIF |
| Indicador Municipal (Inscrição) | Literal | IM |
| Telefone | Literal | fone |
| Nome / Nome Empresarial | Literal | xNome |
| Município / Sigla UF | Literal | cMun ou xCidade |
| Código IBGE / CEP | Literal | cMun + CEP ou cEndPost |
| Endereço | Literal | xLgr + nro + xCpl + xBairro |
| Email | Literal | email |

## 5.7 Divisão VII – Serviço Prestado

Local destinado à exibição dos valores do serviço prestado:

Serviço#002233dashed

### DANFSe - Serviço Prestado

#002233dashed

### Campos NFSE

| Nomes | Tipos | Campos Xml |
| --- | --- | --- |
| Código Tributação Nacional / Municipal | Literal | cTribNac + cTribMun |
| Código NBS | Literal | cNBS |
| Local da Prestação/ Sigla UF / País | Literal | xLocPrestacao + cPaisPrestacao |
| Descrição do Código de Tributação Nacional / Municipal | Literal | xTribNac + xTribMun |
| Descrição do Serviço | Literal | xDescServ |

## 5.8 Divisão VIII – Tributação Municipal (ISSQN)

Local destinado à exibição dos valores do tributo ISSQN:

Tributação ISSQN#002233dashed

### DANFSe - Tipo de Tributação Municipal (ISSQN)

#002233dashed

### Campos NFSE

| Nomes | Tipos | Campos Xml |
| --- | --- | --- |
| Tipo de Tributação do ISSQN | Literal | tribISSQN |
| Município / Sigla UF / País de Incidência do ISSQN | Literal | xLocIncid + cPaisResult |
| Regime Especial de Tributação do ISSQN | Literal | regEspTrib |
| Tipo de Imunidade do ISSQN | Literal | tpImunidade |
| Suspensão de Elegibilidade do ISSQN | Literal | tpSusp |
| Número Processo Suspensão | Literal | nProcesso |
| Benefício Municipal | Literal | tpBM |
| Cálculo BM | Literal | vCalcBM ou vRedBCBM |
| Total Deduções / Reduções | Literal | vDR ou vCalcDR + vCalcReeRepRes |
| Desconto Incondicionado | Literal | vDescIncond |
| BC ISSQN | Literal | vBC |
| Alíquota Aplicada | Literal | pAliqAplic |
| Retenção do ISSQN | Literal | tpRetISSQN |
| ISSQN Apurado | Literal | vISSQN |

## 5.9 Divisão IX – Tributação Federal (Exceto CBS)

Local destinado à Tributação Federal, exceto CBS

Tributação Federal (Exceto CBS)#002233dashed

### DANFSe - Tributação Federal

#002233dashed

### Campos NFS-e

| Nomes | Tipos | Campos Xml |
| --- | --- | --- |
| PIS - Débito Apuração Própria | Literal | vPIS |
| IRRF | Literal | vRetIRRF |
| COFINS - Débito Apuração Própria | Literal | vCOFINS |
| Contribuição Previdenciária - Retida | Literal | vRetCP |
| Descrição Contrib. Sociais - Retidas | Literal | - |
| Contribuições Sociais - Retidas | Literal | vRetCSLL |

## 5.10 Divisão X – Tributação IBS/CBS

Local destinado à tributação do IBS/CS

Tributação IBS/CBS#002233dashed

### DANFSe - Tributação IBS/CBS

#002233dashed

### Campos NFS-e

| Nomes | Tipos | Campos Xml |
| --- | --- | --- |
| CST / cClassTrib | Literal | CST + cClassTrib |
| Exclusões e Reduções da Base de Cálculo | Literal | - |
| Alíq. Efetiva Municipal - IBS | Literal | pAliqEfetMun |
| Valor Total Apurado - IBS | Literal | vIBS |
| Base de Cálculo Após Exclusões e Reduções | Literal | vBC |
| Valor Apurado Municipal - IBS | Literal | vIBSMun |
| Alíquota - CBS | Literal | pCBS |
| Red. Alíquota IBS - Red Alíquota CBS | Literal | pRedAliqMun / pRedAliqUF / pRedAliqCBS |
| Aliq. Efetiva Estadual - IBS | Literal | pAliqEfetUF |
| Alíquota Efetiva - CBS | Literal | pAliqEfetCBS |
| Alíquota - IBS UF / IBS Mun | Literal | pIBSMun / pIBSUF |
| Valor Apuração Estadual - IBS | Literal | vIBSUF |
| Valor Total Apurado - CBS | Literal | vCBS |

## 5.11 Divisão XI – Valor Total da NFS-e

Local onde deverá ser impressas as informações dos dados do Valor Total da NFS-e:

Valor Total da NFS-e#002233dashed

### DANFSe - Valor Total da NFS-e

#002233dashed

### Campos NFS-e

| Nomes | Tipos | Campos Xml |
| --- | --- | --- |
| Valor da Operação | Literal | vServ |
| Desconto Incondicionado | Literal | vDescIncond |
| Desconto Condicionado | Literal | vDescCond |
| Total das Retenções (ISSQN / Federais) | Literal | vTotalRet |
| Valor Líquido da NFS-e | Literal | vLiq |
| Total do IBS / CBS | Literal | vIBSTot + vCBS |
| Valor Líquido da NFS-e + IBS / CBS | Literal | vTotNF |

## 5.12 Divisão XII – Informações Complementares

Área destinada à impressão de mensagens de interesse fiscal contida no arquivo eletrônico da NFS-e:

Informações Complementares#002233dashed

### DANFSe - Informações Complementares

#002233dashed

### Campos NFS-e

| Nomes | Tipos | Campos Xml |
| --- | --- | --- |
| Informações Complementares | Literal | xInfComp + chSubstda + docRef + cObra + inscImobFisc + idAtvEvt + idDocTec + xPed + xItemPed + xOutInf + vTotTribFed, vTotTribEst e vTotTribMu ou pTotTribFed, pTotTribEst e pTotTribMu + Totais Aproximados dos Tributos |

## 5.13 NOTAS - Grupos não informados

Seguem as notas que mudam o comportamento de alguns grupos e definem o comportamento de campos específicos.

Grupos não informados

***Nota 1:*** *Esta linha poderá ser suprimida, ainda que existam dados dos respectivos campos no arquivo XML.*

#002233dashed

### DANFSe - Prestador/Fornecedor, Tomador/Adquirente, Destinatário e Intermediário da Operação

***Nota 2:*** Caso não contenha dados informados de tomador/adquirente, destinatário e/ou intermediário da operação serão exibidos blocos suprimidos com as descrições correspondentes ao grupo.

#002233dashed

### DANFSe - Informações não identificadas

***Nota 3:*** Caso o destinatário da operação seja o próprio tomador/adquirente, será exibido o bloco suprimido com a descrição correspondente ao grupo.

#002233dashed

### DANFSe - Destinatário é o próprio Tomador/Adquirente

  

***Nota 4:*** Para as operações às quais não haja a incidência do ISSQN, será exibido o bloco suprimido com a descrição correspondente ao grupo.

#002233dashed

### DANFSe - Operação não sujeita ao ISSQN

  

***Nota 5:*** *Esta linha poderá ser suprimida caso **não existam dados em todos os campos da mesma linha** no arquivo*.

#002233dashed

### DANFSe - Linhas do ISSQN que podem ser suprimidas

### 

***Nota 6:*** *Esta linha será impressa para as NFS-e emitidas com data de competência até o final do ano-calendário de 2026.*

#002233dashed

### DANFSe - Linha suprimida para competências superiores a 2026

***Nota 7:*** *Em caso de substituição da NFS-e, deve-se informar, no campo de informações complementares, a chave de acesso da NFS-e substituída. Esta informação deverá ser disposta da seguinte forma: NFS-e Subst.: + chave de acesso da NFS-e substituída.*

#002233dashed

### DANFSe - Informação da chave da nota substituída

***Nota 8:*** *Nos casos de obrigatoriedade de preenchimento do grupo de Obra/Imóvel, deverão constar, no campo de informações complementares, o número de identificação da obra e/ou a inscrição imobiliária fiscal, conforme campos “cObra” e “inscImobFisc”, respectivamente, do leiaute da DPS/NFS-e. Estas informações deverão ser dispostas da seguinte forma: Cod. Obra: e Insc. Imob.: + respectivas informações.*

#002233dashed

### DANFSe - Informação de identificação da obra e/ou inscrição imobiliária fiscal

***Nota 9:*** *Nos casos de obrigatoriedade de preenchimento do grupo de Evento, deverá constar, no campo de informações complementares, a identificação da atividade de evento, conforme campos “idAtvEvt”, do leiaute da DPS/NFS-e. Esta informação deverá ser disposta da seguinte forma: Cod. Evt.: + respectiva informação.*

#002233dashed

### DANFSe - Informação de identificação da atividade de evento

***Nota 10:*** *Deve-se constar, obrigatoriamente, a informação de totais aproximados de tributos, que pode ser em preenchida com valores monetários OU percentuais, disposta da seguinte forma: "Totais Aproximados dos Tributos cfe. Lei nº 12.741/2012: Federais: R$ ou % ; Estaduais: R$ ou % ; Municipais: R$ ou %".*

#002233dashed

### DANFSe - Informação de identificação dos totais aproximados de tributos

***Nota 11:*** *Bloco opcional.*

#002233dashed

### DANFSe - Canhoto (Não é gerado)

***Nota 12:*** *Os campos sem informações no XML devem ser preenchidos com um traço (-).*

#002233dashed

### DANFSe - Campos sem valor preenchidos com (-)
