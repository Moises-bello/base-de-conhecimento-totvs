---
article_id: 360059965954
category: LEGAIS - BLOCO H/MATR460
content_hash: 78ebe15ac67b78adb3553d90e9786c1433b478c910cd98b918c0d09217172a65
fetched_at: '2026-06-28T22:42:14.991999+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Guia do Bloco H do
  SPED Fiscal no Protheus
type: support-article
updated_at: '2026-04-06T17:56:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059965954-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Guia-do-Bloco-H-do-SPED-Fiscal-no-Protheus
---

**Ocorrência**

Este documento é um Guia do Bloco H, contendo informações conceituais e técnicas sobre o processo de geração deste bloco e algumas ocorrências comuns.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**

O documento visa sanar dúvidas sobre o Processo e ocorrências relacionadas à geração do Bloco H.

**Solução**

O Registro Bloco H deve ser apresentado para discriminar os valores totais do inventário por itens/produtos existentes à data do balanço. Se a escrituração se referir ao mês de fevereiro, este registro deve obrigatoriamente ser informado. Neste caso, os dados apresentados devem considerar a posição em 31 de dezembro do exercício anterior. Em outros meses, pode ou não ser informado, conforme previsão legal da obrigação de inventariar o estoque.

Veja nosso Webinar sobre o Bloco H:

