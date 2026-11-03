---
article_id: 360057066653
category: Escrita Fiscal - Error.log
content_hash: 94544e20736b872cce65701538bcf77fbc449192ca646e08a57fd93658fd5a11
fetched_at: '2026-06-28T22:39:32.934961+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: MP - FIS - Histórico de Operações Fiscais
type: support-article
updated_at: '2021-04-28T15:43:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057066653-MP-FIS-Hist%C3%B3rico-de-Opera%C3%A7%C3%B5es-Fiscais
---

**Dúvida**Como habilitar o tratamento do Histórico de Operações Fiscais?  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Habilitar o tratamento do Histórico de Operações Fiscais.

No **Configurador (SIGACFG)** acesse **Ambiente/ Cadastros/ Parâmetros** e verifique os parâmetros a seguir:

|  |  |
| --- | --- |
| **Itens/Pastas** | **Descrição** |
| **Nome** | MV\_HISTFIS |
| **Tipo** | Lógico |
| **Descrição** | Histórico das Operações Fiscais |
| **Valor Padrão** | .F. |

# **Procedimentos de Utilização**

* Habilitar o parâmetro MV\_HISTFIS (.T.) para ativar a gravação e o tratamento do Histórico de Operações Fiscais.

|  |  |  |
| --- | --- | --- |
| **Tabela Original** | **Tabela Histórico** | **Nome** |
| SF4 | SS0 | Tipos de Entrada e Saída |
| SF7 | SS1 | Exceções fiscais |
| SA1 | SS2 | Clientes |
| SA2 | SS3 | Fornecedores |
| SB1 | SS4 | Descrição Genérica do Produto |
| SB5 | SS5 | Complemento de produto |
| SBZ | SS6 | Indicadores de Produto |
| SED | SS7 | Natureza Financeira |
| SFB | SS8 | Impostos Variáveis |

Abaixo procedimentos para criação do campo S0\_BICMCMP de forma manual:

**Campo:**

**Campo**: S0\_BICMCMP  
**Tipo**: Caracter   
**Tamanho:** 1  
**Decimal:** 0  
**Formato:** @!  
**Contexto:** 1 Real   
**Propriedade:** Alterar   
**Totvs PDV:** Sim   
**Modal:** Não   
**Grupo de Campos:** Não Tem Grupo de Campos

**Informações:**

**Título:** Red.BCIC Com  
**Título Espanhol:** Red.BCIC Com  
**Titulo Inglês:** Com BCIC   
**Descrição:** Reduz ICMS Complementar   
**Desc. Espanhol:** Reduc ICMS Complementario  
**Desc Inglês:** Reduces Complementary ICM  
**Help:** Informar se a base do ICMS Complementardeve ser reduzida como o ICMS Normal

**Opções:**

**Lista de Opções:** 1=Sim;2=Não.  
**Lista Espanhol:** 1=Si;2=No  
**Lista Inglês:** 1=Yes; 2=No

Uso, marcar como:

Usado   
Browse

Link:

https://tdn.totvs.com/display/public/PROT/FIS0002\_Historico\_de\_Operacoes\_Fiscais
