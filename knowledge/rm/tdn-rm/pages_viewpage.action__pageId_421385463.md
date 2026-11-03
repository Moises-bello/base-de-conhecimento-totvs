---
content_hash: 8f10f76d1292496e4e03f4e91c97db365a0884378d1862ce70fa6207ecabb338
fetched_at: '2026-06-29T00:09:16.133002+00:00'
page_id: '421385463'
product: rm
source: tdn-rm
title: Importação de Ciclos de Transporte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385463
version: 3
---

---

O processo de importação de Ciclos de Transporte é realizado a partir de um WebService disponibilizado no TOTVS Obras e Projetos. O coletor móvel inicia o processo e envia as seguintes informações: - Coligada; - Projeto; - Equipamento (código, ID ou código de barras); - Ciclo de transporte; - Data (data e hora/minuto/segundo); - Tipo (saída/entrada); - Usuário que apontou/registrou.  
 O WebService irá processar, formatar e retornar ao TOTVS Obras e Projetos todos os dados de apontamentos  do Ciclo de Transporte disponíveis no TOP em formato XML. Para realizar a sincronização dos dados do Coletor Móvel para o TOTVS Obras e Projetos o usuário inicia o processo de importação dos dados no coletor. O processo poderá ser iniciado pelo usuário ou por job agendado no coletor. O coletor móvel faz as validações (ciclos de transportes fechados), consolidadas informações, monta o XML e envia para o WebService. As rotinas no TOTVS Obras e Projetos são disparadas pelo WebService e validam usuário/senha de acordo com permissões (usuários de coletores móveis). Rotinas no ERP/TOP disparadas pelo WebService consolidam as informações interpretando-as (casando inicio/fim por equipamento) e as registrando em tabelas no ERP/TOP.

**Observação:**

* Após o final do processo e retorno das informações ao coletor móvel, será gerado um log da integração;
* Serão vários coletores que ora registrarão a entrada e outrora registrarão a saída em locais diferentes. Os registros retornados ao sistema conterão o campo data/hora e tipo preenchidos onde o tipo representará se o registro é uma saída (início/partida) ou entrada (fim/chegada) para que seja possível, posteriormente, efetuar o "casamento" das saídas e entradas para um dado equipamento.
