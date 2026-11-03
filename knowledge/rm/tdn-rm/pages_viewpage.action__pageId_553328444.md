---
content_hash: 9e67e58f77c9d90837d6351e302611914173db5f8ab266bee667cca988031ba5
fetched_at: '2026-06-29T00:10:44.535266+00:00'
page_id: '553328444'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Utilitários - Backup/Restore de Venda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553328444
version: 16
---

Essa funcionalidade permite realizar o backup de uma Coligada, Empreendimento ou Venda, e  realizar a restauração deste backup em uma base de homologação.

Para acessá-la vá em: TCGI | Utilitários | Tarefas Venda | Backup e Restore.

Versão de liberação: 12.1.28.131

CardstrueContrato1- Backup |

Para realizar o backup da base, informe:

* a coligada origem;
* o empreendimento ou o número da venda;
* copiar todos os históricos do TCGI e Financeiro;  (Copiar somente se houver necessidade de avaliar o histórico ou a Ficha Financeira)
* copiar os aditivos da base;
* copiar os documentos do anexo da venda;
* copiar os parâmetros globais e da coligada  de origem do TCGI e Financeiro;
* mascar os dados do Cliente e Fornecedor no backup;
* selecionar o caminho onde o backup será salvo

Execute o processo.  

Global2- Restore |

Para realizar o restore da base, informe:

* a coligada de destino que serão armazenados os dados;
* a conta caixa que irá receber os dados da baixa;
* se deseja importar todos os históricos do TCGI e Financeiro; (Importar somente se houver necessidade de avaliar o histórico ou a ficha financeira)
* se deseja importar os documentos do anexo da venda;
* se deseja importar os parâmetros globais e da coligada do backup do TCGI e Financeiro; (se marcar esta opção, o processo irá sobrepor os parâmetros na coligada destino e global)
* recalcular os campos do lançamento financeiro "Número do Documento" e "Histórico";
* Manter o código da chave primária da base do cliente.  Marcado, facilita a elaboração do script para ajustar a base  de dados do cliente, pois o código é o mesmo.
  + Atenção!!! Com este parâmetro marcado, pode dar erro, de chave primária, na execução de algum processo. Pois o código pode estar em uso na base de dados .
* selecionar o caminho onde o backup está salvo; (Só permite restaurar um arquivo na pasta)

**\*\*\*\*\*\*\*Não realizar o restore em base de produção, pois os dados das tabelas do TCGI de vendas e Financeiro serão sobrepostos\*\*\*\*\*\*\*\*\***

**Para realizar o restore utilize uma base de homologação ou uma base eficaz na versão do cliente.**

**Se for a base eficaz, procure utilizar uma base por cliente, pois os parâmetros, componentes e diversos dados serão sobrepostos com o último restore realizado.**

Após a execução do processo de restore será gerado um identificado de origem de dados no log do processo para identificar os De/Para de todas as chaves;

**Para consultar os De/Para dos dados restaurados, favor utilizar o Identificador de Origem [1] e os dados dos cliente na visão De/Para Restore.**

* **Após a execução do processo de restore com sucesso!**  
  **Reiniciar o Host para que toda a parametrização restaurada vinda do backup do cliente, seja carregado de acordo com o que foi restaurado.**

Agendamento3- De/Para Restore

Para descobrir o De/Para das chaves dos registros do TCGI e Financeiro, utilize o Identificador Origem de Dados  gerando no processo de restore e o nome do campo da tabela que deseja descobrir.

O 'Código Anterior da Chave' é o código do backup do cliente e o 'Código Novo da Chave' é a nova chave gerada na base de restore.
