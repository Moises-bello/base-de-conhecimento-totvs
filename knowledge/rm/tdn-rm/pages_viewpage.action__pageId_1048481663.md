---
content_hash: 86a521bbfe422189411bf1417ea9121443eb2dbd7448e113dd44dc78270128f2
fetched_at: '2026-06-29T00:05:51.174596+00:00'
page_id: '1048481663'
product: rm
source: tdn-rm
title: Documentação sobre Uso e Histórico de Atualizações TISS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1048481663
version: 25
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Histórico de Atualizações de versões TISS**
3. **Guia de Uso**
4. **Alterações da Versão TISS 4.02.00**
5. **Alterações da Versão TISS 4.03.00**

historicoTissgeralidVisão Geral

Este documento tem por finalidade explicar o uso e históricos de atualizações de versão para os Convênios (Operadoras de Saúde) que realizam faturamento eletrônico no padrão TISS (Troca de Informação de Saúde Suplementar), definido pela ANS (Agencia Nacional de Saúde Suplementar).

O Padrão TISS abrange as trocas dos dados de atenção à saúde prestada ao beneficiário de **Plano Privado** de Assistência à Saúde, gerados na rede de **Prestadores** de Serviços de Saúde da Operadora de planos privados de assistência à saúde.

Entende-se como rede de prestadores de serviços de saúde da operadora de planos privados de assistência à saúde: (RN 501)

 Rede de serviços de saúde contratada, referenciada ou credenciada, de forma direta ou indireta; e

 Rede própria da operadora; de entidade ou empresa controlada pela operadora; de entidade ou empresa controladora da operadora e profissional assalariado ou cooperado da operadora.

**Trocas de informações estabelecidas no Padrão TISS -** **Entre operadoras e prestadores de serviços de saúde**

Entre operadoras e prestadores de serviços de saúde, os processospadronizados para troca eletrônica de implantação **obrigatória** são:

- Cobrança de serviços de saúde;

- Autorização de serviços (somente a mensagem de lote de anexos);

- Comunicação de internação ou alta do beneficiário; **(obrigatório a partir da versão 4.03.00)**

- Demonstrativos de retorno;

- Recurso de glosas;

Os processos padronizados para troca eletrônica de implantação **opcional** são:

- Verificação de elegibilidade;

- Autorização de procedimentos (exceto a mensagem de lote de anexos);

- Envio e recebimento de documentos.

**Resumo das mensagens no Padrão TISS – Origem da mensagem Prestador**

|  |  |
| --- | --- |
| **Nome da mensagem no**  **Schema TISS** | **Descrição** |
| LoteGuias | Apresentação de cobrança de consultas, SP/SADT, resumo de internação, honorários e odontologia. |
| LoteAnexos | Apresentação do anexo de situação inicial de odontologia e solicitação de autorização de tratamento de quimioterapia, radioterapia e OPME. |
| SolicitaçãoDemonstrativoRetorno | Solicitação de demonstrativo de análise de conta ou demonstrativo de pagamento. |
| SolicitaçãoStatusProtocolo | Solicita informação de lote de cobrança ou documento recebido pela operadora. |
| SolicitacaoStatusRecursoGlosa | Solicita informação sobre recurso de glosa enviado pelo prestador à operadora. |
| SolicitaçãoProcedimento | Solicitação de autorização de serviços de SP/SADT, internação, prorrogação de internação e tratamento em odontologia. |
| SolicitaStatusAutorização | Solicita status sobre pedido de autorização recebido pela operadora. |
| VerificaElegibilidade | Solicita informação sobre a elegibilidade de um beneficiário da operadora. |
| CancelaGuia | Envia solicitação de cancelamento de lote de guias, guias ou recurso de glosa. |
| ComunicaçãoInternação | Envia comunicado de internação ou alta de um beneficiário. |
| RecursoGlosa | Envia recurso sobre glosa ocorrida em um lote ou em guias do prestador. |
| EnvioDocumentos | Envia documentos complementares para a solicitação, autorização, cobrança e/ou recurso de glosa de procedimentos/itens assistenciais. |

historicoHistórico de Atualizações de versões TISS

A documentação oficial das versões TISS encontram-se no site da TISS - Padrão para Troca de Informação de Saúde Suplementar

