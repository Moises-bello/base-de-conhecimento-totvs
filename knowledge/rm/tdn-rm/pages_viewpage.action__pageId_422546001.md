---
content_hash: c23e7c16e1406fde6597798197274fd707e24eb62ed78b7d207cb8f9fc08bd98
fetched_at: '2026-06-29T00:09:22.555532+00:00'
page_id: '422546001'
product: rm
source: tdn-rm
title: SEF II (Geração da Rotina)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546001
version: 5
---

**Geração da Rotina**   
 A geração de novas rotinas fiscais desenvolvidas pela linha RM é feita através da ferramenta Gerador de Saídas, que nas versões futuras possibilitará a customização da origem das informações geradas na rotina fiscal pelo próprio usuário. Até a presente versão somente o módulo de geração da rotina foi disponibilizada.  O processo é transparente para o usuário e a única mudança no modo de geração das rotinas é a importação do layout que é enviado em arquivo separado. A seguir serão mostrados os passos para a importação do layout e geração da rotina.  
 Após atualizar a biblioteca e o aplicativo siga os seguintes passos para importar o layout:  
    
 **Criação da Categoria do Layout**  
 Acesse o menu Utilitários | Gerador de Saídas  - Importação| Categoria do layout. Se for apresentada a tela de filtros crie um filtro para retornar todas as categorias ou simplesmente feche a tela.  
 Clique no botão NOVO e será aberta a tela para a inclusão da categoria.   
 Na guia Perfis da Categoria do Gerador de Saídas insira o perfil ao qual os usuários que terão permissão para gerar a rotina estão associados. Para isto clique no botão novo e na tela apresentada clique no lookup marcado na figura para ser exibida a lista de perfis existentes. Localize o perfil desejado atentando para o campo do código do sistema que neste caso é D – RM Liber. Um duplo clique selecionará o perfil.  Para finalizar clique no botão OK ou  SALVAR.    
    
 **Importação do Layout**  
 Acesse o menu Utilitários | Gerador de Saídas – Importação | Layout. Se for aberta uma tela de filtros crie um filtro para retornar todos os registros ou simplesmente feche-a.  
 Clique no botão PROCESSOS | IMPORTAR LAYOUT.   
 Na tela que se abrirá clique no botão Adicionar Objetos e aponte para o arquivo de layout recebido e em seguida dê um duplo clique no mesmo.  
 Selecione o layout importado e escolha a opção de gravação para as coligadas. Na guia parâmetros informe a categoria criada anteriormente e clique no botão executar para finalizar a importação.  
 Sendo apresentada a tela que você obteve êxito na importação do layout, feche as telas de Categorias e de Layouts.  
    
**Gerando a Rotina**  
 Acesse o menu Rotinas Legais | Federais | Escolha a rotina desejada  
 Na tela que será apresentada informe o código do layout que acabou de importar e clique no botão avançar.  
 O arquivo da rotina será gravado na pasta indicada no Diretório de Destino.  
 Clique em avançar para ser apresentada a tela de parâmetros da rotina. Preencha todos de acordo com as  informações que deseja gerar para o arquivo e clique em executar para que seja concluído o processo e o arquivo gerado.
