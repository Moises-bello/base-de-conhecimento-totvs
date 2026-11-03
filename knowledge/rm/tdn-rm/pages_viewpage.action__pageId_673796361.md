---
content_hash: 348cc12f980e562af6998af7cbb9dbea2496fdc8a66241f3d09d604a775c3f62
fetched_at: '2026-06-29T00:11:16.557913+00:00'
page_id: '673796361'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Utilitários - Backup/Restore Aluguel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=673796361
version: 20
---

Essa funcionalidade permite realizar o backup de um contrato de Locação, e  realizar a restauração deste backup em uma base de homologação.

Para acessá-la vá em: TCGI | Utilitários | Tarefas Venda | Backup e Restore, selecionando a opção Aluguel.

Versão de liberação: 12.1.32.262

---

xxxx1- Backup |

Para realizar o backup dos contratos de Locação, selecione a opção Backup | Aluguel;

Em Seguida Informe:

* a coligada origem;
* contrato de Locação (caso não seja informado o arquivo será gerado com todos os contratos da coligada informada);
* mascarar dados do Cliente (informações referentes a nomes serão substituídas por caracteres especiais);
* selecionar o caminho onde o backup será salvo

Execute o processo.  

2- Restore |

Para realizar o restore da base, selecione a opção: Aluguel:

Em seguida informe:

* a coligada de destino que serão armazenados os dados;
* a conta caixa que irá receber os dados da baixa;
* selecionar o caminho onde o backup está salvo; (Só permite restaurar um arquivo na pasta)

**\*\*\*\*\*\*\*Não realizar o restore em base de produção, pois os dados das tabelas do TCGI de Alugueis e Financeiro serão sobrepostos\*\*\*\*\*\*\*\*\***

**Para realizar o restore utilize uma base de homologação ou uma base eficaz na versão do cliente.**

**Se for a base eficaz, procure utilizar uma base por cliente, pois os parâmetros, componentes e diversos dados serão sobrepostos com o último restore realizado.**

3- De/Para Restore

Para detectar o De/Para das chaves dos registros do TCGI e Financeiro, selecione a opção De/Para Restore:

Utilize o Identificador Origem de Dados gerado no processo de restore e o nome do campo da tabela que deseja saber.