<https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss>

Deverá ser feito download de todos os documentos disponibilizados neste link.

O resumo das alterações se encontra no link sobre “Componente Organizacional”. Os demais arquivos explicam as alterações em cada estrutura.

aplicacaoGuia de Uso

As documentações sobre configurações e uso da TISS são:

1. **Cadastros TISS:**

Para faturamento de convênios que utilizam padrão TISS é necessário cadastrar informações no menu **Cadastros/Uso Geral/TISS**

1. 1. **Motivo de Alta:** <https://tdn.totvs.com/x/JNumHw>

2 – Faturamento para Convênio: <https://tdn.totvs.com/x/lt6ZJQ>

3 - Envio de XML TISS para Operadora de Saúde: <https://tdn.totvs.com/x/d4rRM>

4 – Importação e Processamento de XML da Operadora: <https://tdn.totvs.com/x/EbSGNg>

Para acessar, utilize o menu:  
**Faturamento** **→** **Faturamento para Conv****ê****nios** **→** **Anexo Fatura de Recurso** **→** **Importa****çã****o do XML de Resposta do Recurso de Glosa**

5 – Número do Protocolo da Remessa: <https://tdn.totvs.com/x/ggtNKQ>

6 - Regras customizadas para Geração XML TISS: <https://tdn.totvs.com/x/sqpLK>

7 - Regras de envio da codificação TISS:  <https://tdn.totvs.com/x/DdkaLg>

8 - Regras de geração XML Santa Casa - Faturamento Unimed Curitiba: <https://tdn.totvs.com/x/WRHQHw>

9 - Regras de preenchimento da TAG Local Contratado: <https://tdn.totvs.com/x/XV1nIw>

10 - Usar Token para solicitar Autorização: <https://tdn.totvs.com/x/ze0aLg>

tiss402Alterações da Versão TISS 4.02.00

Disponibilizada para utilização a partir das versões de mercado 12.1.2502, 12.1.2506 e 12.1.2510 do produto Gestão Hospitalar, contemplada nos patches liberados a partir de 01/10/2025.

tiss403Alterações da Versão 4.03.00

As alterações para uso da versão 4.03.00 da TISS encontra-se em construção.

alteracoes43doctiss43Documentação TISS

A documentação oficial encontra-se no link abaixo:

## Padrão TISS – Janeiro/2026: documentação para a versão 4.03.00 - <https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss/padrao-tiss-janeiro-2026>

250

scripttiss431 - Script necessário

Ao executar o Atualizardor.exe, as alterações abaixo serão aplicadas na base de dados:

* Inserir registros necessário para as Tabelas de Domínio da TISS 4.03, menu Cadastros/Uso Geral/TISS,
* Inserir registros necessário para a TISS 4.03 Tabela 38 (Mensagens de glosas/negativas), na base de dados  SZANSMOTIVOGLOSA do menu Cadastros/Uso Geral/TISS/Mensagens de negativa de elegibilidade,
* Criação da tabela TISS/ANS-Centro de Consumo (SZANSCENTROCONSUMO), referente à Terminologia de Centro de Consumo (tabela 82), da versão 4.03.00 da TISS,
* Criação da  tabela SZANSCENTROCONSUMOCORRELA utilizada no menu Cadastros/Uso Geral/TISS/Correlação Centro de Consumo,
* SA.2026.04\_04 – Observação no demonstrativo de análise de conta.
* SA.2026.04\_15 – Campo "Plano exclusivamente hospitalar" no Cadastro de Planos de Convênio.
* SA.2026.04\_11 – Criação da Tabela de domínio SZANSCOBERTURAESPECIAL
* SA.2026.05\_06 - Adicionado campo de identificação para WebService utilizado durante gravação de log para TISS, campo TIPODOCGERACAO na tabela SZANSLOGAUTORIZ  
  SA.2026.05\_13 **-** Criação de Tabela SZANSLOGCOMUNICACAO para controle de Log para envios de comunicação de Internação e Alta TISS e Criação da tabela SZANSCOMUNICACAO para controle de comunicação e retorno de Internação e Alta TISS

centroconsumo432 – Centro de Consumo - Novo componente TISSitenscentroconsumo43terminologiaconsumoNova Terminologia

