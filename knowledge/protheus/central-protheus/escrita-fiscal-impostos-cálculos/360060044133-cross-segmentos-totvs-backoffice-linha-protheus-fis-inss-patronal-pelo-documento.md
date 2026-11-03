---
article_id: 360060044133
category: Escrita Fiscal - Impostos - Cálculos
content_hash: c987c8471795e3109e3762c2a46b3ab52653ac86d124f9dbc455315ccc16403a
fetched_at: '2026-06-28T22:39:31.089936+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- INSS Patronal pelo
  documento de entrada '
type: support-article
updated_at: '2023-10-05T20:31:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060044133-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-INSS-Patronal-pelo-documento-de-entrada
---

**Dúvida**Como realizar a configuração do calculo do **INSS Patronal** pelo documento de entrada?  
  
**Ambiente**Microsiga Protheus – Fiscal – A partir da versão 12.1.17  
  
**Solução**Implementação de nova funcionalidade no sistema, para que seja possível efetuar o calculo do **INSS Patronal** por Nota Fiscal de Entrada.

**- Importante:** Essa funcionalidade só estará disponível a partir da release 12.1.3 que será disponibilizada dia 07/10/2016. Após atualização da base de dados será necessário executar o compatibilizador de dicionário UPDDISTR;

**Para a implementação:** Foram criados os seguintes campos para essa nova rotina;

**1- Tabela SA2 - Cadastro de Fornecedores;**

| **Campo** | A2\_CALCINP |
| --- | --- |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Calc.INSS.Pt |
| **Descrição** | Calcula INSS Patronal? |
| **Lista Opções** | 1=SIM;2=NAO |
| **Val. Sistema** | Pertence(" 12") |
| **Nível** | 1 |
| **Usado** | SIM |
| **Obrigatório** | NÃO |
| **Browse** | SIM |
| **Help** | Informe se deverá calcular INSS Patronal |

**\*Nos casos em que se tratar de MEI, preencher também na aba "Fiscais" o campo TPJ (A2\_TPJ) com a opção 3 - MEI - Microempreendedor Individual:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18058746407575)

**2- Tabela SED - Cadastro de Naturezas;**

| **Campo** | ED\_CALCINP |
| --- | --- |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Calc.INSS.Pt |
| **Descrição** | Calcula INSS Patronal? |
| **Lista Opções** | 1=SIM;2=NAO |
| **Val. Sistema** | Pertence(" 12") |
| **Nível** | 1 |
| **Usado** | SIM |
| **Obrigatório** | NÃO |
| **Browse** | SIM |
| **Help** | Informe se deverá calcular INSS Patronal |

| **Campo** | ED\_PERCINP |
| --- | --- |
| **Browse** | NÃO |
| **Decimal** | 2 |
| **Descrição** | Percent. do INSS Patronal |
| **Formato** | @E 99.99 |
| **Help** | Informe o Percentualdo INSS Patronal. |
| **Nível** | 1 |
| **Obrigatório** | NÃO |
| **Tamanho** | 5 |
| **Tipo** | Numérico |
| **Título** | Perc.INSS.Pt |
| **Usado** | SIM |
| **Val. Sistema** | Positivo() |

**3- Tabela SD1 - Itens das NF de Entrada;**

| **Campo** | D1\_BASEINP |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Bas.INSS.Pt |
| **Descrição** | Base do INSS Patronal |
| **Val. Sistema** | Positivo() .And. MaFisRef("IT\_BASEINP","MT100",M->D1\_BASEINP) |
| **Nível** | 1 |
| **Usado** | SIM |
| **Obrigatório** | NÃO |
| **Browse** | NÃO |
| **Help** | Base do INSS Patronal. |

| **Campo** | D1\_PERCINP |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Título** | Perc.INSS.Pt |
| **Descrição** | Percent. do INSS Patronal |
| **Val. Sistema** | Positivo() .And. MaFisRef("IT\_PERCINP","MT100",M->D1\_PERCINP) |
| **Nível** | 1 |
| **Usado** | SIM |
| **Obrigatório** | NÃO |
| **Browse** | NÃO |
| **Help** | Informe o Percentual do INSS Patronal. |

