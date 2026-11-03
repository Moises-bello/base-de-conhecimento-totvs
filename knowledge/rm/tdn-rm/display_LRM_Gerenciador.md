---
content_hash: 7e403433ff1b5e3ecede4ebaa55cae6a2b53df1d2895a5e8a4680ab70bf32d40
fetched_at: '2026-06-29T00:09:16.151901+00:00'
page_id: '421385466'
product: rm
source: tdn-rm
title: Gerenciador
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerenciador
version: 3
---

O gerenciador de concorrência eletrônica é utilizado para gestão da exportação e importação das licitações disponibilizadas.   
 Na tela do gerenciador serão definidos os parâmetros utilizados na exportação da planilha utilizada na licitação. Na aba Geral devem ser informados os campos "Código do Processo de Licitação", o "Arquivo de Saída", o "Nome da Planilha", "Linha Inicial" e "Linhas Livres da Planilha", "Licitação com Recursos", "Cabeçalho", "Rodapé", "Senha", "Confirmação" e "Data Limite para Importação".

Caso a opção "Licitação com Recursos" seja marcada ficará disponível na aba 'Campos' a opção "Planilha". Nela será possível escolher a planilha utilizada e quais campos poderão ser inseridos. Para os mesmos campos é possível definir, informando na coluna "Travado" se o campo poderá sofrer alterações ou não. A opção "Bloquear BDI do Projeto" quando marcada, não permite que o campo do BDI seja alterado. A opção "Permitir Inclusão/exclusão de recursos" quando marcada, permite que novos recursos (insumos e composições) sejam inseridos e todas as células fiquem destravadas, caso contrário não será possível fazer inclusões e as células ficarão travadas.

Na aba "Formatação", é possível definir diferentes cores e destacar campos importantes como Título, Cabeçalho, Rodapé, Título da Colunas, Tarefas/Composições/Insumos, Células destravadas e Totais.   
 **Observação:** Quando informado o campo "Senha", ao utilizar a opção "Desproteger Planilha" disponível no MS Excel, a mesma será solicitada.   
 Uma vez exportada e as devidas alterações efetuadas, a planilha poderá ser importada informando o arquivo exportado em formato .XLS ou .XLSX.  
 **Atenção:** Caso um dos recursos importados (composição ou insumo) já existam no sistema, a importação apenas atualizará os dados alterados em campos destravados. Caso seja um novo recurso, a importação copiará todos os dados da planilha.   
 Todas as composições serão importadas desconsiderando a Equipe por Produção, ou seja, as composições são importadas com valor calculado e não existirão composições por produção.   
 **Atenção:** É possível incluir novas composições e insumos, mas a estrutura deve permanecer a mesma e é de responsabilidade do usuário copiar as fórmulas e formatações das células inseridas.   
 **Observação:** Quando informado o campo "Data Limite para Importação" será feita uma validação e não será permitido a importação caso a data atual seja maior que a data definida na exportação.
