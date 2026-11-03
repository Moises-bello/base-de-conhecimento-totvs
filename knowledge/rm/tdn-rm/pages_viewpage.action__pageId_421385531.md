---
content_hash: dc3aed83c8122abb85b595202dbc7a43898134700a3019a5f61e53cc1779bdd3
fetched_at: '2026-06-29T00:09:16.404918+00:00'
page_id: '421385531'
product: rm
source: tdn-rm
title: Sincronizar Construção e Projetos x MS Project (Legado)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385531
version: 2
---

Este processo visa permitir que o usuário efetue o sincronismo de um arquivo do Microsoft Project com o projeto aberto no Totvs Obras e Projetos.   
 O processo de sincronismo é responsável por conciliar as informações do MS Project com as do projeto do Totvs Obras e Projetos, atualizando suas informações, hierarquias, predecessores e recursos, tornando assim as informações das duas fontes de dados compatíveis.  
    
 **Conciliação de Tarefas**  
 A conciliação entre as tarefas do Totvs Obras e Projetos e do MS Project será efetuada através de uma tabela que relaciona os registros a partir da chave da tarefa no TOP e do GUID do registro no MS Project. A tabela será alimentada a cada sincronismo, não sendo necessária nenhuma iteração com a mesma a cada inclusão, alteração ou exclusão no TOP.  
 Esta tabela será limpa a cada troca de arquivo vinculado ou a cada sincronização com o parâmetro "Sincronizar recursos" desmarcado para evitar assim que sejam considerados de forma equivocada que registros estão sendo inseridos/excluídos por não serem encontrados.  
 Durante a conciliação será identificada a ação original executada e a ação de sincronismo a executar seguindo as seguintes regras:  
 **Ação Original:** Registro alterado em uma das extremidades (MS Project ou Base de Dados TOP)  
 **Ação de Sincronismo:** Sincronizar os dados do registro do TOP conforme informações alteradas no MS Project.  
 **Ação Original:** Registro incluído e/ou excluído no TOP  
 **Ação de Sincronismo:** Incluir e ou excluir registro no arquivo do MS Project  
 **Ação Original:** Registro incluído e/ou excluído no MS Project  
 **Ação de Sincronismo:** Incluir e/ou excluir registro no projeto do TOP  
 **Conciliação de recursos (insumos)**  
 Assim como a conciliação entre as tarefas, a conciliação de recursos do Totvs Obras e Projetos e do MS Project será efetuada através de uma tabela que relaciona os registros a partir da chave da tarefa no TOP e do GUID do registro no MS Project. A tabela será alimentada a cada sincronismo, não sendo necessária nenhuma iteração com a mesma a cada inclusão, alteração ou exclusão no TOP.  
 Esta tabela será limpa a cada troca de arquivo vinculado ou a cada sincronização com o parâmetro "Sincronizar recursos" desmarcado para evitar assim que sejam considerados de forma equivocada que registros estão sendo inseridos/excluídos por não serem encontrados.  
 Durante a conciliação será identificada a ação original executada e a ação de sincronismo a executar seguindo as seguintes regras:  
 **Ação Original:** Registro alterado em uma das extremidades (TOP ou MS Project)  
 **Ação de Sincronismo:** Sincronizar os dados do registro do TOP conforme informações alteradas no MS Project.  
 **Ação Original:** Registro incluído no TOP  
 **Ação de Sincronismo:** Incluir registro no arquivo do MS Project  
 **Ação Original:** Registro incluído no MS Project  
 **Ação de Sincronismo:** Incluir registro no projeto do TOP  
 **Ação Original:** Registro excluído no MS Project   
 **Ação de Sincronismo:** Excluir registro no projeto do TOP  
 **Ação Original:** Registro excluído no TOP  
 **Ação de Sincronismo:** Excluir registro no arquivo do MS Project  
    
 **Conciliação de relacionamento de recursos / composições**  
 Visto que o Microsoft Project não possui uma entidade equivalente às composições do Totvs Obras e Projetos, mantendo somente as informações de relacionamento de recursos e tarefas, será seguido as regras abaixo para conciliação do relacionamento de recursos (insumos ou composições).  
    
 **Regras de conciliação**

• Número de recursos da tarefa igual a 0?  
          Inserir nulo nos campos de insumo e composição.

• Número de recursos da tarefa igual a 1?  
          Insumo relacionado à tarefa igual ao recurso relacionados no MS Project?  
           Sim: Nenhuma ação  
           Não: Relacionar insumo na tarefa

