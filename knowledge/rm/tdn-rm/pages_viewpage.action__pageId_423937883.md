---
content_hash: 78aadfb77cecdc9a592d85b1d5f38e38fb20ebb54451c48082c8170ea79f1c93
fetched_at: '2026-06-29T00:09:24.078657+00:00'
page_id: '423937883'
product: rm
source: tdn-rm
title: Período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937883
version: 2
---

Utilize este recurso do sistema para cadastrar períodos do planejamento de produção.   
Os períodos do planejamento estão relacionados à quantidade de dias, semanas, quinzenas, meses, etc; que você utilizará para definir horizontes do planejamento mestre da produção.  
O planejamento mestre da produção utiliza os campos "Período" e "Duração" (preenchimento obrigatório) a partir desses períodos pré-cadastrados.  
***Atenção!***  Ao iniciar cadastros de períodos em uma base de dados vazia ou em uma nova coligada/filial, é necessária uma carga inicial dos períodos, sendo que, essa carga deve obedecer a seguinte regra na informação dos códigos dos períodos:

* Código 0 (zero): refere-se a períodos semanais.
* Código 1 (um): refere-se a períodos quinzenais.
* Código 2 (dois): refere-se a períodos mensais.

Informe o número de dias corridos que serão utilizados para cálculo do planejamento, importação de planejamento ou para serem utilizados no calendário do planejamento.  
**Exemplo**: 10 dias, 5 dias, 25 dias, etc.  
***Observações***: Ao criar um novo planejamento da produção, um novo cadastro de importação do planejamento ou calendário do planejamento (menu Planejamento), serão exibidos os cadastros existentes em forma de lookup, possibilitando a seleção dos períodos.   
A funcionalidade permite utilizar um período com qualquer quantidade de dias, flexibilizando o agrupamento de períodos diferenciados, como por exemplo, 5 dias, 10 dias, 25 dias.   
Não há uma referência de datas (balizador), os períodos customizados funcionam apenas na modalidade de dias corridos.   
Os demais modelos permanecem inalterados para compatibilidade com as planilhas existentes.
