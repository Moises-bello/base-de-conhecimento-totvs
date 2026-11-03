---
content_hash: 16468dd84c6dd5c89fcf7a097aef8848dc912a5f7b39e37ff1eb7a4f937696cc
fetched_at: '2026-06-29T00:09:33.177513+00:00'
page_id: '425458932'
product: rm
source: tdn-rm
title: Importar notas do ENEM
type: documentation
url: https://tdn.totvs.com/display/LRM/Importar+notas+do+ENEM
version: 11
---

Solicitar os dados para o INEP

Este processo será executado a partir da visão de "processos seletivos". Cumprindo as disposições da Portaria nº 195, de 28 de dezembro de 2001 nos artigos 24, 25, 26, 27 e 28 o INEP está disponibilizando o Sistema de solicitação de resultados.

Deverá ser enviado um arquivo texto, contendo na primeira linha do arquivo o identificador da instituição de ensino superior ou escola. As demais linhas devem conter as seguintes informações:

|  |  |  |
| --- | --- | --- |
| Coluna | Descrição | Obrigatório? |
| Ano de participação no exame | Formato (AAAA) com 4 dígitos | Sim |
| Número de inscrição | Formato (999999999999) com 12 dígitos | Sim |
| Nome do inscrito | Tamanho máximo de 80 caracteres | Sim |
| Nome da mãe | Tamanho máximo de 76 caracteres | Sim |
| Número do documento de identidade | Tamanho máximo de 16 caracteres | Sim |
| Órgão expeditor | Tamanho máximo de 10 caracteres | Sim |
| Sigla do estado expeditor do documento de identidade | Tamanho máximo de 2 caracteres | Sim |
| Data de nascimento | Formato (dd/mm/aaaa) dia, mês e ano com 4 dígitos | Sim |

Todos os campos são obrigatórios. "O caractere"; (ponto e vírgula) deverá ser utilizado como separador entre os campos conforme exemplo abaixo.  
56780896121 2000; 200000000033; ADRIANE RENAU BASTOS; FATIMA KENAU BASTOS; 0985382686; SSP; BA; 08/03/1984;  
2001; 200100000099; ADRIANA ALVES DOS SANTOS; ALDENIRA DOS SANTOS; 733335; SSP; RO; 11/07/1984;

Se o identificador da instituição não conferir todo o arquivo será rejeitado. As linhas do arquivo que não estiverem no formato demonstrado acima serão rejeitadas.

Para o caso da instituição não possuir algum dado solicitado, com exceção do ano de participação e número de inscrição que são indispensáveis, proceder da seguinte forma:

|  |  |
| --- | --- |
| Coluna | Descrição |
| Nome do inscrito | Enviar "não informado" |
| Nome da mãe | Enviar "não informado" |
| Número do documento de identidade | Enviar "99999999" |
| Órgão expeditor | Enviar "XXX" |
| Sigla do estado expeditor do documento de identidade | Enviar "XX" |
| Data de nascimento | Enviar "01/01/2000" |

O INEP devolve três tipos de arquivos texto para a instituição de ensino. São eles: "Encontrados", "Diferenças" e "Erros". Para maiores detalhes sobre estes três arquivos veja:  
**Encontrados**: O arquivo a ser importado contém as notas objetiva e de redação de todos os candidatos que tiveram seus dados informados corretamente, uma vez que os mesmos passaram pela validação do INEP. O processo notas do ENEM irá gravar estas notas nas inscrições destes candidatos.

## **Layout 2006/2007**

O modelo 2006/2007 oferece um único campo para nota da prova objetiva.

Campos: Ano; Número da inscrição; Nome do inscrito; Nota objetiva; Nota redação; Situação (Presente ou Faltou);  

Exemplo:

|  |
| --- |
| 2000;200000000033;ADRIANE RENAU BASTOS;99;99;Presente;  2001;200100000099;ADRIANA ALVES DOS SANTOS;99;99;Presente; |

## **Layout 2009/2010**

No momento da importação, caso o layout 2009/2010 seja escolhido, o sistema gravará nos campos "Nota Redação", "Nota da prova de Ciência da Natureza", "Nota da prova de Ciências Humanas", "Nota da prova de Linguagem" e "Nota da prova de Matemática" os valores informados no arquivo enviado pelo INEP, também realizará a média aritmética das quatro notas e salvará no campo "Nota Objetiva".

Campos: Número da inscrição;CPF;Nome;Nota de Ciências da Natureza;Nota de Ciências Humanas;Nota Linguagens;Nota Matemática;Nota redação;Presença;Presença;Presença;Presença;Presença

**Presença na prova:** P – Presente/ F –Faltoso / B –Branco / N - Anulada  
Quando a situação for diferente de P - Presente, as notas não serão importadas para cálculo da média.

Exemplo:

|  |
| --- |
| 200920125630;12225212708;DANIELLE GUIMARAES ALVES;497.65;114.9;583.5;22.06;521.84;P;P;P;P;P |

## **Layout 2013**