| **Campo** | D1\_VALINP |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Val.INSS.Pt |
| **Descrição** | Valor do INSS Patronal |
| **Val. Sistema** | Positivo() .And. MaFisRef("IT\_VALINP","MT100",M->D1\_VALINP) |
| **Nível** | 1 |
| **Usado** | SIM |
| **Obrigatório** | NÃO |
| **Browse** | NÃO |
| **Help** | Valor do INSS Patronal. |

**4- Tabela SFT - Livro Fiscal Por Item de NF;**

| **Campo** | FT\_BASEINP |
| --- | --- |
| **Usado** | SIM |
| **Título** | Bas.INSS.Pt |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Obrigatório** | NÃO |
| **Nível** | 1 |
| **Help** | Base do INSS Patronal. |
| **Formato** | @E 99,999,999,999.99 |
| **Descrição** | Base do INSS Patronal |
| **Decimal** | 2 |
| **Browse** | NÃO |

| **Campo** | FT\_PERCINP |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Título** | Perc.INSS.Pt |
| **Descrição** | Percent. do INSS Patronal |
| **Nível** | 1 |
| **Usado** | SIM |
| **Obrigatório** | NÃO |
| **Browse** | NÃO |
| **Help** | Informe o Percentual do INSS Patronal. |

| **Campo** | FT\_VALINP |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Val.INSS.Pt |
| **Descrição** | Valor do INSS Patronal |
| **Nível** | 1 |
| **Usado** | SIM |
| **Obrigatório** | NÃO |
| **Browse** | NÃO |
| **Help** | Valor do INSS Patronal. |

**5- Tabela SF3 - Livros Fiscais;**

| **Campo** | F3\_BASEINP |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Bas.INSS.Pt |
| **Descrição** | Base do INSS Patronal |
| **Nível** | 1 |
| **Usado** | SIM |
| **Obrigatório** | NÃO |
| **Browse** | NÃO |
| **Help** | Base do INSS Patronal. |

| **Campo** | F3\_PERCINP |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Título** | Perc.INSS.Pt |
| **Descrição** | Percent. do INSS Patronal |
| **Nível** | 1 |
| **Usado** | SIM |
| **Obrigatório** | NÃO |
| **Browse** | NÃO |
| **Help** | Informe o Percentual do INSS Patronal. |

| **Campo** | F3\_VALINP |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Val.INSS.Pt |
| **Descrição** | Valor do INSS Patronal |
| **Nível** | 1 |
| **Usado** | SIM |
| **Obrigatório** | NÃO |
| **Browse** | NÃO |
| **Help** | Valor do INSS Patronal. |

**6- Tabela Genérica** **SX5;**

| Tabela | Chave | Descrição |
| --- | --- | --- |
| 00 | 05 | TIPOS DE TITULOS |

**Novo tipo de titulo incluso;**

| Chave | Descrição |
| --- | --- |
| INP | INSS - Patronal |

**7-Para utilização**: Para que a nota fiscal de entrada calcule o **INSS Patronal**, além das configurações padrões para calcular o **INSS**, será necessário que o fornecedor e a natureza esteja com a configuração dos campos, conforme o exemplo abaixo:

| Tabela | SA2 - Cadastro de Fornecedores |
| --- | --- |
| **A2\_CALCINP - Calcula INSS Patronal?** | 1 = SIM |

| Tabela | SED - Cadastro de Naturezas |
| --- | --- |
| **ED\_CALCINP - Calcula INSS Patronal?** | 1 = SIM |
| **ED\_PERCINP - Percent. do INSS Patronal** | 20 |

**8- Importante**: O valor do **INSS Patronal** será calculado sobre a contratação, incidirá o recolhimento correspondente ao percentual do INSS Patronal (20%) preenchido na natureza sobre o valor total da contratação do fornecedor, sendo esta contribuição um encargo da parte da empresa contratante, não podendo ser deduzida do prestador de serviço;

Mais informações no link abaixo:

<https://tdn.totvs.com/display/public/PROT/TUUAJL_DT_CALCULO_INSS_PATRONAL_NOTA_FISCAL_DE_ENTRADA>
