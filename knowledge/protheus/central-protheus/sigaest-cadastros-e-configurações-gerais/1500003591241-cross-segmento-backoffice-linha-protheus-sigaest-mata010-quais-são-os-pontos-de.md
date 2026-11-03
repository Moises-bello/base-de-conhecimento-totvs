---
article_id: 1500003591241
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 64363900cc50a20e5dae3c0a11e4219d3521bb5e43e1dc5c09706a6eef2241c1
fetched_at: '2026-06-28T22:39:09.532134+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Quais são
  os Pontos de Entrada da rotina de Cadastro de Produtos?
type: support-article
updated_at: '2025-03-12T12:26:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003591241-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Quais-s%C3%A3o-os-Pontos-de-Entrada-da-rotina-de-Cadastro-de-Produtos
---

**Dúvida**Quais são os Pontos de Entrada da rotina  MATA010 - Cadastro de Produtos?

MT010MEM ,MA010FIL ,M010FILB ,MT010COR ,MA010BUT ,MT010VCP ,MT010INC ,MT010CAN ,MT010ALT ,A010TOK ,MT010VLD ,MTA010NC ,M010B5CP ,MT010BRW ,A010BPE ,MTA010NC ,MT010JIN ,MT010EAI ,MATI010.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Veja abaixo os Pontos de Entradas relacionados à rotina MATA010 - Cadastro de Produtos:

|  |  |  |
| --- | --- | --- |
| **Ponto de Entrada:** | **Título:** | **Descrição:** |
| **[MT010MEM](https://tdn.totvs.com/display/public/PROT/MT010MEM+-+Vetor+dos+campos+virtuais+criados)** | Vetor dos campos virtuais criados | Este ponto de entrada permite ao usuário que monte um vetor contendo a relação dos campos virtuais do tipo MEMO que ele criou. |
| **[MA010FIL](https://tdn.totvs.com/display/public/PROT/MA010FIL+-+Adiciona+filtro+para+o+registro+do+cadastro+de+produtos)** | Adiciona filtro para registro do cadastro de produtos | LOCALIZAÇÃO: Function MATA010 - Função principal do programa de inclusão, alteração e exclusão de Produtos. |
| **[M010FILB](https://tdn.totvs.com/pages/releaseview.action?pageId=651920932)** | Cadastro de Produtos | Este ponto de entrada tem como objetivo permitir que o usuário filtre os dados a serem exibidos. |
| **[MT010COR](https://tdn.totvs.com/display/public/PROT/MT010COR+-+Legenda+na+rotina+Cadastro+de+Produtos)** | Legenda na rotina de Cadastro de Produtos | P.E para adicionar legenda de cores na tela Cadastro de Produtos |
| **[MA010BUT](https://tdn.totvs.com/pages/releaseview.action?pageId=6087592)** | Inclusão de Botões de usuário no Cadastro de Produtos | P.E para inclusão de botões do usuário na barra de ferramentas do cadastro de Produtos. |
| [**MT010VCP**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087912) | Visualização do Cadastro de Produtos | Ponto de Entrada com objetivo de informar os campos da tabela SB1 que serão utilizados na visualização do cadastro de produtos. |
| [**MT010INC**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087685) | Grava arquivos e campos do usuário | Ponto de Entrada para complementar a inclusão no cadastro do Produto. |
| [**MT010CAN**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087683) | Executa customizações conforme retorno | Este ponto está localizado nas funções A010Inclui (Inclusão do Produto), A010Altera (Alteração do Produto) e A010Deleta (Deleção do Produto). |
| [**MT010ALT**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087681) | Grava/Altera campos de usuário | Ponto de Entrada para complementar a alteração no cadastro do Produto. |
| **[A010TOK](https://tdn.totvs.com/pages/releaseview.action?pageId=235596878)** | Validação para inclusão ou alteração do produto | LOCALIZAÇÃO : Function A010TudoOK - Função de Validação para inclusão ou alteração do Produto. |
| [**MT010VLD**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087930) | Valida se a cópia do produto está apta para utilização | Localização: Está localizado na função A010Copia. Quando: É chamado no inicio da função da copia do produto. Finalidade: Verifica se a copia do produto está apta para utilização. |
| [**MTA010NC**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087788) | Relaciona campos que não devem ser copiados na inclusão | LOCALIZAÇÃO : Function A010LEREG - Função chamada na inclusão do Produto, quando ativado o botão Cópia. |
| [**M010B5CP**](https://tdn.totvs.com/pages/releaseview.action?pageId=454828045) | Manipulação dos campos do Complemento de Produtos | Ponto de Entrada que permite limpar o conteúdo dos campos de complemento de produto(SB5) quando executada a função de cópia de produto para o cadastro de produtos que atualiza o complemento. |
| [**MT010BRW**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087682) | Adiciona mais opções de menu na Mbrowse | LOCALIZAÇÃO : Function MATA010 - Função principal do programa de inclusão, alteração e exclusão de Produtos. |
| [**A010BPE**](https://tdn.totvs.com/pages/releaseview.action?pageId=268813613) | Tratamentos de validações de conteúdo de caracteres especiais no código do produto | O Ponto de Entrada A010BPE deve ser utilizado para tratamentos de validações de conteúdo de caracteres especiais no código do produto ou descrição, ou validações especificas. |
| [**MTA010NC**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087788) | Relaciona campos que não devem ser copiados na inclusão | LOCALIZAÇÃO : Function A010LEREG - Função chamada na inclusão do Produto, quando ativado o botão Cópia. |
| [**MT010JIN**](https://tdn.totvs.com/pages/releaseview.action?pageId=602830159)  **(MATI010 Produto (Integração)** | Inclusão de campos customizados ou padrões na mensagem única de produtos | O Ponto de Entrada MT010JIN permite adicionar a mensagem única de produtos campos customizados ou padrões |
| [**MT010EAI**](https://tdn.totvs.com/pages/releaseview.action?pageId=270097205)  **(MATI010 Produto (Integração)** | Acrescenta/complementa campos e informações não tratadas na tabela | O Ponto de Entrada é verificado na função V2000 ou V1000 antes de executar a execauto do MATA010 |

**Mais exemplos e detalhes de utilização de pontos de entrada no cadastro de produto:**

<https://tdn.totvs.com/display/public/PROT/Produtos+-+MATA010+-+Estoque+-+P12>

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
