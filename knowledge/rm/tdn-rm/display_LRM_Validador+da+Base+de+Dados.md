---
content_hash: 242b0f8bf7f3fff3d7b708d4ff9919f13b8ae39e417858d313cfae9c0af0727d
fetched_at: '2026-06-29T00:10:08.763733+00:00'
page_id: '452719574'
product: rm
source: tdn-rm
title: Validador da Base de Dados
type: documentation
url: https://tdn.totvs.com/display/LRM/Validador+da+Base+de+Dados
version: 3
---

Neste módulo será possível realizar a validação da base de dados, conforme obrigatoriedade definidas no layout do eSocial.  
 Após a validação será gerado dois gráficos, um irá disponibilizar o percentual de completude geral da base de dados, o segundo gráfico irá exibir o percentual de completude por evento(Layout).  
 Para realizar a verificação da base de dados acesse: eSocial | Validador da Base de Dados.  
 O sistema fará a validação dos seguintes eventos(Layout):

* S-1000 - Informações do Empregador
* S-1005 - Tabela de Estabelecimento/Obras
* S-1010 - Tabela de Rubricas
* S-1020 - Tabela de Lotações Tributárias
* S-1030 - Tabela de Cargos
* S-1050 - Tabela de Horários/Turnos de Trabalho
* S-1070 - Tabela de Processos Administrativos/Judiciais
* S-2200- Admissão /Ingresso de Trabalhador
* S-2300 - Trabalhados sem vinculo de emprego/Estatutário-inicio

**Observação:**

* Na tela de processo do Validador de Base, o usuário poderá selecionar os eventos que deverão ser validados, no caso em específico dos eventos S-2200- Admissão /Ingresso de Trabalhador e S-2300 - Trabalhados sem vinculo de emprego/Estatutário-inicio o usuário deverá informar também a seleção de funcionário que o processo irá considerar.
* A seleção de funcionários somente será habilitada quando o flag correspondente ao evento S-2200- Admissão /Ingresso de Trabalhador e S-2300 - Trabalhados sem vinculo de emprego/Estatutário-inicio for(em) selecionado(s).
* Ao final da execução do processo, o usuário também terá como opção visualizar o resultado no formato de log, essas informações estão disponíveis na aba Log do Wizard do processo do validador de base.
* Em todas as abas o usuário poderá selecionar os registros desejados no Grid e exportar os dados para os formatos CSV, XLS, PDF, XLSX, TXT, RTF ou imprimir.
* Na aba de resumo é exibido um percentual de completude. Esse percentual não leva em consideração os avisos. Abaixo a fórmula de cálculo do percentual de completude:              
  100 - (((Erros Obrigatórios + Erros Validação) / (Campos Obrigatórios + Campos Validados)) \* 100)

 No processo poderá ser selecionado o parâmetro "Exibe avisos" que ao final relacionará os avisos junto com os erros.  
 O parâmetro "Considera Demitidos Antes da Obrigatoriedade" validará os funcionários antes de enviar algum outro evento para demitidos antes da data de obrigatoriedade de envio de eventos não periódicos do eSocial.   
 **Observação:** Será considerada a data do último movimento no cadastro de rescisão para a comparação com a data da competência atual ou com a data de entrega dos eventos Não Periódicos no parametrizador.
