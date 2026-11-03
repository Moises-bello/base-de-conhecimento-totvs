---
content_hash: 8ea2a882c7b0175ab0907b0c62330cebe36f6cb9ad976cbe124e74c9dd77e9f1
fetched_at: '2026-06-29T00:10:10.537326+00:00'
page_id: '452719868'
product: rm
source: tdn-rm
title: Copiar Parâmetros Entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719868
version: 4
---

O processo de "Copiar Parâmetros Entre Coligadas" foi criado para facilitar o processo de parametrização de múltiplas coligadas. Após parametrizar a primeira coligada, é possível executar o processo para copiar as informações para as outras coligadas selecionadas.  
**Copiar Parâmetros Entre Coligadas:**  
Nesta tela, selecione quais serão os parâmetros que deseja realizar a cópia, estão quase todos os parâmetros do parametrizador do Folha de Pagamento exceto dois são eles o "06.01.01 - Configuração de Competência" e "06.02.02 - Gestão Contábil".  
Caso o Parâmetro já exista na coligada destino, existe duas opções são elas:

* Sobrescrever: O intuito deste processo é substituir ou incluir.

Ex: Caso na Coligada Destino o parâmetro "Usa mês comercial na admissão" esteja desmarcado e na coligada de origem marcado, com o processo selecionado ele será marcado na coligada destino.  
Ex: O mesmo acontece com fórmulas e eventos caso a formula ou o evento exista na coligada destino e não esteja informado em algum campo referente a fórmula ou evento, no processo será incluído está formula no parâmetro.  
**Obs: Antes de executar a cópia de parâmetros, é necessário verificar que os eventos, relatórios, fórmulas e etc que são referenciados nos parâmetros também exista na coligada de destino.**

* Ignorar: Este processo, caso exista a informação na coligada destino ele irá ignora-lá porém para eventos e fórmulas irá preencher os parâmetros que não estejam preenchidos e exista a formula ou evento na coligada.

Ex: Na coligada origem o parâmetro "Usa mês comercial na admissão" está marcado e na coligada destino desmarcado, com o processo selecionado ele continuará desmarcado na coligada destino.  
Ex: Para fórmulas ou eventos que exista em ambas coligadas, caso na coligada origem esteja com o parâmetro preenchido com a fórmula e na destino não este processo irá incluir a formula no parâmetro referente.

**Obs: Ele apenas inclui as informações para campos de fórmulas e eventos, para parâmetros de flag ele irá ignora-lo**

**Tela de Seleção de Coligadas:**  
Nesta etapa, você selecionará as coligadas destinos , quais as coligadas que deseja que os parâmetros da coligada base seja copiados para ela.

**Execução Concluída:**  
Nesta tela será exibido o log das tabelas copiadas e para as coligadas.  
Caso o sistema encontre erro copiando os parâmetros para alguma coligada, o processo continuará executando para as demais.

**OBS: Os parâmetros de Integração com o Middleware não serão copiados, pois o preenchimento dos mesmos deverá ser realizado através do processo de Ativação do Middleware.**

|  |  |
| --- | --- |
|  | Veja Também |

---

[Passo a Passo para a Execução](http://tdn.totvs.com/pages/viewpage.action?pageId=336398420)
