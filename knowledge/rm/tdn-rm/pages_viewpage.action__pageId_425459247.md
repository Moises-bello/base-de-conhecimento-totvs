---
content_hash: 14ee741fcf874ba3e327865c9817e1dc123a7a4d52362079b6d0363556813f5c
fetched_at: '2026-06-29T00:09:34.789554+00:00'
page_id: '425459247'
product: rm
source: tdn-rm
title: Layout de Importação de Usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459247
version: 3
---

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **ORDEM** | **NOME** | **DESCRIÇÃO** | **OBRIGATÓRIO** | **TIPO** | **VALIDAÇÃO/MÁSCARA** |
| 1 | NOME | Nome do usuário (cliente) da biblioteca | Sim | Texto(120) |  |
| 2 | TIPOUSUARIO | Tipo de usuário | Sim | Inteiro | Ver tabela LTIPOUSUARIO (referência 8) |
| 3 | DATACADASTRAMENTO | Data de cadastramento | Sim | Data | DD/MM/AAAA |
| 4 | APELIDO | Apelido | Não | Texto(40) |  |
| 5 | DTNASCIMENTO | Data de nascimento | Não | Data | DD/MM/AAAA |
| 6 | SEXO | Sexo | Não | Texto(1) | F - Feminino M - Masculino |
| 7 | NACIONALIDADE | Nacionalidade | Não | Texto(3) | Ver tabela PCODNACAO (referência 9) |
| 8 | NATURALIDADE | Naturalidade | Não | Texto(32) |  |
| 9 | ESTADONATAL | Estado natal | Não | Texto(2) | Ver tabela GETD (referência 10) |
| 10 | ESTADOCIVIL | Estado civil | Não | Texto(1) | C - Casado D - Desquitado I -  Divorciado O - Outros S - Solteiro V - Viúvo |
| 11 | GRAUINSTRUCAO | Grau de instrução | Não | Texto(3) | Ver tabela PCODINSTRUCAO (referência 7) |
| 12 | EMAIL | E-mail | Não | Texto(60) |  |
| 13 | RUA | Endereço: Logradouro (rua, av., praça, etc.) | Não | Texto(100) |  |
| 14 | NUMERO | Endereço: Número | Não | Texto(8) |  |
| 15 | COMPLEMENTO | Endereço: Complemento | Não | Texto(30) |  |
| 16 | BAIRRO | Endereço: Bairro | Não | Texto(30) |  |
| 17 | CIDADE | Endereço: Cidade | Não | Texto(32) |  |
| 18 | ESTADO | Endereço: Estado | Não | Texto(2) | Ver tabela GETD (referência 10) |
| 19 | PAIS | Endereço: País | Não | Texto(16) |  |
| 20 | CEP | Endereço: CEP | Não | Texto(9) |  |
| 21 | TELEFONE1 | Telefone (Opção I) | Não | Texto(15) | Sem separadores, somente dígitos (pode incluir o DDD) |
| 22 | TELEFONE2 | Telefone (Opção II) | Não | Texto(15) | Sem separadores, somente dígitos (pode incluir o DDD) |
| 23 | TELEFONE3 | Telefone (Opção III) | Não | Texto(15) | Sem separadores, somente dígitos (pode incluir o DDD) |
| 24 | FAX | FAX | Não | Texto(15) | Sem separadores, somente dígitos (pode incluir o DDD) |
| 25 | CARTIDENTIDADE | Carteira de identidade | Não | Texto(15) |  |
| 26 | DTEMISSAOIDENT | Data de emissão da carteria de identidade | Não | Data | DD/MM/AAAA |
| 27 | ORGEMISSORIDENT | Órgão emissor da carteira de identidade | Não | Texto(15) |  |
| 28 | UFCARTIDENT | UF da carteira de identidade | Não | Texto(2) | Ver tabela GETD (referência 10) |
| 29 | TITULOELEITOR | Número do título de eleitor | Não | Texto(14) |  |
| 30 | ZONATITELEITOR | Zona eleitoral | Não | Texto(6) |  |
| 31 | SECAOTITELEITOR | Seção eleitoral | Não | Texto(6) |  |
| 32 | CARTEIRATRAB | Número da certeira de trabalho | Não | Texto(10) |  |
| 33 | SERIECARTTRABA | Série da carteira de trabalho | Não | Texto(5) |  |
| 34 | NIT | Carteira do tipo NIT | Não | Inteiro | 0 - Não 1 - Sim |
| 35 | DTCARTTRAB | Data de emissão da carteira de trabalho | Não | Data | DD/MM/AAAA |
| 36 | UFCARTTRAB | UF da carteira de trabalho | Não | Texto(2) | Ver tabela GETD (referência 10) |
| 37 | CARTMOTORISTA | Número da carteira de habilitação | Não | Texto(15) |  |
| 38 | TIPOCARTHABILIT | Tipo da carteira de habilitação | Não | Texto(5) |  |
| 39 | DTVENCHABILIT | Data de vencimento da carteira de habilitação | Não | Data | DD/MM/AAAA |
| 40 | REGPROFISSIONAL | Registro profissional | Não | Texto(15) |  |
| 41 | CPF | CPF | Não | Texto(11) |  |
| 42 | CERTIFRESERV | Número do certificado de reservista | Não | Texto(40) |  |
| 43 | CATEGMILITAR | Categoria militar | Não | Texto(10) |  |
| 44 | NOMESOCIAL | Nome Social | Não | Texto(120) |  |