Criado nova Terminologia TISS - Centro de Consumo (Tabela 82) e utilizado na geração de XML das guias abaixo e seus respectivos impressos.

menucorrelacaoNovo item no menu Cadastros TISS

**Criação do menu Cadastros/Uso Geral/TISS/Correlação Centro de Consumo, para associar os códigos de centro de consumo da TISS-ANS (tabela 82) com os centros de custo do Gestão Hospitalar.**

Ao realizar o “Encerramento da Parcial”, será feito a seguinte validação referente à TISS versão 4.03.00:

- Nos lançamentos de MatMed, o centro de custo deve ter um cadastro de correlação ao centro de consumo ANS.

O novo menu deverá ser configurado permissão de acesso no Perfil de Usuário

No Release 12.1.2602 e superiores, a tela deste cadastro utiliza a nova tecnologia SmartX.

tecnicaconsumoDescrição técnica dos componentes TISS

As alterações citadas na documentação TISS sobre o novo campo centro de consumo são:

6.14. No Componente de Conteúdo e Estrutura, nas mensagems loteGuia (Guia de Resumo de Internação e Outras Despesas – internação), recursoGlosa e demonstrativosRetorno, e nas respectivas guias do Plano de Contingência,

foi incluindo o termo (campo) “Centro de Consumo”.

6.16. No Componente de Comunicação, schema TissSimpleTypesV4\_03\_00, foi o incluído o elemento dm\_centroConsumo.

6.20. No Componente de Comunicação, schema tissGuiasV4\_03\_00, "ctm\_recursoGlosa” foi incluído o elemento dm\_centroConsumo no complex type "itensGuia".

6.21. No Componente de Comunicação, schema tissComplexTypesV4\_03\_00, em ct\_contaMedicaResumo, ct\_procedimentoExecutado, ct\_procedimentoExecutadoInt e ct\_procedimentoExecutadoOutras foi incluído o elemento dm\_centroConsumo.

guiaxmlconsumoGuias XML alteradas

**Guias XML - Incluindo o termo (campo) “Centro de Consumo” nas informações das seguintes guias TISS:**

**Guia de Resumo de Internação e Outras Despesas – internação (estrutura da mensagem loteGuia).**

**Guia (estrutura da mensagem recursoGlosa).**

**Guia (estrutura da mensagem demonstrativosRetorno)**

reltissconsumoRelatórios TISS alterados

**Incluído a mesma informação nos relatórios impressos, que foram alterados e disponibilizados no Book de Relatório.**

* **Anexo de Outras Despesas (antigo SAUREL0028) - campo 28.**

* **Resumo de Internação (antigo SAUREL0029 e antigo SAUREL0027) - campo 67.**

* **Recurso de glosas (antigo SAUREL0134) - campo 37.**

cnpjAlfa3 – CNPJ Alfanumérico

No componente de Comunicação, os simple types “st\_CNPJ” e “st\_CNPJCPFPadrao” foram alterados para adequação do CNPJ ao padrão alfanumérico (Instrução Normativa RFB nº 2.229): raiz (8 caracteres

alfanuméricos) – ordem do estabelecimento (4 caracteres alfanuméricos) e dígito verificador (2 caracteres numéricos).

Alterado o formato do CNPJ para permitir dígitos e letras.

Os 12 primeiros caracteres são alfanuméricos e o dígito verificador somente números. Por exemplo **A1.B2C.3D4/E5F6-99**

assinaturaDig4 – Assinatura Digital opcional– alterado para obrigatória

Na guia de autorização TISS, ao gerar o processo “Envio de Documento”, o arquivo xml será gravado com uma assinatura digital, a partir da versão 4.03.00.

É obrigatório existir um certificado digital com as características solicitadas pela ANS, descritas abaixo.

Ao enviar um documento para a Operadora, será solicitado escolher o certificado digital.

No componente Organizacional, seção V – Padrão TISS / Escopo, o item 21 da versão 202309 foi alterado:

“O certificado digital ICP-Brasil a que se refere o item anterior, assim como aqueles utilizados para assinatura pelas operadoras e prestadores, deve ser do tipo e-CNPJ referente à instituição que está transmitindo a mensagem, e se destina a realização de assinatura digital das mensagens eletrônicas, a fim de garantir a integridade e identificar sua origem institucional, agregando a propriedade de não-repúdio.