O sistema gravará nos campos "Nota Redação", "Nota da prova de Ciência da Natureza", "Nota da prova de Ciências Humanas", "Nota da prova de Linguagem" e "Nota da prova de Matemática" os valores informados no arquivo enviado pelo INEP, também realizará a média aritmética das quatro notas e salvará no campo "Nota Objetiva".

Campos: Número da inscrição;CPF;Nome;Nota de Ciências da Natureza;Nota de Ciências Humanas;Nota Linguagens;Nota Matemática;Nota redação;Presença;Presença;Presença;Presença;Presença;Data de Nascimento;Sexo;RG – Número;RG – Orgão expedidor;RG – UF expedição;Local de Prova – UF;Local de Prova – Município

**Presença na prova:** 7 – Presente/ 6 –Faltoso / 1 –Branco / 2, 9, 11 – Anulada / 5, 10 – Texto insuficiente / 3, 4 – Fuga Tema / - Eliminado.

Exemplo:

|  |
| --- |
| 131048639695;84954728053;PAMELA PRISCILA LESSA DUTRA;477.9;504.7;515.3;403.7;400.0;7;7;7;7;7;20/07/1994;F;4115564355;SSP;RS;RS;PORTO ALEGRE |

## **Layout 2014**

O sistema gravará nos campos "Nota Redação", "Nota da prova de Ciência da Natureza", "Nota da prova de Ciências Humanas", "Nota da prova de Linguagem" e "Nota da prova de Matemática" os valores informados no arquivo enviado pelo INEP, também realizará a média aritmética das quatro notas e salvará no campo "Nota Objetiva".

Campos: Número da inscrição;CPF;Nome;Nota de Ciências da Natureza;Nota de Ciências Humanas;Nota Linguagens;Nota Matemática;Nota redação;Presença;Presença;Presença;Presença;Presença;Data de Nascimento;Sexo;RG – Número;RG – Orgão expedidor;RG – UF expedição;Local de Prova – UF;Local de Prova – Município;Unidade Prisional/Socioeducativa;Lingua Estrangeira

**Presença na prova:** 7 – Presente/ 6 –Faltoso / 1 –Branco / 2, 9, 11 – Anulada / 5, 10 – Texto insuficiente / 3, 4 – Fuga Tema / - Eliminado.

Exemplo:

|  |
| --- |
| 131048639695;84954728053;PAMELA PRISCILA LESSA DUTRA;477.9;504.7;515.3;403.7;400.0;7;7;7;7;7;20/07/1994;F;4115564355;SSP;RS;RS;PORTO ALEGRE;NAO;INGLES |

## **Layout 2022**

O sistema gravará nos campos "Nota Redação", "Nota da prova de Ciência da Natureza", "Nota da prova de Ciências Humanas", "Nota da prova de Linguagem" e "Nota da prova de Matemática" os valores informados no arquivo enviado pelo INEP, também realizará a média aritmética das quatro notas e salvará no campo "Nota Objetiva".

Campos: Número da inscrição;CPF;Nome;Nota de Ciências da Natureza;Nota de Ciências Humanas;Nota Linguagens;Nota Matemática;Nota redação;Presença;Presença;Presença;Presença;Presença;Data de Nascimento;Sexo;Local de Prova – UF;Local de Prova – Município;Unidade Prisional/Socioeducativa;Lingua Estrangeira

**Presença na prova:** 7 – Presente/ 6 –Faltoso / 1 –Branco / 2, 9, 11 – Anulada / 5, 10 – Texto insuficiente / 3, 4 – Fuga Tema / - Eliminado.

Exemplo:

|  |
| --- |
| 200920125630;12225212708;DANIELLE GUIMARAES ALVES;497.65;114.9;583.5;22.06;521.84;P;P;P;P;P;20/07/1991;F;MG;BELO HORIZONTE;N;INGLÊS |

## **Layout 2024**

O sistema gravará nos campos "Nota Redação", "Nota da prova de Ciência da Natureza", "Nota da prova de Ciências Humanas", "Nota da prova de Linguagem" e "Nota da prova de Matemática" os valores informados no arquivo enviado pelo INEP, também realizará a média aritmética das quatro notas e salvará no campo "Nota Objetiva".

Campos: Número da inscrição;CPF;Nome;Nota de Ciências da Natureza;Nota de Ciências Humanas;Nota Linguagens;Nota Matemática;Nota redação;Presença;Presença;Presença;Presença;Presença;Unidade Prisional/Socioeducativa;Lingua Estrangeira

**Presença na prova:** 7 – Presente/ 6 –Faltoso / 1 –Branco / 2, 9, 11 – Anulada / 5, 10 – Texto insuficiente / 3, 4 – Fuga Tema / - Eliminado.

Exemplo:

|  |
| --- |
| 200920125630;12225212708;DANIELLE GUIMARAES ALVES;497.65;114.9;583.5;22.06;521.84;7;7;7;7;7;N;INGLÊS |

## **Notas inconsistentes**

Para notas inconsistentes consulte
