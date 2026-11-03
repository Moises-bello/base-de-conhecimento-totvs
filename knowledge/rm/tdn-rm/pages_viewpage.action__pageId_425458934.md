---
content_hash: fa1b3b3567f2270139366f1ea58cb00df79e3e88b7c729af37b45d960555460d
fetched_at: '2026-06-29T00:09:33.190885+00:00'
page_id: '425458934'
product: rm
source: tdn-rm
title: Layout Arquivos Importação de ENEM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458934
version: 7
---

O INEP devolve três tipos de arquivos texto para a instituição de ensino. São eles: "Encontrados", "Diferenças" e "Erros". Para maiores detalhes sobre estes três arquivos veja:  
**Encontrados**: O arquivo a ser importado contém as notas objetiva e de redação de todos os candidatos que tiveram seus dados informados corretamente, uma vez que os mesmos passaram pela validação do INEP. O processo notas do ENEM irá gravar estas notas nas inscrições destes candidatos.

* **Layout 2006/2007** O modelo 2006/2007 oferece um único campo para nota da prova objetiva. Ano; Número da inscrição; Nome do inscrito; Nota objetiva; Nota redação; Situação (Presente ou Faltou);   Exemplo:

  |  |
  | --- |
  | 2000; 200000000033; ADRIANE RENAU BASTOS; 99; 99; Presente;  2001; 200100000099; ADRIANA ALVES DOS SANTOS; 99; 99; Presente; |
* **Layout 2009/2010** No momento da importação, caso o layout 2009/2010 seja escolhido, o sistema gravará nos campos "Nota Redação", "Nota da prova de Ciência da Natureza", "Nota da prova de Ciências Humanas", "Nota da prova de Linguagem" e "Nota da prova de Matemática" os valores informados no arquivo enviado pelo INEP, também realizará a média aritmética das quatro notas e salvará no campo "Nota Objetiva".  Número da inscrição do ENEM;CPF;Nome;Nota de Ciências da Natureza;Nota de Ciências Humanas;Nota Linguagens;Nota Matemática;Nota redação;Presença;Presença;Presença;Presença;Presença

**Presença na prova:** P – Presente/ F –Faltoso / B –Branco / N - Anulada  
Quando a situação for diferente de P - Presente, as notas não serão importadas para cálculo da média.

|  |
| --- |
| 200920125630;12225212708;DANIELLE GUIMARAES ALVES;497.65;114.9;583.5;22.06;521.84;P;P;P;P;P |

* **Layout 2013** O sistema gravará nos campos "Nota Redação", "Nota da prova de Ciência da Natureza", "Nota da prova de Ciências Humanas", "Nota da prova de Linguagem" e "Nota da prova de Matemática" os valores informados no arquivo enviado pelo INEP, também realizará a média aritmética das quatro notas e salvará no campo "Nota Objetiva".

  + Número da inscrição do ENEM;CPF;Nome;Nota de Ciências da Natureza;Nota de Ciências Humanas;Nota Linguagens;Nota Matemática;Nota redação;Presença;Presença;Presença;Presença;Presença;Data de Nascimento;Sexo;RG – Número;RG – Orgão expedidor;RG – UF expedição;Local de Prova – UF;Local de Prova – Município

    |  |
    | --- |
    | 131048639695;84954728053;PAMELA PRISCILA LESSA DUTRA;477.9;504.7;515.3;403.7;400.0;7;7;7;7;7;20/07/1994;F;4115564355;SSP;RS;RS;PORTO ALEGRE |

    **Presença na prova:** 7 – Presente/ 6 –Faltoso / 1 –Branco / 2, 9, 11 – Anulada / 5, 10 – Texto insuficiente / 3, 4 – Fuga Tema / - Eliminado.
