---
content_hash: 4adb3d648b2746930f504c04b1cd608268d5a977a8122a76cf0b5b675086114f
fetched_at: '2026-06-29T00:10:31.738004+00:00'
page_id: '522002763'
product: rm
source: tdn-rm
title: Anonimizar usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=522002763
version: 5
---

Informações

Atenção

Esta funcionalidade está disponível a partir da versão 12.1.27.

## **CONTEÚDO**

1. **Visão Geral**
2. **Regras para anonimizar usuários**
3. **Processo para anonimizar usuários**

## **01. VISÃO GERAL**

Para atender a [Lei Nº 13.709/18](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm) foi criado o processo "anonimizar usuários", este processo irá verificar se o usuário do processo seletivo possui algum vínculo com algum processo seletivo, se não possuir o processo irá excluir o usuário, caso este possua algum vínculo o sistema irá verificar algumas regras (descritas no item 02) e se o usuário for elegível para anonimizar o sistema irá alterar os campos permitidos e definidos para um valor fictício (ex: 000).

Campos passíveis de anonimizar:

| Coluna | Descrição |
| --- | --- |
| APELIDO | Apelido |
| CARTEIRATRAB | Número da carteira de trabalho |
| CARTIDENTIDADE | Número da carteira de identidade |
| CARTMOTORISTA | Número da carteira de motorista |
| CATEGMILITAR | Categoria Militar |
| CERTIFRESERV | Número do certificado de reservista |
| CPF | CPF |
| CSM | Circunscrição do Serviço Militar |
| DATANATURALIZACAO | Data de naturalização do estrangeiro no brasil |
| DTCARTTRAB | Data de emissão da carteira de trabalho |
| DTEMISSAOCNH | Data de emissão CNH |
| DTEMISSAOIDENT | Data de emissão da identidade |
| DTEMISSAORIC | Data de emissão do registro único de cadastro |
| DTEMISSAORNE | Data de emissão do registro nacional de estrangeiros |
| DTEMISSPASSAPORTE | Data Emissão Passaporte |
| DTEXPCML | Data de Emissão do Certificado Militar |
| DTTITELEITOR | Data de emissão do Título de Eleitoral |
| DTVALPASSAPORTE | Data Validade Passaporte |
| DTVENCHABILIT | Data de Vencimento da Habilitação |
| EMAIL | E-mail |
| ESTELEIT | UF do título eleitoral |
| EXPED | Órgão Expedidor do Certificado Militar |
| FAX | Fax |
| NIT | Tipo de carteira de trabalho |
| NOME | Nome |
| NOMESOCIAL | Nome Social |
| NPASSAPORTE | Número do passaporte |
| NUMERORIC | Número do registro único de cadastro |
| ORGEMISSORCNH | Orgão emissor da carteira habilitação |
| ORGEMISSORIDENT | Órgão emissor da identidade |
| ORGEMISSORRIC | Orgão emissor do registro único de cadastro |
| ORGEMISSORRNE | Orgão emissor do registro nacional de estrangeiros |
| PORTARIANATURALIZACAO | Portaria de Naturalização |
| REGPROFISSIONAL | Registro profissional |
| RM | Região Militar |
| SECAOTITELEITOR | Seção de votação |
| SERIECARTTRAB | Série da carteira de trabalho |
| SITMILITAR | Situação militar |
| TELEFONE1 | Telefone para contato (opção I) |
| TELEFONE2 | Telefone para contato (opção II) |
| TELEFONE3 | Telefone para contato (Opção III) |
| TIPOCARTHABILIT | Tipo de Carteira de Habilitação |
| TITULOELEITOR | Título de eleitor |
| UFCARTIDENT | UF da carteira de identidade |
| UFCARTTRAB | UF da carteira de trabalho |
| UFCNH | UF de Emissão da Carteira de Motorista |
| ZONATITELEITOR | Zona de votação |

## **02. REGRAS PARA ANONIMIZAR USUÁRIOS**

O usuário que possuir vínculo com pelo menos um processo seletivo só poderá ser anonimizado se atender as regras abaixo:

* Se o usuário não foi matriculado através do processo de matrícula do processo seletivo RM no TOTVS Educacional.
* Se o processo seletivo estiver inativo, sem data válida e o usuário não foi matriculado pelo TOTVS Educacional.
* Se o processo seletivo estiver ativo e válido e a inscrição estiver cancelada.
* Se o usuário não tiver nenhum lançamento gerado em seu nome por um processo seletivo.

## **03. PROCESSO PARA ANONIMIZAR USUÁRIOS**

Para ter acesso ao processo é necessário que seja concedida permissão ao item de menu no perfil desejado:

O processo será executado com base na visão de usuários, sendo necessário somente selecionar o(s) usuário(s) que o sistema irá executar o processo.

O processo será executado em segundo plano e seu resultado poderá ser consultado no rodapé do TOTVS Educacional:

Log do processo:

Dados do usuário anonimizado:
