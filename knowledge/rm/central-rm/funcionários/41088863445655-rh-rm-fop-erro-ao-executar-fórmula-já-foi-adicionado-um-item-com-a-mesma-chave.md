---
article_id: 41088863445655
category: Funcionários
content_hash: 9683af36a58b713e96c0b619d055eb93d479020ff36c321f4d86e35adfb3d33d
fetched_at: '2026-06-28T22:47:03.114975+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: 'RH - RM - FOP - Erro ao executar fórmula: Já foi adicionado um item com a
  mesma chave'
type: support-article
updated_at: '2026-06-09T17:42:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41088863445655-RH-RM-FOP-Erro-ao-executar-f%C3%B3rmula-J%C3%A1-foi-adicionado-um-item-com-a-mesma-chave
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41088832208279) Tempo aproximado para leitura: **00:03:55min**  
  
**Ocorrência**  
Ocorreu o seguinte erro ao executar a formula **"Código da Formula"**:  
A fórmula **"Código da Formula"** não pode ser executada! Já foi adicionado um item com a mesma chave.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento -Todas as versões  
  
**Causa**  
O erro ocorre devido a uma inconsistência ou quebra de integridade na base de dados do funcionário afetado. Quando o sistema realiza o processamento em lote (grandes grupos, filiais ou seções), ele tenta carregar e indexar as informações históricas e cadastrais na memória. Se houver registros com caracteres invisíveis (como um espaço em branco ao final do código) ou códigos que perderam a amarração com suas respectivas tabelas master, a aplicação gera a exceção de chave duplicada ao tentar adicionar o item no dicionário interno de cálculo.

Na maioria dos cenários mapeados, a causa está relacionada a:

* Um caractere de espaço em branco inserido incorretamente ao final do campo `CODHORARIO` na tabela de Histórico de Horários (`PFHSTHOR`).
* Um caractere de espaço em branco inserido incorretamente ao final do campo `CODFUNCAO` na tabela de Histórico de Funções (`PFHSTFCO`).

**Solução**

Como as validações de tela atuais do sistema impedem a gravação de códigos inexistentes ou com espaços, essas inconsistências são heranças de migrações antigas ou inserções diretas via banco de dados executadas no passado.

Realize os seguintes passos:

1. Identifique no log de execução do processo, qual é a chapa do funcionário em que o processamento é interrompido;
2. Através de uma ferramenta de banco de dados (como SQL Server Management Studio), realize uma consulta nas tabelas de histórico do funcionário afetado para checar a existência de espaços em branco ao final dos códigos cadastrados. Utilize comandos que verifiquem o comprimento do caractere ou que evidenciem o espaço (exemplo: `WHERE CODHORARIO LIKE '% '`);
3. Verifique especificamente o preenchimento dos campos nas seguintes tabelas:

* Tabela `PFHSTHOR`, coluna `CODHORARIO` (Histórico de Horário).
* Tabela `PFHSTFCO`, coluna `CODFUNCAO` (Histórico de Função).

4. Realize o ajuste fino no banco de dados para remover o caractere de espaço em branco ao final do código (utilizando funções de tratamento de string como `RTRIM`), garantindo que o código fique idêntico à chave primária correspondente na tabela master (`AHORARIO` ou `PFUNCAO`);
5. Após efetuar a correção na base de dados e retirar o espaço em branco das tabelas de histórico, acesse o sistema novamente e reexecute o processo de lançamento do grupo de eventos ou geração de encargos para o lote de funcionários.

Além das orientações apresentadas acima, recomendamos realizar a validação da base de dados conforme indicado no material abaixo. Como apoio à análise, também sugerimos utilizar ferramentas de banco de dados para monitorar e identificar possíveis ocorrências relacionadas ao erro.

**Saiba Mais**

[RH - RM - FOP - Validação da Base de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411526824599-RH-RM-FOP-Valida%C3%A7%C3%A3o-da-Base-de-Dados)

[Framework - Framework RM - BD - Executando Profiler/Trace em uma Base de Dados Oracle](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015973632--Framework-Framework-RM-BD-Executando-Profiler-Trace-em-uma-Base-de-Dados-Oracle)
