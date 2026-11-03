---
article_id: 360021778232
category: Administração de Pessoal
content_hash: 52941a907869245c4f083ec0c584f181454aeb8f38d902f074581f254fb0a180
fetched_at: '2026-06-28T22:47:02.268545+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Cópia de registros entre coligadas
type: support-article
updated_at: '2026-03-20T21:47:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021778232-RH-RM-FOP-C%C3%B3pia-de-registros-entre-coligadas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25019044804247)**Tempo aproximado para leitura:**00:04:10 min****Dúvida**Qual a ordem correta para copiar os dados de uma coligada para outra?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Alguns módulos do sistema obrigatoriamente necessitam seguir uma ordem específica na cópia de registro entre suas coligadas. O roteiro abaixo deverá ser seguido quando o usuário desejar realizar a cópia de todos os registros para outra coligada:  
  
1. Acesse **Administração de Pessoal | Cálculos | Tabelas de Cálculo** e copie as tabelas de cálculos para a coligada destino em **Processos | Copiar Registro entre Coligadas**;2. Acesse **Administração de Pessoal | Cadastros Globais | Tabelas Dinâmicas** e copie as tabelas dinâmicas para a coligada destino em **Processos | Copiar de tabelas dinâmicas entre Coligadas.** Nesta etapa, marque apenas os registros que não estiverem disponíveis a todas as coligadas;3. Acesse **Administração de Pessoal | Fórmulas** e copie as fórmulas para a coligada destino através do caminho **Processos | Copiar fórmulas entre Coligadas**;  
  
4. Acesse **Encargos | Cadastros | Cadastros Contábeis | Plano de Contas (Gestão Contábil)** e copie o plano de contas para a coligada destino em **Processos | Copiar Contas Contábeis entre Coligadas**;5. Acesse **Encargos | Cadastros | Históricos Padrões** e copie o histórico padrão em **Processos | Copiar Histórico Padrão entre Coligadas**;6. Acesse **Administração de Pessoal | Eventos | Rateio de Eventos** e copie o rateio de eventos para a coligada destino em **Processos | Copiar rateio entre coligadas**;  
  
**O passo 06 só deverá ser realizado caso o usuário utilize cálculo por centro de custo e os eventos seguirem algum rateio**.7. Acesse **Administração de Pessoal | Eventos | Eventos** e copie os eventos para a coligada destino em **Processos | Copiar eventos entre coligadas**;  
  
8. Acesse **Administração de Pessoal | Eventos | Eventos** e copie os eventos para a coligada destino em **Processos | Copiar eventos entre coligadas**. Desta vez, marque o parâmetro **Substitui registros no destino se eles já existirem**;  
  
- Se caso o usuário fizer a cópia de registro em ordem inversa poderá ocorrer erros de chave estrangeira violada;  
- O passo 8 só deverá ser realizado caso o passo anterior tenha sido executado, ou o campo Evento para diferença no módulo de eventos estiver selecionado.  
  
9. Acesse **Administração de Pessoal | Sindicatos** e copie os sindicatos para a coligada destino em **Processos | Cópia de sindicatos entre coligadas**;  
  
10. Acesse **Administração de Pessoal | Cálculos | Valores Fixos** e copie os valores fixos para a coligada destino em **Processos | Copiar valor fixo entre coligadas**;  
  
11. Acesse **Encargos | Cadastros | Encargos** e copie os encargos para a coligada destino em **Processos | Cópia de registro entre coligadas**;  
  
12. Acesse **Administração de Pessoal | Vale-transporte | Tarifas de Transporte** e copie as tarifas de transporte entre coligadas em **Processos | Copiar tarifa entre coligadas**;   
  
13. Acesse **Administração de Pessoal | Vale-transporte | Linhas de Transporte** e copie as linhas de transporte entre coligadas em **Processos | Copiar linhas de transporte entre coligadas**;   
  
**Importante**  
Certifique-se que as Tarifas de Transportes tenham sido copiadas corretamente ou que na coligada destino existam as mesmas tarifas cadastradas nas linhas de transporte para a cópia correta. Caso contrário a coligada destino ficará inconsistente.
