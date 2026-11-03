---
content_hash: 6b08b8bd3dacec3bc5c10f569603659fea5ddf0af8da7c3627967d97ed7aaf7e
fetched_at: '2026-06-29T00:10:31.030955+00:00'
page_id: '520659335'
product: rm
source: tdn-rm
title: Contrato de Locação - Gestão - Encerrar / Rescindir
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520659335
version: 7
---

**Encerrar**

---

O encerramento é o termino do contrato de forma natural dentro do prazo de vigência determinado, ou seja não havendo renovação o contrato será encerrado.  
Para informações detalhadas acesse:

**Rescindir**

---

A rescisão é o encerramento de um contrato antes do período previsto de vigência final e pode ocorrer por inciativa do locador ou locatário.  
Para informações detalhadas acesse:   
  
*OBS: A data informada na rescisão é considerada como dia locado, ou seja, o sistema entende que o imóvel ainda está em uso nessa data.*

*Exemplo prático*

*Se o cliente realizar a rescisão no dia 30/09, todas as parcelas com vencimento até o dia 30/09 (inclusive este dia) serão mantidas.*  
*O sistema cancelará apenas os lançamentos a partir do dia 01/10, incluindo esta data.*

Contabilização do Encerramento/Rescisão do Contrato de locação

* **Evento Contábil:** O processo de encerramento do contrato poderá impactar em ajustes e contabilizações específicas, pois impacta nos valores linearizados e talvez já contabilizados. O tratamento de possíveis valores de devolução será feito nos eventos financeiros da rescisão.
* O encerramento do contrato irá excluir as contabilizações, de todos os processos, posteriores à data da rescisão/encerramento.
* Apenas a contabilização do Evento Contábil de rescisão poderá ser processada após a data de rescisão/encerramento. Serão bloqueadas as demais contabilizações posteriores a rescisão/encerramento.
* **Data para início da contabilização:** Definirá qual a data inicial a ser considerada para os processos de contabilização e linearização. As opções de data são:
  + Início da vigência do contrato
  + Início da locação do contrato
  + Data-base de contabilização
* **Aplicar linearização:** irá definir se a contabilização será linearizada (Arrendamento mercantil) ou não. Esta definição irá impactar na forma em que serão realizados os cálculos internos do sistema.
* **Lançamentos Remetidos:** O sistema não irá excluir parcelas com status “Baixada” ou “Remetida” quando a data selecionada estiver dentro do mesmo mês em que o lançamento foi realizado. Caso este contrato possui pró-rata o sistema irá proporcionar os valores gerando a diferença.