• Número de recursos da tarefa maior que 1?  
          Insumos da composição relacionada à tarefa são iguais aos recursos relacionados no MS Project (insumos e quantidades)?  
           Sim: Nenhuma ação  
           Não: Incluir nova composição

   
 **Conciliação de dependências de tarefas (predecessoras e sucessoras)**  
 Para o sincronismo serão consideradas as informações de tarefas predecessoras e sucessoras da fonte de dados conforme informações do MS Project, assim desconsiderando ações efetuadas na outra fonte de dados no intervalo entre o ultimo sincronismo e o corrente.  
    
 **Atualizar o modelo de dados**  
 Durante a conciliação dos registros é utilizada a definição de relação de campos equivalentes entre o TOP e o MS Project.  Os campos que podem ser parametrizáveis são: Descrição, Unidade de Medida, Código Auxiliar, Campo Livre 1, Campo Livre 2, Campo Livre 3, Campo Livre 4, Campo Livre 5, Moeda de Valor, Quantidade da Tarefa, Campo Livre 1 - Valor, Campo Livre 2 - Valor, Campo Livre 3 - Valor, Campo Livre 4 - Valor, Campo Livre 5 - Valor. Esta parametrização permite que o usuário possa selecionar se deseja envia-los e para qual campo (de tipo de dado compatível) relacionar.   
 Esta parametrização pode ser feita acessando:  Parâmetros Gerais|Configuração do MS Project.  
    
 **Conciliação de alteração hierárquica e impasses**  
 A hierarquia de tarefas será espelhada conforme dados extraídos do arquivo do MS Project, desconsiderando assim alterações hierárquicas efetuadas no TOTVS Obras e Projetos.  
 Caso a inclusão de tarefas ou a alteração de hierarquia gere impasses, onde a tarefa é marcada como filha de uma etapa excluída ou marcada para exclusão, a mesma também será marcada para exclusão nas duas fontes de dados.  
    
 **Cálculo da curva ABC**  
 O sincronismo baseia-se em dados calculados da curva ABC para a integração dos recursos (insumos e composições), sendo necessário que o cálculo da curva ABC seja efetuado previamente. Ao solicitar o sincronismo o usuário será questionado sobre a execução do recalculo, ficando a cargo do mesmo informar se este deve ser executado ou não.

**Regras de Integridade**  
**Versão do Microsoft Project**  
 Compatível com a política de manutenção da Microsoft, esta nova funcionalidade mantém compatibilidade a partir da versão 2007 do MS Project.  
**Sincronização de único cenário e planilha**  
 A sincronização não manipula múltiplos arquivos, assim somente sincronizando um cenário e planilha (atividade ou serviço) de cada vez. Caso seja necessário alternar para um novo cenário ou tipo de planilha deverá ser iniciada a sincronização com um novo arquivo, descartando o anterior.  
**Tipo de duração das tarefas**  
 Visando compatibilizar com o funcionamento do TOP o arquivo do MS Project será tratado sempre como "duração fixa".   
**Tipo das tarefas sem recursos**  
 Tarefas integradas que não possuírem recursos serão marcadas como "Valor cotado" no TOP.   
**Parâmetros gerais e de projeto não utilizados no processo de sincronismo**  
 Parâmetros de Projeto: Os parâmetros "Versão do Project" e "Criar recursos que não existirem na base de dados" são desconsiderados pelo novo processo de sincronismo.  
 Parâmetros Gerais: A visão de parametrização de equivalência de campos em sincronismo com MS Project apresenta mais campos do que os sincronizados no novo processo, sendo estes desconsiderados e não necessitando parametriza lós.  
**Recalculo de EDT**  
 Caso existam códigos de tarefa repetidos em alguma das fontes de dados o mesmo será recalculado, considerando o primeiro na ordem de leitura como o válido e os próximos terão o seu último número recalculado.  
**Relacionamento de Recursos em Obras e Etapas**  
 O MS Project possui comportamento diferente do TOTVS Obras e Projetos, permitindo relacionar recursos em tarefas do tipo Sumary (Etapas ou Obras do TOP). Ao efetuar o sincronismo considerando o MS Project como mandatário a informação de recursos (insumos/composições) em Obras ou Etapas será enviada ao TOP mas o mesmo as desconsiderará, conforme sua própria regra de negócio, inserindo valor vazio nos respectivos campos, podendo assim tornar as duas fontes de dados com informações diferentes mas sem gerar nenhum impacto funcional.

**Importante:**  
Para ambiente 3 camadas é necessário informar o diretório relativo onde o arquivo se encontra, e esse mesmo diretório deverá ter permissão de leitura e escrita para o usuário do Host:  
Ex:   
·          Diretório local: C:\Temp\ArquivoProject.mpp  
·          Diretório relativo: \\NOME\_DO\_COMPUTADOR\_OU\_IP\Temp\ArquivoProject.mpp  
·          A pasta "Temp" deverá estar compartilhada e permitir leitura e escrita para o usuário do Host.  
       Caso hajam erros ao efetuar o download do arquivo sincronizado é importante que o verificar o log de execução para identificar o status o  sincronismo, pois esta etapa do processo não compartilha da mesma transação.  
·                     Caso haja erro no download do arquivo o mesmo ficará desatualizado, devendo identificar se o mesmo poderá ser utilizado novamente em futuros sincronismos ou um novo arquivo deve ser gerado.  
·                     Exemplo: Caso o sincronismo seja efetuado corretamente mas o arquivo não seja retornado, o mesmo não será atualizado com o ID de execução utilizado para armazenar o relacionamento De-Para de registros. Ou seja, caso este arquivo seja sincronizado novamente os registros existentes no mesmo serão duplicados no TOP (o mesmo ocorre com registros existentes no TOP). Neste caso o aconselhado é que seja gerado um novo arquivo a partir do processo de sincronismo com o campo "Criar novo arquivo" marcado.