Caso o agente atue como pessoa física o certificado deverá ser o e-CPF.”

**A informação passa a ser obrigatória na versão 4.03.00.**

O certificado digital exportado, a ser utilizado deverá possuir propósito de uso de assinatura digital, ou seja, ter o campo key usage definido como Digital Signature e NonRepudiation e verificar se é certificado digital ICP-Brasil de assinatura tipo A1, A2, A3 ou A4.

Ao executar o processo "Enviar Documento", caso a versão TISS do Convênio seja igual ou maior que 4.03.00, será realizado as seguintes validações:

* Obrigatório existir certificado de assinatura digital.
* A assinatura digital requer uma chave definida como tipo Digital Signature e NonRepudiation definida na propriedade Key Usage.
* O certificado utilizado deve ser ICP-Brasil do tipo e-CNPJ (institucional) ou e-CPF (quando o prestador atuar como pessoa física)**.**
* A data de validade do certificado não deverá estar expirada.

Exemplo de propriedades do certificado:

Propriedade Uso da Chave (“Key Usage”):  Assinatura Digital e Não-Recusa

Propriedade Uso Avançado de Chave (“Extended Key Usage”): deve conter OID = 1.3.6.1.5.5.7.3.3 referente a Assinatura de Código.

Propriedade Válido até: a data não poderá estar vencida

honorarioCarater5 - Guia de Honorário - Caráter de atendimento

Inclusão do campo 42 - “Caráter de atendimento” na Guia de Honorários e seus respectivos relatório impressos (antigo SAUREL0047 e antigo SAUREL0048) , que foram alterados e disponibilizados no Book de Relatório.

**5.1 - Descrição técnica dos componentes TISS**

6.13. No Componente de Conteúdo e Estrutura, na mensagem loteGuia (Guia

de Honorários) e na Guia de Honorários do Plano de Contingência, foi

incluindo o termo (campo) “Caráter do atendimento”.

6.19. No Componente de Comunicação, schema tissGuiasV4\_03\_00,

"ctm\_honorarioIndividualGuia” foi incluído o elemento “caraterAtendimento”

no complex type "dadosInternacao".

demonstrativoObs6 – Demonstrativo de Análise de Conta – campo Observação

A atualização do padrão TISS versão 4.03.00 incluiu, no componente Conteúdo e Estrutura, o termo Observação/Justificativa na mensagem Demonstrativo de Análise de Conta (**demonstrativoRetorno**). Fluxo: Operadora para Prestador

Essa mensagem é utilizada pela operadora para retornar ao prestador o resultado da análise das contas, podendo incluir observações adicionais relacionadas ao processamento da guia.

**Relatório impresso:**

**6.1 - Descrição técnica dos componentes TISS**

6.12. No Componente de Conteúdo e Estrutura, na mensagem Demonstrativo

de Análise de Conta foi incluído o termo (campo) “Observação” no final das

informações da guia (após o “Valor glosa da guia”).

6.22. No Componente de Comunicação, schema tissComplexTypesV4\_03\_00,

em ct\_contaMedicaResumo, foi incluído o elemento "observacao” após o

grupo de elementos com os valores das guias.

comunicacaoInternacao7 - Comunicação de internação ou alta do beneficiário - Obrigatório

O processo TISS Comunicação de internação ou alta do beneficiário passa a ser obrigatório, conforme texto abaixo da documentação disponibilizada sobre versão 4.03

**Trocas de informações estabelecidas no Padrão TISS - Entre operadoras e prestadores de serviços de saúde**

Os processos padronizados para troca eletrônica de implantação **obrigatória** são:

- Cobrança de serviços de saúde;

- Autorização de serviços (somente a mensagem de lote de anexos);

**-** **Comunicação de internação ou alta do beneficiário;**

- Demonstrativos de retorno;

- Recurso de glosas;

Nesse processo ocorre a comunicação sobre a internação ou alta do beneficiário. Para tanto, é necessário identificar o beneficiário.

**7.1 -  Comunicação de internação/alta:** é a mensagem do prestador para a operadora com a informação da data de internação ou alta de um beneficiário.

