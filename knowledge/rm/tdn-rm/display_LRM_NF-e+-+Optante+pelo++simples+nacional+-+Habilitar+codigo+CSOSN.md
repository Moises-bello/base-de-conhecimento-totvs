---
content_hash: 9ef03803970ad1325f5fc747e2a05a4950afadb2b3ef623be6ff8f45c52415b2
fetched_at: '2026-06-29T00:11:25.600409+00:00'
page_id: '71336338'
product: rm
source: tdn-rm
title: NF-e - Optante pelo  simples nacional - Habilitar codigo CSOSN
type: documentation
url: https://tdn.totvs.com/display/LRM/NF-e+-+Optante+pelo++simples+nacional+-+Habilitar+codigo+CSOSN
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***a partir 11.40* |
| **Processo** | **:** | Optante pelo simples nacional - Habilitar código CSOSN |
| **Subprocesso** | **:** | Optante pelo simples nacional - Habilitar código CSOSN |
| **Data da publicação** | **:** | 22/07/2013 |

**I****ntrodução:**

Para Este documento tem como finalidade auxiliar na parametrização da filial quando optante pelo regime simplificado nacional e o preenchimento da Tag CSOSN (Código de Situação da Operação - Simples Nacional) 

**Filial:**

É necessário parametrizar a filial como optante pelo regime simplificado através do seguinte caminho: Cadastros | Filial | selecione a filial | clique em editar | Anexos | Dados Fiscais | marque o flag Optante Regime Simplificado. Feito isso clique em salvar.

**Liber:**

É necessário habilitar o “campo opcional 3” do cadastro de CFOP através dos parâmetros do RM Liber.

Acesse  o  RM Líber  no  seguinte  menu:  Opções | Parâmetros | Gerais  Tabelas  | 03.03  - Escrituração | Etapa 10 – Natureza de Operação e habilite a opção “Usar Campos Opcionais”

**CFOP (Natureza de operação):**

O código CSOSN deverá ser informado no cadastro da CFOP obrigatoriamente no “Campo 3”.

Acesse: Cadastros | Natureza do Operação | Edite a natureza desejada | Aba Campos Opcionais.

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
