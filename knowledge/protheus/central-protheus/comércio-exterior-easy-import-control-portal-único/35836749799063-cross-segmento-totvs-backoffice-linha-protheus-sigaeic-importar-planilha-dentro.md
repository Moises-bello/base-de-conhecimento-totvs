---
article_id: 35836749799063
category: Comércio Exterior - Easy Import Control - Portal Único
content_hash: 0815116c9162bd162e843ede7d7ebda6c7f6f212ed04ec9f5011135f5f2eba46
fetched_at: '2026-06-28T22:39:40.295288+00:00'
product: protheus
section_id: 27387892471703
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Importar Planilha
  dentro do Catálogo de Produtos
type: support-article
updated_at: '2025-10-24T20:26:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35836749799063-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Importar-Planilha-dentro-do-Cat%C3%A1logo-de-Produtos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35836758476695) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
É possível a Importação de Planilhas dentro do Catálogo de Produtos (EICCP400) do SIGAEIC?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control - a partir da versão 12  
  
**Solução**  
Ação responsável para facilitar a Importação de dados para o Catálogo de Produtos. Esta funcionalidade permite que os usuários carreguem uma planilha ".xlsx" com Atributos e Vínculos entre Catálogos, Produtos, Fabricantes e Países de Origem.  
  
**Para realizar a importação da planilha, basta seguir os passos:**  
- Ao selecionar a opção Importar da Planilha, o sistema agora apresenta uma tela para que o usuário possa informar o arquivo na extensão ".xlsx". Antes de processar a planilha, o sistema valida o cabeçalho para garantir que esteja consistente, exibindo uma mensagem de erro caso haja inconsistências.

- Os dados são processados de acordo com as chaves: Filial e Código Chave da pasta "NCM XXXX.XX.XX', permitindo a atualização dos Catálogos de Produtos. Campos vazios na planilha resultarão na exclusão dos conteúdos previamente preenchidos nesses campos no sistema.

- Além disso, os dados das pastas "RELAÇÃO DE PRODUTOS" e "RELAÇÃO DE FABRICANTES" são carregados e vinculados aos Catálogos de Produtos. Os Catálogos de Produtos que recebem o ID e a versão pela planilha têm seu status atualizado para "Registrado Manualmente", enquanto aqueles que não recebem estas informações são configurados para "Pendente de Registro" ou "Pendente de Retificação", dependendo do caso.

- Durante o processamento, uma barra de progressão é exibida, e ao concluir, um grid com o resultado por catálogo é mostrado. Por fim, o arquivo importado é renomeado para \*.processado\*, indicando a finalização do processo. Caso o usuário desejar, é possível exportar os logs para uma planilha excel.  
  
**Saiba mais:**  
[**Catálogo de Produtos - EICCP400**](https://tdn.totvs.com/pages/releaseview.action?pageId=549491819)  
[**Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Catálogo de Produtos para tratativa da DUIMP.**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8423200910487-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Cat%C3%A1logo-de-Produtos-para-tratativa-da-DUIMP)  
[**EIC 001 - FAQ - Novo processo de Importação - Portal Único**](https://tdn.totvs.com/pages/releaseview.action?pageId=788602791)