[![Webinar.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39257277344535)](https://youtu.be/UZqxBR7VGuY?si=PER4NjRymmug1_J2)

|  |
| --- |
| **Requisitos para correta geração do Bloco H** |
| Em resumo, o Bloco H no Protheus é um espelho do relatório Inventário Modelo 7 (MATR460/P7). Tendo isso como base, para gerarmos o Bloco H, veja as informações abaixo:  **1. Certifique-se de que os fontes de Livros Fiscais e Estoque/Custos estejam plenamente atualizados.**   * [**Pacote Acumulado Estoque/Custos**](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/EST_expedicao_continua) * [**Pacote Acumulado Livros Fiscais**](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/FIS_expedicao_continua)   A atualização destes pacotes garantirão que todos os fontes responsáveis pela geração do P7 e do SPED Fiscal estejam atualizados de maneira equalizada. |

|  |
| --- |
| **Processo de geração do Bloco H do SPED** |
| **1. Gere o Relatório MATR460 - "Registro de Inventário Modelo P7", ou acesse ao caminho:** *Menu 04 - Estoque/Custos -> Relatórios -> Legais -> Registro de Inventário Modelo P7.*     |  | | --- | | **Atenção**  **Os produtos que forem impressos neste relatório serão a base do que irá para o Bloco H do SPED.** |       Veja abaixo emissão ilustrativa do processo de parametrização do Relatório:  parametrizacao p7.gif    Para entender melhor cada pergunta deste relatório, [**clique aqui e veja maiores detalhes**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001540542-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Perguntas-do-relat%C3%B3rio-MATR460-Invent%C3%A1rio-Modelo-7-)  Porém, existem algumas perguntas-chave para que o Bloco H no final do processo seja gerado corretamente, e são estas abaixo:  🟢 **Gerar Exp. SPED Fiscal?** = Sim; 🟢 **Data de fechamento de Estoque** = 31/12/2023 (Data de quando o inventário foi fechado); 🟢 **Nome Arq. Gerado no Reg. In. MOD 7** =  20231231 (Data de fechamento do inventário em formato americano).     |  | | --- | | **Observações:**  - O Bloco H nada mais é do que um espelho do Registro de Inventário Modelo 7 (MATR460). Desta forma, é muito importante parametrizar com informações que satisfaçam a impressão dos dados;  - Atente-se às perguntas como "Prods c/ Saldo Neg?", " Prods c/ Saldo Zerado?", "Lista Custo Zerado?". Estas perguntas podem fatalmente gerar impressão diferente do desejado.  Exemplo de possível "impressão incorreta" no MATR460**:**  Ao parametrizar a pergunta **"Prods com Saldo Zerado?" = Não e todos os armazéns**, se o produto A tiver armazém 01 e 02 e, por algum motivo no armazém 01 tiver saldo físico zerado, a impressão imprimirá o custo que estiver atrelado ao armazém 01 juntamente ao custo e quantidade do armazém 02. Para maiores detalhes [**clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4497301878807-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Comportamento-da-pergunta-Prods-c-Saldo-Zerado-no-P7). |     **2. Assim que o** ***Protheus*** **imprime o relatório P7, ao mesmo tempo, será gravado no Banco de Dados os resultados do relatório na tabela H\_20231231 + grupo + filial. Veja o exemplo abaixo pela APSDU**:  geracaotabelah.gif   |  | | --- | | **Importante**: Caso tenha aberto a tabela para efetuar uma conferência dos dados, lembre-se de fechar a tabela antes de prosseguir com a geração do SPED Fiscal |     **3. Gere o arquivo do Sped Fiscal, acessando ao caminho**: *Menu 09 - Livros Fiscais -> Arquivos Magnéticos-> Sped Fiscal*    Durante a geração do SPED, para que seja gerado o Bloco H, atente-se às seguintes perguntas no Wizard: 🟢 **Gera Inventário** = Sim; 🟢 **Data de fechamento do estoque** = Data em que foi feito o fechamento do estoque (31/12/2023); 🟢 **Motivo do Inventário** = 01-Final do Período.  Exemplo de parametrização da primeira tela do SPED Fiscal (em um cenário hipotético do SPED ser do mês de Fevereiro):      mceclip2.png    **4. Efetue a conferência do SPED e do Bloco H no arquivo TXT gerado após o Processamento:**  Este é o momento em que o usuário pode conferir cada Pipe do Bloco H, bem como fazer comparações com a tabela H\_ gerada anteriormente (passo 3).  Para entender cada *pipe* de cada Bloco do SPED, recomendamos baixar o Guia Prático do EFD ICMS IPI [**clicando aqui.**](http://sped.rfb.gov.br/pasta/show/1573) |

|  |
| --- |
| **Cenários e dúvidas comuns sobre o Bloco H** |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **O que quer dizer cada código de Situação na tabela H (H\_20231231)?**  A tabela H\_  é basicamente um espelho do relatório MATR460 (P7), a diferença é que os registros de saldos, custos e seções (em estoque, de terceiros, etc), ficam em forma de tabela. O campo "SITUACAO" seria um paralelo com a "Seção", onde:     |  |  | | --- | --- | | **Situação** | **Descrição** | | 1 | **Estoque** (Em estoque próprio) | | 2 | [**Processo**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061473074)(Saldo em Processo - Insumos sendo requisitados em OPs) | | 3 | **Sem Saldo** (Quando o produto literalmente imprime com quantidade física zerada) | | 4 | **De Terceiros**(Saldo DE terceiros em nosso poder) | | 5 | **Em Terceiros** (Saldo nosso EM poder de terceiros) | | 6 | **De Terceiros usados em OPs** (Saldo requisitado em Ordem de Produção "RE9". Constará antes da Virada de Saldos) | | 7 | [**Em Fabricação**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004741202-MP-SIGAEST-MATR460-Montagem-da-se%C3%A7%C3%A3o-Em-Fabrica%C3%A7%C3%A3o-Em-Elabora%C3%A7%C3%A3o-) (quando a última pergunta do P7 está com conteúdo = Sim - Produtos finais em processo de fabricação) | |

|  |
| --- |
| **Tenho produtos que apareceram no P7 com saldo negativo e eles não foram para o Bloco H. O que fazer?**    É muito comum isso acontecer, principalmente em uma base de dados com muitos produtos, onde eventualmente por algum motivo, o mesmo pode terminar o período com saldo físico negativo. Por padrão, o SPED Fiscal não leva para o Bloco H produtos nessa situação (ainda que no Relatório P7 ele apresente), vide exemplo abaixo com o MP01:    P7 com Saldo Negativo:  mceclip7.png    A tabela H\_ não traz o produto em questão:  mceclip8.png    Consequentemente, o produto não aparece no Bloco H (apenas o Bloco K, que aparece saldo negativo, embora o validador rejeite):  mceclip9.png    Neste caso, é importante efetuar uma análise da base de dados (Kardex, movimentações) para entender se esse saldo gerado no P7 negativo é coerente com os movimentos ou não. Segue abaixo lista de alguns cenários em que isso acontece:  - Fonte do relatório P7 (MATR460) desatualizado;  - Parâmetro [**MV\_SDTESN3**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060289014-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Valida%C3%A7%C3%A3o-do-par%C3%A2metro-MV-SDTESN3)influenciando na impressão dos dados;  - [**Outros parâmetros**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901)influenciando na impressão do registro negativo;  - Movimentos com data retroativa influenciando no saldo naquela data em questão;  - Estornos ou manipulações na base de dados; |

|  |
| --- |
| **Consigo filtrar determinados tipos de Produto para que sejam levados ao Bloco H?**    Através da geração do P7 é possível definir quais tipos de produtos serão levados (ou não) para a tabela H e Bloco H. Os detalhes de como efetuar este tipo de parametrização estão no do documento abaixo:  [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - É possível imprimir no relatório P7 apenas produtos de Tipos específicos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004656001) |

|  |
| --- |
| **Consigo filtrar determinados Armazéns para que sejam levados ao Bloco H?**  Através da parametrização de armazéns (Armazém De / Armazém Até) é possível delegar quais os Armazéns terão seus saldos considerados na geração do P7 e Bloco H. Caso o usuário queira definir um intervalo de armazéns (Exemplo: Armazéns 2, 5 e 8), pode-se efetuar uso do Ponto de Entrada [**A460RLOC.**](https://tdn.totvs.com/pages/releaseview.action?pageId=651923218) |

|  |
| --- |
| **LINKS ÚTEIS** |

|  |
| --- |
| * [**Guia Prático SPED - Versão 3.1.8**](http://sped.rfb.gov.br/estatico/30/007F992E2E9F284F1DC7D9AC50A4CF3BE4513C/Guia%20Pr%c3%a1tico%20EFD%20-%20Vers%c3%a3o%203.1.8.pdf)  * [**Acumulado BackOffice**](https://tdn.totvs.com/pages/releaseview.action?pageId=522000602#issues-17) * [**SIGAEST - Perguntas do relatório MATR460 (Inventário Modelo 7)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001540542-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Perguntas-do-relat%C3%B3rio-MATR460-Invent%C3%A1rio-Modelo-7-) * [**SIGAEST - MATR460 - Validação do parâmetro MV\_ SDTESN3**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060289014-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Valida%C3%A7%C3%A3o-do-par%C3%A2metro-MV-SDTESN3)  * [**SIGAEST - Parâmetros relacionados ao MATR460 - Registro de Inventário Mod 7**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901)  * [**Seção de artigos sobre o Relatório P7 - MATR460**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538741-LEGAIS-BLOCO-H-MATR460) |

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538741-LEGAIS-BLOCO-H-MATR460)
