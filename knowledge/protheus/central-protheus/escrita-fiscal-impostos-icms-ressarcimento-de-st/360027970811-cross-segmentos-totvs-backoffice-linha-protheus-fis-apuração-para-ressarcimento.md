---
article_id: 360027970811
category: Escrita Fiscal - Impostos - ICMS - Ressarcimento de ST
content_hash: bc6546d472818db41263e91345e0af122932ecd55dd7bcf1ccd54b18e7840f1f
fetched_at: '2026-06-28T22:39:27.403776+00:00'
product: protheus
section_id: 1500001538661
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Apuração para Ressarcimento
  , Restituição e Complemento ICMS - SC
type: support-article
updated_at: '2021-07-15T18:23:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027970811-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Apura%C3%A7%C3%A3o-para-Ressarcimento-Restitui%C3%A7%C3%A3o-e-Complemento-ICMS-SC
---

## **01. VISÃO GERAL**

O Estado de SC, através do **Decreto Nº 1818 DE 28/11/2018**, introduz, no RICMS/SC-2001 as alterações 3.991 e 3.992, que, em resumo, instituem o **ressarcimento**, a **restituição** e a **complementação**de ICMS retido por substituição tributária em operações anteriores em favor deste Estado. Também dispõem sobre a nova obrigação acessória para a apuração dos valores, a **DRCST (Demonstrativo para Apuração Mensal****do Ressarcimento, da Restituição e da Complementação do ICMS Substituição Tributária)**.

 Conforme as novas disposições, caberá, ao substituído tributário.

1. Ressarcimento do imposto retido por substituição tributária, quando:
   1. Efetuar saídas interestaduais;
   2. Efetuar saídas internas destinadas a empresa optante pelo Simples Nacional;
2. Restituição do imposto retido por substituição tributária correspondente à diferença, quando o valor efetivo da saída destinada a consumidor final se realizar por valor inferior ao da respectiva base de cálculo presumida que serviu para retenção do imposto devido por substituição tributária;
3. Complementação do imposto retido correspondente à diferença, quando o valor efetivo da saída destinada a consumidor final se realizar por valor superior ao da respectiva base de cálculo presumida que serviu para retenção do imposto devido por substituição tributária.

## **02. PROCEDIMENTO PARA IMPLANTAÇÃO**

Importante

Para esta implementação será necessário processar o compatibilizador UPDDISTR com o diferencial de dicionário em anexo.

