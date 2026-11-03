---
content_hash: b480e387444f6b054a58b8e973a2e969c0e0690e448102e97ccb37ff1fd37a1e
fetched_at: '2026-06-29T00:11:11.395417+00:00'
page_id: '64652212'
product: rm
source: tdn-rm
title: NF-e - Complementar
type: documentation
url: https://tdn.totvs.com/display/LRM/NF-e+-+Complementar
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***a partir 11.40* |
| **Processo** | **:** | NF-e Complementar |
| **Subprocesso** | **:** | NF-e Complementar |
| **Data da publicação** | **:** | 03/07/2013 |

**Introdução**

 Este Documento auxilia a criação de um movimento básico para complementar impostos de uma NF-e no sistema. Qualquer NF-e complementar deve ser emitida de acordo com a legislação vigente mesmo que esteja em desacordo com este documento.

**Criando uma NF-e Complementar**

1. 1. Parametrize um movimento de NF-e normalmente (caso seja NF-e de entrada siga os passo da FAQ  “Como Fazer - parametrizar movimentos de entrada para NF-e.pdf”);
   2. Acesse os parâmetros do movimento em: Opções | Parâmetros | RMNucleus | selecione onde o tipo de movimento esta inserido (compras, vendas, outras movimentações);

3. Habilitar nos parâmetros do Tipo de Movimento o parâmetro “Usar Cópia de Movimento por referência”, na etapa “Mov – Outros Dados”. O motivo da referencia deve ser  “6 – Complementar/Retificadora”;

4. Na etapa “Item – Preços” marque a opção “Aceitar Preço Zero”;

5. Acesse os Menu Cadastros | Produtos e Serviços e Cadastre um Produto Genérico para complementar o Imposto.

6. Entre no cadastro da natureza de operação (CFOP) em Cadastros | Tabelas de tributação | Natureza de operação | edite a natureza a ser utilizada | aba Tributação ICMS/IPI | edite a regra de ICMS | na aba identificação o tipo de tributação tem que ser “Outros” | na aba Outros dados marque o flag Operação complementar com o tipo de ICMS a ser complementado | salve as configurações.

7. Entre no tipo de movimento criado para complemento (Movimentos | selecione o tipo de movimento | preencha o filtro com o movimento complementar), gere um movimento por referencia através do menu Processos | "assistente de copia por referencia“.

Preencha o filtro para referenciar ao movimento original:

OBS: Os itens não serão copiados você deverá utilizar o item cadastrado anteriormente na etapa 5.

8. Preencha apenas a quantidade 1 e os valores que serão complementados.

Após a realização do passo a passo proceda com o envio da NF-e Normalmente.

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica);
