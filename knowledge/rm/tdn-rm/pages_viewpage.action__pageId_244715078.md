---
content_hash: cfd9dfe0e2b571e30b55d4734be906b32cc5fe42ef611d4f472a2b70bb8a8c0e
fetched_at: '2026-06-29T00:08:14.747793+00:00'
page_id: '244715078'
product: rm
source: tdn-rm
title: eSocial  - Qualificação Cadastral em Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244715078
version: 14
---

# Qualificação Cadastral em Lote

false🔔 ATENÇÃO:

Com a implantação do FGTS Digital e a validação dos dados do trabalhador sendo realizada unicamente com base no CPF, a Consulta de Qualificação Cadastral Online (individual) foi **desativada** e **não está mais disponível** no portal do eSocial.

Diante disso, o **menu de Qualificação Cadastral** foi **removido da Folha de Pagamento** a partir dos patches:

* 12.1.2410.287
* 12.1.2502.190
* 12.1.2506.130 e superiores

📌 Para mais informações, acesse: [eSocial- Qualificação Cadastral Desativada](https://tdn.totvs.com/pages/releaseview.action?pageId=975770468)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | **RM** | | |
| ****Segmento Executor:**** | *Recursos Humanos* | | |
| **Módulo:** | *Folha de Pagamento* | | |
| **Rotina:** | *eSocial - Qualificação Cadastral em Lote* | | |
|  |  | | |

## Objetivo

Tem por objetivo gerar um arquivo para possibilitar aos empregadores realizar a validação dos CPF e NIS em lote, visando identificar possíveis divergências entre os cadastros internos da empresa, a fim de não comprometer o cadastramento inicial ou admissões de trabalhadores no eSocial.

### 

### Definição da Regra de Negócio

**Layout do Arquivo**

|  |  |  |
| --- | --- | --- |
| **Campo** | **Tamanho** | **Formato** |
| CPF | 11 | Numérico |
| NIS | 11 | Numérico |
| Nome | 60 | Alfanumérico |
| Data Nascimento | 8 | Data (DDMMAAAA) |

                O formato do arquivo será “TXT” com delimitador ';' (ponto e vírgula) entre os campos.

                Exemplo de arquivo: QUALIF\_ESOCIAL\_COL0001.TXT

 

32283644291;18000474420;nome do empregado1;13011974

34879579149;11816788893;nome do empregado2;28091986

18576263467;18000474420;nome do empregado3;13011973

18576263467;10000411830;nome do empregado4;08051950

**Processo de Geração do Arquivo**

Para gerar o arquivo, deve-se seguir os seguintes passos:

1. Aba  eSocial
2. Botão Qualificação Cadastral

**1º- Etapa**

Será possível salvar perfil para os parâmetros desse processo.

**2º- Etapa**

Os parâmetros exigidos serão:

1- Quebra de seção;

2- Seleção de Funcionários;

3- Seleção de Coligadas;

4- Pasta que será salvo o arquivo;

**3ª- Etapa**

Na última etapa será gerado e gravado o arquivo

Deverá importar o arquivo no site [www.esocial.gov.br](http://www.esocial.gov.br)  tópico  **Consulta Qualificação Cadastral**

**Arquivo de retorno.**

Os arquivos de retorno têm a mesma regra de formação dos de envio acrescidos das palavras

"PROCESSADO" e "REJEITADO", conforme o caso.

• D.CNS.CPF.002.aaaammddhhmmss.num**CNPJ**.num**CPF**.TXT.PROCESSADO

• D.CNS.CPF.003.aaaammddhhmmss.num**CNPJ**.num**CPF**.TXT.REJEITADO

Para maiores informações sobre o retorno que será enviado ao cliente após processamento, leia o manual disponível no site do eSocial, link abaixo.

**<http://www.esocial.gov.br/QualificacaoCadastral.aspx>**

### 

###