Para mais informações sobre o UPDDISTR consultar [Atualizador de dicionário e base de dados - UPDDISTR](http://tdn.totvs.com/pages/viewpage.action?pageId=181965468)

**09. DICIONARIO DE DADOS**

**Tabelas**

| **Chave** | **Nome** | **Modo** | **Pyme** |
| --- | --- | --- | --- |
| F1I | Ress.ICMSST-Apuração | Exclusivo | Sim |

**Principais Campos e Parâmetros**

| **Campo** | F1I\_FILIAL |
| --- | --- |
| **Tipo** | Caracter |
| **Tamanho** | 8 |
| **Decimal** | 0 |
| **Título** | Filial |
| **Descrição** | Filial do Sistema |
| **Usado** | Não |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Grupo de Campos** | 033 - Tamanho da Filial |
| **Ordem** | 01 |

|  |  |
| --- | --- |
| **Campo** | F1I\_IDAPUR |
| **Tipo** | Caracter |
| **Tamanho** | 36 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Id. Apuração |
| **Descrição** | Identificador da Apuração |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 02 |

|  |  |
| --- | --- |
| **Campo** | F1I\_ANOMES |
| **Tipo** | Caracter |
| **Tamanho** | 6 |
| **Decimal** | 0 |
| **Formato** | @R 9999/99 |
| **Título** | Período Apur |
| **Descrição** | Período da Apuração |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 03 |

|  |  |
| --- | --- |
| **Campo** | F1I\_VLREST |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr. Restit. |
| **Descrição** | Valor ICMS ST - Restituir |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 04 |

|  |  |
| --- | --- |
| **Campo** | F1I\_VLCOMP |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr. Complem |
| **Descrição** | Valor ICMS ST - Complemen |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 05 |

|  |  |
| --- | --- |
| **Campo** | F1I\_SDREST |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Sld. Restit. |
| **Descrição** | Saldo ICMS ST - Restituir |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 06 |

|  |  |
| --- | --- |
| **Campo** | F1I\_SDRESS |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Sld. Ressar. |
| **Descrição** | Saldo ICMS ST - Ressarcir |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 07 |

|  |  |
| --- | --- |
| **Campo** | F1I\_SDCOMP |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Sld. Complem |
| **Descrição** | Saldo ICMS ST - Complemen |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 08 |

|  |  |
| --- | --- |
| **Campo** | F1I\_SDICOP |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Sld. ICMS OP |
| **Descrição** | Saldo ICMS - Op. Próprias |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 09 |

|  |  |
| --- | --- |
| **Campo** | F1I\_VLACRE |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr.Ap.Cred. |
| **Descrição** | Valor Apurado - Crédito |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 10 |

|  |  |
| --- | --- |
| **Campo** | F1I\_VLACOM |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr.Ap.Comp. |
| **Descrição** | Valor Apurado - Complemen |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 11 |

**Índices**

|  |  |
| --- | --- |
| **Índice** | F1I |
| **Ordem** | 1 |
| **Chave** | F1I\_FILIAL + F1I\_ANOMES |
| **Descrição** | Período Apur |
| **Mostra Pesq.** | Sim |

|  |  |
| --- | --- |
| **Índice** | F1I |
| **Ordem** | 2 |
| **Chave** | F1I\_FILIAL + F1I\_IDAPUR |
| **Descrição** | Id. Apuração |
| **Mostra Pesq.** | Sim |

**Tabelas**

| **Chave** | **Nome** | **Modo** | **Pyme** |
| --- | --- | --- | --- |
| F1J | Ress.ICMSST-Apuração Produto | Exclusivo | Sim |

**Principais Campos e Parâmetros**

|  |  |
| --- | --- |
| **Campo** | F1J\_FILIAL |
| **Tipo** | Caracter |
| **Tamanho** | 8 |
| **Decimal** | 0 |
| **Título** | Filial |
| **Descrição** | Filial do Sistema |
| **Usado** | Não |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Grupo de Campos** | 033 - Tamanho da Filial |
| **Ordem** | 01 |

|  |  |
| --- | --- |
| **Campo** | F1J\_IDAPUR |
| **Tipo** | Caracter |
| **Tamanho** | 36 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Id. Apuração |
| **Descrição** | Identificador da Apuração |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 02 |

|  |  |
| --- | --- |
| **Campo** | F1J\_ANOMES |
| **Tipo** | Caracter |
| **Tamanho** | 6 |
| **Decimal** | 0 |
| **Formato** | @R 9999/99 |
| **Título** | Período Apur |
| **Descrição** | Período da Apuração |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 03 |

|  |  |
| --- | --- |
| **Campo** | F1J\_PRODUT |
| **Tipo** | Caracter |
| **Tamanho** | 30 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Cód. Produto |
| **Descrição** | Código do Produto |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Grupo de Campos** | 030 - Tamanho do Produto |
| **Ordem** | 04 |

|  |  |
| --- | --- |
| **Campo** | F1J\_QTDVCF |
| **Tipo** | Numérico |
| **Tamanho** | 16 |
| **Decimal** | 2 |
| **Formato** | @E 9,999,999,999,999.99 |
| **Título** | Qtd Venda CF |
| **Descrição** | Qtde Total de Venda a CF |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 05 |

|  |  |
| --- | --- |
| **Campo** | F1J\_VLRVCF |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr Venda CF |
| **Descrição** | Valor Total de Venda a CF |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 06 |

|  |  |
| --- | --- |
| **Campo** | F1J\_VMUVCF |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vl.Med.Un.CF |
| **Descrição** | Valor Med Unit Venda a CF |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 07 |

|  |  |
| --- | --- |
| **Campo** | F1J\_VBSTCF |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr.BC.ST.CF |
| **Descrição** | Valor Base Calc ST Ven CF |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 08 |

|  |  |
| --- | --- |
| **Campo** | F1J\_VMABST |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vl.Dif.Maior |
| **Descrição** | Valor Dif Mai BCST Vlr CF |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 09 |

|  |  |
| --- | --- |
| **Campo** | F1J\_VMEBST |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vl.Dif.Menor |
| **Descrição** | Valor Dif Men BCST Vlr CF |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 10 |

|  |  |
| --- | --- |
| **Campo** | F1J\_ALIQEF |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Título** | Aliq. Efetiv |
| **Descrição** | Alíquota Efetiva do ICMS |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 11 |

|  |  |
| --- | --- |
| **Campo** | F1J\_VLREST |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr. Restit. |
| **Descrição** | Valor ICMS ST - Restituir |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 12 |

|  |  |
| --- | --- |
| **Campo** | F1J\_VLCOMP |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr. Complem |
| **Descrição** | Valor ICMS ST - Complemen |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 13 |

|  |  |
| --- | --- |
| **Campo** | F1J\_QTDSOE |
| **Tipo** | Numérico |
| **Tamanho** | 16 |
| **Decimal** | 2 |
| **Formato** | @E 9,999,999,999,999.99 |
| **Título** | Qtd Venda OE |
| **Descrição** | Qtde Total de Venda a OE |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 14 |

|  |  |
| --- | --- |
| **Campo** | F1J\_VICMOE |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr ICMS OE |
| **Descrição** | Valor ICMS Ref Saidas OE |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 15 |

|  |  |
| --- | --- |
| **Campo** | F1J\_VISTOE |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr ICMST OE |
| **Descrição** | Valor ICMST Ref Saidas OE |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 16 |

|  |  |
| --- | --- |
| **Campo** | F1J\_QTDSSN |
| **Tipo** | Numérico |
| **Tamanho** | 16 |
| **Decimal** | 2 |
| **Formato** | @E 9,999,999,999,999.99 |
| **Título** | Qtd Venda SN |
| **Descrição** | Qtde Total de Venda a SN |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 17 |

|  |  |
| --- | --- |
| **Campo** | F1J\_VCRDSN |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr Cred SN |
| **Descrição** | Valor Total Cred Venda SN |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 18 |

**Índices**

|  |  |
| --- | --- |
| **Índice** | F1J |
| **Ordem** | 1 |
| **Chave** | F1J\_FILIAL + F1J\_ANOMES + F1J\_PRODUT |
| **Descrição** | Período Apur + Cód. Produto |
| **Mostra Pesq.** | Sim |

|  |  |
| --- | --- |
| **Índice** | F1J |
| **Ordem** | 2 |
| **Chave** | F1J\_FILIAL + F1J\_IDAPUR + F1J\_PRODUT |
| **Descrição** | Id. Apuração + Cód. Produto |
| **Mostra Pesq.** | Sim |

|  |  |  |  |
| --- | --- | --- | --- |
| **Chave** | **Nome** | **Modo** | **Pyme** |
| F1K | Ress.ICMSST-Apuração Venda ECF | Exclusivo | Sim |

**Campos**

|  |  |
| --- | --- |
| **Campo** | F1K\_FILIAL |
| **Tipo** | Caracter |
| **Tamanho** | 8 |
| **Decimal** | 0 |
| **Título** | Filial |
| **Descrição** | Filial do Sistema |
| **Usado** | Não |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Grupo de Campos** | 033 - Tamanho da Filial |
| **Ordem** | 01 |

|  |  |
| --- | --- |
| **Campo** | F1K\_IDAPUR |
| **Tipo** | Caracter |
| **Tamanho** | 36 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Id. Apuração |
| **Descrição** | Identificador da Apuração |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 02 |

|  |  |
| --- | --- |
| **Campo** | F1K\_ANOMES |
| **Tipo** | Caracter |
| **Tamanho** | 6 |
| **Decimal** | 0 |
| **Formato** | @R 9999/99 |
| **Título** | Período Apur |
| **Descrição** | Período da Apuração |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 03 |

|  |  |
| --- | --- |
| **Campo** | F1K\_PRODUT |
| **Tipo** | Caracter |
| **Tamanho** | 30 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Cód. Produto |
| **Descrição** | Código do Produto |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Grupo de Campos** | 030 - Tamanho do Produto |
| **Ordem** | 04 |

|  |  |
| --- | --- |
| **Campo** | F1K\_QTDVCF |
| **Tipo** | Numérico |
| **Tamanho** | 16 |
| **Decimal** | 2 |
| **Formato** | @E 9,999,999,999,999.99 |
| **Título** | Qtd Vd CF NF |
| **Descrição** | Qtde Total Venda a CF NF |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 05 |

|  |  |
| --- | --- |
| **Campo** | F1K\_UNID |
| **Tipo** | Caracter |
| **Tamanho** | 2 |
| **Decimal** | 0 |
| **Título** | Unid Prod NF |
| **Descrição** | Unidade do Produto na NF |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Grupo de Campos** | 122 - Unidade de Medida |
| **Ordem** | 06 |

|  |  |
| --- | --- |
| **Campo** | F1K\_FATCON |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Título** | Fator Conver |
| **Descrição** | Fator Convers. p/ Un 0200 |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 07 |

|  |  |
| --- | --- |
| **Campo** | F1K\_QTVCFC |
| **Tipo** | Numérico |
| **Tamanho** | 16 |
| **Decimal** | 2 |
| **Formato** | @E 9,999,999,999,999.99 |
| **Título** | Qtd Venda CF |
| **Descrição** | Qtde Total de Venda a CF |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 08 |

|  |  |
| --- | --- |
| **Campo** | F1K\_VLRVCF |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr Venda CF |
| **Descrição** | Valor Total de Venda a CF |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 09 |

**Índices**

|  |  |
| --- | --- |
| **Índice** | F1K |
| **Ordem** | 1 |
| **Chave** | F1K\_FILIAL + F1K\_ANOMES + F1K\_PRODUT + F1K\_UNID |
| **Descrição** | Período Apur + Cód. Produto + Unid Prod NF |
| **Mostra Pesq.** | Sim |

|  |  |
| --- | --- |
| **Índice** | F1K |
| **Ordem** | 2 |
| **Chave** | F1K\_FILIAL + F1K\_IDAPUR + F1K\_PRODUT + F1K\_UNID |
| **Descrição** | Id. Apuração + Cód. Produto + Unid Prod NF |
| **Mostra Pesq.** | Sim |

**Tabela**

|  |  |  |  |
| --- | --- | --- | --- |
| **Chave** | **Nome** | **Modo** | **Pyme** |
| F1L | Ress.ICMSST-Apuração Entradas | Exclusivo | Sim |

**Campos**

|  |  |
| --- | --- |
| **Campo** | F1L\_FILIAL |
| **Tipo** | Caracter |
| **Tamanho** | 8 |
| **Decimal** | 0 |
| **Título** | Filial |
| **Descrição** | Filial do Sistema |
| **Usado** | Não |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Grupo de Campos** | 033 - Tamanho da Filial |
| **Ordem** | 01 |

|  |  |
| --- | --- |
| **Campo** | F1L\_IDAPUR |
| **Tipo** | Caracter |
| **Tamanho** | 36 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Id. Apuração |
| **Descrição** | Identificador da Apuração |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 02 |

|  |  |
| --- | --- |
| **Campo** | F1L\_ANOMES |
| **Tipo** | Caracter |
| **Tamanho** | 6 |
| **Decimal** | 0 |
| **Formato** | @R 9999/99 |
| **Título** | Período Apur |
| **Descrição** | Período da Apuração |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 03 |

|  |  |
| --- | --- |
| **Campo** | F1L\_PRODUT |
| **Tipo** | Caracter |
| **Tamanho** | 30 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Cód. Produto |
| **Descrição** | Código do Produto |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Grupo de Campos** | 030 - Tamanho do Produto |
| **Ordem** | 04 |

|  |  |
| --- | --- |
| **Campo** | F1L\_QTDENT |
| **Tipo** | Numérico |
| **Tamanho** | 16 |
| **Decimal** | 2 |
| **Formato** | @E 9,999,999,999,999.99 |
| **Título** | Qtd Entradas |
| **Descrição** | Qtde Total de Entradas |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 05 |

|  |  |
| --- | --- |
| **Campo** | F1L\_TOTBST |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr.Tot.BCST |
| **Descrição** | Valor Total da BC ICMS ST |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 06 |

|  |  |
| --- | --- |
| **Campo** | F1L\_VMUBST |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | V.Med.Un.BST |
| **Descrição** | Valor Med Unit BC ICMS ST |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 07 |

|  |  |
| --- | --- |
| **Campo** | F1L\_TOTICM |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr.Tot.ICMS |
| **Descrição** | Valor Total do ICMS OP |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 08 |

|  |  |
| --- | --- |
| **Campo** | F1L\_VMUICM |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | V.Med.Un.ICM |
| **Descrição** | Valor Med Unit ICMS OP |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 09 |

|  |  |
| --- | --- |
| **Campo** | F1L\_TOTIST |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr.Tot.ST |
| **Descrição** | Valor Total do ICMS ST |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 10 |

|  |  |
| --- | --- |
| **Campo** | F1L\_VMUIST |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vl.Med.Un.ST |
| **Descrição** | Valor Med Unit ICMS ST |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 11 |

**Índices**

|  |  |
| --- | --- |
| **Índice** | F1L |
| **Ordem** | 1 |
| **Chave** | F1L\_FILIAL + F1L\_ANOMES + F1L\_PRODUT |
| **Descrição** | Período Apur + Cód. Produto |
| **Mostra Pesq.** | Sim |

|  |  |
| --- | --- |
| **Índice** | F1L |
| **Ordem** | 2 |
| **Chave** | F1L\_FILIAL + F1L\_IDAPUR + F1L\_PRODUT |
| **Descrição** | Id. Apuração + Cód. Produto |
| **Mostra Pesq.** | Sim |

**Tabela**

|  |  |  |  |
| --- | --- | --- | --- |
| **Chave** | **Nome** | **Modo** | **Pyme** |
| F1M | Ress.ICMSST-Apuração Detalhada | Exclusivo | Sim |

**Campos**

|  |  |
| --- | --- |
| **Campo** | F1M\_FILIAL |
| **Tipo** | Caracter |
| **Tamanho** | 8 |
| **Decimal** | 0 |
| **Título** | Filial |
| **Descrição** | Filial do Sistema |
| **Usado** | Não |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Grupo de Campos** | 033 - Tamanho da Filial |
| **Ordem** | 01 |

|  |  |
| --- | --- |
| **Campo** | F1M\_IDAPUR |
| **Tipo** | Caracter |
| **Tamanho** | 36 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Id. Apuração |
| **Descrição** | Identificador da Apuração |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 02 |

|  |  |
| --- | --- |
| **Campo** | F1M\_ANOMES |
| **Tipo** | Caracter |
| **Tamanho** | 6 |
| **Decimal** | 0 |
| **Formato** | @R 9999/99 |
| **Título** | Período Apur |
| **Descrição** | Período da Apuração |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 03 |

|  |  |
| --- | --- |
| **Campo** | F1M\_PRODUT |
| **Tipo** | Caracter |
| **Tamanho** | 30 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Cód. Produto |
| **Descrição** | Código do Produto |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Grupo de Campos** | 030 - Tamanho do Produto |
| **Ordem** | 04 |

|  |  |
| --- | --- |
| **Campo** | F1M\_ORDEM |
| **Tipo** | Caracter |
| **Tamanho** | 9 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Ordem Movim. |
| **Descrição** | Ordem do Movimento |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 05 |

|  |  |
| --- | --- |
| **Campo** | F1M\_DTMOV |
| **Tipo** | Data |
| **Tamanho** | 8 |
| **Decimal** | 0 |
| **Título** | Data Movim. |
| **Descrição** | Data do Movimento |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 06 |

|  |  |
| --- | --- |
| **Campo** | F1M\_TPMOV |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Tipo Movim. |
| **Descrição** | Tipo do Movimento |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 07 |

|  |  |
| --- | --- |
| **Campo** | F1M\_INDOP |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Ind.Operacao |
| **Descrição** | Indicador da Operação |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 08 |

|  |  |
| --- | --- |
| **Campo** | F1M\_NFISCA |
| **Tipo** | Caracter |
| **Tamanho** | 9 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Num.Doc.Fisc |
| **Descrição** | Núm. do Documento Fiscal |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Grupo de Campos** | 018 - Documento de entrada/saída |
| **Ordem** | 09 |

|  |  |
| --- | --- |
| **Campo** | F1M\_SERIE |
| **Tipo** | Caracter |
| **Tamanho** | 3 |
| **Decimal** | 0 |
| **Formato** | !!! |
| **Título** | Ser.Doc.Fisc |
| **Descrição** | Série do Documento Fiscal |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Grupo de Campos** | 094 - Id de Controle dos doc.fiscais |
| **Ordem** | 10 |

|  |  |
| --- | --- |
| **Campo** | F1M\_ITEM |
| **Tipo** | Caracter |
| **Tamanho** | 4 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Ite.Doc.Fisc |
| **Descrição** | Item do Documento Fiscal |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 11 |

|  |  |
| --- | --- |
| **Campo** | F1M\_CFOP |
| **Tipo** | Caracter |
| **Tamanho** | 5 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | CFOP |
| **Descrição** | Código Fiscal Oper/Prest |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 12 |

|  |  |
| --- | --- |
| **Campo** | F1M\_ESPECI |
| **Tipo** | Caracter |
| **Tamanho** | 5 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Espécie Doc |
| **Descrição** | Espécie Documento Fiscal |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 13 |

|  |  |
| --- | --- |
| **Campo** | F1M\_CHVDOC |
| **Tipo** | Caracter |
| **Tamanho** | 44 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Chav.Doc.Fis |
| **Descrição** | Chave do Documento Fiscal |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 14 |

|  |  |
| --- | --- |
| **Campo** | F1M\_SERECF |
| **Tipo** | Caracter |
| **Tamanho** | 21 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | N. Série ECF |
| **Descrição** | Número de Série do ECF |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 15 |

|  |  |
| --- | --- |
| **Campo** | F1M\_PARTIC |
| **Tipo** | Caracter |
| **Tamanho** | 6 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Participante |
| **Descrição** | Código do Participante |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Grupo de Campos** | 001 - Codigo Cliente/Fornecedor |
| **Ordem** | 16 |

|  |  |
| --- | --- |
| **Campo** | F1M\_LOJA |
| **Tipo** | Caracter |
| **Tamanho** | 2 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Loja |
| **Descrição** | Loja do Participante |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Grupo de Campos** | 002 - Loja Cliente/Fornecedor |
| **Ordem** | 17 |

|  |  |
| --- | --- |
| **Campo** | F1M\_CNPJ |
| **Tipo** | Caracter |
| **Tamanho** | 14 |
| **Decimal** | 0 |
| **Formato** | @R 99.999.999/9999-99 |
| **Título** | CNPJ/CPF |
| **Descrição** | CNPJ ou CPF Participante |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 18 |

|  |  |
| --- | --- |
| **Campo** | F1M\_QTDMOV |
| **Tipo** | Numérico |
| **Tamanho** | 16 |
| **Decimal** | 2 |
| **Formato** | @E 9,999,999,999,999.99 |
| **Título** | Qtd. Mov. NF |
| **Descrição** | Qtde do Movimento na NF |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 19 |

|  |  |
| --- | --- |
| **Campo** | F1M\_UNIDAD |
| **Tipo** | Caracter |
| **Tamanho** | 2 |
| **Decimal** | 0 |
| **Título** | Unid Prod NF |
| **Descrição** | Unidade do Produto na NF |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Grupo de Campos** | 122 - Unidade de Medida |
| **Ordem** | 20 |

|  |  |
| --- | --- |
| **Campo** | F1M\_FATCON |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Título** | Fator Conver |
| **Descrição** | Fator Convers. p/ Un 0200 |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 21 |

|  |  |
| --- | --- |
| **Campo** | F1M\_QTDCON |
| **Tipo** | Numérico |
| **Tamanho** | 16 |
| **Decimal** | 2 |
| **Formato** | @E 9,999,999,999,999.99 |
| **Título** | Qtd.Mov.Conv |
| **Descrição** | Qtde do Movimento Convert |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 22 |

|  |  |
| --- | --- |
| **Campo** | F1M\_VLRCON |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr.Doc.Fisc |
| **Descrição** | Valor do Documento Fiscal |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 23 |

|  |  |
| --- | --- |
| **Campo** | F1M\_BASICM |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr. BC. ICM |
| **Descrição** | Valor da Bas Calc ICMS OP |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 24 |

|  |  |
| --- | --- |
| **Campo** | F1M\_ALQICM |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Alq. ICMS OP |
| **Descrição** | Alíquota do ICMS OP |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 25 |

|  |  |
| --- | --- |
| **Campo** | F1M\_VLRICM |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr. ICMS OP |
| **Descrição** | Valor do ICMS OP |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 26 |

|  |  |
| --- | --- |
| **Campo** | F1M\_BASIST |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr.BC.ICMST |
| **Descrição** | Valor da Bas Calc ICMS ST |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 27 |

|  |  |
| --- | --- |
| **Campo** | F1M\_ALQIST |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Alq. ICMS ST |
| **Descrição** | Alíquota do ICMS ST |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 28 |

|  |  |
| --- | --- |
| **Campo** | F1M\_VLRIST |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr. ICMS ST |
| **Descrição** | Valor do ICMS ST |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 29 |

|  |  |
| --- | --- |
| **Campo** | F1M\_CODAJU |
| **Tipo** | Caracter |
| **Tamanho** | 10 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Cód. Ajuste |
| **Descrição** | Código Ajuste Débito C197 |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 30 |

|  |  |
| --- | --- |
| **Campo** | F1M\_CODDA |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Cód.Mod.Arre |
| **Descrição** | Código do Mod. de Arrecad |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 31 |

|  |  |
| --- | --- |
| **Campo** | F1M\_NMDARE |
| **Tipo** | Caracter |
| **Tamanho** | 12 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Num. DARE |
| **Descrição** | Número do DARE |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 32 |

|  |  |
| --- | --- |
| **Campo** | F1M\_CODRES |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Cód.Resp.Ret |
| **Descrição** | Código Respons. Retenção |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 33 |

|  |  |
| --- | --- |
| **Campo** | F1M\_INDSAI |
| **Tipo** | Caracter |
| **Tamanho** | 2 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Ind. Saída |
| **Descrição** | Indicador do Tipo Saida |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 34 |

|  |  |
| --- | --- |
| **Campo** | F1M\_VCRDSN |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vlr.Cred.SN |
| **Descrição** | Valor de Créd. Venda SN |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Ordem** | 35 |

**Índices**

|  |  |
| --- | --- |
| **Índice** | F1M |
| **Ordem** | 1 |
| **Chave** | F1M\_FILIAL + F1M\_ANOMES + F1M\_PRODUT + F1M\_ORDEM |
| **Descrição** | Período Apur + Cód. Produto + Ordem Movim. |
| **Mostra Pesq.** | Sim |

|  |  |
| --- | --- |
| **Índice** | F1M |
| **Ordem** | 2 |
| **Chave** | F1M\_FILIAL + F1M\_IDAPUR + F1M\_PRODUT + F1M\_ORDEM |
| **Descrição** | Id. Apuração + Cód. Produto + Ordem Movim. |
| **Mostra Pesq.** | Sim |

**Parâmetros do Sistema**

|  |  |
| --- | --- |
| **Nome Var.** | FS\_GCTCOT |
| **Tipo** | Caracter |
| **Descrição** | Tipo Contrato para cotacao |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_A390QTD |
| **Tipo** | Logico |
| **Descrição** | Indica se no cadastro de saldos iniciais poderão |
| **Cont.Descric.** | ser informados apenas um lote(.T.) ou N Lotes(.F.) |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_CODMUNF |
| **Tipo** | Caracter |
| **Descrição** | campo da Tabela SA2 em que sera armazenado o codig |
| **Cont.Descric.** | o da cidade do prestador dr servico segundo arquiv |
| **Cont.Descric.** | o de cidades disponibilizado p prefeitura de Goian |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_EFD |
| **Tipo** | Logico |
| **Descrição** |  |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_ESPOBG |
| **Tipo** | Logico |
| **Descrição** | Determina se o campo F1\_ESPECIE deve ser |
| **Cont.Descric.** | obrigatório no cabeçalho do Documento de Entrada. |
| **Cont.Descric.** | (.T.) Sim (.F.) Não; |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_FINATFN |
| **Tipo** | Caracter |
| **Descrição** | "1" = Fluxo Caixa On-Line,"2" = Fluxo Caixa Off-Li |
| **Cont.Descric.** | ne |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_HVERAOF |
| **Tipo** | Data |
| **Descrição** | Data de término do horário de verão. |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_HVERAOI |
| **Tipo** | Data |
| **Descrição** | Data de início do horário de verão. |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_JGERDES |
| **Tipo** | Numérico |
| **Descrição** | Habilitar a Geracao de despesa com base nos valore |
| **Cont.Descric.** | s: (1= Negociacoes; 2= Valor Final da Causa) |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_NTSV |
| **Tipo** | Caracter |
| **Descrição** | Informe as categorias de TSV que nao sao obrigados |
| **Cont.Descric.** | a terem o evento S-2300 |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_PERAUT |
| **Tipo** | Logico |
| **Descrição** | Permite geracao do evento S-1200 de autonomos agru |
| **Cont.Descric.** | pados por semana (.F. = padrao) ou por data de pag |
| **Cont.Descric.** | amento (.T.) |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_PLGERNC |
| **Tipo** | Caracter |
| **Descrição** | Define se deve gerar um titulo do tipo “NCC (Nota |
| **Cont.Descric.** | Credito ao Cliente)”, quando os creditos forem mai |
| **Cont.Descric.** | ores que os debitos da familia / beneficiarios. ”1 |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_PLRDEM |
| **Tipo** | Caracter |
| **Descrição** | Calcula PLR para demitidos no ano posterior a |
| **Cont.Descric.** | referencia de calculo? |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_PROFERP |
| **Tipo** | Numérico |
| **Descrição** | Define se realiza Calc Ferias Progr Particionada |
| **Cont.Descric.** | 0 - Nao utiliza; 1 - Inicia sempre na 2a-Feira; |
| **Cont.Descric.** | 2 - Dias Corridos |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_REPLRAT |
| **Tipo** | Logico |
| **Descrição** | Replica a programação de rateio de um mês para o |
| **Cont.Descric.** | outro durante o fechamento da folha. |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_RHTAF |
| **Tipo** | Logico |
| **Descrição** | Habilita a integração de dados do eSocial com TAF |
| **Cont.Descric.** | Se .T., passa a integrar dados de eventos não |
| **Cont.Descric.** | periodicos do SIGAGPE com o SIGATAF |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_SATTEST |
| **Tipo** | Caracter |
| **Descrição** | Possibilita configurar o sistema para vendas no |
| **Cont.Descric.** | regime SAT em modo de teste |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_UFALCMP |
| **Tipo** | Caracter |
| **Descrição** | Informe os Estados que calculam DIFAL considerando |
| **Cont.Descric.** | a diferenca entre aliquota interestadual e interna |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_VL13137 |
| **Tipo** | Numérico |
| **Descrição** | Define o valor mínimo para retenção do |
| **Cont.Descric.** | Pis/Cofins/Csll de acordo com a Lei 13.137 |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_XMLSIZE |
| **Tipo** | Numérico |
| **Descrição** | Parametro criado para aumentar a limitacao de tran |
| **Cont.Descric.** | smissao do XML que atualmente e de 500 KB. |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_SATTEST |
| **Tipo** | Caracter |
| **Descrição** | Possibilita configurar o sistema para vendas no |
| **Cont.Descric.** | regime SAT em modo de teste |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_UFALCMP |
| **Tipo** | Caracter |
| **Descrição** | Informe os Estados que calculam DIFAL considerando |
| **Cont.Descric.** | a diferenca entre aliquota interestadual e interna |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_VL13137 |
| **Tipo** | Numérico |
| **Descrição** | Define o valor mínimo para retenção do |
| **Cont.Descric.** | Pis/Cofins/Csll de acordo com a Lei 13.137 |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_XMLSIZE |
| **Tipo** | Numérico |
| **Descrição** | Parametro criado para aumentar a limitacao de tran |
| **Cont.Descric.** | smissao do XML que atualmente e de 500 KB. |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_SATTEST |
| **Tipo** | Caracter |
| **Descrição** | Possibilita configurar o sistema para vendas no |
| **Cont.Descric.** | regime SAT em modo de teste |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_SATTEST |
| **Tipo** | Caracter |
| **Descrição** | Possibilita configurar o sistema para vendas no |
| **Cont.Descric.** | regime SAT em modo de teste |

|  |  |
| --- | --- |
| **Nome Var.** | MV\_VL13137 |
| **Tipo** | Numérico |
| **Descrição** | Define o valor mínimo para retenção do |
| **Cont.Descric.** | Pis/Cofins/Csll de acordo com a Lei 13.137 |

## **03. PROCEDIMENTO PARA CONFIGURAÇÃO**

**CONFIGURAÇÃO DE MENUS**

1.  No **Configurador (SIGACFG),**acesse **Ambientes/Cadastro/Menu (CFGX013)**. Informe a nova opção de menu, conforme instruções a seguir:

| **Menu** | SIGAFIS |
| --- | --- |
| **Submenu** | Miscelânea |
| **Nome da Rotina** | **Apuracão****Ressarcimento de ICMS-ST SC** |
| **Programa** | **FISA230** |
| **Módulo** | Todos |
| **Tipo** | Protheus |

Importante

Para mais informações sobre inclusão de rotinas no menu: [PSIGABD0006 - CFGX013- Inclusão de rotina no Menu.](http://tdn.totvs.com/pages/viewpage.action?pageId=219693837)

**04. PROCEDIMENTO PARA UTILIZAÇÃO**

A rotina possui opções que permitem a apuração de valores de ressarcimento , restituição ou complemento do ICMS retido por substituição tributária em operações anteriores para o estado de Santa Catarina,  além da extração de relatório para conferência desses valores e a geração do arquivo digital para transmissão DRCST.  
Para o processamento da apuração, a rotina possui um cadastro de regras que será carregado na primeira vez que a rotina for acessada.  Será necessário também o fechamento mensal do estoque e inventário.

Atenção

A rotina de apuração foi desenvolvida segundo o [Manual do Sistema Ressarcimento, Restituição e Complementação de ICMS-ST na Portaria 378/2018 de Santa Catarina](http://legislacao.sef.sc.gov.br/html/regulamentos/icms/ricms_01_03_pas.htm), e sua execução é obrigatória para a geração do relatório e do arquivo final. Após o processamento, apresentará os valores estimados do tributo, à ressarcir, restituir e à complementar, no período analisado. No entanto, trata-se de uma **rotina de apoio.**Para geração e validação do arquivo DRCST foi desenvolvido com apoio do [leiaute do arquivo eletrônico](http://legislacao.sef.sc.gov.br/html/portarias/2018/port_18_378.htm).

**As opções disponíveis são:**

* Ressarcimento, Restituição e Complemento do ICMS ST
* Regras para Movimentos
* Relatório de Conferência
* Geração do Arquivo

![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-17_11-31-26.png?version=1&modificationDate=1555511487157&api=v2)

## **05. FECHAMENTO DO ESTOQUE**

         Antes de gerar a apuração é necessário seguir os procedimento para fechar o estoque , segue o  link com as orientações: [PEST05502 - MATA280 - Roteiro para a realização da virada de saldos no estoque](http://tdn.totvs.com/pages/viewpage.action?pageId=284352086).

        Caso não siga os procedimento de fechamento de estoque a mensagem abaixo será exibida quando for executar a apuração da rotina FISA230.

       ![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-17_15-23-30.png?version=1&modificationDate=1555525410747&api=v2)

Atenção!

Segundo o [Manual do Sistema Ressarcimento, Restituição e Complementação de ICMS-ST na Portaria 378/2018 de Santa Catarina](http://legislacao.sef.sc.gov.br/html/regulamentos/icms/ricms_01_03_pas.htm), quando o estabelecimento ingressar neste sistema de apuração do ICMS passível de ressarcimento, restituição  ou complemento, procederá ao levantamento dos estoques existentes , que deverão ser escriturados no Livro Registro de Inventário, modelo 7.

## **05. REGRAS PARA MOVIMENTOS**

No primeiro acesso na rotina FISA230 é gerado uma carga inicial com as Regras de Movimentos com os **CFOP** (Código Fiscal  de Operações  e de Prestações ) x **CST**(Código de Situação Tributária). Para operações que o cliente entende que não deveria ser considerada, pode  excluir o cadastro ou adicionar sua operação específica.

![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-17_14-49-54.png?version=1&modificationDate=1555523394580&api=v2)

![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-17_15-3-22.png?version=1&modificationDate=1555524202850&api=v2)

## **07.** **APURAÇÃO**

A rotina de Apuração do Ressarcimento , Restituição e Complemento , parte de um fechamento de estoque e o cadastro de Regras de Movimentos, para o período selecionado, e, dentro desse período, analisa movimentos de entrada e saída, adotando,  o método do custo médio ponderado.

A apuração analisará a movimentação de entrada e saída de produtos que possuam o campo **Cont. ICMS-ST** (**B1\_CRICMST**) ajustados com "**1 - Sim**". 

Quanto à ressarcimento/complemento, movimentos de saída **podem ou não gerar ressarcimento ou complemento de imposto**.

Ao final do processamento, a rotina apresentará os valores estimados do tributo, à ressarcir, restituir e à complementar, no período analisado.

Deverá ser informado o período para o processamento:

![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-18_14-14-44.png?version=1&modificationDate=1555607685487&api=v2)

**Mês/Ano Ref. ?**- Informe o Mês/Ano de Referencia para apuração.

**% Red MVA Simples Nacional ? -**Percentual de redução do MVA utilizado em saídas internas destinadas a empresa optante pelo Simples Nacional.

Caso seja informado um período já processado anteriormente, será exibida a pergunta abaixo. Caso o reprocessamento seja confirmado, os registros existentes do período informado serão excluídos e reprocessados.

![](http://tdn.totvs.com/download/attachments/484701377/image2018-12-3_16-21-34.png?version=1&modificationDate=1555587466787&api=v2)

Tela principal com o resultado do processamento da apuração:

![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-18_9-0-17.png?version=1&modificationDate=1555588817870&api=v2)

**Visualizar**

Será possível verificar o resultado da apuração:

![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-18_9-30-31.png?version=1&modificationDate=1555590632477&api=v2)

**Excluir**

Serão excluídos todos os registros da apuração no período selecionado.

**7.1 -****RESTITUIÇÃO**

Para a apuração do valor à restituir (saídas a Consumidor Final), para cada mercadoria sujeita ao ICMS-ST, será utilizado o valor ponderado médio:

1. da base de cálculo da substituição tributária relativo às entradas;
2. das saídas destinadas a consumidor final.

Na rotina de apuração a tabela F1L , terá as medias ponderadas das Entradas por Produto

![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-17_16-11-17.png?version=1&modificationDate=1555528277733&api=v2)

Na apuração dos valores ponderados médios de entrada serão consideradas:

1. Para o período apurado, todas as aquisições de cada mercadoria envolvida, deduzidas das devoluções ocorridas
2. O valor ponderado médio mensal relativo à entrada será o resultado da divisão:
   1. do somatório dos valores das entradas **/** pela quantidade de entradas de cada item de mercadoria, desde que esta quantidade seja maior ou igual ao somatório das saídas: Ex: 39200/30 = 1306,67 ; 3860/30 = 128,67.
3. Sempre que a quantidade das entradas de cada item de mercadoria for menor que o somatório das saídas , a rotina irá buscar entrada anteriores do período em apuração até que se satisfaça a condição prevista.

Para as operações Consumidor Final  os campos da tabelas F1J são utilizados para o calculo

![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-17_19-2-39.png?version=1&modificationDate=1555538559967&api=v2)

Onde 6533,33 - 6000,00 = 66,67

66,67 \* 17% = 11,33 a Complementar , por que o Valor Base Calculo do  ST  da Venda a  Consumidor Final  é menor que o valor Valor Total de Venda a CF,  se o Valor Total de Venda a CF for maior teríamos valor a Restituir.

**7.2 - RESSARCIMENTO**

Para a apuração do valor de ressarcimento, para cada mercadoria sujeita ao ICMS-ST, será utilizado:

1. Hipótese de saídas interestaduais: o valor ponderado médio para o imposto retido e para o imposto próprio relativos à entrada;
2. Hipótese de saídas internas destinadas a empresa optante pelo Simples Nacional: a soma dos valores calculados em cada saída , deduzidas das respectivas anulações e devoluções de venda;
3. Para todas as hipóteses, a soma das quantidades de saídas, deduzidas as respectivas anulações e devoluções de venda.

Para movimentações das empresas optante pelo Simples Nacional, necessita configurar no cadastro de produto de produto o campo F2Q\_RESVSN(**Ress.Vend.SN**)  ,para ocorrer o ressarcimento e a apuração gravar os valores na tabela F1M( Movimentos de Entrada e Saida) - **F1M\_VCRDSN**

Importante

Para habilitar no cadastro de produto SB1, o cadastro de complemento Fiscal , segue link com a documentação : [PEST018 - MV\_CADPROD - Parâmetro para informar quais cadastros complementares devem ser apresentados no cadastro de produto](http://tdn.totvs.com/pages/viewpage.action?pageId=317003310)

Tabela F1M - Movimentos detalhados e as soma dos campos de BASE , serão gravados na F1L. **Ex: 14000+25200 = 39200**

**![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-17_18-45-20.png?version=1&modificationDate=1555537520407&api=v2)**

Para as operações Consumidor Final  os campos da tabelas F1J são utilizados para o calculo em destaque

![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-17_19-8-7.png?version=1&modificationDate=1555538887787&api=v2)

![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-17_19-10-32.png?version=1&modificationDate=1555539032450&api=v2)

 Memoria de Calculo:

3860 / 30 = 128,67 - Valor Unitário do ICMS Proprio

128,67 \* 8 = 1029,33 - Valor ICMS Proprio

93,47 \* 8 = 747,73  - Valor ICMS ST Outros Estados

**7.3 - COMPLEMENTO**

A complementação aplica-se às saídas , onde o ICMS mensal a complementar ou a ser restituído será o resultado da compensação das diferenças apuradas a menor ou a maior entre  
o valor da saída efetiva e o da base de cálculo presumida**.**

Na tabela F1I teremos o valor final a Ressarcimento, Restituição e Complemento.

![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-17_18-25-11.png?version=1&modificationDate=1555536312170&api=v2)

Esse valores serão visualizados na rotina FISA230

![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-17_18-38-36.png?version=1&modificationDate=1555537116817&api=v2)

## **08.** **RELATÓRIO DE CONFERENCIA**

Para fins de conferência dos valores apurados, é possível extrair, em formato de planilha, um relatório detalhando cada movimentação do produto no período selecionado.

![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-18_13-24-51.png?version=1&modificationDate=1555604692060&api=v2)

Parâmetros para geração do relatório:

**Mês/Ano Ref. ?**- Informe o Mês/Ano de Referencia inicial para seleção dos registros.

**Produto De** ?- Informe o Produto inicial para seleção dos registros.

**Produto Até** ?- Informe o Produto final para seleção dos registros.

**Tipo de Impressão ?Movimento** - Informe se o relatório será impresso:

1. Por **Produto**: A impressão será agrupada por produto.
2. Por **Movimento**: A impressão será com todos os movimentos utilizados na apuração.

Por Produto:

![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-18_13-31-32.png?version=1&modificationDate=1555605093083&api=v2)

Por Movimento:

![](http://tdn.totvs.com/download/attachments/484701377/image2019-4-18_13-35-39.png?version=1&modificationDate=1555605339977&api=v2)

Link: <http://tdn.totvs.com/pages/viewpage.action?pageId=484701377>
