---
content_hash: ddbd57079275ff4f5d761c4564fded57296e745697da96e6bc03b12b85176f08
fetched_at: '2026-06-29T00:11:06.251550+00:00'
page_id: '633054996'
product: rm
source: tdn-rm
title: Configuração de limpeza de tabela
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=633054996
version: 3
---

# Resumo

---

A tabela 'TRF\_documents' ganha registros a partir do momento em que relatórios são gerados e visualizados 'agora', sendo assim, existe uma configuração para definir de quanto em quanto tempo essa tabela será limpa.

# Configuração

---

No appsettings.json do TReports é possivel configurar o tempo entre as verificações de limpeza.

**ShortDueTime:** Representa o tempo de vida do documento e o período de verificação da limpeza do cache em memória.

**LongDueTime:** É o período de tempo que será realizada a verificação da limpeza.

O tempo é contado em segundos.

* Exemplos:
  + 1 minuto = 60 seg
  + 1 hora = 3600 seg
  + 12 horas = 43200 seg
  + 1 dia = 86400 seg

#### 

Observação

 Na configuração de tempo de suspensão do pool do IIS, o tempo padrão é de 20 minutos, caso o IIS colocar o pool do TReports em suspensão dentro deste tempo, **as verificações recorrentes de limpeza do cache não serão realizadas**, pois esta ação do IIS vai parar o serviço de verificação, deixando-o em modo de espera.

Após a iniciação do TReports, depois de 1 minuto é feita a primeira verificação de limpeza, depois o período de tempo das proximas verificações são conforme o tempo informado na configuração.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.29

false

**Processo:** Configuração do TReports
