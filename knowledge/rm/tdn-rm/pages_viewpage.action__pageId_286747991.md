---
content_hash: d1d307574ce347bc0234f7b556d875d9a4df5c058eef0435aa10d8736f8e660d
fetched_at: '2026-06-29T00:08:41.764811+00:00'
page_id: '286747991'
product: rm
source: tdn-rm
title: RMCTB00004_Integrar Lote(s)/Lançamento(s) ao Lote Oficial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286747991
version: 8
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Integrar Lote(s)/Lançamento(s) ao Lote Oficial |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do processo**  Este processo tem por objetivo transferir os dados do lote **N** (blocos de lançamentos não integrados ao lote oficial), vindos de outros módulos ou do próprio Totvs Gestão Contábil, para o lote **Zero** (lote oficial da contabilidade).  Receber/efetuar lançamentos em um lote **N** auxilia no controle de todas as atividades contábeis propiciando uma contabilidade mais fidedigna.  **Regras Gerais**  Antes da Integração de Lotes, algumas validações nos lançamentos são realizadas a fim de manter a integridade dos dados, por exemplo:   * Diferenças entre débito e crédito; * Se o Parâmetro do Sistema **Verifica Duplicidade de Lote na Integração** estiver marcado, o sistema verifica primeiro se já foi integrado anteriormente algum lote que utilizou este mesmo código e será emitida uma mensagem advertindo-o sobre a integração anterior, permitindo que o usuário opte por continuar ou não o processo; * Se o parâmetro do sistema **Aplicar regras de validação de lançamentos na Integração de Lotes** estiver marcado, o sistema fará a validação das regras de inclusão de lançamentos presentes nas **Fórmulas** e **Amarrações de Lançamentos** ativas e só fará a integração de lotes se os lançamentos estiverem satisfazendo a estas fórmulas e amarrações ativas.   **Importante**  O processo é **irreversível**, não podendo, portanto, ser desfeita a integração dos lançamentos do(s) lote(s) recém integrado(s) ao lote oficial da contabilidade, Lote Zero.  **Parametrização Necessária**  1 - Para realizar a integração de lotes acesse **Escrituração Contábil/Lotes**, selecione o lote a ser integrado e clique em **Processos/Integrar Lote(s)/Lançamento(s) ao Lote Oficial**, conforme abaixo:    2 - Em seguida, o lote selecionado já estará relacionado no processo, sendo possível neste momento adicionar novos lotes ou excluir lotes relacionados. Em seguida avance e execute o processo:    3 - Como em todo processo no sistema, são gerados arquivos de log, e sua consulta é recomendável para verificar eventuais inconsistências:  **Atenção as dicas: Agendamento:** A execução do processo de Integração dos Lotes pode ser agendada para um determinado horário. Este recurso pode ser muito útil uma vez que com o agendamento a execução pode ser programada para um horário estratégico, onde não exista grande utilização do aplicativo, como à noite, por exemplo, otimizando desta forma a sua utilização. Para isto, o processo de integração deve ser parametrizado normalmente, mudando apenas a informação da data e hora para execução do processo conforme desejar. O agendamento, porém, só estará disponível quando o *JobServer* estiver configurado para executar em **modo 3 Camadas**.  **Fracionamento:** A partir da versão 12.1.2302 é possível realizar o [fracionamento de *jobs*](https://tdn.totvs.com.br/pages/viewpage.action?pageId=708893468)para integração de lotes, assim, otimizando o tempo de execução. |
| **Observações:** | É importante lembrar que os Lotes que possuírem parametrização fixa em módulos externos ao da contabilidade, como no TOTVS Gestão Financeira, Gestão Patrimonial etc., em nenhuma hipótese serão excluídos pelo sistema após a sua integração, pois o código continua informado no módulo de Origem. Para mais informações acesse [Integração de Lotes - Lote Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=423938460). |
