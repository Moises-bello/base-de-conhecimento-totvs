---
content_hash: 2b5c2a1280e1b7ebd303d7410d89ee1269231c27e66de3a5f8a02482aa0e9299
fetched_at: '2026-06-29T00:05:57.212915+00:00'
page_id: '165283407'
product: rm
source: tdn-rm
title: MDF-e - Parametrizar tipo de movimento para emissão de MDF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=165283407
version: 4
---

# PUBLICADO

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | MDF-e                        **Versão:***a partir 11.52* |
| **Processo** | **:** | Parametrizar o tipo de movimento para emissão de MDF-e |
| **Subprocesso** | **:** | Parametrizar o tipo de movimento para emissão de MDF-e |
| **Data da publicação** | **:** | 03/10/2014 |

**Introdução:**

Este documento tem como objetivo orientar os parâmetros específicos do movimento para correta emissão de MDF-e, caso deseje criar um novo tipo de movimento entre em contato com o suporte do RM Nucleus e após a criação siga este Como Fazer.

**Procedimentos:** 

Acesse o RM Nucleus no seguinte menu: Opções | Parâmetros | RMNucleus | Selecione o Tipo de movimento e clique em Parametrizar. Para selecionar o tipo de movimento deve se atentar a classificação do mesmo (Outras movimentações, vendas e etc).

MDI: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento.

**Observação: Para emissão de MDF-e  é obrigatório que o código do tipo de movimento seja iniciado por 2.2.xx**

**Etapa Mov – Identificação:** A máscara do número com 9 dígitos

**Etapa Mov - Emitente / Destinatário 1/2:** Campos "Emitente" e "Destinatário" têm que ser iguais a empresa.

**Etapa Mov - Datas 1/2:** Campo "Edição da Data de Emissão" deve estar como edita ou mostra.

**Etapa Mov - Transporte 2/3:**

  Habilitar campo "Tipo de Frete" ;

  Marcar os "flags" dos campos "Editar dados de Cálculo do Frete da Mercadoria" e "Editar Dados da Placa do Veículo;

**Mov – Transporte 3/3:** Marcar os "Flags " dos campos "Editar Peso Bruto" e "Editar Peso Liquido".

**Item - Identificação 1/2 :** Campo "Tipo dos Itens", selecionar entre serviços ou Ambos.

**Item - Preços 1/2:** Campo "Edição do Preço", selecionar Não edita.

**Estoque:** Não afeta os estoques tanto físico quanto financeiro.

**Integração:** **Não** possui integrações Financeiras e Fiscais (movimento não será escriturado). Contudo na etapa "Fis - Escrituração 1/2" deve ser informado no campo "Tipo de Documento de Escrituração" algum tipo de documento que utilize o **CODMODDOC** = 58. Para isso marque o "Flag" **Gerar Escrituração** | selecione o tipo de documento com **CODMODDOC** = 58 | desmarque o "Flag" **Gerar Escrituração.**

**Fis - Tributação - Item:** Não possui tributos.

**Fis - Tributação - Movimento:** Não possui tributos.

**Fis - Conhecimento de Transporte (etapa NOVA):**

Campo "Tipo de Operação do Conhecimento de de Transporte": Definir como "Emitir MDF-e".

Campo "Modal": Definir a modalidade que será utilizada.

Campo "DAMDFE": informar o relatório default para impressão do DAMDFE (o relatório esta disponível na MDI | Botão TOTVS By You (lado direito da tela) | preencher o campo "Localizar Recurso" com a informação "DAMDFE" | **não** clicar no icone da "Lupa" | Clicar no icone do "By You" na parte inferior da tela).

Campo "Tipo do Emitente": definir se é "Transportador de carga propria" (será associado NF-es) ou "Prestador de serviço de transportes" (será associado CT-es).

**Para maiores informações:**

 **[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
