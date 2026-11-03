---
content_hash: b9009c3a3d77bffaa7bb0153a890662397b8672550519683af5971f0b34a099f
fetched_at: '2026-06-29T00:10:09.327442+00:00'
page_id: '452719631'
product: rm
source: tdn-rm
title: Importação de Dados Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719631
version: 5
---

O sistema de folha de pagamento permite a migração da base de trabalho de outro sistema, ou do próprio sistema de folha de pagamento para a base atual.  
   
Os arquivos serão importados de acordo com a coligada utilizada no momento e segue um layout definido para cada conjunto de dados. No caso de importação para bases vazias, defina as Máscaras de Departamento, Centro de Custo e o Código de Quebra para o CNPJ da empresa.  
   
Ao iniciar a parametrização do processo de importação de dados, será necessário gravar um Perfil de Parâmetros para que todos os parâmetros definidos fiquem "salvos" para futuras importações de dados.  
   
Para gravar o perfil, na primeira tela do wizard deverá inserir uma descrição no campo "Perfil de Parâmetros" e clicar no Box "Salvar perfil ao concluir".  
   
Se desejar, poderá informar uma Descrição do Processo, para que no histórico de processo executados seja identificado com a descrição.  
Os arquivos serão exportados a partir do Gerador de Relatórios. Os arquivos exportados deverão seguir o padrão definido pelo Layout de Folha de Pagamento.  
Para manter a consistência dos dados e um bom funcionamento dos recursos, sugerimos a seguinte ordem para importação dos layouts Sugestão de ordem para importação dos layouts  
Nas pastas, Parâmetros I, Parâmetros II, Funcionário I, Funcionário II,  Férias Funcionário e Históricos Funcionário, o usuário deve  informar o nome dos arquivos a serem importados.  
 **Exemplo:** C:\ temp   
Para procurar o diretório, selecione **Caminho Default**. Quando o usuário seta um diretório Default este caminho permanece gravado.   
**Observações:**   
Os valores importados (por exemplo, de empréstimos, dados cadastrais) serão sobrepostos a valores existentes.  
   
Fique atento que você pode **Desmarcar Todos** ou **Selecionar Todos** os arquivos que serão importados.  
   
É OBRIGATÓRIO importar pelo menos a linha da situação atual dos seguintes históricos, sob pena de inconsistências no funcionamento do sistema:

* Histórico de Salário
* Histórico de Função
* Histórico de Férias
* Histórico de Horário
* Histórico de Número de Dependentes (Caso o funcionário possua Dependentes)
* Histórico de Seção
* Histórico de Situação
* Histórico de Afastamento (Caso exista afastamento para o funcionário e deve conter todos os dados referentes ao exercício corrente.)

Sendo RECOMENDÁVEL que se importe a linha atual dos outros históricos.   
O sistema exibirá, na base da janela, o progresso da importação. Mensagens relativas às ocorrências do processo são exibidas no **Arquivo de Log de Importação**, para verificação e eventual correção de erros. 

Importação Férias funcionário

Quando o parâmetro “Permite antecipação de dias de férias do próximo período aquisitivo” em Cadastros / Sindicatos / Férias estiver marcado.

Na importação com gozo de férias não finalizados será verificado se possui dias de antecipação

* Se o gozo de férias não estiver finalizado, será importado sem nenhuma tratativa, pois no finaliza férias será feito os procedimentos para antecipação.

Na importação com gozo de férias finalizados será verificado se possui dias de antecipação

* Se não existir o período aquisitivo futuro será inserido automaticamente
* Se não existir saldo suficiente no período aquisitivo para período de gozo antecipado, seja por mais de 32 faltas dentro do período aquisitivo ou por já possuir gozo de férias cadastradas em que o saldo seja menor que os dias de antecipação, por exemplo, será apresentada mensagem.

**Exemplo:**  Funcionário 00001 tem 35 dias de faltas na ficha financeira dentro do período aquisitivo que seria para a antecipação de férias. Então o saldo desse período seria 0 devido a mais de 32 dias de faltas. Será apresentada mensagem:

 “Linha <1>. Erro ao realizar importação de Períodos de gozo: Funcionário: 00001 Saldo do Período Futuro: 0 não comporta os dias de Antecipação: 5,00”

* Se o período aquisitivo for período perdido seja por será apresentada mensagem.

**Exemplo**: Foi importado o período que seria para a antecipação com informações de período perdido e motivo do período perdido, nesse caso apresenta a mensagem:

 “Linha <1>Erro ao realizar importação de Períodos de gozo:

Funcionário: 00001 Período Aquisitivo perdido não pode ser usado para incluir férias referente a antecipação. ”

Quando o parâmetro “Permite antecipação de dias de férias do próximo período aquisitivo” em Cadastros / Sindicatos / Férias estiver desmarcado as validações acima não serão executadas.

Layouts
