---
content_hash: e1051a499edd16dad4dec1444eed613ff976e3ff964937e6503b7e67740328a4
fetched_at: '2026-06-29T00:10:52.340613+00:00'
page_id: '572012884'
product: rm
source: tdn-rm
title: Geração da EAP Automática
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572012884
version: 51
---

Geração da EAP AutomáticaGeração

Requisitos de configurações para geração da EAP:

* Configurar os níveis da EAP no Menu BIM | [Template de Criação de EAP](https://tdn.totvs.com.br/pages/viewpage.action?pageId=573206863).

Após configurado, o Processo de Geração da EAP Automática tem como objetivo gerar automaticamente a EAP a partir do modelo 3D no processo de upload do arquivo IFC ou executando o processo de gerar EAP.

* No processo de upload, selecionar o template que será utilizado para a geração da EAP.
* Log da execução do processo

* EAP gerada automaticamente através do arquivo IFC:

Observação: As tarefas geradas na EAP serão automaticamente associadas aos objetos de origem no modelo 3D.

# **Vínculo entre tarefas e recursos na Geração da EAP:**

Ao realizar a Geração Automática da EAP a partir de um arquivo IFC as tarefas serão geradas de acordo com os objetos do arquivo, porém, caso não exista vínculo entre recursos e tarefas, as tarefas são geradas sem recursos associados.

O vínculo entre tarefas e recursos ocorre após a realização da Geração Automática da EAP onde o usuário preenche manualmente os recursos em cada tarefa gerada a partir do arquivo IFC.

O sistema irá aprender automaticamente com o usuário e uma vez que o vínculo seja preenchido para tarefas de um respectivo arquivo IFC, ao gerar a EAP automaticamente para o mesmo arquivo em outro projeto, o vínculo será mantido e as tarefas serão geradas com os recursos.

Na geração da EAP o sistema irá seguir as seguintes prioridades:

* A última tarefa associada manualmente em outros projetos/coligadas.
* Insumo/composição "global": Caso a composição/insumo seja da mesma coligada da tarefa.
* Código Emop: Importação da Orcecerto Sicro/Sinapi.
* Código composição/insumo: Caso exista uma composição/insumo "local" de mesmo código.
* Descrição composição/insumo: Caso exista uma composição/insumo "local" de mesmo nome.

Regerar

Após realizar a importação de um arquivo IFC no projeto e e as tarefas forem geradas, é possível regerar a planilha de tarefas através do processo "Geração de EAP".  
Nesse processo pode ser selecionado mais de um arquivo IFC de diferentes disciplinas (Arquitetural, Estrutural, Hidráulico, etc.) para que seja gerado uma planilha em comum contendo a junção desses arquivos.

O Template de Criação de EAP virá preenchido com o mesmo que foi utilizado durante a importação do arquivo IFC, podendo ser alterado pelo usuário.

Caso seja selecionado dois ou mais projetos, virá preenchido com o primeiro arquivo que tenha um template associado durante a importação do arquivo IFC.

* Só é possível executar o processo de Geração da EAP com um Template de Criação de EAP selecionado.
* Após excetuar o processo de Geração da EAP a planilha será substituída com as tarefas que forem regeradas.
* Caso a propriedade não seja encontrada no objeto, a tarefa não será gerada e será gerado um aviso para o usuário no log do processo.
* Para gerar um log de trace durante a Geração da EAP, marque a opção "Gerar log de trace" antes de executar o processo. O log trace é um nível de registro detalhado que captura informações sobre o comportamento da aplicação, auxiliando na depuração e análise de fluxos de trabalho.

Log da execução do processo:

Log de trace do processo:

Planilha com as tarefas regeradas:

Tarefas associadas após a geração da EAP:

[Voltar](https://tdn.totvs.com.br/display/LRM/Modelos+de+Projeto)
