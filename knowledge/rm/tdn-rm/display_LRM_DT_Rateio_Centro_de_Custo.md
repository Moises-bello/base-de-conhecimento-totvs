---
content_hash: 07c3535ea6b2206d97f63cc9b3d214db386977e6a5145bdebbd0d6339ab3df27
fetched_at: '2026-06-29T00:06:06.293405+00:00'
page_id: '201729727'
product: rm
source: tdn-rm
title: DT_Rateio_Centro_de_Custo
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Rateio_Centro_de_Custo
version: 6
---

# RATEIO DO CENTRO DE CUSTO

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Projetos* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Gestão Organizacional* | *Rateio do centro de custo* | |
| **Versões/Release:** | *12.1.8* |

## Descrição

O sistema possibilita o usuário ratear centro de custos para funcionário/vaga nas requisições de substituição, alteração de dados funcionais, transferências, transferências com alteração de dados funcionais, exceto requisição de aumento de quadro e requisição de transferência em lote. 

## Procedimento para Utilização

Para utilizar rateios por centros de custos nas requisições, será necessário marcar o parâmetro **Habilitar o rateio de centros de custos em requisições** localizado em Configurações / Requisições / Requisições 2. Iniciamos com o processo de parametrização. Esse parâmetro ativará ou desativará o recurso mencionado dentro das requisições citadas

\*O parâmetro **Rateio de centro de custos do funcionário** tem que estar ativado para que as requisições habilitem os recursos. Caso contrário, os recursos serão desabilitados.

**Rotinas:** Planejamento e Captação / Requisições  
 Desenvolvimento / Requisições  
 Gestão Organizacional / Requisições

Nas requisições afetadas por esta especificação, foi criada uma nova aba que permitirá ao solicitante/aprovador propor um rateio de centro de custos para o funcionário/vaga relacionado à requisição. Após criar uma requisição, será possível editar o rateio somente quando ela estiver com status “Pendente”. Após a requisição estar “Em andamento”, a edição poderá ser feita através da inclusão de pareceres.

O sistema mostrará a visão onde o usuário poderá incluir o rateio.  
 Após o usuário preencher todos os campos obrigatórios, o sistema carregará automaticamente o rateio atual do funcionário.

O usuário informará ou alterará o rateio conforme sua necessidade. O rateio sempre deverá totalizar 100%. Depois de salvar a requisição, o sistema irá validar e gravar as informações no banco de dados.

No portal do RH Online, nas requisições, a funcionalidade “Propor rateio” está disponível nas mesmas requisições citadas anteriormente neste documento.  
Acesse o Painel de Controle de Requisições, escolha qual requisição deseja abrir ou analisar. Caso queira analisar uma requisição, será aberta a tela para inclusão de parecer, onde será possível editar o rateio. Caso queira abrir uma nova requisição, será exibida a tela para criar a nova requisição.  
 Para visualizar ou editar o rateio, clique no botão “Rateio de C. Custos”.

Para incluir um rateio, clique no *link* “Incluir novo rateio”; Para editar um rateio, clique na descrição do centro de custos a ser alterado, que estará numlink.

Ao salvar a requisição ou avançar a etapa, o sistema valida e grava as informações no banco de dados.
