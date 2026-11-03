---
article_id: 360027776931
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: eae51984c599a71f1568942930107989d76237e289ebd5e61e098523ff720aff
fetched_at: '2026-06-28T22:39:22.237026+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: MP - FIS - Demonstrativo da Apuração Mensal Fomentar/Produzir/Microproduzir
type: support-article
updated_at: '2021-10-20T18:18:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027776931-MP-FIS-Demonstrativo-da-Apura%C3%A7%C3%A3o-Mensal-Fomentar-Produzir-Microproduzir
---

**Dúvida:**

Na Apuração de ICMS (MATA953), está disponível em um novo folder (Apuração-Fomentar), o demonstrativo da apuração mensal do Fomentar do estado de Goiás.

**Ambiente:**

Microsiga Protheus – Livros Fiscais – A partir da versão 11

**Solução:**

|  |  |
| --- | --- |
| **A quem se destina** | Aos estabelecimentos industriais enquadrados como beneficiários do programa Fomentar que devem adotar os procedimentos estabelecidos na instrução normativa, na apuração dos saldos de ICMS correspondente às operações incentivadas e não incentivadas pelo referido programa, bem assim na aferição de limites fixados, na legislação, para a fruição do incentivo. |
| **Objetivo** | Calcular os créditos, baseado no demonstrativo da apuração mensal, no qual se destina a apurar:  I - a proporção entre as saídas incentivadas e não incentivadas em relação às saídas totais do período;  II - os saldos de ICMS correspondente à parte incentivada e não incentivada;  III - o saldo de credor de ICMS a ser transferido para o período de apuração seguinte;  IV - o valor do ICMS a pagar;  V - o valor dos créditos e débitos passíveis de deduções ou  acréscimos na linha OBSERVAÇÕES do livro Registro de Apuração |
| **Prazo de entrega** | Não há entrega. Os contribuintes beneficiários do programa Fomentar devem preencher, mensalmente, na linha OBSERVAÇÕES do livro Registro de Apuração do ICMS - LRA - o relatório denominado “Demonstrativo da Apuração Mensal - Fomentar/Produzir/Microproduzir”. |
| **Competência** | Estadual – Goiás |
| **Versão do aplicativo contemplado pela Microsiga** | 3.4 |
| **Onde encontrar informações sobre o assunto** | [http://www.sefaz.go.gov.br](http://www.sefaz.go.gov.br/)  <http://www.sefaz.go.gov.br/pops/fomentar.htm> |
| **Legislação contemplada** | Instrução Normativa nº 885/07-GSF, de 22 de novembro de 2007 |

1. No ambiente Configurador, opção “Ambiente/Cadastros/Parâmetros”, crie ou observe os parâmetros a seguir:

|  |  |
| --- | --- |
| **Nome da Var.** | MV\_FOMENGO |
| **Tipo** | Lógico |
| **Conteúdo** | .T. está enquadrado.  .F. não está enquadrado. |
| **Descrição** | Indica se o contribuinte está, ou não, enquadrado como beneficiário do programa Fomentar. |
| **Exemplo** | .T. |

**Importante**

Este parâmetro será verificado em conjunto com o parâmetro MV\_ESTADO, que deverá estar preenchido como “GO”. Caso o parâmetro não seja criado, será considerado como conteúdo *default*.F., para que não apareça na rotina de Apuração de ICMS (MATA953) o folder referente à apuração do Fomentar.

|  |  |
| --- | --- |
| **Nome da Var.** | MV\_RNDFOM |
| **Tipo** | Lógico |
| **Conteúdo** | .T. Não realizar arredondamento.  .F. Realizar arredondamento. |
| **Descrição** | Indica se a função de arredondamento de casas decimais para o cálculo da apuração será desligado. |
| **Exemplo** | .T. |

|  |  |
| --- | --- |
| **Nome da Var.** | MV\_CRDFOM |
| **Tipo** | Caracter |
| **Conteúdo** |  |
| **Descrição** | Indique os CFOPs das operações de entradas que não deverão ser considerados na composição dos créditos por entrada na apuração do Fomentar. |
| **Exemplo** | 1101/1102/2101/ |

|  |  |
| --- | --- |
| **Nome da Var.** | MV\_MERAMOV |
| **Tipo** | Caracter |
| **Conteúdo** |  |
| **Descrição** | Informe neste parâmetro os CFOPs de saída constituam mera movimentação física da mercadoria. |
| **Exemplo** | 5901/6901/5923/ |

### Apuração do ICMS

Acessar a rotina de Apuração do ICMS e após o seu processamento, será exibido um novo folder  **“Apuração-Fomentar”**, em que deverão ser informados os valores solicitados no demonstrativo da apuração mensal – Fomentar.

![](http://tdn.totvs.com/download/attachments/223906427/image2015-9-4%208_49_53.png?version=1&modificationDate=1551703518897&api=v2)

**Importante**

Os cálculos feitos neste folder “Apuração-Fomentar”, são baseados no arquivo *“instrucao-de-preenchimento-do-demonstrativo-versao-34.pdf”* disponibilizado no site da SEFAZ – GO.

Sobre o carregamento automático das informações na linha 001 da aba Fomentar, temos o posicionamento :  
  
*" Atualmente a informação da linha "001 - Saídas das Operações Incentivadas na Apuração de ICMS/ Apuração- Fomentar " não é gerada automaticamente pela rotina MATA953, o contribuinte precisa informar manualmente a receita incentivada.*  
  
*Os itens de Fomentar - GO existente no sistema hoje foram desenvolvimento de forma participativa porque são tratamentos de Regime Especial.  "*  
  
Será necessário o preenchimento manual, conforme detalhado acima. Sobre o tratamento no registro E115, o mesmo é vinculado ao registro na tabela CDV, então quando a configuração é feita na rotina FISA140 e o registro é gerado na tabela CDV o registro será gerado na EFD ICMS/IPI, sem ligação direta com as informações da aba "Fomentar".   
  
Abaixo temos a documentação com o tratamento do registro E115 para que possa ser configurado:  
  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033721013-MP-FIS-REGISTRO-E115-SPED-FISCAL-Informa%C3%A7%C3%B5es-Adicionais-da-Apura%C3%A7%C3%A3o-Valores-Declarat%C3%B3rios>
