---
content_hash: 437af7bd8cf63893e867222604cadb85898fa59ff5ec7887243d3fd63ed6d56b
fetched_at: '2026-06-29T00:09:19.485360+00:00'
page_id: '422545597'
product: rm
source: tdn-rm
title: Importação Natureza de Operação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545597
version: 13
---

A importação de Natureza de Operação tem como objetivo inserir no sistema naturezas de operações informadas via arquivo texto, o qual deve ser escrito de acordo com layout determinado.

false1lefttrue1Registro N

**Natureza de Operação:**Este registro tem por objetivo descrever os dados referentes ao cadastro da Natureza de Operação.

***Observação*:**Os campos código de regra do ICMS e IPI serão obrigatórios quando o campo FISCAL for igual a "1" – Com ICMS / IPI.2Registro O

**Outros Tributos:**Neste registro devem ser informados os dados dos demais tributos relacionados à Natureza de Operação.

***Observação*:** O campo código do tributo deve referenciar algum tributo já cadastrado no sistema. 3Registro H

**Dispositivo Legal da Natureza:**Este registro deve conter os registros referentes às linhas que serão inseridas no campo DISPOSITIVO LEGAL do Cadastro da Natureza.

***Observação:***O campo Dispositivo Legal não deve conter quebra de linha, caso exista quebra de linha deve ser criada nova linha do registro. 4Registro C

**Default Contábil da Natureza Fiscal:**Este registro deve conter todos os Defaults Contábeis relacionados à Natureza de Operação.

5Registro R

**Rateio do Default Contábil da Natureza Fiscal:**Este registro deve conter todos os Rateios dos Defaults Contábeis relacionados à Natureza de Operação.

6Registro D

**Registro D: Regras de Tributação:**Este registro deve conter todas as regras de tributação relacionada à Natureza de Operação. As combinações das regras de tributação na importação devem seguir as mesmas regras determinadas na inclusão de Natureza, exemplo:

Exemplo 1

| IDREGISTRO | TIPODEPEND | IDREGRA | CHAVE | CODCOLIGADADACHAVE |
| --- | --- | --- | --- | --- |
| D | C | C | C00001 | 00001 |
| D | P | T | 000002 | 00001 |

InformaçõesRegras de Dependências

| Tipo de Dependência | Identificador de Regra de Dependência | Descrição |
| --- | --- | --- |
| C | C | Cliente/Fornecedor |
| M | Empresa |
| T | Tipo de Cliente/Fornecedor |
| E | R | Região |
| E | Estado |
| U | Grupo de Município |
| P | P | Produto |
| T | Tipo de Produto |

Esclarecimentos sobre o layout

| Onde | Tipo |
| --- | --- |
| C | Campo alfanumérico |
| N | Campo numérico |
| Dec | Número de casas decimais |
| **Completar A** | |
| D | Direita |
| E | Esquerda |

***Observações*:**Todos os registros de nível 2 devem ser escritos logo abaixo do registro nível 1 acima dele. Para qualquer campo nulo, mesmo sendo Inteiro ou Valor, deverá ser preenchido com espaços. NotaNo momento da importação da Natureza de Operação, o sistema irá consistir se existe o Nível Sintético da Natureza a que se deseja importar, do contrário não irá importar o registro e irá gerar um arquivo de log de erro.   
O arquivo de log será gerado no caminho indicado em Ambiente | Parâmetros | TOTVS Gestão Fiscal | Rotinas Legais | Diretório de Arquivos Temporários.***Atenção!***As Regras de ICMS e Regras de IPI devem ser cadastradas no sistema e em seguida o arquivo de natureza deverá ser importado.Outras Informações
