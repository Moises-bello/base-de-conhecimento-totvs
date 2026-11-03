---
content_hash: 73231511a66bca737380d7c25118b580f8f06ca785fc895e4056db63398374c3
fetched_at: '2026-06-29T00:06:26.483424+00:00'
page_id: '225267817'
product: rm
source: tdn-rm
title: DT_PCREQ-7797_Integ. BackOffice RM x SigaLoja - RM - Produto
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_PCREQ-7797_Integ.+BackOffice+RM+x+SigaLoja+-+RM+-+Produto
version: 119
---

# Integ. BackOffice RM x SigaLoja - RM - Produto

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  |  | | --- | --- | --- | | **Rotina** | **Nome Técnico** | **Mensagem Única TOTVS** | | Produto | EstPrdAction. | Item (3.004) |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Unidades de Medida | EstUndAction. | | Local de Estoque | EstLocAction | | Tributação Cupom Fiscal | MovTributacaoECFAction | | Configuração da Integração | ConConfiguraIntegracaoAction | | Integrações de Mensagem Única. | ConIntegracaoAction | |
| **Cadastros Iniciais:** | Cadastrar Unidade de Medida.  Cadastrar Local de Estoque.  Cadastrar Tributação de Cupom Fiscal. |
| **Parâmetro(s):** | N/A. |
| **Ponto de Entrada:** | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Estoque, Compras e Faturamento \ Produto |
| **Chamados Relacionados** | N/A. |
| **Requisito (ISSUE):** | PCREQ-7797. |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL SERVER, ORACLE |
| **Tabelas Utilizadas:** | * TPRODUTO - Produtos Globais. * TPRODUTODEF - Dados dos Produtos Globais por Coligada * TPRDLOCINFO - Informações do Estoque * TPRDFIL - Filiais de Um Produto * TPRDCODIGO - Código Genérico de Produtos * TUND - Unidades de Medida * TTRIBUTACAOECF - Tributação ECF |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

Este requisito tem por objetivo possibilitar a integração do cadastro de Produto com o PDV PROTHEUS através do protocolo de Mensagem Única TOTVS.

Quando o Produto no RM estiver parametrizado para trabalhar com Controle de Nível de Máscara, serão integrados ao Protheus somente os Produtos de Último Nível.

Ao ativar a integração, não será permitido o cadastramento de produtos controlados por lote e série, devendo ser selecionada somente uma das opções.

**Envio de Preços**

O RM enviará na mensagem os preços de 1 a 5  do Produto, ficando a cargo do PDV Protheus a utilização destes ou de demais formas de precificação disponíveis no mesmo. Não haverá integração da Tabela de Preços da linha RM  ou da precificação no Protheus. O RM considerará como valor de venda o valor retornado na mensagem de Cupom Fiscal.

**Tributação ECF**

Esta informação será enviada na mensagem quando for informado a **Tributação de Cupom Fiscal** no cadastro de **Produto**. Com base no código de tributação informado no produto, o RM irá buscar as informações de **Código do Tributo, Tipo de Tributação** e **Alíquota** cadastrados na tabela Tributação ECF  e enviar estas informações ao Protheus.

Visto que os códigos dos tributos no Protheus obrigatoriamente seguem um padrão de nomenclatura, deve-se efetuar o cadastro destes tributos no RM respeitando o mesmo código utilizado no Protheus para viabilizar a integração de registros que utilizem estes tributos.  Os códigos dos tributos devem seguir a seguinte nomenclatura:

* **Tributado ICMS**: Sempre inicia com T + alíquota do produto + 00. Exemplo: 7% = T0700, 12% = T1200, 18% = T1800.
* **Tributado ISS:** Sempre inicia com I  + alíquota do produto + 00. Exemplo: 5% = I0500, 10% = I1000
* **Não Tributado:** código fixo N1.
* **Isento:** código fixo I1.
* **Substituição Tributária:** código fixo F1.

**Produto Global no RM**

Produtos globais no BackOffice RM não serão considerados globais no sistema de destino, sendo enviada uma mensagem de inclusão para cada empresa a qual o produto faz parte. Caso haja ao menos uma mensagem enviada com sucesso ao PDV (SigaLoja), mesmo havendo erro nas mensagens referentes ao produto para as outras coligadas, não será apresentada mensagem de erro e a alteração/inclusão não será desfeita.

## Procedimento para Configuração

**CONFIGURAÇÃO DE INTEGRAÇÃO**

1. No módulo de **Integração**, acesse **Ferramentas/Configurar**. Informe **Usuário/Senha** do banco de dados, teste a conexão. Avance até a **Projetos de Integração** e selecione o item**BackOffice RM x PDV Protheus (Novo Modelo)** e execute o processo.
2. Acesse **Integração/Mensagem Única/Integrações**, selecione a opção de filtro. Na visão de **Integrações** editar a integração de **Identificador 1016** e verifique se está informado a **URL WebService** do Protheus.
3. Verifique em **Anexos/Mapeamento de Entidades** se a mensagem **Item versão 3.004** está mapeada.

**IMPORTAÇÃO DE FÓRMULA VISUAL**

1. Acesse **Gestão\Fórmula Visual\Fórmula visual\Processo\Importação de Fórmula Visual.** Clique em **Adicionar Objetos** e localize o arquivo a ser importado que encontra-se disponível na pasta **Fórmulas Visuais**, interna à pasta **ObjetosGerencias** no ambiente instalado do sistema (**../CorporeRM/ObjetosGerencias/Fórmulas Visuais**). Deverá ser marcado o parâmetro **Importar Gatilho**.
2. Visando oferecer facilidade para clientes que já possuam a base de dados com Produtos foi disponibilizado também uma Fórmula Visual para sincronização dos registros existentes, que é responsável por filtrar somente os registros não enviados ou desatualizados no Protheus. Esta fórmula visual pode ser utilizada para carga inicial, novo sincronismo em casos onde o gatilho tenha sido desabilitado ou como forma de integração assíncrona.

## Procedimento para Utilização

1. No módulo ****Gestão de Estoque, Compras e Faturament******o**, acesse **Cadastros/Produtos** e selecione um filtro.

O sistema apresenta a janela de produtos cadastrados.

2. Na visão clique em **Incluir**.

O sistema apresenta a janela de edição Produto. Informe os dados **Código do Produto**, se é de **Último Nível,** **Inativo**, **Nome fantasia, Tipo (Produto ou Serviço).**

3. Na **Pasta Detalhes:**

* + **Pasta Descrição**informe a **Descrição do Produto;**
  + **Pasta Características:**informe o **Peso Bruto**e **Peso Líquido**
  + **Pasta Outros Dados:** informe a **Referência**, **Tributação Cupom Fiscal**.

4. Na **Pasta Preço:** informe os **Preços Selecionados** (Moeda, Data-Base, e Preço).

5. Na **Pasta Controle d****e Estoque** informe se o produto é **Controlado por lote**, **Usa número de série, Unidade de Controle** e **Unidade de Venda.**

6. Na pasta **Pasta** **Custos** informe o **Custo Médio / Valor**, **Custo unitário / Valor**

7. Confira os dados e confirme.

divs