* **Layout 2014** O sistema gravará nos campos "Nota Redação", "Nota da prova de Ciência da Natureza", "Nota da prova de Ciências Humanas", "Nota da prova de Linguagem" e "Nota da prova de Matemática" os valores informados no arquivo enviado pelo INEP, também realizará a média aritmética das quatro notas e salvará no campo "Nota Objetiva".

  + Número da inscrição do ENEM;CPF;Nome;Nota de Ciências da Natureza;Nota de Ciências Humanas;Nota Linguagens;Nota Matemática;Nota redação;Presença;Presença;Presença;Presença;Presença;Data de Nascimento;Sexo;RG – Número;RG – Orgão expedidor;RG – UF expedição;Local de Prova – UF;Local de Prova – Município;Unidade Prisional/Socioeducativa;Lingua Estrangeira

    |  |
    | --- |
    | 131048639695;84954728053;PAMELA PRISCILA LESSA DUTRA;477.9;504.7;515.3;403.7;400.0;7;7;7;7;7;20/07/1994;F;4115564355;SSP;RS;RS;PORTO ALEGRE;NAO;INGLES |

    **Presença na prova:** 7 – Presente/ 6 –Faltoso / 1 –Branco / 2, 9, 11 – Anulada / 5, 10 – Texto insuficiente / 3, 4 – Fuga Tema / - Eliminado.

    Layout 2022

    Layout 2022 está disponível somente a partir das versões 12.1.33.342, 12.1.2205.230, 12.1.2209.176 e 12.1.2302.104 e superiores.
* **Layout 2022** O sistema gravará nos campos "Nota Redação", "Nota da prova de Ciência da Natureza", "Nota da prova de Ciências Humanas", "Nota da prova de Linguagem" e "Nota da prova de Matemática" os valores informados no arquivo enviado pelo INEP, também realizará a média aritmética das quatro notas e salvará no campo "Nota Objetiva".

  + - Número da inscrição do ENEM;CPF;Nome;Nota de Ciências da Natureza;Nota de Ciências Humanas;Nota Linguagens;Nota Matemática;Nota redação;Presença;Presença;Presença;Presença;Presença;Data de Nascimento;Sexo;Local de Prova – UF;Local de Prova – Município;Unidade Prisional/Socioeducativa;Lingua Estrangeira

      |  |
      | --- |
      | 131048639695;84954728053;PAMELA PRISCILA LESSA DUTRA;477.9;504.7;515.3;403.7;400.0;7;7;7;7;7;20/07/1994;F;RS;PORTO ALEGRE;NAO;INGLES |

      **Presença na prova:** 7 – Presente/ 6 –Faltoso / 1 –Branco / 2, 9, 11 – Anulada / 5, 10 – Texto insuficiente / 3, 4 – Fuga Tema / - Eliminado.

**Diferenças**: Este arquivo contém as diferenças entre os dados informados no arquivo enviado pela instituição e aqueles constantes nas bases do INEP. Para cada inscrição de candidato existem duas linhas. A primeira contém os dados da forma que foram solicitados sendo que o primeiro campo indica as coincidências encontradas e tem o formato abaixo:  
Coincidências; Ano; Número da inscrição; Nome do inscrito; Nome da mãe; Documento; Órgão expedidor; UF documento; Data nascimento. Descrição das coincidências:

|  |  |
| --- | --- |
| Código | Descrição |
| 1 | Número de inscrição |
| 2 | Nome do inscrito |
| 3 | Nome da mãe |
| 4 | Número do documento |
| 5 | Data de nascimento |

A linha seguinte contém os dados da forma em que se encontra cadastrada no banco de dados do INEP. Segue o formato abaixo:  
Ano; Número da inscrição; Nome do inscrito; Nome da mãe; Documento; Órgão expedidor; UF documento; Data nascimento; Nota objetiva; Nota redação; Situação (Presente ou Faltou)   Exemplo:

|  |
| --- |
| 2002; 200201368245; ADRIANE RENAU BASTOS; FATIMA K BASTOS; 0985382686; SSP; BA; 08/03/1984  2002; 200201368245; ADRIANE RENAU BASTOS; FATIMA KENAU BASTOS; 0985382686; SSP; BA; 08/03/1984; 99; 0; Presente |

No caso do exemplo acima indica que o nome da mãe não coincidiu, pois não existe a coincidência número 3.  
**Erros**: Este arquivo contem todos os dados recebidos que não puderam ser encontrados no banco de dados do INEP. Segue o formato:  
Ano; Número da inscrição; Nome do inscrito; Nome da mãe; Documento; Órgão expedidor; UF documento; Data nascimento; Situação (não encontrado)  
Exemplo:

|  |
| --- |
| 2001; 200202595848; ADRIANA ALVES DOS SANTOS; ALDENIRA DE SOUZA SANTOS; 733335; SSP; RO; 11/07/1984; não encontrado |