**comunicacaoBeneficiarioWS** -> Prestador envia informação sobre internação/alta de beneficiário na estrutura do xml ctm\_beneficiarioComunicacao

**Neste xml foi incluído o campo “centroConsumo”.**

**7.2 - Recibo de comunicação:** é a mensagem da operadora para o prestador de recebimento da comunicação de internação ou alta de um beneficiário.

**reciboComunicacaoWS** -> Operadora responde a informação de internação/alta de beneficiário na estrutura do xml ct\_reciboComunicacao.

**Não houve alteração.**

coberturaEspecial8 - Cobertura Especial foi alterada de “Opcional” para “Condicionado”

No componente de Conteúdo e Estrutura a condição de preenchimento do termo (campo) Cobertura Especial foi alterada de “Opcional” para “Condicionado” em todas as mensagens e nas guias do Plano de Contingência (Relatórios) em que o termo está presente.

**No Totvs Gestão Hospitalar,** para atender a versão 4.03.00 da TISS, foi criado o novo campo **“Plano com cobertura exclusivamente Hospitalar”** no menu **“Cadastros/Faturamento/Outros/Planos de convênios”**.

Caso esteja marcado como exclusivamente hospitalar e a versão TISS deste convênio for maior ou igual a 4.03.00, então o campo “Cobertura Especial” passará a ser de preenchimento obrigatório nas guias de autorização do tipo SP-SADT e guia de Consulta.

Na Guia de Consulta, o campo "Cobertura Especial" somente será habilitado se o Convênio estiver na versão TISS igual ou superior a 4.03.00.

Necessário executar script marcação SA.2026.04\_15 pelo Atualizador.exe.

Criação da tabela SZANSCOBERTURAESPECIAL contendo os códigos da tabela de domínio TISS 75 - Terminologia de Cobertura Especial, incluído na versão 4.03.00 da TISS, referente ao campo “Cobertura Especial” da Guia de Autorização no Gestão Hospitalar, marcação SA.2026.04\_11.

Na guia de autorização TISS e na Central de Autorizações, o campo “Cobertura especial” passará a listar os itens desta tabela de acordo com a versão TISS do convênio.

Ao realizar o “Encerramento da Parcial”, será feito as seguintes validações referentes à TISS versão 4.03.00:

- O campo cobertura especial deve ser informado no cabeçalho das guias de Consulta e guia SP-SADT, caso o plano do convênio esteja marcado como “Plano exclusivamente hospitalar”.

- Nos lançamentos de MatMed, o centro de custo deve ter um cadastro de correlação ao centro de consumo ANS.

relatoriosTissPlano de Contingência – Relatórios TISS

Plano de Contingência – Relatórios TISS

Os seguintes relatórios de contingência da TISS foram alterados:

|  |  |  |
| --- | --- | --- |
| **Nome Guia TISS** | **Campo Incluído** | **Relatório no Totvs Gestão Hospitalar** |
| Anexo outras despesas | 28 – Centro de Consumo | SAUREL0028 – Guia de Outras Despesas |
| Demonstrativo de análise de conta | 50 – Centro de Consumo |  |
| Guia Resumo de Internação | 67 – Centro de Consumo | SAUREL0029 e SAUREL0027 |
| Guia Recurso de Glosa | 37 – Centro de Consumo | SAUREL0134 – Recurso de Glosa |
|  |  |  |
| Guia de Consulta | 27 – Indicador de Cobertura Especial | SAUREL0094 – Guia de Consulta - MSSQL (TISS403)  \*\*já existia a descrição do campo, passará a preencher com a informação |
| Guia de SP/SADT | 90 – Indicador de Cobertura Especial | SAUREL0049 – Guia de Solicitação de SP-SADT (MSSQL)  SAUREL0050 – Guia de Solicitação de SP-SADT (ORACLE)  \*\*já existia a descrição do campo, passará a preencher com a informação    SAUREL0054 – Guia de Solicitação de SP-SADT (Pedido de Exames) - MSSQL (TISS403)  SAUREL0055 – Guia de Solicitação de SP-SADT (Pedido de Exames) – ORACLE (TISS403)  \*\*incluir o campo no relatório    Lista de relatórios de GUIA SP-SADT no Saúde: |
