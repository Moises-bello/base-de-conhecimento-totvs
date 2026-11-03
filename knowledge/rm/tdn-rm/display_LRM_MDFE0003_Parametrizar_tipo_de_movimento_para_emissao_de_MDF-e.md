---
content_hash: 8e0e54c43e712f55f764728752d8080d3f6dd74e3198ffe989516e05fc5d6151
fetched_at: '2026-06-29T00:08:13.854357+00:00'
page_id: '244428640'
product: rm
source: tdn-rm
title: MDFE0003_Parametrizar_tipo_de_movimento_para_emissao_de_MDF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/MDFE0003_Parametrizar_tipo_de_movimento_para_emissao_de_MDF-e
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | MDF-e - Manifesto Eletrônico de Documentos Fiscais |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | Parametrizar o tipo de movimento para emissão de MDF-e |
| **Passo a passo:** | **Introdução:**  Este documento tem como objetivo orientar os parâmetros específicos do movimento para correta emissão de MDF-e, caso deseje criar um novo tipo de movimento entre em contato com o suporte do RM Nucleus e após a criação siga este Como Fazer.  **Procedimentos:**  Acesse o RM Nucleus no seguinte menu: Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento |Outras Movimentações/Vendas (dependendo da classificação do tipo movimento desejado) | Selecione o Tipo de movimento e clique em Parametrizar  **Observação: Para emissão de MDF-e  é obrigatório que o código do tipo de movimento seja iniciado por 2.2.xx**  **Etapa Mov – Identificação:**A máscara do número com 9 dígitos    **Etapa Mov - Emitente / Destinatário 1/2:**Campos "Emitente" e "Destinatário"  têm  que ser iguais a empresa.    **Etapa Mov - Datas 1/2:** Campo "Edição da Data de Emissão" deve estar como edita ou mostra.  **Etapa Mov - Transporte 2/3:**  Habilitar campo "Tipo de Frete" ;  Marcar os "flags" dos campos "Editar dados de Cálculo do Frete da Mercadoria" e "Editar Dados da Placa do Veículo;    **Mov – Transporte 3/3:** Marcar os "Flags " dos campos "Editar Peso Bruto" e "Editar Peso Liquido".  **Item - Identificação 1/2 :** Campo "Tipo dos Itens", selecionar entre serviços ou Ambos.  **Item - Preços 1/2:** Campo "Edição do Preço", selecionar Não edita.  **Estoque:** Não afeta os estoques tanto físico quanto financeiro.  **Integração:** **Não** possui integrações Financeiras e Fiscais (movimento não será escriturado). Contudo na etapa "Fis - Escrituração 1/2" deve ser informado no campo "Tipo de Documento de Escrituração" algum tipo de documento que utilize o **CODMODDOC** = 58. Para isso marque o "Flag" **Gerar Escrituração** | selecione o tipo de documento com **CODMODDOC** = 58 | desmarque o "Flag" **Gerar Escrituração.**  **Fis - Tributação - Item:** Não possui tributos.  **Fis - Tributação - Movimento:** Não possui tributos.  **Fis - Conhecimento de Transporte (etapa NOVA):**  Campo "Tipo de Operação do Conhecimento de de Transporte": Definir como "Emitir MDF-e".  Campo "Modal": Definir a modalidade que será utilizada.  Campo "DAMDFE": informar o relatório default para impressão do DAMDFE (o relatório esta disponível na MDI | Botão TOTVS By You (lado direito da tela) | preencher o campo "Localizar Recurso" com a informação "DAMDFE" | **não** clicar no icone da "Lupa" | Clicar no icone do "By You" na parte inferior da tela). |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
